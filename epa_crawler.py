

import shutil

import csv


# ==============================
# ==============================
# common
# ==============================
# ==============================

# import os
# import sys
# import re
# import time
# import random
# import traceback
# import sein
# from sein import String as ss

# import io
# import os
# import sys
# from pprint import pprint
# import re
# from time import sleep
# from pylon import all_files
# from pylon import datalines
# from pylon import windows
# from pylon import enumrange
# import platform

# import random
# import math
# import fnmatch
# import inspect
# import datetime
# import itertools
# from itertools import groupby

# from collections import OrderedDict
# from collections import defaultdict
# from collections import namedtuple
# from collections import Counter
# from collections import deque

# from pprint import pprint

# from pylon import dedupe
# from pylon import rotate
# from pylon import flatten
# from pylon import transpose
# from pylon import rand
# from pylon import all_files
# from pylon import datalines
# from pylon import datamatrix
# from pylon import file_timer
# from pylon import windows
# from pylon import transpose
# from pylon import random_split
# from pylon import load_title
# from pylon import load_csv














# ==============================
# ==============================
# crawler
# ==============================
# ==============================

# import html2text
# import requests
# sess = requests.Session()
# from pyquery import PyQuery
# from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium.common.exceptions import TimeoutException, NoSuchElementException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver import FirefoxProfile






# from pylon import datalines
def datalines(data, sample=None):
  '''返回一段文字中有效的行(非空行, 且不以注释符号开头)'''
  ret = []
  for l in data.splitlines():
    line = l.strip()
    if line and not line.startswith('#'):
      ret.append(line)
  if sample:
    return ret[:sample]
  else:
    return ret

import requests
session = requests.Session()





state_ids = '''

'''






def test_requests_with_cookie():
  cookie_text = '''

    Host: ofmpub.epa.gov
    Connection: keep-alive
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
    Referer: https://ofmpub.epa.gov/apex/sfdw/f?p=108:103:::NO:RP::
    Accept-Encoding: gzip, deflate, br
    Accept-Language: zh-CN,zh;q=0.8
    Cookie: ORA_WWV_APP_108=ORA_WWV-lkCV6C-ZDyEH-33g7wGsz6yA; _ceg.s=otyph1; _ceg.u=otyph1; has_js=1; _ga=GA1.2.1107459310.1501516229; _gid=GA1.2.2014277172.1502115954; acs.t=%7B%22_ckX%22%3A1509292394728%2C%22rid%22%3A%22de35431-94229866-5529-4d1f-2e785%22%2C%22cp%22%3A%7B%22url%22%3A%22https%3A%2F%2Fofmpub.epa.gov%2Fapex%2Fsfdw%2Ff%3Fp%3D108%3A103%3A%3A%3ANO%3ARP%3A%3A%22%2C%22VisitorID%22%3A%22%22%2C%22section_www2%22%3A%22N%22%2C%22section_www%22%3A%22Y%22%2C%22nlquery%22%3A%22N%22%2C%22GA_UID%22%3A%221107459310.1501516229%22%2C%22terms%22%3A%22%22%2C%22browser%22%3A%22Chrome%2059%22%2C%22os%22%3A%22Mac%22%2C%22flash%22%3A%2226.0%22%2C%22hosted%22%3A%22true%22%2C%22referrer%22%3A%22%22%2C%22site%22%3A%22epa.gov%22%2C%22trigger_version%22%3A%2219.0.33%22%2C%22pv%22%3A%224%22%2C%22locale%22%3A%22en%22%2C%22dn%22%3A%22default%22%7D%2C%22pl%22%3A1%2C%22pv%22%3A4%2C%22def%22%3A0%2C%22browsepv%22%3A4%2C%22dn%22%3A%22default%22%2C%22i%22%3A%22d%22%7D

  '''

  cookie_text = '''
   ORA_WWV_APP_108=ORA_WWV-lkCV6C-ZDyEH-33g7wGsz6yA;
   _ceg.s=otyph1;
   _ceg.u=otyph1;
   has_js=1;
   _ga=GA1.2.1107459310.1501516229;
   _gid=GA1.2.2014277172.1502115954;
   acs.t={"_ckX":1509292394728,"rid":"de35431-94229866-5529-4d1f-2e785","cp":{"url":"https://ofmpub.epa.gov/apex/sfdw/f?p=108:103:::NO:RP::","VisitorID":"","section_www2":"N","section_www":"Y","nlquery":"N","GA_UID":"1107459310.1501516229","terms":"","browser":"Chrome 59","os":"Mac","flash":"26.0","hosted":"true","referrer":"","site":"epa.gov","trigger_version":"19.0.33","pv":"4","locale":"en","dn":"default"},"pl":1,"pv":4,"def":0,"browsepv":4,"dn":"default","i":"d"}
  '''





  # cookies = {line.split(':')[0]: line.split(':')[1].strip() for line in datalines(cookie_text)}
  # print(cookies)

  url = 'https://ofmpub.epa.gov/apex/sfdw/f?p=108:103::CSV::::'

  response = session.get(url, cookies=cookie_text)
  print(response.text)







# https://ofmpub.epa.gov/apex/sfdw/f?p=108:103:::NO:RP::
# <a href="f?p=108:103::CSV::::" id="SFDWIR_download_CSV">
#   <img src="/i_owpub/ws/download_csv_64x64.gif" alt="CSV" title="CSV">
# </a>

# water_system_summary_{state_code}

