import time

from bs4 import BeautifulSoup, element
from selenium import webdriver, common
import json
from selenium.webdriver import ActionChains
from Utils import write_json

option = webdriver.ChromeOptions()
option.add_argument('headless')


def crawl_root_data():
    # da nang
    url = 'https://www.agoda.com/search?city=16440&locale=en-us&ckuid=09c9f292-c021-4959-ab8d-4bcd6052dc6a&prid=0&currency=VND&pageTypeId=103&realLanguageId=1&languageId=1&origin=VN&cid=-1&userId=09c9f292-c021-4959-ab8d-4bcd6052dc6a&whitelabelid=1&loginLvl=0&storefrontId=3&currencyId=78&currencyCode=VND&htmlLanguage=en-us&cultureInfoName=en-us&machineName=hk-crweb-2009&trafficGroupId=4&sessionId=bvg0jxxktjbke4bcemqfc4sl&trafficSubGroupId=4&aid=130243&useFullPageLogin=true&cttp=0&isRealUser=true&checkIn=2020-12-10&checkOut=2020-12-11&rooms=1&adults=2&children=0&priceCur=VND&los=1&textToSearch=Da%20Nang&travellerType=1&familyMode=off&hotelAccom=34&productType=-1'
    # khanh hoa
    # url = 'https://www.agoda.com/search?asq=u2qcKLxwzRU5NDuxJ0kOF4nXBEFt8WfGbmiC%2FljJXfi9R1xRXEs3RlLFc1I%2BnPwzgaWsZry4D8u2ZqHImbNnC0WE2jkGop%2B4ghmDo51%2BcGL0zQ9B%2Fk69LAz7dTM%2B4appTa9%2BsEP3GcmzLHUo%2FcdS1U9Z%2FuvkiW887FqC89c%2FgLV0pPzPHlbkGKgx1S4b%2F%2BqDUGhF5qJXFIAHM2mvssfgbg%3D%3D&city=2679&tick=637428180942&locale=en-us&ckuid=c3b8b7d1-bc20-49d8-b4fb-af6390f90949&prid=0&currency=VND&pageTypeId=103&realLanguageId=1&languageId=1&origin=VN&cid=-1&userId=c3b8b7d1-bc20-49d8-b4fb-af6390f90949&whitelabelid=1&loginLvl=0&storefrontId=3&currencyId=78&currencyCode=VND&htmlLanguage=en-us&cultureInfoName=en-us&machineName=hk-crweb-2011&trafficGroupId=4&sessionId=5okaqds3n1s5yvv2cj200muk&trafficSubGroupId=4&aid=130243&useFullPageLogin=true&cttp=0&isRealUser=true&checkIn=2020-12-05&checkOut=2020-12-06&rooms=1&adults=2&children=0&priceCur=VND&los=1&textToSearch=Nha%20Trang&travellerType=1&familyMode=off&hotelAccom=34&productType=-1'
    # da lat
    # url = 'https://www.agoda.com/search?city=15932&languageId=1&userId=f7bcfac2-f18c-46c6-8186-e837fc714967&sessionId=eqe5rtvaxmjusfwz3duf4n5f&pageTypeId=103&origin=VN&locale=en-US&cid=-1&aid=130243&currencyCode=VND&htmlLanguage=en-us&cultureInfoName=en-US&ckuid=f7bcfac2-f18c-46c6-8186-e837fc714967&prid=0&checkIn=2020-12-05&checkOut=2020-12-06&rooms=1&adults=2&children=0&priceCur=VND&los=1&textToSearch=Dalat&travellerType=1&familyMode=off&hotelAccom=34&productType=-1'
    driver = webdriver.Chrome()
    driver.get(url)

    stt = 0
    time.sleep(3)

    for page in range(3):
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        SCROLL_PAUSE_TIME = 1
        count = 0
        while True:
            driver.execute_script("window.scrollTo({start}, {end});".format(start=count * 1080, end=(count + 1) * 1080))
            time.sleep(SCROLL_PAUSE_TIME)
            count += 1
            if count == 32:
                break

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

            data_set.append(data)

        with open('../output/data_agoda' + str(page) + '.json', 'w') as outfile:
            json.dump(data_set, outfile, indent=4)
        time.sleep(3)
        button_nextpage = driver.find_element_by_id('paginationNext')
        try:
            button_nextpage.click()
        except common.exceptions.ElementClickInterceptedException:
            ActionChains(driver).click(button_nextpage).perform()
        time.sleep(3)


