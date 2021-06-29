import pandas  # импортирование библиотеки для считывания данных


def get_sex_distrib(data):
    """
    1. Какое количество мужчин и женщин ехало на параходе? Приведите два числа через пробел.
    """

    n_male, n_female = 0, 0

    res = data['Sex'].value_counts()

    n_male, n_female = res['male'], res['female']

    return n_male, n_female


def get_port_distrib(data):
    """
    2. Подсчитайте сколько пассажиров загрузилось на борт в различных портах? Приведите три числа через пробел.
    """

    port_S, port_C, port_Q = 0, 0, 0

    res = data['Embarked'].value_counts()

    port_S, port_C, port_Q = res['S'], res['C'], res['Q']

    return port_C, port_Q, port_S


def get_surv_percent(data):
    """
    3. Посчитайте долю погибших на параходе (число и процент)?
    """

    n_died, perc_died = 0, 0

    res = data['Survived'].value_counts()
    common_n = len(data)

    n_died, perc_died = res[0], round(res[0] / common_n, 2)

    return n_died, perc_died


def get_class_distrib(data):
    """
    4. Какие доли составляли пассажиры первого, второго, третьего класса?
    """
    n_pas_f_cl, n_pas_s_cl, n_pas_t_cl = 0, 0, 0

    res = data['Pclass'].value_counts()
    common_n = len(data)

    n_pas_f_cl = round(res[1] / common_n, 2)
    n_pas_s_cl = round(res[2] / common_n, 2)
    n_pas_t_cl = round(res[3] / common_n, 2)

    return n_pas_f_cl, n_pas_s_cl, n_pas_t_cl


def find_corr_sibsp_parch(data):
    """
    5. Вычислите коэффициент корреляции Пирсона между количеством супругов (SibSp) и количеством детей (Parch).
    """

    sum_p, sum_x, sum_y = 0, 0, 0

    sibsp = data['SibSp']
    parch = data['Parch']

    for i in range(len(data)):
        x = sibsp[i + 1]
        y = parch[i + 1]
        sum_p += x * y
        sum_x += x**2
        sum_y += y**2

    if sum_x == 0 or sum_y == 0:
        corr_val = -1
    else:
        corr_val = round(sum_p / (sum_x * sum_y)**0.5, 3)

    return corr_val


def find_corr_age_survival(data):
    """
    6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
    - возрастом и параметром survival;
    """

    sum_p, sum_x, sum_y = 0, 0, 0

    ages = data['Age'].fillna(0)
    survived = data['Survived']

    for i in range(len(data)):
        x = ages[i + 1]
        y = survived[i + 1]
        sum_p += x * y
        sum_x += x**2
        sum_y += y**2

    if sum_x == 0 or sum_y == 0:
        corr_val = -1
    else:
        corr_val = round(sum_p / (sum_x * sum_y)**0.5, 3)

    return corr_val


def find_corr_sex_survival(data):
    """
    6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
    - полом человека и параметром survival;
    """

    sum_p, sum_x, sum_y = 0, 0, 0

    sex = data['Sex']
    survived = data['Survived']

    for i in range(len(data)):
        x = sex[i + 1]
        if x == 'male':
            x = 2
        elif x == 'female':
            x = 1
        else:
            x = 0
        y = survived[i + 1]
        sum_p += x * y
        sum_x += x**2
        sum_y += y**2

    if sum_x == 0 or sum_y == 0:
        corr_val = -1
    else:
        corr_val = round(sum_p / (sum_x * sum_y)**0.5, 3)

    return corr_val


def find_corr_class_survival(data):
    """
    6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
    - классом, в котором пассажир ехал, и параметром survival.
    """

    sum_p, sum_x, sum_y = 0, 0, 0

    pclass = data['Pclass'].fillna(0)
    survived = data['Survived']

    for i in range(len(data)):
        x = pclass[i + 1]
        y = survived[i + 1]
        sum_p += x * y
        sum_x += x**2
        sum_y += y**2

    if sum_x == 0 or sum_y == 0:
        corr_val = -1
    else:
        corr_val = round(sum_p / (sum_x * sum_y)**0.5, 3)

    return corr_val


def find_pass_mean_median(data):
    """
    7. Посчитайте средний возраст пассажиров и медиану.
    """

    mean_age = round(data['Age'].mean(axis=0, skipna=True), 2)
    median = round(data['Age'].median(axis=0, skipna=True), 2)

    return mean_age, median


