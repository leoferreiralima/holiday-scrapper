from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from driver import get_firefox_driver

if __name__ == "__main__":

  try:
    browser = get_firefox_driver(True)

    browser.get("https://www.feriados.com.br")
    timeout_in_seconds = 10
    
    # WebDriverWait(browser, timeout_in_seconds).until(ec.presence_of_element_located((By.CSS_SELECTOR, 'resultado_busca')))
    html = browser.page_source
    soup = BeautifulSoup(html, features="html.parser")
    citiesOptions = soup.find("select", id="cidade").find_all("option")

    for cityOption in citiesOptions:
      print(cityOption["value"])
    # print(soup)

    # print(citySelect)
  except TimeoutException:
    print("I give up...")
  finally:
    browser.quit()
