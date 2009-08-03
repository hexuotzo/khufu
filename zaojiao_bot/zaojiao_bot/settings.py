# Scrapy settings for zaojiao_bot project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here
#
#     http://doc.scrapy.org/ref/settings.html
#
# Or you can copy and paste them from where they're defined in Scrapy:
# 
#     scrapy/conf/default_settings.py
#

import zaojiao_bot

PROJECT_NAME = 'zaojiao_bot'

BOT_NAME = PROJECT_NAME
BOT_VERSION = '1.0'

SPIDER_MODULES = ['zaojiao_bot.spiders']
NEWSPIDER_MODULE = 'zaojiao_bot.spiders'
TEMPLATES_DIR = '%s/templates' % zaojiao_bot.__path__[0]
DEFAULT_ITEM_CLASS = 'zaojiao_bot.items.ZaojiaoBotItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

LOGFILE = '/home/yanxu/khufu/zaojiao_bot/zaojiao_bot.log'
