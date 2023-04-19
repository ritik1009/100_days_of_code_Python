from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_driver = "C:\Devlopment\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element(By.CSS_SELECTOR,'#articlecount a')
print(article_count.text)
#article_count.click()

# Find Element by link

#content_portals = driver.find_element(By.LINK_TEXT,"Content portals")
#content_portals.click()


search = driver.find_element(By.NAME,'search')
search.send_keys("Python")
search.send_keys(Keys.ENTER)

