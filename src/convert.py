# https://www.kaggle.com/datasets/benediktgeisler/perrenial-plants-detection

import supervisely as sly
import os
import xml.etree.ElementTree as ET
import xmltodict


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    dataset_path = r"C:\Users\German\Documents\perrenial plants\voc_annotations\voc_annotations"
    project = api.project.get_info_by_name(workspace_id, project_name)
    if project is not None:
        api.project.remove(project.id)
    project = api.project.create(workspace_id, project_name)
    meta = sly.ProjectMeta()

    dataset = api.dataset.create(project.id, "ds0", change_name_if_conflict=True)
    ann_paths = sly.fs.list_files(dataset_path)

    for path in ann_paths:
        tree = ET.parse(path)
        xml_data = tree.getroot()
        xmlstr = ET.tostring(xml_data, encoding="utf-8", method="xml")

        data_dict = dict(xmltodict.parse(xmlstr))
        # get image path and upload
        image_path = os.path.join(
            r"C:\Users\German\Documents\perrenial plants\raw_images\raw_images",
            data_dict["annotation"]["filename"],
        )
        image_info = api.image.upload_path(
            dataset.id, data_dict["annotation"]["filename"], image_path
        )

        labels = []
        if "object" not in data_dict["annotation"]:
            continue

        if type(data_dict["annotation"]["object"]) == list:
            for obj in data_dict["annotation"]["object"]:
                # get bbox cords
                xmin = int(obj["bndbox"]["xmin"])
                ymin = int(obj["bndbox"]["ymin"])
                xmax = int(obj["bndbox"]["xmax"])
                ymax = int(obj["bndbox"]["ymax"])

                # get class name, create labels
                bbox = sly.Rectangle(top=ymin, left=xmin, bottom=ymax, right=xmax)
                class_name = obj["name"]
                obj_class = meta.get_obj_class(class_name)
                if obj_class is None:
                    obj_class = sly.ObjClass(class_name, sly.Rectangle)
                    meta = meta.add_obj_class(obj_class)
                    api.project.update_meta(project.id, meta)
                label = sly.Label(bbox, obj_class)
                labels.append(label)

            # upload annotation
            ann = sly.Annotation(
                img_size=[
                    int(data_dict["annotation"]["size"]["height"]),
                    int(data_dict["annotation"]["size"]["width"]),
                ],
                labels=labels,
            )
            api.annotation.upload_ann(image_info.id, ann)
            print(f"uploaded bbox to image(id:{image_info.id})")
        else:
            xmin = int(data_dict["annotation"]["object"]["bndbox"]["xmin"])
            ymin = int(data_dict["annotation"]["object"]["bndbox"]["ymin"])
            xmax = int(data_dict["annotation"]["object"]["bndbox"]["xmax"])
            ymax = int(data_dict["annotation"]["object"]["bndbox"]["ymax"])
            bbox = sly.Rectangle(top=ymin, left=xmin, bottom=ymax, right=xmax)
            class_name = data_dict["annotation"]["object"]["name"]
            obj_class = meta.get_obj_class(class_name)
            if obj_class is None:
                obj_class = sly.ObjClass(class_name, sly.Rectangle)
                meta = meta.add_obj_class(obj_class)
                api.project.update_meta(project.id, meta)
            label = sly.Label(bbox, obj_class)
            labels.append(label)

            # upload annotation
            ann = sly.Annotation(
                img_size=[
                    int(data_dict["annotation"]["size"]["height"]),
                    int(data_dict["annotation"]["size"]["width"]),
                ],
                labels=labels,
            )
            api.annotation.upload_ann(image_info.id, ann)
            print(f"uploaded bbox to image(id:{image_info.id})")
    print(f"Dataset {dataset.id} has been successfully created.")
    return project
