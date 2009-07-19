#!/usr/bin/env python

import os
os.environ.setdefault('SCRAPYSETTINGS_MODULE', 'zaojiao_bot.settings')

from scrapy.command.cmdline import execute
execute()
