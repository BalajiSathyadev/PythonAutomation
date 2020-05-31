from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import uuid
import pandas as pd
import numpy as np
#driver=webdriver.Chrome(r'C:\Users\BALAJI_G2\Pictures\Dell-Internship\selenium\Software\chromedriver_win32 (2)')
driver = webdriver.Chrome(r'C:\Users\BALAJI_G2\Pictures\Dell-Internship\selenium\Software\chrome72\chromedriver.exe')
result=[]
data = pd.read_csv("data3.csv")
#print(data)
arr = data.to_numpy()
name=[]
url='https://www.tdscpc.gov.in/app/login.xhtml'
username='VVHTDS'
password='VVHTDS,2019'
deductor='CHEV14047F'
driver.get(url)
driver.find_element_by_xpath("//*[@id='userId']").send_keys(username)
driver.find_element_by_xpath("//*[@id='psw']").send_keys(password)
driver.find_element_by_xpath("//*[@id='tanpan']").send_keys(deductor)
time.sleep(20)
driver.find_element_by_xpath("//*[@id='clickLogin']").click()
driver.find_element_by_xpath("//*[@title='PAN Verification']").click()


for i in range(0,len(arr)):
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='pannumber']").send_keys(arr[i])

    driver.find_element_by_xpath("//*[@id='clickGo1']").click()
    time.sleep(2)
    na=driver.find_element_by_xpath("//*[@id='name']").text
    print(na)
    name.append(na)
    driver.find_element_by_xpath("//*[@id='pannumber']").clear()
    final = pd.DataFrame(name)
    final.to_csv('outputbagu.csv')







