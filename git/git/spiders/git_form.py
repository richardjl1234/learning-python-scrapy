import scrapy


class GitFormSpider(scrapy.Spider):
    name = "git_form"
    allowed_domains = ["github.com"]
    start_urls = ["https://github.com/login"]

    def parse(self, response):
        print('--------0----------')
        # get the token from the login page
        token = response.xpath('//*[@name="authenticity_token"]/@value').extract_first()

        # get the input from the console, promt text is please input form data in raw format
        print("Please input form data in raw format:")
        print("Example: commit: Sign in\nauthenticity_token: xxxxxxxxxxxxxxx\nadd_account:\nlogin:\npassword:\nwebauthn-conditional: undefined\njavascript-support: true\nwebauthn-support: supported\nwebauthn-iuvpaa-support: unsupported\nreturn_to: https://github.com/login\nallow_signup:\nclient_id:\nintegration:\nrequired_field_eff4:\ntimestamp: 1720871116860\ntimestamp_secret: xxxxxxxxxxxx\n")  
        print("copy the raw form data from the chrome developer console..")
        print("in the network section, remember to check the preserve log as ON")
        print("Please input form data in raw format, input END when finished the input: ")
        print("------------------------------------------------")
        # continue to get the input from the console, until the user types END to stop receiving data
        raw_form_data  = ''
        while True: 
            text = input()
            if text == "END": break
            raw_form_data += text

        # get the post data from the login page
        form_data = {data.split(':')[0].strip(): data.split(':')[1].strip() for data in raw_form_data.split('\n') if ':' in data}
        form_data['authenticity_token'] = token 

        for k, v in form_data.items(): print(k, v)

        # sent the post request
        yield scrapy.FormRequest(
            url = "https://github.com/session",
            formdata = form_data,
            callback= self.after_login
        )

    def after_login(self, response):
        print('--------1----------')
        yield scrapy.Request("https://github.com/richardjl1234", callback=self.check_login)


    def check_login(self, response):
        print('-------2----------')
        with open("res_form.html", 'wb') as f: 
            f.write(response.body)

        xpath = '//*[@class="repo"]/text()'

        # get the elements based on the xpath
        elements = response.xpath(xpath).extract()
        print(elements)
            





    
