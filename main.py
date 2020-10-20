from selenium import webdriver
import pandas as pd
import numpy as np
import time
def get_articles(nombre_de_page=10):
    articles = []
    links = []
    options = webdriver.ChromeOptions()
    options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
    chrome_driver_binary = "C:/Windows/chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
    #get links
    for x in range(1,nombre_de_page):
        link = "https://www.jumia.ma/samsung/?page="+str(x)
        driver.get(link)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        for i in range(1, 40):
            name = driver.find_element_by_xpath('//*[@id="jm"]/main/div[2]/div[2]/section/div[1]/article[' + str(i) + ']/a/div[2]/h3').text
            price = driver.find_element_by_xpath('//*[@id="jm"]/main/div[2]/div[2]/section/div[1]/article['+str(i)+']/a/div[2]/div[1]').text
            products = [name,price]
            articles.append(products)
    return articles

if __name__ == "__main__" :
    p = get_articles(nombre_de_page=20)
    df = pd.DataFrame(p)