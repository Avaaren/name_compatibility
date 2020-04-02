import requests
from bs4 import BeautifulSoup 
from pytils.translit import slugify
from datetime import datetime
from threading import Thread


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
        
    print(len(result))
    return result


responses = []
def get_responses():
    url_list = get_names()
    for url in url_list:
        response = 



@benchmark
def get_relationship_type(pre_slice, post_slice, relationships):
    counter = 1

    total_values = get_names()
    # print(total_values)
    for value in total_values[pre_slice:post_slice]:
        name = []
        URL = f'https://goroskop365.ru/sovmestimost-imen/{value[2]}/'

        response = requests.get(URL)
        if response.status_code != 200:
            # total_values.remove(value[2])
            continue
        else:
            soup = BeautifulSoup(response.text, 'html.parser')
            header = soup.find('div', class_='sovmestimost').find('br').text
            percent_text = soup.find('div', class_='compatibility-percentage')
            # percent_in_marriage = percent_in_love.next_sibling.text

            percent_text = percent_text.text
            percent_text = percent_text.split('\n')
            percent_in_love = percent_text[1].split('–')[1].strip().split('%')[0].strip()
            percent_in_marriage = percent_text[2].split('–')[1].strip().split('%')[0].strip()
            name.append(value[0])
            name.append(value[1])
            name.append(value[2])
            name.append(percent_in_love)
            name.append(percent_in_marriage)
            name.append(header)
            body = soup.find('div', class_='sovmestimost')
            for s in body.next_siblings:
                if s.name == None:
                    continue
                elif s.name == 'p':
                    name.append(s.text)
                else:
                    break
            relationships.append(name)
            print(f'{counter} - {name[5]}')
            counter += 1
    # print(relationships)
    return relationships

@benchmark
def return_relations():

    thread_list = []

    first_arg = 0
    length = 18763
    for i in range(10):
        
        t = Thread(target=get_relationship_type,
                name=f'Thread{i}',
                args=(first_arg, first_arg+10, relationships))
        thread_list.append(t)
        t.start()
        first_arg += 10

    for t in thread_list:
        t.join()

    print(len(relationships))
    # print(relationships)
    # get_relationship_type(0, 100)
    ss = relationships
    print(type(ss))
    return ss


s = return_relations()
# get_names()
print(type(s))