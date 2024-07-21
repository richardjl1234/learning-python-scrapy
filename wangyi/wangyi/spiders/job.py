import scrapy


class JobSpider(scrapy.Spider):
    name = "job"
    # allowed_domains = ["163.com"]
    allowed_domains = ["itcast.com"]
    # start_urls = ["https://hr.163.com/job-list.html"]
    start_urls = ["https://www.itcast.cn/channel/teacher.shtml#ajavaee"]

    def parse(self, response):
        # extract the data
        with open('res.html', 'wb') as f:
            f.write(response.body)


        node_list = response.xpath('//*[@id="p-job-list"]/div[2]/div[2]/div/div/div[2]/div/div/div')
        print(len(node_list))


        # page down
