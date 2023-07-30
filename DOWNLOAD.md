Dataset **Perrenial Plants Detection** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/Y/Y/HP/qBGrLmgbOXmDajPKhKWdADXlBzkLJ0hpxpF0JbGoaaRsA5iLEXEoI9CtdF72t1xiNSiukGvEso9qvAgJfCUfOL4rgejd2Yj55806USGmpj1nkOK68JaAZQSy0gKX.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Perrenial Plants Detection', dst_path='~/dtools/datasets/Perrenial Plants Detection.tar')
```
The data in original format can be 🔗[downloaded here](https://www.kaggle.com/datasets/benediktgeisler/perrenial-plants-detection/download?datasetVersionNumber=2)