# -*- coding: utf-8 -*-
import scrapy
import sys

from english_crawl.items import EnglishCrawlItem

reload(sys)
sys.setdefaultencoding("utf-8")#设置默认编码为utf-8
class EnglishSpiderSpider(scrapy.Spider):
    name = 'english_spider'
    allowed_domains = ['cn.bing.com']
    offset = 0
    base_URL = "https://cn.bing.com/dict/service?q=%e7%89%a9%e7%90%86&offset="
    end_URL = '&dtype=sen&&qs=n&form=Z9LH5&sp=-1&pq=%E7%89%A9%E7%90%86&sc=8-2&sk=&cvid=93A8F03149F64A7899E591C107A76A16'
    start_urls = ['https://cn.bing.com/dict/service?q=%e7%89%a9%e7%90%86&offset='+str(offset)+'&dtype=sen&&qs=n&form=Z9LH5&sp=-1&pq=%E7%89%A9%E7%90%86&sc=8-2&sk=&cvid=93A8F03149F64A7899E591C107A76A16']

    def parse(self, response):
        english_sentence = response.xpath("//div[@class='sen_en']")
        chinese_sentence = response.xpath("//div[@class='sen_cn']")
        english_list = []
        for sub_sentence in english_sentence:
            sentence = sub_sentence.xpath('./span/text() | ./a/text()').extract()
            str1 = "".join(sentence)
            english_list.append(str1)
        chinese_list = []
        for sub_sentence in chinese_sentence:
                sentence = sub_sentence.xpath('./a/text()').extract()
                str1 = "".join(sentence)
                chinese_list.append(str1)

        for sentence_index in range(len(english_list)):
            item = EnglishCrawlItem()
            item["english"] = english_list[sentence_index]
            item["chinese"] = chinese_list[sentence_index]
            print(item["chinese"])
            yield item
            # print sub_sentence.xpath('./a/text()').extract()

        if self.offset < 1000:
            self.offset += 10
            print "=========================="
            print self.offset
            url = self.base_URL + str(self.offset) + self.end_URL
            yield scrapy.Request(url,callback=self.parse)


