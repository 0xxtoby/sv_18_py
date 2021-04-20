import re

import scrapy
from scrapy import cmdline


class SvSpider(scrapy.Spider):
    name = 'sv'

    def start_requests(self):
        url = ['https://18cute.fun/booklist?tag=%E5%85%A8%E9%83%A8&area=-1&end=-1']

        yield scrapy.Request(url=url[0], callback=self.parse)

        for i in range(2,3):
            url_s=f'https://18cute.fun/booklist?page={i}&tag=%E5%85%A8%E9%83%A8&area=-1&end=-1'
            yield scrapy.Request(url=url_s,callback=self.parse)

    def parse(self, response):
        f= open('html/1.html','wb')
        f.write(response.body)
        # print(rsponse.body)

        html=response.text

        # url_list=response.xpath('/html/body/section[2]/div/ul/li/div/a/@href').extrcat()
        url_list=re.findall('<a href="(.*?)" title=".*?" ',html)
        print(url_list)

        for url in url_list:
            uurl = url.split('/')[-1]
            print(uurl)



if __name__ == '__main__':
    cmdline.execute("scrapy crawl sv  ".split())
