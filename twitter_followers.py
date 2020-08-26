import time
from selenium import webdriver
import time
path = "C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(path)
account=input("inter the account name such @AliNaserMohamed")
driver.get('https://twitter.com/'+account)
time.sleep(4)
follow_box = driver.find_element_by_xpath("//a[@href='/AliNaserMohamed/followers']")
print(follow_box.text)


