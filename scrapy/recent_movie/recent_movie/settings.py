# -*- coding: utf-8 -*-

# Scrapy settings for todayMoive project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'recent_movie'

SPIDER_MODULES = ['recent_movie.spiders']
NEWSPIDER_MODULE = 'recent_movie.spiders'
#ITEM_PIPELINES = {'recent_movie.pipelines.RecentMoviePipeline': 300}

ITEM_PIPELINES = {
    'recent_movie.pipelines.RecentMoviePipeline': 300
}
