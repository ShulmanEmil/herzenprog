import json
import re

from bs4 import BeautifulSoup
from urllib.request import urlopen


def get_urls(main_url, part_url):

    html = urlopen(main_url)
    bs = BeautifulSoup(html, 'html.parser')

    a_tags = bs.find_all('a')
    result_a_tags = set()

    for a_tag in a_tags:
        one_url = a_tag.attrs.get('href')
        if part_url in one_url and part_url != one_url:
            result_a_tags.add(a_tag)

    return result_a_tags


def get_institutes(a_tags, first_part_of_url):

    institutes = []
    institutes_names = {}

    for a_tag in a_tags:
        name_lower = a_tag.text.lower()
        if name_lower not in institutes_names.keys():
            institutes.append({
                'institute_name':
                name_lower,
                'url':
                first_part_of_url + a_tag.attrs.get('href'),
            })
            institutes_names[name_lower] = len(institutes)
    return institutes, institutes_names


def get_head_email(main_url, head_name, bs):

    try:
        url = main_url + (bs.findAll(
            text=re.compile(head_name))[1].parent).attrs['href']
        html = urlopen(url)
        bs = BeautifulSoup(html, 'html.parser')
        if bs.findAll(text=re.compile('@')) != []:
            return bs.findAll(text=re.compile('@'))[0]
        else:
            return 'Почта не указана'
    except:
        return 'Нет ссылки на страницу'


def one_academic_department_info(main_url, url, institutes, institutes_names):

    html = urlopen(main_url + url)
    bs = BeautifulSoup(html, 'html.parser')

    if bs.findAll(text=re.compile('институт')) != []:

        info = bs.find_all('p')
        inst_name = info[1].text.lower()
        head_name = info[2].text.split(', ')[0]
        email = get_head_email(main_url, head_name, bs)
        academic_department_info = {
            'dep_name': 'кафедра ' + info[0].text,
            'head_name': head_name,
            'email': email
        }

        if inst_name not in institutes_names:
            institutes.append({
                'institute_name': inst_name,
                'url': 'Нет на основном сайте'
            })
            institutes_names[inst_name] = len(institutes_names)

        if 'academic_department' not in institutes[institutes_names[inst_name]
                                                   - 1].keys():
            institutes[institutes_names[inst_name] -
                       1]['academic_department'] = [academic_department_info]
        else:
            institutes[institutes_names[inst_name] -
                       1]['academic_department'] += [academic_department_info]

    return institutes


def get_academic_department_info(main_url, first_url, part_url, institutes,
                                 institutes_names):

    all_academic_departments_urls = get_urls(main_url + first_url, part_url)
    for url in all_academic_departments_urls:
        institutes = one_academic_department_info(main_url, url.attrs['href'],
                                                  institutes, institutes_names)
    return institutes


institutes, institutes_names = get_institutes(
    get_urls('https://www.herzen.spb.ru/main/structure/inst/',
             '/main/structure/inst/'), 'https://www.herzen.spb.ru')
result_structure = get_academic_department_info('https://atlas.herzen.spb.ru/',
                                                'faculty.php',
                                                'chair_type.php?id=',
                                                institutes, institutes_names)
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(result_structure, f, ensure_ascii=False, indent=4)
