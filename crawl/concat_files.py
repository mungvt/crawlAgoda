import json

from Utils import write_json


def concat_files():
    base_path = '../output/data_detail_crawled/all_city/data_detail_total'
    # base_path = 'data_detail_crawled/hcm/hcm_data_detail_'
    # base_path = '../filter/data_root_after_filter_null_value/all_city/data_root_total_'
    total_data = []
    for page in range(0, 5):
        with open(base_path + str(page) + '.json') as json_file:
            data = json.load(json_file)
            for p in data:
                total_data.append(p)
    write_json(total_data, base_path + 'total.json')


def compare_stt_root_detail():
    detail_path = '../output/data_detail_crawled/all_city/data_detail_total4.json'
    root_path = '../output/data_root_after_filter_null_value/all_city/data_root_total_500.json'
    stt_root_list = []
    with open(root_path) as json_file:
        data = json.load(json_file)
        for p in data:
            stt = p['stt']
            stt_root_list.append(stt)
    print(stt_root_list)

    stt_detail_list = []
    with open(detail_path) as json_file:
        data = json.load(json_file)
        for p in data:
            stt = p['stt']
            stt_detail_list.append(stt)
    print(stt_detail_list)


if __name__ == '__main__':
    # compare_stt_root_detail()
    concat_files()