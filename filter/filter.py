import json
from visualize import statistic

base_path = '../output/data_root_after_filter_null_value/vungtau_data_root_total.json'
# base_path = 'data_root_after_filter_duplicate_hotel/data_root_total_400.json'

r = 13


def write_json(data, filename='data_agoda.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def filter_null_root():
    null_final_price = statistic.statistic_root_price()[1]
    print(null_final_price)
    print(len(null_final_price))
    while null_final_price:
        print(null_final_price)
        remove_data_by_stt(null_final_price)
        null_final_price = statistic.statistic_root_price()[1]

    null_total_point = statistic.statistic_root_total_point()[0]
    print(null_total_point)
    print(len(null_total_point))
    while null_total_point:
        print(null_total_point)
        remove_data_by_stt(null_total_point)
        null_total_point = statistic.statistic_root_total_point()[0]


def filter_null_data_root():
    num_of_null = [0] * r
    num_of_total = [0] * r
    num_of_full = [0] * r
    for page in range(r):
        with open(base_path + str(page) + '.json') as json_file:
            data = json.load(json_file)
            for p in data:
                num_of_total[page] += 1
                if p["id_hotel"] == "null" or p['link'] == "null":
                    num_of_null[page] += 1
                else:
                    num_of_full[page] += 1
    print('total: {} ==> sum = {}'.format(num_of_total, sum(num_of_total)))
    print('null: {} ==> sum = {}'.format(num_of_null, sum(num_of_null)))
    print('full: {} ==> sum = {}'.format(num_of_full, sum(num_of_full)))


def remove_data_by_stt(ls):
    with open(base_path) as json_file:
        data = json.load(json_file)
        for p in data:
            if p['stt'] in ls:
                data.remove(p)
    write_json(data, base_path)


def filter_duplicate():
    ids = []
    unique_ids = []
    duplicate_list = []
    # read id list
    with open(base_path) as json_file:
        data = json.load(json_file)
        for p in data:
            ids.append([{'stt': p['stt']}, {'id': p['id_hotel']}])
    # separate ids to unique_ids and duplicate_list
    for i in ids:
        if i[1]['id'] not in unique_ids:
            unique_ids.append(i[1]['id'])
        else:
            duplicate_list.append(i[0]['stt'])
    # remove the hotels have stt in duplicate_list in json files .
    remove_data_by_stt(duplicate_list)

    print(len(ids))
    print(len(unique_ids))
    print(duplicate_list)


if __name__ == '__main__':
    # filter_null_data_root()
    # filter_duplicate()
    # filter_null_point_data_root()
    filter_null_root()
    # remove_data_by_stt([])