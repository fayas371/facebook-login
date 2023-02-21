import pandas as pd
# Python program to demonstrate Facebook Login using excel
from selenium import webdriver
data=pd.read_excel("password.xlsx")
list1=data['Username'].tolist()
list2=data['password'].tolist()
for i in range(3):

    driver = webdriver.Chrome()
    driver.get("https://mbasic.facebook.com")

# Creating a Reference of Form For Finding Email and Password
    form = driver.find_element('xpath', "//form[@id ='login_form']")

    email = form.find_element('name', "email")
    password = form.find_element("name","pass")
#for sending the data from excel
    email.send_keys(list1[i])
    password.send_keys(list2[i])

    submit_button = driver.find_element('xpath', "//input[@type ='submit']")

    submit_button.click()
# Error Password in Output
# Because didn't used my real password here