def crawl_detail_data():
    r = 0
    root_path = ''
    detail_path = ''
    # null_list = [21, 31, 38, 42, 43, 45, 56, 57, 65, 69, 77, 85, 92, 93, 114, 116, 127, 131, 133, 135, 136, 138, 142, 144, 146, 150, 152, 153, 157, 160, 163, 164, 165, 166, 167, 168, 169, 170, 175, 177, 179, 182, 187, 189, 190, 193, 194, 195, 198, 204, 211, 213, 214, 217, 219, 221, 223, 225, 226, 227, 228, 231, 233, 235, 236, 239, 241, 243, 258, 261, 262, 263, 264, 265, 266, 267, 268, 270, 271, 272, 273, 274, 275, 276, 277, 278, 280, 281, 283, 286, 287, 289, 306, 307, 309, 310, 312, 313, 314, 315, 317, 324, 326, 330, 334, 335, 339]
    # null_list = [38, 45, 56, 77, 103, 114, 129, 142, 152, 153, 158, 170, 192, 193, 204, 208, 211, 213, 222, 224, 225, 229, 232, 237, 241, 257, 261, 267, 276, 278, 283, 286, 287, 289, 293, 306, 307, 309, 310, 312, 313, 317, 324, 330, 334, 339]
    for i in range(6):
        if i == 0:
            continue
            root_path = "../output/data_root_after_filter_null_value/hanoi_data_root_total.json"
            detail_path = "../output/data_detail_crawled/hanoi/hanoi_data_detail_"
        elif i == 1:
            continue
            root_path = "../output/data_root_after_filter_null_value/dalat_data_root_total.json"
            detail_path = "../output/data_detail_crawled/dalat/dalat_data_detail_"
        elif i == 2:
            continue
            root_path = "../output/data_root_after_filter_null_value/danang_data_root_total.json"
            detail_path = "../output/data_detail_crawled/danang/danang_data_detail_"
        elif i == 3:
            root_path = "../output/data_root_after_filter_null_value/vungtau_data_root_total.json"
            detail_path = "../output/data_detail_crawled/vungtau/vungtau_data_detail_"
        elif i == 4:
            continue
            root_path = "../output/data_root_after_filter_null_value/halong_data_root_total.json"
            detail_path = "../output/data_detail_crawled/halong/halong_data_detail_"
        else:
            continue
            root_path = "../output/data_root_after_filter_null_value/hcm_data_root_total.json"
            detail_path = "../output/data_detail_crawled/hcm/hcm_data_detail_"
        with open(root_path) as json_file:
            data_set = []
            data_root = json.load(json_file)
            count = 0
            for p in data_root:
                stt = p['stt']
                count += 1
                # if stt in null_list:
                if count % 100 == 0:
                    write_json(data_set, detail_path + str(count) + '.json')
                    data_set = []
                    print('Done a file')
                    print(time.ctime())

                url = 'https://' + p['link']
                print('stt: ' + str(stt))
                print(url)
                driver = webdriver.Chrome(options=option)
                try:
                    driver.get(url)
                except common.exceptions.WebDriverException:
                    continue
                time.sleep(3)
                html = driver.page_source
                soup = BeautifulSoup(html, "html.parser")
                detail_data = {'stt': p['stt'], 'link': p['link']}

                # name
                try:
                    name_tag = soup.find('h1')
                    name = name_tag.contents[0]
                    detail_data['name'] = name
                except AttributeError:
                    detail_data['name'] = 'null'

                # address
                # try:
                #     addr_tag = soup.find('span', {'data-selenium': 'hotel-address-map'})
                #     addr = addr_tag.contents[0]
                #     detail_data['address'] = addr
                # except AttributeError:
                #     detail_data['address'] = 'null'

                # tips
                # try:
                #     all_tip_tag = soup.find('div', {'data-selenium': 'RoomGridFilter-filterGroup'})
                #     all_tip = []
                #     for tip in all_tip_tag.contents:
                #         tags = tip.find_all('div')
                #         if not tags:
                #             tags = tip.find_all('span')
                #         all_tip.append(tags[-1].contents[0])
                #     detail_data['all tips'] = all_tip
                #
                # except AttributeError:
                #     detail_data['all tips'] = 'null'

                # total point
                try:
                    total_point_tag = soup.find('div', {'class': 'ReviewScore-Number'})
                    if total_point_tag is None:
                        total_point_tag = soup.find('span', {'class': 'Review__ReviewFormattedScore'})
                    total_point = total_point_tag.contents[0]
                    detail_data['total point'] = total_point
                except AttributeError:
                    detail_data['total point'] = 'null'

                # detail point
                try:
                    detail_point_tag = soup.find('div', {'class': 'Review-travelerGrade-Cell'})
                    detail_point = {}
                    for cp in detail_point_tag.contents:
                        grade_category_tag = cp.find('span', {'class': 'Review-travelerGradeCategory'})
                        grade_score_tag = cp.find('span', {
                            'class': 'Review-travelerGradeScore Review-travelerGradeScore--highlight'})
                        if grade_score_tag is None:
                            grade_score_tag = cp.find('span', {
                                'class': 'Review-travelerGradeScore Review-travelerGradeScore--'})
                        grade_category = grade_category_tag.contents[0]
                        grade_score = grade_score_tag.contents[0]
                        detail_point[grade_category] = grade_score
                    detail_data['detail point'] = detail_point
                except AttributeError:
                    detail_data['detail point'] = 'null'

                # rank
                # try:
                #     badge_tag = soup.find('span', {'class': 'IconBadge__text'})
                #     badge = badge_tag.contents[0]
                #     detail_data['rank'] = badge
                # except AttributeError:
                #     detail_data['rank'] = 'null'

                # price
                # try:
                #     price_tag = soup.find('div', {'class': 'CrossedOutPrice'})
                #     first_price = price_tag.get_attribute_list('data-element-cor')
                #     final_price = price_tag.get_attribute_list('data-room-price')
                #     detail_data['first_price'] = first_price[0]
                #     detail_data['final_price'] = final_price[0]
                # except AttributeError:
                #     detail_data['first_price'] = 'null'
                #     detail_data['final_price'] = 'null'

                # # of reviews
                try:
                    review_basedon_tag = soup.find('div', {'class': 'review-basedon'})
                    total_num_reviews_tag = review_basedon_tag.find('span', {'class': 'text'})
                    total_num_reviews = total_num_reviews_tag.contents[0]
                except AttributeError:
                    total_num_reviews = 'null'
                detail_data['# of reviews'] = total_num_reviews
                # print(total_num_reviews)

                # # of review by levels
                try:
                    num_review_by_level = []
                    review_tag = soup.find('div', {'class': 'ReviewSideFilter__GuestRatingColumn'})
                    review_item_tag = review_tag.find_all('div', {'class': 'ReviewSideFilter__Item'})

                    for i in review_item_tag:
                        num_review_by_level_tag = i.find('span', {'class': 'ReviewSideFilter__ItemText'})
                        try:
                            num_review_by_level.append(num_review_by_level_tag.contents[0])
                        except AttributeError:
                            num_review_by_level.append('null')

                    if not num_review_by_level:
                        detail_data['# of reviews by levels'] = 'null if else'
                    else:
                        detail_data['# of reviews by levels'] = num_review_by_level

                except AttributeError:
                    detail_data['# of reviews by levels'] = 'null exception'

                # print('num by level: ' + str(detail_data['# of reviews by levels']))

                # review_comments = []
                # rv_cmt_tags = soup.find_all('div', {'class': 'Review-comment'})
                # for rv_cmt_tag in rv_cmt_tags:
                #     review_comment = {}
                #     try:
                #         rv_score = rv_cmt_tag.find('div', {'class': 'Review-comment-leftScore'}).contents[0]
                #     except AttributeError:
                #         rv_score = 'null'
                #     try:
                #         rv_score_text = rv_cmt_tag.find('div', {'class': 'Review-comment-leftScoreText'}).contents[
                #             0]
                #     except AttributeError:
                #         rv_score_text = 'null'
                #     try:
                #         rv_title = rv_cmt_tag.find('p', {'class': 'Review-comment-bodyTitle'}).contents[0]
                #     except AttributeError:
                #         rv_title = 'null'
                #     review_comment['review title'] = rv_title[0:len(rv_title) - 1]
                #     review_comment['review score'] = rv_score
                #     review_comment['review score text'] = rv_score_text
                #     review_comments.append(review_comment)
                # review['review comment'] = review_comments

                # # of room
                try:
                    room_icon_tag = soup.find('i', {'class': 'ficon ficon-18 ficon-number-of-rooms'})
                    parent = room_icon_tag.find_parent()
                    sib = parent.find_next_sibling()
                    num_room = sib.contents[0]
                    if isinstance(num_room, element.Tag):
                        span_tag = num_room.find_all('span')
                        detail_data['# of rooms'] = span_tag[-1].contents[0]
                    elif isinstance(num_room, element.NavigableString):
                        detail_data['# of rooms'] = num_room
                    else:
                        detail_data['# of rooms'] = 'null if else'
                except Exception:
                    detail_data['# of rooms'] = 'null exception'

                data_set.append(detail_data)
                driver.quit()
            write_json(data_set, detail_path + 'last.json')


