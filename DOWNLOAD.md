Dataset **Perrenial Plants Detection** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzE5NDhfUGVycmVuaWFsIFBsYW50cyBEZXRlY3Rpb24vcGVycmVuaWFsLXBsYW50cy1kZXRlY3Rpb24tRGF0YXNldE5pbmphLnRhciIsICJzaWciOiAiaWlRYXZybkZnU0xRdDBORzNHalhBb3NQYmZid2RXSnRpc3BaTkxZWXk3dz0ifQ==)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Perrenial Plants Detection', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://www.kaggle.com/datasets/benediktgeisler/perrenial-plants-detection/download?datasetVersionNumber=2).