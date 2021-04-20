import re

import scrapy
from scrapy import cmdline
from sv_18.items import Sv18Item


class SvSpider(scrapy.Spider):
    name = 'sv'

    def start_requests(self):
        url = ['https://18cute.fun/booklist?tag=%E5%85%A8%E9%83%A8&area=-1&end=-1']

        yield scrapy.Request(url=url[0], callback=self.parse)

        # for i in range(2,3):
        #     url_s=f'https://18cute.fun/booklist?page={i}&tag=%E5%85%A8%E9%83%A8&area=-1&end=-1'
        #     yield scrapy.Request(url=url_s,callback=self.parse)

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

            url_data = 'https://18cute.fun/chapter/' + uurl

            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
                ,'Host': '18cute.fun'
            }
            cookies={ 'PHPSESSID':'3pgdq8toqni3e4uoc966i0pts2'
                    ,'_pk_ref.10.8d30':'%5B%22%22%2C%22%22%2C1618929727%2C%22https%3A%2F%2Ftheporndude.com%2F%22%5D'
                    ,'_pk_ses.10.8d30':'1'
                    ,'nav_switch':'booklist'
                    ,'_pk_id.10.8d30':'c5b309affd244777.1611059840.7.1618929766.1618929727.'
                    ,
                     }
            yield scrapy.Request(url=url_data,callback=self.jpg,headers=headers,cookies=cookies)


    def jpg(self,response):
        item=Sv18Item();

        # print(response.text)

        jpg_url=re.findall('<img class="lazy" data-original="(.*?)" ',response.text)
        print(jpg_url)
        jap_name = re.findall('<a class="comic-name" href=".*?" title=".*?">(.*?)</a>', response.text)
        print(jap_name)
        nno=re.split('\(',jap_name[0])[-1]
        sum=re.split('P\)',nno)[0]
        print(sum)

        item['name']=jap_name[0]
        item['urls']=jpg_url
        item['sum']=sum
        yield item




if __name__ == '__main__':
    cmdline.execute("scrapy crawl sv  ".split())
