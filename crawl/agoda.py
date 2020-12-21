import time
from bs4 import BeautifulSoup
from selenium import webdriver, common
from Utils import write_json


from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

# da nang
# url = 'https://www.agoda.com/search?asq=u2qcKLxwzRU5NDuxJ0kOF6avr75lkfd3ANKpB0nqCtPL9RPqAWLLG2sFhiqVcu0TaHCCFa2By49WJavLIHbLR6LIG3cwwX4PVHnR7dUzaiYLYhBUbCNaKwckfB1RifzxkSJQDD1qJINJ5scjnnnW709F0gKS8sZXX3kYfaiVawgKkDMnL4g9wiFkiVcKUPLKPCmSQjSNwheWz%2Fqrvge81Q%3D%3D&city=16440&tick=637431277850&languageId=1&userId=8051031a-2eab-4c0f-958b-7b233c1ceea7&sessionId=wjnikndjbaimgtwladrdggc4&pageTypeId=1&origin=VN&locale=en-US&cid=-1&aid=178961&currencyCode=VND&htmlLanguage=en-us&cultureInfoName=en-US&ckuid=8051031a-2eab-4c0f-958b-7b233c1ceea7&prid=0&checkIn=2020-12-19&checkOut=2020-12-20&rooms=1&adults=2&children=0&priceCur=VND&los=1&textToSearch=Da%20Nang&travellerType=1&familyMode=off&hotelAccom=34&productType=-1'
# khanh hoa
# url = 'https://www.agoda.com/search?asq=u2qcKLxwzRU5NDuxJ0kOF4nXBEFt8WfGbmiC%2FljJXfi9R1xRXEs3RlLFc1I%2BnPwzgaWsZry4D8u2ZqHImbNnC0WE2jkGop%2B4ghmDo51%2BcGL0zQ9B%2Fk69LAz7dTM%2B4appTa9%2BsEP3GcmzLHUo%2FcdS1U9Z%2FuvkiW887FqC89c%2FgLV0pPzPHlbkGKgx1S4b%2F%2BqDUGhF5qJXFIAHM2mvssfgbg%3D%3D&city=2679&tick=637428180942&locale=en-us&ckuid=c3b8b7d1-bc20-49d8-b4fb-af6390f90949&prid=0&currency=VND&pageTypeId=103&realLanguageId=1&languageId=1&origin=VN&cid=-1&userId=c3b8b7d1-bc20-49d8-b4fb-af6390f90949&whitelabelid=1&loginLvl=0&storefrontId=3&currencyId=78&currencyCode=VND&htmlLanguage=en-us&cultureInfoName=en-us&machineName=hk-crweb-2011&trafficGroupId=4&sessionId=5okaqds3n1s5yvv2cj200muk&trafficSubGroupId=4&aid=130243&useFullPageLogin=true&cttp=0&isRealUser=true&checkIn=2020-12-05&checkOut=2020-12-06&rooms=1&adults=2&children=0&priceCur=VND&los=1&textToSearch=Nha%20Trang&travellerType=1&familyMode=off&hotelAccom=34&productType=-1'
# da lat
# url = 'https://www.agoda.com/search?city=15932&languageId=1&userId=f7bcfac2-f18c-46c6-8186-e837fc714967&sessionId=eqe5rtvaxmjusfwz3duf4n5f&pageTypeId=103&origin=VN&locale=en-US&cid=-1&aid=130243&currencyCode=VND&htmlLanguage=en-us&cultureInfoName=en-US&ckuid=f7bcfac2-f18c-46c6-8186-e837fc714967&prid=0&checkIn=2020-12-05&checkOut=2020-12-06&rooms=1&adults=2&children=0&priceCur=VND&los=1&textToSearch=Dalat&travellerType=1&familyMode=off&hotelAccom=34&productType=-1'
# ho chi minh
# url ='https://www.agoda.com/search?city=13170&checkIn=2020-12-13&los=1&rooms=1&adults=2&children=0&locale=en-us&ckuid=8051031a-2eab-4c0f-958b-7b233c1ceea7&prid=0&currency=VND&pageTypeId=5&realLanguageId=1&languageId=1&origin=VN&cid=-1&userId=8051031a-2eab-4c0f-958b-7b233c1ceea7&whitelabelid=1&loginLvl=2&storefrontId=3&currencyId=78&currencyCode=VND&htmlLanguage=en-us&cultureInfoName=en-us&memberId=262278541&machineName=hk-crweb-2005&trafficGroupId=4&sessionId=o0g1dp1htarn5crlmd2cmm2r&trafficSubGroupId=4&aid=130243&useFullPageLogin=true&cttp=0&isRealUser=true&checkOut=2020-12-14&priceCur=VND&textToSearch=Ho%20Chi%20Minh%20City&travellerType=1&familyMode=off&hotelAccom=34&productType=-1'
# ha noi 13, dalat 677-8, vung tau 346-4, da nang 785-9, ha long 234-3
urls = [
    'https://www.agoda.com/search?city=2758&checkIn=2020-12-13&los=1&rooms=1&adults=2&children=0&locale=en-us&ckuid=d779c89a-80d5-422a-8c77-54288397d23f&prid=0&currency=VND&pageTypeId=5&realLanguageId=1&languageId=1&origin=VN&cid=-1&userId=d779c89a-80d5-422a-8c77-54288397d23f&whitelabelid=1&loginLvl=0&storefrontId=3&currencyId=78&currencyCode=VND&htmlLanguage=en-us&cultureInfoName=en-us&machineName=hk-crweb-2008&trafficGroupId=4&sessionId=044tg3y24yvgg2ige0pado3w&trafficSubGroupId=4&aid=130243&useFullPageLogin=true&cttp=0&isRealUser=true&checkOut=2020-12-14&priceCur=VND&textToSearch=Hanoi&travellerType=1&familyMode=off&hotelAccom=34&productType=-1',
    'https://www.agoda.com/search?city=15932&checkIn=2020-12-13&los=1&rooms=1&adults=2&children=0&locale=en-us&ckuid=d779c89a-80d5-422a-8c77-54288397d23f&prid=0&currency=VND&pageTypeId=5&realLanguageId=1&languageId=1&origin=VN&cid=-1&userId=d779c89a-80d5-422a-8c77-54288397d23f&whitelabelid=1&loginLvl=0&storefrontId=3&currencyId=78&currencyCode=VND&htmlLanguage=en-us&cultureInfoName=en-us&machineName=hk-crweb-2010&trafficGroupId=4&sessionId=044tg3y24yvgg2ige0pado3w&trafficSubGroupId=4&aid=130243&useFullPageLogin=true&cttp=0&isRealUser=true&checkOut=2020-12-14&priceCur=VND&textToSearch=Dalat&travellerType=1&familyMode=off&hotelAccom=34&productType=-1',
    'https://www.agoda.com/search?city=17190&checkIn=2020-12-13&los=1&rooms=1&adults=2&children=0&locale=en-us&ckuid=d779c89a-80d5-422a-8c77-54288397d23f&prid=0&currency=VND&pageTypeId=5&realLanguageId=1&languageId=1&origin=VN&cid=-1&userId=d779c89a-80d5-422a-8c77-54288397d23f&whitelabelid=1&loginLvl=0&storefrontId=3&currencyId=78&currencyCode=VND&htmlLanguage=en-us&cultureInfoName=en-us&machineName=hk-crweb-2010&trafficGroupId=4&sessionId=044tg3y24yvgg2ige0pado3w&trafficSubGroupId=4&aid=130243&useFullPageLogin=true&cttp=0&isRealUser=true&checkOut=2020-12-14&priceCur=VND&textToSearch=Vung%20Tau&travellerType=1&familyMode=off&hotelAccom=34&productType=-1',
    'https://www.agoda.com/search?city=16440&checkIn=2020-12-13&los=1&rooms=1&adults=2&children=0&locale=en-us&ckuid=d779c89a-80d5-422a-8c77-54288397d23f&prid=0&currency=VND&pageTypeId=5&realLanguageId=1&languageId=1&origin=VN&cid=-1&userId=d779c89a-80d5-422a-8c77-54288397d23f&whitelabelid=1&loginLvl=0&storefrontId=3&currencyId=78&currencyCode=VND&htmlLanguage=en-us&cultureInfoName=en-us&machineName=hk-crweb-2012&trafficGroupId=4&sessionId=044tg3y24yvgg2ige0pado3w&trafficSubGroupId=4&aid=130243&useFullPageLogin=true&cttp=0&isRealUser=true&checkOut=2020-12-14&priceCur=VND&textToSearch=Da%20Nang&travellerType=1&familyMode=off&hotelAccom=34&productType=-1',
    'https://www.agoda.com/search?city=17190&checkIn=2020-12-13&los=1&rooms=1&adults=2&children=0&locale=en-us&ckuid=d779c89a-80d5-422a-8c77-54288397d23f&prid=0&currency=VND&pageTypeId=5&realLanguageId=1&languageId=1&origin=VN&cid=-1&userId=d779c89a-80d5-422a-8c77-54288397d23f&whitelabelid=1&loginLvl=0&storefrontId=3&currencyId=78&currencyCode=VND&htmlLanguage=en-us&cultureInfoName=en-us&machineName=hk-crweb-2010&trafficGroupId=4&sessionId=044tg3y24yvgg2ige0pado3w&trafficSubGroupId=4&aid=130243&useFullPageLogin=true&cttp=0&isRealUser=true&checkOut=2020-12-14&priceCur=VND&textToSearch=Vung%20Tau&travellerType=1&familyMode=off&hotelAccom=34&productType=-1'
]

