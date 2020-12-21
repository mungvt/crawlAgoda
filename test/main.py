import time
from bs4 import BeautifulSoup
from selenium import webdriver
import re

from selenium.webdriver import ActionChains

url = 'https://www.agoda.com/search?city=16440&languageId=1&userId=09c9f292-c021-4959-ab8d-4bcd6052dc6a&sessionId=s0sogddai0rdcr5tdno2latq&pageTypeId=103&origin=VN&locale=en-US&cid=-218&aid=130589&currencyCode=VND&htmlLanguage=en-us&cultureInfoName=en-US&ckuid=09c9f292-c021-4959-ab8d-4bcd6052dc6a&prid=0&checkIn=2020-11-14&checkOut=2020-11-15&rooms=1&adults=2&children=0&priceCur=VND&los=1&textToSearch=Da%20Nang&travellerType=1&familyMode=off&productType=-1'

driver = webdriver.Chrome()
# driver = webdriver.Firefox(executable_path="/home/m/CodeSpace/SeleniumPrj/geckodriver")
driver.get(url)

stt = 0
time.sleep(5)


for page in range(1):

    SCROLL_PAUSE_TIME = 4

    # Get scroll height
    count = 0
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo({start}, {end});".format(start=count * 1080, end=(count + 1)*1080))

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        count += 1

        if count == 10:
            break

    # SCROLL_PAUSE_TIME = 0.5
    #
    # # Get scroll height
    # last_height = driver.execute_script("return document.body.scrollHeight")
    #
    # while True:
    #     # Scroll down to bottom
    #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #
    #     # Wait to load page
    #     time.sleep(SCROLL_PAUSE_TIME)
    #
    #     # Calculate new scroll height and compare with last scroll height
    #     new_height = driver.execute_script("return document.body.scrollHeight")
    #     if new_height == last_height:
    #         break
    #     last_height = new_height

    elements = driver.find_elements_by_class_name('ReviewWithDemographic')
    print(len(elements))
    print(elements)

    for element in elements:
        ActionChains(driver).move_to_element(element).perform()
        time.sleep(3)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    all_divs = soup.find('div', {'id': 'contentContainer'})

    ids = all_divs.find_all(lambda tag: bool(tag.get("data-hotelid")))

    #
    # for id in ids:
    #     stt += 1
        # print(str(page + 1) + '_' + str(stt))
        # try:
        #     id_hotel = id['data-hotelid']
        #     print(id_hotel)
        # except Exception:
        #     print('null_id')


        #
        # try:
        #     link_tag = id.find('a')
        #     link = 'www.agoda.com' + str(link_tag['href'])
        #     print(link)
        # except Exception:
        #     print('null_link')
        #
        # try:
        #     name_tag = id.find('h3')
        #     name = name_tag.contents[0]
        #     print(name)
        # except AttributeError:
        #     print('null_name')

        #
        # try:
        #     addr_tag = id.find('span', {'class': 'Address__Text'})
        #     addr = addr_tag.contents[0]
        #     print(addr)
        # except AttributeError:
        #     print('null_addr')
        #
        # try:
        #     tip_tags = id.find_all('li', {'data-selenium': 'pill-item'})
        #     all_tip = ''
        #     for tip_tag in tip_tags:
        #         tip = tip_tag.contents[0]
        #         all_tip = all_tip + str(tip) + ', '
        #     print(all_tip)
        # except AttributeError:
        #     print('null_tip')
        #
        # try:
        #     star_tag = id.find(lambda tag: bool(tag.get("title")))
        #     star = star_tag['title']





        #     print(star)
        # except Exception:
        #     print('null_star')
        #
        # try:
        #     first_cor_tag = id.find('div', {'data-element-name': 'first-cor'})
        #     first_cor = first_cor_tag.contents[0]
        #     print(first_cor)
        # except AttributeError:
        #     print('null_first_cor')
        #
        # try:
        #     final_price_tag = id.find('span', {'data-selenium': 'display-price'})
        #     final_price = final_price_tag.contents[0]
        #     print(final_price)
        # except AttributeError:
        #     print('null_final_price')

    # button_nextpage = driver.find_element_by_id('paginationNext')
    # ActionChains(driver).click(button_nextpage).perform()
    t = 0
    review_lists = soup.find_all('ul', {'class': 'demographics-review-list'})
    for review_list in review_lists:
        review_names = review_list.find_all('span', {'class': 'review-bar__name'})
        review_points = review_list.find_all('strong', {'class': 'review-bar__point'})
        t += 1
        print(t)
        print(review_list)
        for i in range(len(review_names)):
            # print(review_names[i].contents[0] + ':' + review_points[i].contents[0])
            print(review_names[i].contents[0])
            print(review_points[i].contents[0])
        # for review in review_list:

# driver.quit()

