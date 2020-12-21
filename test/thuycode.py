from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = 'https://www.agoda.com/vi-vn/search?asq=CV8PluF9Y22Ww8gXoGNHEF8SPUCS79CWCSp98aqBrzmNVq58SzLbPKs3qBGIptzBOIUOgFZWw%2BifeaLz7ZPvWPfMRQ2rNUsFt8KRalfsBhh4ogKey8Qi%2BOZMBuaf1JnhxDftxzeeUD4leEKmfR6%2FVXpf4eOvMDsIFAn4oylDy9ZRlW4r%2F3lUz4J0oQchUPlFikrSP3cx4715NAYXt0MMqbpgNINyoa0UTfRk8xlU16c%3D&city=13170&cid=1729665&tick=637401301995&languageId=24&userId=ec63a88d-6893-48bd-98c0-3248689fdddc&sessionId=aaasmyv4bdzqpzuwpmxink2v&pageTypeId=103&origin=VN&currency=VND&locale=vi-VN&aid=169310&currencyCode=VND&htmlLanguage=vi-VN&cultureInfoName=vi-VN&memberId=260384531&ckuid=00000000-0000-0000-0000-000000000000&checkIn=2020-11-05&checkOut=2020-11-06&rooms=1&adults=2&children=0&priceCur=VND&los=1&textToSearch=H%E1%BB%93%20Ch%C3%AD%20Minh&travellerType=1&familyMode=off&productType=-1'

driver = webdriver.Firefox(executable_path="/geckodriver")
driver.get(url)

f = open("../list_hotel_hanoi.txt", "w")
time.sleep(10)
# a=driver.find_element_by_xpath("//button[@data-selenium='searchButton']")
# a.click()

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
for i in range(0, 10):
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    time.sleep(10)

try:
    while True:
        list_hotel = driver.find_elements_by_xpath("//li[@data-selenium='hotel-item']")
        print(len(list_hotel), "   ")
        next = driver.find_element_by_id("panigationNext")
        next.click()
except:
    pass