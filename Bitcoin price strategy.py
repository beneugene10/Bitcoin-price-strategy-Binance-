from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
driver=webdriver.Chrome("/Users/beneu/Downloads/chromedriver" )
driver.get("https://www.binance.com/tw/trade/pro/BTC_USDT")

#Find the Price
def Bitcoin_price():
    html=requests.get("https://www.binance.com/tw/trade/pro/BTC_USDT").content
    data=BeautifulSoup(html,"html.parser")
    data1 = data.find_all("span",{"class":"sc-1yysggs-4 cdRUYO"})
    price=[float(i.text) for i in data1][0]
    return price

#How long you want to monitor Bitcoin price(price updated every 1 minute)
for j in range(int(input("Please enter how long you want to monitor Bitcoin price(Time unit: minute):"))):
    print("Current Price:")
    print(Bitcoin_price())

#First Strategy:Reach the target point and set a market order
    if Bitcoin_price()<8000:
        driver.find_element_by_xpath("/html//a[@id='TabbedOrderFormsMargin-a-exchangeMarket']").click()
        driver.find_element_by_xpath("//div[@id='__next']//main/div/div/div[@wrap='nowrap']/div[2]/div[2]/div[2]/div/div[@wrap='nowrap']/div[1]/form/div[4]//input[@value='100%']").click()
        break

#Second Strategy:Reach the target point and set a stop-limit order
    if Bitcoin_price()<10000:
        driver.find_element_by_xpath("//a[@id='TabbedOrderFormsMargin-a-exchange']/span[.='現貨']").click()
        driver.find_element_by_xpath("//div[@id='__next']//main/div/div/div[@wrap='nowrap']/div[2]/div[2]/div[2]/div/div[2]//ul/li[3]/span").click()
        driver.find_element_by_xpath("/html//span[@id='TabbedOrderFormsMargin-a-exchangeStopLimit']").click()
        driver.find_element_by_xpath("/html//input[@id='FormRow-BUY-stopPrice']").send_keys(int(0.96*Bitcoin_price()))
        driver.find_element_by_xpath("/html//input[@id='FormRow-BUY-stopLimitPrice']").send_keys(int(0.95*Bitcoin_price()))
        driver.find_element_by_xpath("//div[@id='__next']//main/div/div/div[@wrap='nowrap']/div[2]/div[2]/div[2]/div/div[@wrap='nowrap']/div[1]/form/div[5]//input[@value='100%']").click()
    break