url = 'https://www.agoda.com/search?city=2758&checkIn=2020-12-13&los=1&rooms=1&adults=2&children=0&cid=1830024&tag=d302e7cb-d60d-40b8-a7c3-6bd1dcf84c07&gclid=Cj0KCQiA8dH-BRD_ARIsAC24umYQh_sIyNPbmQOJm5IkdiUG0fxPfyxS_BoS_GKL1q-opfR_NW05fUAaAlaJEALw_wcB&languageId=1&userId=8051031a-2eab-4c0f-958b-7b233c1ceea7&sessionId=o0g1dp1htarn5crlmd2cmm2r&pageTypeId=1&origin=VN&locale=en-US&aid=82361&currencyCode=VND&htmlLanguage=en-us&cultureInfoName=en-US&memberId=262278541&ckuid=8051031a-2eab-4c0f-958b-7b233c1ceea7&prid=0&checkOut=2020-12-14&priceCur=VND&textToSearch=Hanoi&travellerType=1&familyMode=off&hotelAccom=34&productType=-1'
# for i in range(5):
try:
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox(executable_path="/home/m/CodeSpace/SeleniumPrj/geckodriver")
    driver.get(url)

    stt = 0
    time.sleep(5)
    base_path = "../output/hanoi/hanoi_data_root_"
    # if i == 0:
    #     base_path = "../output/hanoi/hanoi_data_root_"
    # elif i == 1:
    #     base_path = "../output/dalat/dalat_data_root_"
    # elif i == 2:
    #     base_path = "../output/vungtau/vungtau_data_root_"
    # elif i == 3:
    #     base_path = "../output/danang/danang_data_root_"
    # else:
    #     base_path = "../output/halong/halong_data_root_"

    for page in range(13):

        # if 0:
        #     stt = stt + 98
        #     SCROLL_PAUSE_TIME = 0.5
        #
        #     # Get scroll height
        #     last_height = driver.execute_script("return document.body.scrollHeight")
        #
        #     while True:
        #         # Scroll down to bottom
        #         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #
        #         # Wait to load page
        #         time.sleep(SCROLL_PAUSE_TIME)
        #
        #         # Calculate new scroll height and compare with last scroll height
        #         new_height = driver.execute_script("return document.body.scrollHeight")
        #         if new_height == last_height:
        #             break
        #         last_height = new_height
        #     driver.find_element_by_id('paginationNext').click()
        #     time.sleep(5)
        #     continue
        # else:
        SCROLL_PAUSE_TIME = 2
        count = 0
        while True:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo({start}, {end});".format(start=count * 1080, end=(count + 1) * 1080))

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            count += 1

            if count == 30:
                break

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        all_divs = soup.find('div', {'id': 'contentContainer'})
        ids = all_divs.find_all(lambda tag: bool(tag.get("data-hotelid")))
        data_set = []

        for id in ids:
            data = {}
            stt += 1
            data['stt'] = stt

            try:
                id_hotel = id['data-hotelid']
                data['id_hotel'] = id_hotel
            except Exception:
                data['id_hotel'] = 'null'

            try:
                link_tag = id.find('a')
                link = 'www.agoda.com' + str(link_tag['href'])
                data['link'] = link
            except Exception:
                data['link'] = 'null'

            try:
                name_tag = id.find('h3')
                name = name_tag.contents[0]
                data['name'] = name
            except AttributeError:
                data['name'] = 'null'

            try:
                addr_tag = id.find('span', {'class': 'Address__Text'})
                addr = addr_tag.contents[0]
                data['address'] = addr
            except AttributeError:
                data['address'] = 'null'

            try:
                tip_tags = id.find_all('li', {'data-selenium': 'pill-item'})
                all_tip = ''
                for tip_tag in tip_tags:
                    tip = tip_tag.contents[0]
                    all_tip = all_tip + str(tip) + ', '
                data['all tips'] = all_tip
            except AttributeError:
                data['all tips'] = 'null'

            try:
                div_tag = id.find('div', {'class': 'ReviewWithDemographic'})
                span_tags = div_tag.find_all('span')
                point_tag = span_tags[2]
                point = point_tag.contents[0]
                data['total point'] = point
            except AttributeError:
                data['total point'] = 'null'

            try:
                star_tag = id.find(lambda tag: bool(tag.get("title")))
                star = star_tag['title']
                data['rank'] = star
            except Exception:
                data['rank'] = 'null'

            try:
                first_cor_tag = id.find('div', {'data-element-name': 'first-cor'})
                first_cor = first_cor_tag.contents[0]
                data['first price'] = first_cor
            except AttributeError:
                data['first price'] = 'null'

            try:
                final_price_tag = id.find('span', {'data-selenium': 'display-price'})
                final_price = final_price_tag.contents[0]
                data['final price'] = final_price
            except AttributeError:
                data['final price'] = 'null'

            data_set.append(data)
        write_json(data_set, base_path + str(page) + '.json' )

        button_nextpage = driver.find_element_by_id('paginationNext')
        # button_nextpage = driver.find_element_by_id('footer-partner-hotels')
        try:
            button_nextpage.click()
        except common.exceptions.ElementClickInterceptedException:
            ActionChains(driver).click(button_nextpage).perform()
        time.sleep(5)
    driver.quit()
except common.exceptions.NoSuchElementException:
    print("done")


