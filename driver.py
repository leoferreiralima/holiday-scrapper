from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

def get_firefox_driver(is_headless = False):
  options = webdriver.FirefoxOptions()
  
  if(is_headless):
    options.add_argument('--headless')

  return webdriver.Firefox(options=options, service=Service(GeckoDriverManager().install()))