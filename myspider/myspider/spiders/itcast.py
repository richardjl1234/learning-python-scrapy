import scrapy
# import pandas as pd
from myspider.items import MyspiderItem


class ItcastSpider(scrapy.Spider):
    name = "itcast"
    allowed_domains = ["itcast.cn"]
    # STEP 1, update the start url
    start_urls = ["https://www.itcast.cn/channel/teacher.shtml#ajavaee"]

    # STEP 2, define the parse method
    # parse the result from the response
    def parse(self, response):
        # parse the result from the response
        # define the parse method
        with open('itcast.html', 'wb') as f:
            f.write(response.body)
        # get alll the teacher's 
        teacher_list = response.xpath('//div[@class="li_txt"]')
        print(len(teacher_list))

        for node in teacher_list: 
            item = MyspiderItem()
            # get name
            item['name'] = node.xpath('./h3/text()').extract_first()
            # get title
            item['title'] = node.xpath('./h4/text()').extract_first()
            # get description
            item['desc'] = node.xpath('./p/text()').extract_first() 

            yield item

        print(response.url)
        print(response.request.url)
        print(response.headers)
        print(response.request.headers)

