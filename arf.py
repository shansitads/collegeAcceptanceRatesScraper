from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import sys

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


file1 = open('collegeList.csv','r')
file2 = open('acceptanceRates.txt','w')

PATH = input('Enter chromedriver path: ') # '/Users/shansitads/CodingProjects/PythonProjects/chromedriver'
driver = webdriver.Chrome(PATH)

for line in file1.readlines():
    driver.get('https://www.google.com/')

    collegeName = line[:-1]

    searchTerm = collegeName+' acceptance rate'
    frame = driver.find_element('name','q').send_keys(searchTerm)
    time.sleep(2)

    driver.find_element('name','btnK').click()
    time.sleep(2)

    try:
        info = driver.find_element(By.CLASS_NAME, 'kp-hc')
        file2.write(collegeName+': '+info.text[0:-5]+'\n')
    except:
        print(collegeName+': not found')
        file2.write('\n')

    time.sleep(2)


driver.close()
file1.close()
file2.close()