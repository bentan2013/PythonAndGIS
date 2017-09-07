# ArcGIS API for Python

## 介绍与点评

1. 主要针对ArcGIS Online和 ArcGIS Portal的用户，使用python api能够很方便的完成很多繁琐的功能，并提供一定的展示能力。

2. 主要功能和特点（注意，基本上所有的功能都需要基于Online或者Portal）
	- 分析栅格矢量
	- 地理编码，逆编码
	- 制图
	- 管理Online，Portal上的用户，内容，资源，群组等
	- 上传，发布，分享数据
	- 与Jupyter, Pandas等集成较好

如果购买了Online或者Portal，但是不想用鼠标点点点的话，这个API比较适合你。
如果单纯是想展示一个数据，不需要持久的host服务，管理数据，不使用Esri相关的分析功能，那么不需要使用这个API。

目前该API的数据管理，展示，分析完全和Portal绑定在一起，不支持换用其他公司产品作为内核。可视化效果比较差，自身也没有host服务的能力。没有后端，也没有前段，用在自己的产品中的话，他的定位比较尴尬，我觉得只能定位于工具层。

## 资源链接

- [主页](https://developers.arcgis.com/python/)

- [在线实验](https://notebooks.esri.com/user/mMSRCUS0hstp/tree)

## 唯一推荐安装方式

### 1. 安装Conda

安装最新版的Anaconda (Python 3x)

### 2. 安装 arcgis 包

`conda install -c esri arcgis`

就完成了，接下来是测试安装效果

`jupyter notebook` 启动jupyter

运行
```
from arcgis.gis import GIS
gis = GIS()
gis.map()
```
如果看到了[地图](https://github.com/bentan2013/PythonAndGIS/blob/master/esri/show_map.ipynb)，就成功了。更多的代码参考官网代码和示例

![](http://esri.github.io/arcgis-python-api/notebooks/nbimages/guide_getstarted_InstallAndSetup_02.PNG)


至于其他的安装方法，离线包，源码编译，ArcGIS Pro安装，等等。都能成功，但是我个人不推荐，因为不利于更新。
而且由于ArcGIS Python API的代码与Esri的业务联系太紧密，对于非Esri公司人员，研究意义不大。

**但是**我觉得源码写得很好，从学习python的角度，是可以深入学习一下的。

对于非web端，例如桌面端和移动端，Esri产品体系的ArcGIS Runtime SDK是一个不错的工具，2D部分还是很完善的。3D部分的产品有ArcGIS Earth和Drone2Map。