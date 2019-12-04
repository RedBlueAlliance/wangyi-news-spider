from scrapy import cmdline

cmdline.execute("scrapy crawl wangyinews -o news.csv".split())#该命令可将数据导出为csv格式


