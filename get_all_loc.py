import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

#open the browser
s = Service("C:\Program Files\msedgedriver.exe")
browser = webdriver.Edge(service=s)

#open the link
browser.get("https://en.wikipedia.org/wiki/Areas_of_Chennai")

#wait for the page to load fully
time.sleep(2)

# find the element in which the results are in
result = browser.find_element(by=By.XPATH, value='//*[@id="mw-content-text"]/div[1]/table/tbody')
string=str(result.text) #get the text value of the necessary result
string_to_list=string.split(sep='\n') #convert it into a list
string_to_list.pop(0) #delete the header
print(string_to_list) #printing the list
browser.close()