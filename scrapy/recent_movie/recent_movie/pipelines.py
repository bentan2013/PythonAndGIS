# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class RecentMoviePipeline(object):

    def __init__(self):
        self.f = None

    def open_spider(self, spider):
        self.f = open('../movie.txt', 'w')
        self.f.write("Recent Movie are:\n")
        self.f.close()
        self.f = open('../movie.txt', 'a')

    def close_spider(self, spider):
        if self.f is not None:
            self.f.write("The End\n")
            self.f.close()

    def process_item(self, item, spider):
        name = item['movie_name'][0].encode('utf8')
        self.f.write(name + "\n")
        return item
