##Site

[developers](https://developers.arcgis.com/python)


##Install

`Conda install -c esri arcgis`

但是我用这种方法安装的时候，widget总有问题，觉得还是从源代码安装比较好，如果能拿到源代码的话。

```
Install steps for developers:

Install Anaconda for Python 3.5 from https://www.continuum.io/downloads
Download or clone this repo. git clone https://github.com/ArcGIS/geosaurus.git
conda install -c conda-forge ipywidgets
conda install pandas
pip install -e ./src (for using latest source code)
jupyter nbextension install --py --sys-prefix arcgis (for enabling the map widget for Jupyter notebook)
jupyter nbextension enable --py --sys-prefix arcgis (to initialize the map widget in the browser every time the notebook loads)
```




##
