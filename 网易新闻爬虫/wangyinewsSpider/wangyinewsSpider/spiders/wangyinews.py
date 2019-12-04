# coding=utf-8
import scrapy
import json
import os


# 创建目录
def mkdir(file_path):
    path = file_path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        return True
    else:
        return False

class WangyinewsSpider(scrapy.Spider):
    # 爬虫名字，必须唯一
    name = "wangyinews"
    # 允许采集的域名
    allowed_domains = ["news.163.com"]
    # 开始采集的网站
    start_urls = ["http://news.163.com/special/0001220O/news_json.js?0.11149173201495954"]

    # 解析响应数据，提取数据，或者网址等，response响应，网页源码
    def parse(self, response):
        # response相应返回的字符串
        string = response.body
        # 截取成标准的json字符串数据
        jsonStr = string[9:-1]
        # json字符串转换成json对象，gbk编码格式
        jsonData = json.loads(jsonStr.decode('gbk'))
        # 获取news对象
        news = jsonData.get('news')
        # 类别表示
        kinds = {0:'国内',1:'国际',2:'社会',3:'评论',4:'探索',5:'军事',6:'图片',7:'视频'}
        # 创建类别文件夹
        base_path = r'database'
        for name in kinds:
            mkdir(base_path+'/'+kinds[name])
        # 获取各个数组下的内容
        for items in news:
            for item in items:
                # 类别
                kind = kinds[item.get('c')]
                # 标题
                title = item.get('t')
                # 链接
                link = item.get('l')
                # 时间
                time = item.get('p')
                yield {'kind': kind, 'title': title, 'link': link, 'time': time}

