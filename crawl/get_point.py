import json
import time

from bs4 import BeautifulSoup
from selenium import webdriver


def write_json(data, filename='data_agoda.json'):
    with open(filename,'w') as f:
        json.dump(data, f, indent=4)


for page in range(10):
    error = []
    with open('output/data_agoda_test' + str(page) + '.json') as json_file:
        data = json.load(json_file)

        for p in data:
            url = p['link']
            driver = webdriver.Chrome()
            try:
                driver.get('https://' + url)

                time.sleep(5)
                html = driver.page_source
                soup = BeautifulSoup(html, "html.parser")

                all_divs = soup.find('div', {'class': 'Review-travelerGrade-Cell'})

                point = {}
                try:
                    for i in all_divs:
                        try:
                            review_name_tag = i.span
                            review_name = review_name_tag.contents[0]
                        except Exception:
                            review_name = 'null'

                        try:
                            review_point_tag = i.span.next_sibling
                            review_point = review_point_tag.contents[0]
                        except Exception:
                            review_point = 'null'

                        point[str(review_name)] = str(review_point)

                except Exception:
                    print(str(p['stt']) + 'uncompleted')
                    error.append(p['stt'])

                p['point detail'] = point

                write_json(data, 'output/data_agoda_test' + str(page) + '.json')

                driver.close()
            except Exception:
                print(str(p['stt']) + 'uncompleted')
                error.append(p['stt'])

    print(error)
