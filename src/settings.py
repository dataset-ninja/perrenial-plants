from typing import Dict, List, Optional

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "Perrenial Plants Detection"
PROJECT_NAME_FULL: str = "Perrenial Plants Detection"

##################################
# * After uploading to instance ##
##################################
LICENSE: str = "MIT License"
# Available licenses: ["CC0", "CC BY-SA 4.0"]

INDUSTRIES: List[str] = ["general domain"]
# Available industries: ["general domain"]

CV_TASKS: List[str] = ["instance segmentation"]
# Available cv tasks: ["semantic segmentation", "instance segmentation"]

ANNOTATION_TYPES: List[str] = ["instance segmentation"]
# Available annotation types: ["semantic segmentation", "instance segmentation"]

RELEASE_YEAR: int = 2021
HOMEPAGE_URL: str = "https://www.kaggle.com/datasets/benediktgeisler/perrenial-plants-detection"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 350493
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/perrenial-plants"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[
    str
] = "https://www.kaggle.com/datasets/benediktgeisler/perrenial-plants-detection/download?datasetVersionNumber=2"
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = None
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

##################################
#### ? Templates. Do not edit ####
##################################

LICENSE_URLS = {
    "CCO": "https://creativecommons.org/publicdomain/zero/1.0/",
    "CC BY-SA 4.0": "https://creativecommons.org/licenses/by-sa/4.0/",
    "MIT License": "https://spdx.org/licenses/MIT.html",
}

LICENSE_TEXTS = {
    "CCO": "CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
    "CC BY-SA 4.0": "Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)",
    "MIT License": "MIT License",
}

CITATION_TEMPLATE = (
    "If you make use of the {project_name_full} data, "
    "please cite the following reference (to be prepared after the challenge workshop) "
    "in any publications:\n\n"
    "```\n@misc{{{project_name},\n"
    '\tauthor = "Benedikt Geisler",\n'
    '\ttitle = "{project_name_full}",\n'
    '\thowpublished = "{homepage_url}"\n}}\n```\n\n'
    "[🔗 Source]({homepage_url})"
)

LICENSE_TEMPLATE = "{project_name_full} data uses [{license_text}]({license_url})."

README_TEMPLATE = "# {project_name_full}\n\n{project_name} is a dataset for {cv_tasks} tasks."

##################################
###### ? Checks. Do not edit #####
##################################


def check_before_upload():
    fields_before_upload = [PROJECT_NAME, PROJECT_NAME_FULL]
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def check_after_upload():
    fields_after_upload = [
        LICENSE,
        INDUSTRIES,
        CV_TASKS,
        ANNOTATION_TYPES,
        RELEASE_YEAR,
        HOMEPAGE_URL,
        PREVIEW_IMAGE_ID,
        GITHUB_URL,
    ]
    if any([field is None for field in fields_after_upload]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")
