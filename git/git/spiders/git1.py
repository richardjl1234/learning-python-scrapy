from typing import Iterable
import scrapy
import scrapy.resolver


class Git1Spider(scrapy.Spider):
    name = "git1"
    allowed_domains = ["github.com"]
    start_urls = ["https://github.com/richardjl1234"]


    # update the start_requests method to add the cookies , cookies will be hardcoded in this method
    def start_requests(self) -> Iterable[scrapy.Request]:
        url = self.start_urls[0]

        temp_text = """
        _octo=GH1.1.2003289776.1720863235; preferred_color_mode=light; tz=America%2FDetroit; _device_id=cf2791fc9ff9b820206644556fce31fd; tz=America%2FDetroit; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; saved_user_sessions=64469809%3AAhUqVXwtr6Rkp7kywOUeomodNIJAz5YzOQbaPtwQiGz7C12H; user_session=AhUqVXwtr6Rkp7kywOUeomodNIJAz5YzOQbaPtwQiGz7C12H; __Host-user_session_same_site=AhUqVXwtr6Rkp7kywOUeomodNIJAz5YzOQbaPtwQiGz7C12H; logged_in=yes; dotcom_user=richardjl1234; _gh_sess=L%2FC11LtQZeUd4kzyBs6BqDR1FXz3beDRh8nT3Y5R8RY%2Buq5XHlK9D5HSS3CNf9qwjsHohD6i0Gta3IDjHC3iryAvLl238onifDmFjkQ4mb3XLkRj3bi%2BGSWl%2FxRffHO08Sd2O4Iffy2oFBHkno212QhpIZ7lspOonqq3tiPS3aLiPSawiacqryaTb1psK7tXB06yZ6cY2hcSQUcYd5wkkqZC0qSkNEwQ3RtChtxdfZ9pIGcOpD1e2hesUSQFU73QoVApHO%2FC2xsfqX5Dc996oxPgNF3ufR7hcUPvJDYl2xoVUFFHo32a4odgddZcyrBiQ544yA3pnakUcXRX8FhO4RcWgXZ0AQuOG%2BK5fXmVWL3X0mgFEKnASP5eC%2B8ddIdSSQw1lIc3dzwz8Nwv3KFo5z3vdWBkrK7w2Gv0lEUVAKGageAs5RVX%2Bcpdia2EFyEjjU6fwCQG4PV8S5dMzM1rxz0uMYeIZ5ZA9DMsbBN%2BXLED6f7irV0shf2Qf9%2FSDQUzaIqjw26%2Fg%2BmxwKjj9ASkrbjkotdqN6kSNIHKXqfz8SELVr8NKgb1a9iYOiDgtMbKwBlToJQyVgCjwTE2bgXF7G27DHZDMvkEY4ZTRWyajL%2FOKh%2F50%2FwY7Djr8xM04T15SmglXwrFBFfGMr3xeFXo4ki8YkDZs5s26kal%2Fk67jpu0Kwi1xsCsab1GFIyw%2FtWvPwlsQeFOMU8QeDB6Lrw%2F4UTIRWqrj84sej%2BwGt2tKoHY98mURJJkX%2BZTOBE9JorPLD1vOPhW7i1%2F0lWrVMAjM%2FvMyIsyzsSEa18WG3eT1jwJkzuEPaCxnmUegwKp4vk8Gt29ezMXnowFYEdH815UrL7X9XU2RqcwptC6jUi0qr3CwkgwRHeLQU03Rm8%3D--V6mlOFehVywWMOPY--1Yy0omb%2FUSGDYqnOgpMABA%3D%3D
"""
        cookies = {data.split('=')[0]: data.split('=')[1] for data in temp_text.split(';')}
        print(cookies)

        yield scrapy.Request(
            url = url, 
            callback= self.parse, 
            cookies=cookies
        )




    def parse(self, response):
        with open("res.html", 'wb') as f: 
            f.write(response.body)
