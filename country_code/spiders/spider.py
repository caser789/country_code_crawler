from ..items import CountryCodeItem as Item
from scrapy import Spider, Request, Selector


class CountryCodeSpider(Spider):

    name = 'country_code'
    allowed_domains = ['countrycode.org']

    def start_requests(self):
        url = "https://countrycode.org/"
        yield Request(url, callback=self.parse)

    def parse(self, response):
        table2_tr_xpath = "//div[@class='visible-sm visible-xs']//tr"
        # codes = response.xpath(code_xpath).extract()
        t2_trs = response.xpath(table2_tr_xpath).extract()
        for ele in t2_trs[1:]:
            sel = Selector(text=ele)
            iso_code_xpath = "//td[3]/text()"
            country_name_xpath = "//a/text()"
            iso_code = sel.xpath(iso_code_xpath).extract()[0][0:2]
            country_name = sel.xpath(country_name_xpath).extract()[0]
            item = Item()
            item['country_name'] = country_name
            item['country_iso_code'] = iso_code
            yield item
