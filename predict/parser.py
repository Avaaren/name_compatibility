import requests
from bs4 import BeautifulSoup 
from pytils.translit import slugify
from datetime import datetime
from multiprocessing import Pool


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

responses = []
def get_responses(first, last):
    
    url_list = get_names()
    for url in url_list[first:last]:
        URL = f'https://goroskop365.ru/sovmestimost-imen/{url[2]}/'
        response = requests.get(URL)
        responses.append(response)
    
# def threading_urls():
#     thread_list = []
#     first = 0
#     length = 18762

#     for i in range(3):
#         if length < 2000:
#             t = Thread(target=get_responses, args=(first, first+length))
#         else:
#             t = Thread(target=get_responses, args=(first, first+2000))
#         thread_list.append(t)
#         t.start()
#         first += 2000
#         length -= 2000

#     for thread in thread_list:
#         thread.join()
#     # print(responses)
#     return responses

@benchmark
def get_relationship_type():
    counter = 1
    page_info = []
    relationships = []

    # responses_list = threading_urls()
    for response in responses_list:
        try:
            if response.status_code != 200:
                continue
            else:
                
                soup = BeautifulSoup(response.text, 'html.parser')
                header = soup.find('div', class_='sovmestimost').find('br').text

                percent_text = soup.find('div', class_='compatibility-percentage')
                percent_text = percent_text.text
                percent_text = percent_text.split('\n')

                percent_in_love = percent_text[1].split('–')[1].strip().split('%')[0].strip()
                percent_in_marriage = percent_text[2].split('–')[1].strip().split('%')[0].strip()

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
                
                relationships.append(page_info)
                counter += 1
        except Exception as exception:
            print(type(exception).__name__)
            continue
    return relationships
