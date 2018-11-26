"""
create by 维尼的小熊 on 2018/11/23

"""
__autor__ = 'yasin'

from scrapy.cmdline import execute

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(['scrapy', 'crawl', 'jobbole'])