def find_ticket_mean_median(data):
    """
    8. Посчитайте среднюю цену за билет и медиану.
    """

    mean_price = round(data['Fare'].mean(axis=0, skipna=True), 2)
    median = round(data['Fare'].median(axis=0, skipna=True), 2)

    return mean_price, median


def popular_male_name_func(frame):
    dict_of_names = {}

    for name in frame:
        lname, fname = name.split('. ')
        for name in fname.split(' '):
            if name not in dict_of_names.keys():
                dict_of_names.update({name: 0})
            dict_of_names.update({name: dict_of_names[name] + 1})

    keys_names = list(dict_of_names.keys())
    values_names = list(dict_of_names.values())

    name = keys_names[values_names.index(max(values_names))]

    return name


def popular_female_name_func(frame):
    dict_of_names = {}

    for name in frame:
        parts = name.split(' ')
        for name in parts:
            if name.find('.' or ',') == -1:
                while name.find('(' or ')') != -1:
                    ind = name.find('(' or ')')
                    name = name[:ind] + name[ind + 1:]
                if name not in dict_of_names.keys():
                    dict_of_names.update({name: 0})
                dict_of_names.update({name: dict_of_names[name] + 1})

    keys_names = list(dict_of_names.keys())
    values_names = list(dict_of_names.values())

    name = keys_names[values_names.index(max(values_names))]

    return name


def find_popular_name(data):
    """
    9. Какое самое популярное мужское имя на корабле?
    """

    frame_of_names = data[data['Sex'] == 'male']['Name']

    name = popular_male_name_func(frame_of_names)

    return name


def find_popular_adult_names(data):
    """
    10. Какие самые популярные мужское и женские имена людей, старше 15 лет на корабле?
    """

    frame_of_male_names = []
    frame_of_female_names = []

    for i in range(len(data)):
        if data['Age'][i + 1] > 15:
            if data['Sex'][i + 1] == 'male':
                frame_of_male_names.append(data['Name'][i + 1])
            elif data['Sex'][i + 1] == 'female':
                frame_of_female_names.append(data['Name'][i + 1])

    popular_male_name = popular_male_name_func(frame_of_male_names)
    popular_female_name = popular_female_name_func(frame_of_female_names)

    return popular_male_name, popular_female_name


def tests():
    data = pandas.read_csv('train.csv', index_col="PassengerId")

    assert get_sex_distrib(data) == (
        577, 314), 'Количество мужчин и женщин на Титанике'
    assert get_port_distrib(data) == (
        168, 77, 644
    ), 'Количество пассажиров, которые сели в портах городов Чербург, Квинстон, Саусэмпшон'
    assert get_surv_percent(data) == (549,
                                      0.62), 'Количество и процент погибших'
    assert get_class_distrib(data) == (
        0.24, 0.21, 0.55), 'Доли пассажиров первого, второго и третьего класса'
    assert find_corr_sibsp_parch(
        data
    ) == 0.522, 'Коэффициент корреляции Пирсона - связь количества супругов и детей'
    assert find_corr_age_survival(
        data
    ) == 0.503, 'Коэффициент корреляции Пирсона - связь возраста и выживаемости'
    assert find_corr_sex_survival(
        data
    ) == 0.476, 'Коэффициент корреляции Пирсона - связь принадлежности к полу и выживаемости'
    assert find_corr_class_survival(
        data
    ) == 0.492, 'Коэффициент корреляции Пирсона - связь между классом пассажира на корабле и выживаемости'
    assert find_pass_mean_median(data) == (
        29.7, 28.0), 'Среднее значение и медиана возраста'
    assert find_ticket_mean_median(data) == (
        32.2, 14.45), 'Средняя цена на билет и ее медиана'
    assert find_popular_name(
        data) == 'William', 'Самое популярное мужское имя на корабле'
    assert find_popular_adult_names(data) == (
        'William', 'Elizabeth'
    ), 'Самые популярные мужское и женское имена людей, старше 15 лет на корабле'


def main():
    data = pandas.read_csv('train.csv', index_col="PassengerId")

    tests()

    print(*get_sex_distrib(data))
    print(*get_port_distrib(data))
    print(*get_surv_percent(data))
    print(*get_class_distrib(data))
    print(find_corr_sibsp_parch(data))
    print(find_corr_age_survival(data))
    print(find_corr_sex_survival(data))
    print(find_corr_class_survival(data))
    print(*find_pass_mean_median(data))
    print(*find_ticket_mean_median(data))
    print(find_popular_name(data))
    print(*find_popular_adult_names(data))


main()
