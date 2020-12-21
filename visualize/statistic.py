import json
import re

r = 4
base_url = 'crawl/data_detail_crawled/vungtau/v3/data_detail_total3.json'
# base_url = '../filter/data_root_after_filter_null_value/data_root_total_400.json'


def write_json(data, filename='data_agoda.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def statistic_root_star():
    num_hotel_star = [0] * 12
    list_by_star = [[] * 11]
    for i in range(11):
        list_by_star.append([])
    for page in range(r):
        with open(base_url + str(page) + '.json') as json_file:
            data = json.load(json_file)

            for p in data:
                rank = p['rank']
                if rank == " star":
                    num_hotel_star[0] = num_hotel_star[0] + 1
                    list_by_star[0].append(p['id_hotel'])
                if rank == "0.5 star":
                    num_hotel_star[1] = num_hotel_star[1] + 1
                    list_by_star[1].append(p['id_hotel'])
                if rank == "1 star":
                    num_hotel_star[2] = num_hotel_star[2] + 1
                    list_by_star[2].append(p['id_hotel'])
                if rank == "1.5 star":
                    num_hotel_star[3] = num_hotel_star[3] + 1
                    list_by_star[3].append(p['id_hotel'])
                if rank == "2 star":
                    num_hotel_star[4] = num_hotel_star[4] + 1
                    list_by_star[4].append(p['id_hotel'])
                if rank == "2.5 star":
                    num_hotel_star[5] = num_hotel_star[5] + 1
                    list_by_star[5].append(p['id_hotel'])
                if rank == "3 star":
                    num_hotel_star[6] = num_hotel_star[6] + 1
                    list_by_star[6].append(p['id_hotel'])
                if rank == "3.5 star":
                    num_hotel_star[7] = num_hotel_star[7] + 1
                    list_by_star[7].append(p['id_hotel'])
                if rank == "4 star":
                    num_hotel_star[8] = num_hotel_star[8] + 1
                    list_by_star[8].append(p['id_hotel'])
                if rank == "4.5 star":
                    num_hotel_star[9] = num_hotel_star[9] + 1
                    list_by_star[9].append(p['id_hotel'])
                if rank == "5 star":
                    num_hotel_star[10] = num_hotel_star[10] + 1
                    list_by_star[10].append(p['id_hotel'])
                if rank == "null":
                    num_hotel_star[11] = num_hotel_star[11] + 1
    print(num_hotel_star)
    print(sum(num_hotel_star))
    print()
    return num_hotel_star


def statistic_root_price():
    null_final_price_list = []
    null_first_price_list = []
    null_price_list = []
    price_by_star = []
    for i in range(12):
        price_by_star.append([])

    with open(base_url) as json_file:
        data = json.load(json_file)
        for p in data:
            stt = p['stt']
            rank = p['rank']
            first_price = p['first price']
            final_price = p['final price']
            if final_price == 'null':
                null_final_price_list.append(stt)
            else:
                final_price_split = final_price.split(",")
                final_price_joined = ''.join(final_price_split)
                final_price = int(final_price_joined)

                if rank == " star":
                    price_by_star[0].append(final_price)
                elif rank == "0.5 star":
                    price_by_star[1].append(final_price)
                elif rank == "1 star":
                    price_by_star[2].append(final_price)
                elif rank == "1.5 star":
                    price_by_star[3].append(final_price)
                elif rank == "2 star":
                    price_by_star[4].append(final_price)
                elif rank == "2.5 star":
                    price_by_star[5].append(final_price)
                elif rank == "3 star":
                    price_by_star[6].append(final_price)
                elif rank == "3.5 star":
                    price_by_star[7].append(final_price)
                elif rank == "4 star":
                    price_by_star[8].append(final_price)
                elif rank == "4.5 star":
                    price_by_star[9].append(final_price)
                elif rank == "5 star":
                    price_by_star[10].append(final_price)
                else:
                    price_by_star[11].append(final_price)
            if first_price == 'null':
                null_first_price_list.append(stt)
            if first_price == 'null' and final_price == 'null':
                null_price_list.append(stt)

    # print(null_price_list)
    # print(len(null_price_list))
    # print(null_first_price_list)
    # print(len(null_first_price_list))
    # print(null_final_price_list)

    return price_by_star, null_final_price_list


def statistic_root_total_point():
    point_by_star = []
    null_point_list = []
    for i in range(12):
        point_by_star.append([])

    with open(base_url) as json_file:
        data = json.load(json_file)
        for p in data:
            stt = p['stt']
            rank = p['rank']
            point = p['total point']
            if point == 'null':
                null_point_list.append(stt)
            else:
                if rank == " star":
                    point_by_star[0].append(point)
                elif rank == "0.5 star":
                    point_by_star[1].append(point)
                elif rank == "1 star":
                    point_by_star[2].append(point)
                elif rank == "1.5 star":
                    point_by_star[3].append(point)
                elif rank == "2 star":
                    point_by_star[4].append(point)
                elif rank == "2.5 star":
                    point_by_star[5].append(point)
                elif rank == "3 star":
                    point_by_star[6].append(point)
                elif rank == "3.5 star":
                    point_by_star[7].append(point)
                elif rank == "4 star":
                    point_by_star[8].append(point)
                elif rank == "4.5 star":
                    point_by_star[9].append(point)
                elif rank == "5 star":
                    point_by_star[10].append(point)
                else:
                    point_by_star[11].append(point)
    return null_point_list, point_by_star


def statistic_room():
    room_by_star = []
    null_room_list = []
    for i in range(12):
        room_by_star.append([])
    for page in range(r):
        with open(base_url + str(page) + '.json') as json_file:
            data = json.load(json_file)
            for p in data:
                stt = p['stt']
                rank = p['rank']
                try:
                    room = p['# of rooms']
                except KeyError:
                    continue
                if room == 'null':
                    null_room_list.append(stt)
                else:
                    room = int(room)
                    if rank == "Hotel":
                        room_by_star[0].append(room)
                    elif rank == "0.5-star  Hotel":
                        room_by_star[1].append(room)
                    elif rank == "1-star  Hotel":
                        room_by_star[2].append(room)
                    elif rank == "1.5-star  Hotel":
                        room_by_star[3].append(room)
                    elif rank == "2-star  Hotel":
                        room_by_star[4].append(room)
                    elif rank == "2.5-star  Hotel":
                        room_by_star[5].append(room)
                    elif rank == "3-star  Hotel":
                        room_by_star[6].append(room)
                    elif rank == "3.5-star  Hotel":
                        room_by_star[7].append(room)
                    elif rank == "4-star  Hotel":
                        room_by_star[8].append(room)
                    elif rank == "4.5-star  Hotel":
                        room_by_star[9].append(room)
                    elif rank == "5-star  Hotel":
                        room_by_star[10].append(room)
                    else:
                        room_by_star[11].append(room)
    for i in room_by_star:
        # print(i)
        sum += len(i)
    return room_by_star


def statistic_hotel_by_star_detail():
    num_hotel_star = [0] * 13
    list_hotel_by_star = []
    for i in range(13):
        list_hotel_by_star.append([])
    for page in range(r):
        with open(base_url + str(page) + '.json') as json_file:
            data = json.load(json_file)

            for p in data:
                rank = p['rank']
                if rank == "Hotel":
                    num_hotel_star[0] = num_hotel_star[0] + 1
                    list_hotel_by_star[0].append(p['stt'])
                elif rank == "0.5-star  Hotel":
                    num_hotel_star[1] = num_hotel_star[1] + 1
                    list_hotel_by_star[1].append(p['stt'])
                elif rank == "1-star  Hotel":
                    num_hotel_star[2] = num_hotel_star[2] + 1
                    list_hotel_by_star[2].append(p['stt'])
                elif rank == "1.5-star  Hotel":
                    num_hotel_star[3] = num_hotel_star[3] + 1
                    list_hotel_by_star[3].append(p['stt'])
                elif rank == "2-star  Hotel":
                    num_hotel_star[4] = num_hotel_star[4] + 1
                    list_hotel_by_star[4].append(p['stt'])
                elif rank == "2.5-star  Hotel":
                    num_hotel_star[5] = num_hotel_star[5] + 1
                    list_hotel_by_star[5].append(p['stt'])
                elif rank == "3-star  Hotel":
                    num_hotel_star[6] = num_hotel_star[6] + 1
                    list_hotel_by_star[6].append(p['stt'])
                elif rank == "3.5-star  Hotel":
                    num_hotel_star[7] = num_hotel_star[7] + 1
                    list_hotel_by_star[7].append(p['stt'])
                elif rank == "4-star  Hotel":
                    num_hotel_star[8] = num_hotel_star[8] + 1
                    list_hotel_by_star[8].append(p['stt'])
                elif rank == "4.5-star  Hotel":
                    num_hotel_star[9] = num_hotel_star[9] + 1
                    list_hotel_by_star[9].append(p['stt'])
                elif rank == "5-star  Hotel":
                    num_hotel_star[10] = num_hotel_star[10] + 1
                    list_hotel_by_star[10].append(p['stt'])
                elif rank == "null":
                    num_hotel_star[11] = num_hotel_star[11] + 1
                    list_hotel_by_star[11].append(p['stt'])
                else:
                    num_hotel_star[12] = num_hotel_star[12] + 1
                    list_hotel_by_star[12].append(p['stt'])

    print(num_hotel_star)
    print(sum(num_hotel_star))
    return num_hotel_star


def statistic_num_hotel_by_page():
    num_hotel = [0]*r
    for page in range(r):
        with open(base_url + str(page) + '.json') as json_file:
            data = json.load(json_file)
            for p in data:
                num_hotel[page] += 1
    print(num_hotel)
    print(sum(num_hotel))


def statistic_num_hotel_by_point():
    num_hotel_by_point = []
    points = []
    unique_points = []

    for page in range(r):
        print('page' + str(page))
        with open(base_url + str(page) + '.json') as json_file:
            data = json.load(json_file)
            for p in data:
                if p['total point'] != 'null':
                    point = float(p['total point'])
                else:
                    point = -1
                points.append(point)
                if point not in unique_points:
                    unique_points.append(point)
        unique_points.sort()

    for p in unique_points:
        num = points.count(p)
        num_point = {'point': p, 'num': num}
        num_hotel_by_point.append(num_point)
    print(unique_points)
    # for p in num_hotel_by_point:
    #     print(p)
    print(num_hotel_by_point)
    return num_hotel_by_point


def extract_num_of_review(num_text):
    all_num = re.findall(r'[0-9]+', num_text)
    num = ''.join(all_num)
    return int(num)


def statistic_reviews():
    review_by_star = []
    null_review_list = []
    for i in range(12):
        review_by_star.append([])
    for page in range(r):
        with open(base_url + str(page) + '.json') as json_file:
            data = json.load(json_file)
            for p in data:
                stt = p['stt']
                rank = p['rank']
                try:
                    review_text = p['review']['# of review'][0]
                    review_num = extract_num_of_review(review_text)
                except (KeyError, TypeError) as e:
                    null_review_list.append(stt)
                    continue

                if rank == "Hotel":
                    review_by_star[0].append(review_num)
                elif rank == "0.5-star  Hotel":
                    review_by_star[1].append(review_num)
                elif rank == "1-star  Hotel":
                    review_by_star[2].append(review_num)
                elif rank == "1.5-star  Hotel":
                    review_by_star[3].append(review_num)
                elif rank == "2-star  Hotel":
                    review_by_star[4].append(review_num)
                elif rank == "2.5-star  Hotel":
                    review_by_star[5].append(review_num)
                elif rank == "3-star  Hotel":
                    review_by_star[6].append(review_num)
                elif rank == "3.5-star  Hotel":
                    review_by_star[7].append(review_num)
                elif rank == "4-star  Hotel":
                    review_by_star[8].append(review_num)
                elif rank == "4.5-star  Hotel":
                    review_by_star[9].append(review_num)
                elif rank == "5-star  Hotel":
                    review_by_star[10].append(review_num)
                else:
                    review_by_star[11].append(review_num)
    for i in review_by_star:
        print(i)
    return review_by_star


def statistic_star():
    null_star_list = []
    list_star = []
    with open(base_url) as json_file:
        data = json.load(json_file)
        for p in data:
            stt = p['stt']
            rank = p['rank']
            if rank == 'null':
                null_star_list.append(stt)
            elif rank not in list_star:
                list_star.append(rank)
    print(null_star_list)
    print(len(null_star_list))
    print(list_star)


def statistic_detail_room():
    null_ifelse_list = []
    null_exception_list = []
    done_list = []
    with open(base_url) as json_file:
        data = json.load(json_file)
        for p in data:
            stt = p['stt']
            num_room = p['# of rooms']
            if num_room == 'null if else':
                null_ifelse_list.append(stt)
            elif num_room == 'null exception':
                null_exception_list.append(stt)
            else:
                done_list.append(stt)
    print(null_ifelse_list)
    print(null_exception_list)
    return null_ifelse_list


def statistic_detail_review():
    null_num_review_list = []
    with open(base_url) as json_file:
        data = json.load(json_file)
        for p in data:
            stt = p['stt']
            review = p['review']
            if review == 'null':
                null_num_review_list.append(stt)
    print(len(null_num_review_list))
    print(null_num_review_list)


if __name__ == '__main__':
    # statistic_root_total_point()
    # statistic_root_price
    # statistic_detail_room()
    statistic_detail_review()