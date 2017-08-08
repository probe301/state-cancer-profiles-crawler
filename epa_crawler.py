
from pyquery import PyQuery
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.support.ui import Select
import os
import time
import csv

def record_csv(headers, content, path):
  with open(path, 'w', encoding='utf-8') as f:
    f_csv = csv.writer(f, lineterminator='\n')
    f_csv.writerow(headers)
    f_csv.writerows(content)
  print('save csv done', path)



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



class DriverFindElementByCSS:
  ''' usage:
      driver / css(pat)  => one element
      driver // css(pat)  => [element list]
  '''
  def __call__(self, pat):
    self.pat = pat
    return self
  def __rtruediv__(self, driver):
    return driver.find_element_by_css_selector(self.pat)
  def __rfloordiv__(self, driver):
    return driver.find_elements_by_css_selector(self.pat)

css = DriverFindElementByCSS()



def get_windows_firefox_driver():
  gecko_path = '/Users/probe/git/Lottery_Hedge_Crawler/geckodriver'
  gecko_path = 'C:/Program Files/Mozilla Firefox/geckodriver.exe'
  profile = webdriver.FirefoxProfile()
  # profile.set_preference("browser.download.dir","/Users/probe/git/StateCancerProfilesCrawler/");
  # profile.setPreference("browser.download.folderList", 2);
  profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream,text/csv");
  profile.set_preference("browser.download.dir",os.getcwd())

  # if proxies:
  #   profile.set_preference("network.proxy.type", 1)
  #   profile.set_preference("network.proxy.socks", "127.0.0.1")
  #   profile.set_preference("network.proxy.socks_port", 1080)
  #   profile.set_preference("network.proxy.socks_version", 5)
  #   # profile.setAssumeUntrustedCertificateIssuer(False)
  #   profile.update_preferences()
  driver = webdriver.Firefox(firefox_profile=profile,
                             executable_path=gecko_path)
  return driver



def fetch_one_page(driver, state_code):
  driver.get('https://ofmpub.epa.gov/apex/sfdw/f?p=108:200::::::')
  print('get US map page...')
#   state_code = '09'
  selector = Select(driver / css('#P200_STATE'))
  selector.select_by_value(state_code)
  search_button = driver / css('#P200_SEARCH')
  search_button.click()
  print('click search button...')
  WebDriverWait(driver, 120).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, '#SFDWIR_row_select'))
  )
  change_all_selector = Select(driver / css('#SFDWIR_row_select'))
  change_all_selector.select_by_value('100000')
  print('click show all rows...')
  WebDriverWait(driver, 120).until(
      EC.invisibility_of_element_located((By.CSS_SELECTOR, 'span.u-Processing-spinner'))
  )
  WebDriverWait(driver, 400).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, '.t-fht-tbody'))
  )

  time.sleep(10)
  print('prepare to fetch')
  tables_header, tables_body = driver // css('.a-IRR-table')
  headers = [td.text.replace('\n', ' ') for td in tables_header // css('th')]


  content = []
  for row in PyQuery(tables_body.get_attribute('outerHTML'))('tr'):
    row = PyQuery(row)
    if not row:
      continue
    row = [td.text for td in row('td')]
    if row and row[0]:
      content.append(row)
  record_csv(headers, content, 'epa_water_system_summary_{}_[{}].csv'.format(state_code, len(content)))


state_codes = '''
  AK AL AR AZ CA CO CT DC DE FL GA HI IA ID IL IN KS KY LA MA MD ME MI MN MO MS MT NC ND NE NH NJ NM NV NY OH OK OR PA RI SC SD TN TX UT VA VT WA WI WV WY AS MP PR VI 01 02 03 04 05 06 07 08 09 10 NN
'''
state_codes = state_codes.strip().split(' ')


driver = get_windows_firefox_driver()

for state_code in state_codes[:3]:
  fetch_one_page(driver=driver, state_code=state_code)