def crawl_detail_data_by_list(list_stt):
    r = 0
    root_path = '../output/data_root_after_filter_null_value/hcm_data_root_total.json'
    detail_path = '../output/data_detail_crawled/hcm/hcm_data_detail_more.json'

    with open(root_path) as json_file:
        data_set = []
        data_root = json.load(json_file)
        count = 0
        for p in data_root:
            stt = p['stt']
            if stt in list_stt:
                count += 1
                if count % 100 == 0:
                    write_json(data_set, detail_path + str(count) + '.json')
                    data_set = []
                    print('Done a file')
                    print(time.ctime())
                url = 'https://' + p['link']
                print('stt: ' + str(stt))
                print(url)
                driver = webdriver.Chrome(options=option)
                try:
                    driver.get(url)
                except common.exceptions.WebDriverException:
                    continue

                time.sleep(3)

                html = driver.page_source
                soup = BeautifulSoup(html, "html.parser")
                detail_data = {'stt': p['stt'], 'link': p['link']}

                # name
                try:
                    name_tag = soup.find('h1')
                    name = name_tag.contents[0]
                    detail_data['name'] = name
                except AttributeError:
                    detail_data['name'] = 'null'

                # total point
                try:
                    total_point_tag = soup.find('div', {'class': 'ReviewScore-Number'})
                    if total_point_tag is None:
                        total_point_tag = soup.find('span', {'class': 'Review__ReviewFormattedScore'})
                    total_point = total_point_tag.contents[0]
                    detail_data['total point'] = total_point
                except AttributeError:
                    detail_data['total point'] = 'null'

                # detail point
                try:
                    detail_point_tag = soup.find('div', {'class': 'Review-travelerGrade-Cell'})
                    detail_point = {}
                    for cp in detail_point_tag.contents:
                        grade_category_tag = cp.find('span', {'class': 'Review-travelerGradeCategory'})
                        grade_score_tag = cp.find('span', {
                            'class': 'Review-travelerGradeScore Review-travelerGradeScore--highlight'})
                        if grade_score_tag is None:
                            grade_score_tag = cp.find('span', {
                                'class': 'Review-travelerGradeScore Review-travelerGradeScore--'})
                        grade_category = grade_category_tag.contents[0]
                        grade_score = grade_score_tag.contents[0]
                        detail_point[grade_category] = grade_score
                    detail_data['detail point'] = detail_point
                except AttributeError:
                    detail_data['detail point'] = 'null'

                # # of reviews
                try:
                    review_basedon_tag = soup.find('div', {'class': 'review-basedon'})
                    total_num_reviews_tag = review_basedon_tag.find('span', {'class': 'text'})
                    total_num_reviews = total_num_reviews_tag.contents[0]
                except AttributeError:
                    total_num_reviews = 'null'
                detail_data['# of reviews'] = total_num_reviews

                # # of review by levels
                try:
                    num_review_by_level = []
                    review_tag = soup.find('div', {'class': 'ReviewSideFilter__GuestRatingColumn'})
                    review_item_tag = review_tag.find_all('div', {'class': 'ReviewSideFilter__Item'})

                    for i in review_item_tag:
                        num_review_by_level_tag = i.find('span', {'class': 'ReviewSideFilter__ItemText'})
                        try:
                            num_review_by_level.append(num_review_by_level_tag.contents[0])
                        except AttributeError:
                            num_review_by_level.append('null')

                    if not num_review_by_level:
                        detail_data['# of reviews by levels'] = 'null if else'
                    else:
                        detail_data['# of reviews by levels'] = num_review_by_level

                except AttributeError:
                    detail_data['# of reviews by levels'] = 'null exception'

                # # of room
                try:
                    room_icon_tag = soup.find('i', {'class': 'ficon ficon-18 ficon-number-of-rooms'})
                    parent = room_icon_tag.find_parent()
                    sib = parent.find_next_sibling()
                    num_room = sib.contents[0]
                    if isinstance(num_room, element.Tag):
                        span_tag = num_room.find_all('span')
                        detail_data['# of rooms'] = span_tag[-1].contents[0]
                    elif isinstance(num_room, element.NavigableString):
                        detail_data['# of rooms'] = num_room
                    else:
                        detail_data['# of rooms'] = 'null if else'
                except Exception:
                    detail_data['# of rooms'] = 'null exception'

                data_set.append(detail_data)
                driver.quit()
            else:
                continue
        write_json(data_set, detail_path)


if __name__ == '__main__':
    print(time.ctime())
    # crawl_root_data()
    # crawl_detail_data()
    crawl_detail_data_by_list([946])
    print(time.ctime())
