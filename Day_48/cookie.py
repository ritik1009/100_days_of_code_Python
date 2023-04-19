from selenium import webdriver
from selenium.webdriver.common.by import By
import time
chrome_driver = "C:\Devlopment\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID,"cookie")
start = time.time()
while True:
    start_time = time.time()
    while time.time() - start_time <5:
        cookie.click()
        #print("Inside")
    options = driver.find_elements()
    #print(start_time)
    option = driver.find_elements(By.CSS_SELECTOR,"#store div")
    class_=[]
    option_ids = []
    cost_list = driver.find_elements(By.CSS_SELECTOR, "#store b")
    cost = [int(i.text.split(" ")[-1].replace(',','')) for i in cost_list]
    score = int(driver.find_element(By.ID,'money').text)

    for i in option:
        class_.append(i.get_attribute("class"))
        option_ids.append(i.get_attribute("id"))
    print("\n Cost",cost)
    for in_,op in enumerate(option_ids):
        try:
            if class_[in_]=="" and cost[in_] < score:
                print("\n option_price", op)
                option_click = driver.find_element(By.ID,op)
            else:
                print("\n not selected",op)
        except:
            pass
    try:
        print("\n Options to be clicked",option_click.text)
        option_click.click()
    except:
        pass
    if time.time()- start > 300:
        break


            


