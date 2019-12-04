# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
reload(sys)
sys.setdefaultencoding('utf8')

class WangyidocumentsspiderPipeline(object):
    # 获取item对象，将抓取的内容以txt文件格式存储到指定路径下
    def process_item(self, item, spider):
        link = item['link'].encode('utf-8')
        title = item['title'].encode('utf-8')
        time = item['time'].encode('utf-8')
        source = item['source'].encode('utf-8')
        editor = item['editor'].encode('utf-8')
        text = "".join(item['text'])
        file_name = title+".txt"
        file = open(item['path']+'/'+file_name,'w')
        file.write(link+ '\n' + title+ '\n' + time+ '\n' + source+ '\n'+editor+ '\n'+text)
        file.close()
        return item