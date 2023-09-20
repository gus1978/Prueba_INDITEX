import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.google.com/")


buscador = driver.find_element_by_css_selector("#APjFqb")
buscador.clear()
buscador.send_keys("automatizacion")
button = driver.find_element_by_name("input")

time.sleep(1000)


driver.quit()




