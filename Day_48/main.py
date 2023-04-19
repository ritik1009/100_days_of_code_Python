from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_driver = "C:\Devlopment\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get("https://www.python.org/")

event_name = []
time = driver.find_elements(By.CSS_SELECTOR,".event-widget time")
time_array = [i.get_attribute('datetime') for i in time]
event_name = driver.find_elements(By.CSS_SELECTOR, ".event-widget .menu a")
event_name = [i.text for i in event_name]

data_dic={}
for i in range(len(time_array)):
    dic = {
        'time':time_array[i],
        'name':event_name[i]
    }
    data_dic[i] = dic

print(data_dic)
'''
# getting the elemnt using the id
price = driver.find_element(By.CLASS_NAME,"a-price-whole")
print(price.text)

#getting the element using the name
search = driver.find_element(By.NAME,"field-keywords")
print("\n Search Text",search.get_attribute("placeholder"))

# getting element using the css Selector
search_css = driver.find_element(By.CSS_SELECTOR,".nav-search-field input")
print("\n Search Text CSS",search_css.get_attribute("placeholder"))

# getting element using the XPATH
search_xpath = driver.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]')
print("\n Search Text CSS",search_xpath.get_attribute("placeholder"))
'''