引用来源，《Python网络爬虫实战》，不过这本书不太推荐，很多错别字和错误的地方，代码也不标准。

不知道是否过时了。。文中的例子是自己改的，因为书中的网站已经不能访问了。所以说明和代码分开看吧。
因为代码是我后来改的。

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

文件结构大概如上面所示，第一次通过模板创建了基本的文件结构之后，二周目就可以自己创建文件了。不需要通过模板。
- 创建一个文件夹，叫spiders，里面创建一个自己的spider，从Scrapy.Spider继承，注意需要赋值名字
- 创建一个items.py文件，里面定义一个item类，同样给一个名字
- 创建一个pipelines.py文件，里面顶一个pipeline，从object继承
- 创建一个settings。注意需要定义spider模块和文件夹，和使用的pipelines
- 在外层创建一个cfg，否则识别不了这个文件夹是scrapy的文件，从而就不能一层层的解析出各个spider

## 爬虫编写

目标：这个爬虫只爬取最近电影名字

PartI: spider
- 在spider的starturl中设置需要爬取的url
- 通过xpath等来获取爬取的内容

xpath的简易结构如下：


```
表达式	描述
nodename	选取此节点的所有子节点。
/	从根节点选取。
//	从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。
.	选取当前节点。
..	选取当前节点的父节点。
@	选取属性。
```

似乎需要yield一下各个item，要不然pipeline不能运行，不知道具体原理是什么

Part II: item

只需告诉它一个名字就行

Part III: pipelines

设置开启关闭爬虫和运行过程中需要做的事情。
大概就是开启爬虫时，调用一次，爬取数据中每个item 调用(yield)的时候运行一次，关闭爬虫的时候运行一次

Part IV: settings
大概就是设置pipeline和优先级



## 运行
```
scrapy crawl wuHanMovieSpider
```

## pycharm中调试
我在这儿创建了一个文件，pycharm_debugger.py，里面就是，我们在控制台运行 crawl spider实际运行的语句，在pycharm的config中按代码中设置好，就能调试了。