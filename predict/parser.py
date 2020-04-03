import requests
from bs4 import BeautifulSoup
from pytils.translit import slugify
from datetime import datetime
from multiprocessing import Pool
import csv


def benchmark(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        func(*args, **kwargs)
        print(datetime.now() - start)
    return wrapper


def get_names():
    url = 'https://goroskop365.ru/sovmestimost-imen/agnessa-averyan/'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    result = []
    man_values = []
    woman_values = []

    women_names_list = soup.find('select', {'name': 'female_name'})
    women_names_list = women_names_list.find_all('option')

    for woman_name in women_names_list:
        try:
            woman_values.append(woman_name['value'])
        except KeyError:
            continue

    men_names_list = soup.find('select', {'name': 'male_name'})
    men_names_list = men_names_list.find_all('option')

    for man_name in men_names_list:
        try:
            man_values.append(man_name['value'])
        except KeyError:
            continue

    for women_name in woman_values:
        for man_name in man_values:
            total_values = []
            _str = f'{women_name}-{man_name}'
            total_values.append(women_name)
            total_values.append(man_name)
            total_values.append(slugify(_str))
            result.append(total_values)
    return result


def get_urls():
    url_list = []
    names_list = get_names()
    for name in names_list:
        url = f'https://goroskop365.ru/sovmestimost-imen/{name[2]}/'
        url_list.append(url)
    return url_list


def get_response(url):
    response = requests.get(url)
    return response


def get_page_data(response):
    page_info = []
    if response.status_code != 200:
        pass
    else:
        soup = BeautifulSoup(response.text, 'html.parser')
        header = soup.find('div', class_='sovmestimost').find('br').text

        percent_text = soup.find('div', class_='compatibility-percentage')
        percent_text = percent_text.text
        percent_text = percent_text.split('\n')

        percent_in_love = percent_text[1].split(
            '–')[1].strip().split('%')[0].strip()
        percent_in_marriage = percent_text[2].split(
            '–')[1].strip().split('%')[0].strip()

        header_with_names = soup.find_all('h2')[1].text.strip()
        header_with_names = header_with_names.split(' ')

        male_name = header_with_names[::-1][0]
        female_name = header_with_names[::-1][2]
        slug = slugify(f'{female_name}-{male_name}')

        page_info.append(female_name)
        page_info.append(male_name)
        page_info.append(slug)
        page_info.append(percent_in_love)
        page_info.append(percent_in_marriage)
        page_info.append(header)

        body = soup.find('div', class_='sovmestimost')
        for s in body.next_siblings:
            if s.name == None:
                continue
            elif s.name == 'p':
                page_info.append(s.text)
            else:
                break

        descr = ''
        for string in page_info[6:]:
            descr += string

        page_data = {
            'female_name': page_info[0],
            'male_name': page_info[1],
            'slug': page_info[2],
            'percent_in_love': page_info[3],
            'percent_in_married': page_info[4],
            'header': page_info[5],
            'description': descr
        }
        return page_data


def write_csv(page_data):
    with open('relationships.csv', 'a') as f:
        writer = csv.writer(f)
        try:
            writer.writerow((
                page_data['female_name'],
                page_data['male_name'],
                page_data['slug'],
                page_data['percent_in_love'],
                page_data['percent_in_married'],
                page_data['header'],
                page_data['description'])
            )
            print(page_data['slug'])
        except:
            pass


def write_all_to_csv(url):
    response = get_response(url)
    page_data = get_page_data(response)
    write_csv(page_data)


url_list = get_urls()
with Pool(40) as pool:
    pool.map(write_all_to_csv, url_list)
