from scrapy import cmdline

cmdline.execute("scrapy crawl wangyidocuments -o documents.csv".split())#该命令可将数据导出为csv格式

