# -*- coding: utf-8 -*-
import csv
import scrapy
from wangyidocumentsSpider.items import WangyidocumentsspiderItem


class WangyidocumentsSpider(scrapy.Spider):
    # 爬虫名字，必须唯一
    name = 'wangyidocuments'
    # 允许采集的域名
    allowed_domains = ['news.163.com']
    kinds = []
    start_urls = []
    index = 0
    base_path = r'/home/magicstar/Desktop/project/wangyinewsSpider/database'
    # 从第一个爬虫中读取新闻列表里的内容
    with open("/home/magicstar/Desktop/project/wangyinewsSpider/news.csv",'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # 添加开始采集的网站
            start_urls.append(row['link'])
            # 添加该网站的类别信息
            kinds.append(row['kind'])
    file.close()


    def parse(self, response):
        link = response.url
        # 构造txt文件保存的路径
        path = self.base_path + '/' + self.kinds[self.index]
        # XPath：从HTML中提取数据语法
        # 标题
        title = response.xpath('//*[@id="epContentLeft"]/h1/text()').extract_first()
        # 时间
        time = response.xpath('//*[@id="epContentLeft"]/div[1]/text()').extract_first()
        # 来源
        source = response.xpath('//*[@id="ne_article_source"]/text()').extract_first()
        # 正文
        text = response.xpath('//*[@id="endText"]/p/text()').extract()
        # 编辑
        editor = response.xpath('//*[@id="endText"]/div/span[2]/text()').extract_first()
        self.index = self.index + 1
        # 保存数据到item对象中，方便等会的管道处理成txt文件保存
        item = WangyidocumentsspiderItem()
        item['path'] = path
        item['title'] = title
        item['time'] = time
        item['source'] = source
        item['text'] = text
        item['editor'] = editor
        item['link'] = link
        yield {'path':path,'link':link,'title': title, 'time': time, 'source': source, 'text': text, 'editor': editor}



