# -*- coding: utf-8 -*-
__author__ = 'Mark'
__date__ = '2018/4/15 10:18'

import scrapy
from urllib import parse
import re


class ZhihuLoginSpider(scrapy.Spider):
    name = "zhihu"
    allowed_domains = ["www.zhihu.com"]
    start_urls = ['https://www.zhihu.com/']

    # question的第一页answer的请求url
    start_answer_url = "https://www.zhihu.com/api/v4/questions/{0}/answers?include=data%5B%2A%5D.is_normal%2" \
                       "Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2" \
                       "Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2" \
                       "Cis_thanked%2Cis_nothelp%2Cis_labeled%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2" \
                       "A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit={1}&offset={2}&sort_by=default"

    headers = {
        "HOST": "www.zhihu.com",
        "Referer": "https://www.zhizhu.com",
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/68.0.3440.106 Safari/537.36"
    }

    custom_settings = {
        "COOKIES_ENABLED": True,
        "DOWNLOAD_DELAY": 1.5,
    }

    def parse(self, response):
        """
        提取出html页面中的所有url 并跟踪这些url进行一步爬取
        如果提取的url中格式为 /question/xxx 就下载之后直接进入解析函数
        """

    def parse_question(self, response):
        # 处理question页面， 从页面中提取出具体的question item
        pass

    def start_requests(self):
        from selenium import webdriver
        import time
        PATH = "/Users/yiyang/Desktop/phantomjs-2.1-2.1-macosx/bin/phantomjs"
        browser = webdriver.PhantomJS(PATH)

        browser.get("https://www.zhihu.com/signin")
        browser.find_element_by_css_selector(".SignFlow-accountInput.Input-wrapper input").send_keys('18565619007')
        time.sleep(1)
        browser.find_element_by_css_selector(".SignFlow-password input").send_keys('yy6831062')
        time.sleep(2)
        browser.find_element_by_css_selector(".Button.SignFlow-submitButton").click()
        time.sleep(3)
        browser.get("https://www.zhihu.com/")
        time.sleep(6)
        zhihu_cookies = browser.get_cookies()
        print(zhihu_cookies)
        cookie_dict = {}
        import pickle
        for cookie in zhihu_cookies:
            # base_path = path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            # f = open(base_path + "/zhihu/" + cookie['name'] + '.zhihu', 'wb')
            # pickle.dump(cookie, f)
            # f.close()
            cookie_dict[cookie['name']] = cookie['value']
        browser.close()
        return [scrapy.Request(url=self.start_urls[0], dont_filter=True, cookies=cookie_dict, headers=self.headers)]
