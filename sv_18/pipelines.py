# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os

import requests
from itemadapter import ItemAdapter


class Sv18Pipeline:
    def process_item(self, item, spider):


        dir_name='.//data//'+item['name']
        if not os.path.exists(dir_name):  # 判断文件夹是否存在
            os.mkdir(dir_name)
            print('=================='+dir_name+'==========================')
            i = 0
            for url in item['urls']:
                i = i + 1
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:84.0) Gecko/20100101 Firefox/84.0'
                }

                r = requests.get(url, headers=headers).content
                f = open(dir_name+ '//' + str(i) + '.jpg', 'wb')
                f.write(r)
                print('保存成功：' + dir_name+ '//' + str(i) + '.jpg')
                if os.listdir(dir_name)==len(item['urls'])+1:
                    print("===========满===============")

        elif os.listdir(dir_name)< len(item['urls'])+1:
            print('==================' + dir_name + '==========================')
            i = 0
            for url in item['urls']:
                i = i + 1
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:84.0) Gecko/20100101 Firefox/84.0'
                }

                r = requests.get(url, headers=headers).content
                f = open(dir_name + '//' + str(i) + '.jpg', 'wb')
                f.write(r)
            print('保存成功：' + dir_name + '//' + str(i) + '.jpg'+'====未满=====')
        else:
            print("文件已存在")


        return item
