import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://es.wikipedia.org/wiki/Wikipedia")



Wikipedia = driver.find_elements_by_css_selector("#searchInput")
Wikipedia.clear()
Wikipedia.send_keys("En qué año se hizo el primer proceso automático")
button = driver.find_element_by_xpath("//button[@id='']")

time.sleep(1000)

driver.quit()






