import matplotlib.pyplot as plt
import statistic


def num_of_hotel_by_star():
    names = ['0', '0,5', '1', '1,5', '2', '2.5', '3', '3.5', '4', '4.5', '5', 'null']
    values = statistic.statistic_hotel_by_star()

    plt.bar(names, values, width=0.5, color='blue')
    plt.axis([-0.3, 11.5, 0, max(values) + 5])
    plt.xlabel('Star', fontsize=20, color='red')
    plt.ylabel('Number of hotels', fontsize=20, color='red')
    plt.title("Statistic number of hotels by star", fontsize=20, color='green')
    plt.legend()
    plt.show()


def rate_duplicate_data():
    labels = 'Unique', 'Duplicate'
    sizes = [534, 253]
    explode = (0, 0.1)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title("Rate duplicate data", fontsize=20, color='black')
    plt.show()


def num_of_hotel_by_point():
    names = []
    values = []
    n = statistic.statistic_num_hotel_by_point()
    for p in n:
        names.append(p['point'])
        values.append(p['num'])
    print(names)
    print(values)

    plt.bar(names, values, width=0.5, color='blue')
    plt.axis([-1.3, 10.5, 0, max(values) + 5])
    plt.xlabel('Point', fontsize=20, color='red')
    plt.ylabel('Number of hotels', fontsize=20, color='red')
    plt.title("Statistic number of hotels by point", fontsize=20, color='green')
    plt.legend()
    plt.show()


def point_by_star():
    point_star = statistic.statistic_point_by_star()
    float_point_star = []
    print(len(point_star))
    for i in point_star:
        float_point_star_page = []
        for j in i:
            float_point_star_page.append(float(j))
        float_point_star.append(float_point_star_page)

    avg_point_by_star = []
    for star in float_point_star:

        if star:
            avg_point_by_star.append(sum(star)/len(star))
            print(sum(star)/len(star))
        else:
            avg_point_by_star.append(0)
            print(0)
    x = ['0', '0,5', '1', '1,5', '2', '2.5', '3', '3.5', '4', '4.5', '5', 'null']
    y = avg_point_by_star
    plt.figure()
    plt.plot(x, y)
    # plt.yticks(y)
    plt.grid(True)
    plt.show()


def price_by_star():
    price_star = statistic.statistic_root_price()
    min_price_star = []
    mean_price_star = []
    max_price_star = []
    for i in price_star:
        if len(i) == 0:
            min_price_star.append(0)
            max_price_star.append(0)
            mean_price_star.append(0)
        else:
            min_price_star.append(min(i))
            mean_price_star.append(int(sum(i)/len(i)))
            max_price_star.append(max(i))
    print(min_price_star)
    print(mean_price_star)
    print(max_price_star)
    star = ['0', '0,5', '1', '1,5', '2', '2.5', '3', '3.5', '4', '4.5', '5', 'null']
    plt.figure()
    # plt.plot(star, min_price_star)
    plt.plot(star, mean_price_star)
    # plt.plot(star, max_price_star)
    # plt.yticks(min_price_star)
    plt.grid(True)
    plt.show()


def room_by_star():
    room_star = statistic.statistic_room()
    min_room_star = []
    mean_room_star = []
    max_room_star = []
    for i in room_star:
        if len(i) == 0:
            min_room_star.append(0)
            max_room_star.append(0)
            mean_room_star.append(0)
        else:
            min_room_star.append(min(i))
            mean_room_star.append(int(sum(i) / len(i)))
            max_room_star.append(max(i))
    print(min_room_star)
    print(mean_room_star)
    print(max_room_star)
    star = ['0', '0,5', '1', '1,5', '2', '2.5', '3', '3.5', '4', '4.5', '5', 'null']
    plt.figure()
    plt.plot(star, min_room_star, label="Min")
    plt.plot(star, mean_room_star, label="Mean")
    plt.plot(star, max_room_star, label='Max')
    plt.xlabel('Star')
    plt.ylabel('Number of rooms')
    plt.legend()
    plt.grid(True)
    plt.show()


def review_by_star():
    review_star = statistic.statistic_reviews()
    min_review_star = []
    mean_review_star = []
    max_review_star = []
    for i in review_star:
        if len(i) == 0:
            min_review_star.append(0)
            max_review_star.append(0)
            mean_review_star.append(0)
        else:
            min_review_star.append(min(i))
            mean_review_star.append(int(sum(i) / len(i)))
            max_review_star.append(max(i))
    print(min_review_star)
    print(mean_review_star)
    print(max_review_star)
    star = ['0', '0,5', '1', '1,5', '2', '2.5', '3', '3.5', '4', '4.5', '5', 'null']
    plt.figure()
    plt.plot(star, min_review_star, label="Min")
    plt.plot(star, mean_review_star, label="Mean")
    plt.plot(star, max_review_star, label='Max')
    plt.xlabel('Star')
    plt.ylabel('Number of reviews')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    
if __name__ == '__main__':
    # num_of_hotel_by_star()
    # rate_duplicate_data()
    # num_of_hotel_by_point()
    # num_of_hotel_by_point()
    # point_by_star()
    # price_by_star()
    # room_by_star()
    review_by_star()
