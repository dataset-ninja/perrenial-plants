# https://www.kaggle.com/datasets/benediktgeisler/perrenial-plants-detection

import supervisely as sly
import os
import xml.etree.ElementTree as ET
import xmltodict
import json


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    project = api.project.get_info_by_name(workspace_id, project_name)
    if project is not None:
        api.project.remove(project.id)
    project = api.project.create(workspace_id, project_name)
    meta = sly.ProjectMeta()

    ann_dir = "/mnt/c/users/german/documents/perrenial_plants/voc_annotations/voc_annotations"
    ann_paths = sly.fs.list_files(ann_dir)

    split_paths = sly.fs.list_files(
        "/mnt/c/users/german/documents/perrenial_plants/coco_annotations/coco_annotations/classification"
    )
    for dataset_path in split_paths:
        # split filename into dataset name and create dataset
        dataset_name = (os.path.splitext(os.path.basename(dataset_path))[0]).split("_")[2]
        dataset = api.dataset.create(project.id, dataset_name)
        # open and read json file, take all filenames
        f = open(dataset_path)
        jdata = json.load(f)
        current_dataset_images_list = []
        for i in jdata["images"]:
            current_dataset_images_list.append(i["file_name"])

        # iterate through filenames
        for fname in current_dataset_images_list:
            ann_fname = sly.fs.get_file_name(fname) + ".xml"
            path = os.path.join(ann_dir, ann_fname)
            tree = ET.parse(path)
            xml_data = tree.getroot()
            xmlstr = ET.tostring(xml_data, encoding="utf-8", method="xml")

            data_dict = dict(xmltodict.parse(xmlstr))
            # get image path and upload
            image_path = os.path.join(
                "/mnt/c/users/german/documents/perrenial_plants/raw_images/raw_images",
                fname,
            )
            image_info = api.image.upload_path(dataset.id, fname, image_path)

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
                    class_name = obj["name"].lower()
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
