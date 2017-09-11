引用来源，《Python网络爬虫实战》，不过这本书不太推荐，很多错别字和错误的地方，代码也不标准。

不知道是否过时了。。文中的例子是自己改的，因为书中的网站已经不能访问了。

## 创建工程
可以通过下面的语句来创建工程

```
cd

cd code/crawler/scrapyProject/

scrapy startproject todayMovie

tree todayMovie
```

文件树如下图所示：

```
C:\PROJECTS\PYTHONANDGIS\SCRAPY\TODAYMOIVE
│  scrapy.cfg
│
└─todayMovie
    │  items.py
    │  pipelines.py
    │  settings.py
    │  __init__.py
    │
    └─spiders
            __init__.py
```

## 创建spider

```
cd todayMovie

scrapy genspider wuHanMoiveSpider jycinema.com
```

scrapy genspider命令创建一个名字为wuHanMoiveSpider的爬虫脚本。这个脚本搜索的域为jycinema.com。

在本次的爬虫项目示例中，需要修改、填空的只有4个文件，它们分别是items.py、settings.py、pipelines.py、wuHanMoiveSpider.py。

- 其中items.py决定爬取哪些项目，
- wuHanMoiveSpider.py决定怎么爬，
- settings.py决定由谁去处理爬取的内容，
- pipelines.py决定爬取后的内容怎样处理。

## 爬虫编写

目标：这个爬虫只爬取最近电影名字

```
表达式	描述
nodename	选取此节点的所有子节点。
/	从根节点选取。
//	从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。
.	选取当前节点。
..	选取当前节点的父节点。
@	选取属性。
```

## 运行
```
scrapy crawl wuHanMovieSpider
```

## pycharm中调试