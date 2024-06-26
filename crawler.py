# crawler.py
import requests
from bs4 import BeautifulSoup

def get_menu_from_burgerking():
    url = "https://www.burgerking.co.kr/menu"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    menus = soup.find_all('div', class_='menu-item')
    result = []
    for menu in menus:
        name = menu.find('h3').text
        if '조개' in name or '게' in name or '문어' in name:
            result.append(name)
    return result

def get_menu_from_subway():
    url = "https://www.subway.co.kr/menu"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    menus = soup.find_all('div', class_='menu-item')
    result = []
    for menu in menus:
        name = menu.find('h3').text
        if '조개' in name or '게' in name or '문어' in name:
            result.append(name)
    return result

def get_menu_from_kimbabcheonguk():
    url = "https://www.kimbabcheonguk.co.kr/menu"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    menus = soup.find_all('div', class_='menu-item')
    result = []
    for menu in menus:
        name = menu.find('h3').text
        if '조개' in name or '게' in name or '문어' in name:
            result.append(name)
    return result

def get_menu_from_kimgane():
    url = "https://www.kimgane.co.kr/menu"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    menus = soup.find_all('div', class_='menu-item')
    result = []
    for menu in menus:
        name = menu.find('h3').text
        if '조개' in name or '게' in name or '문어' in name:
            result.append(name)
    return result

def get_menu_from_hansot():
    url = "https://www.hsd.co.kr/menu"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    menus = soup.find_all('div', class_='menu-item')
    result = []
    for menu in menus:
        name = menu.find('h3').text
        if '조개' in name or '게' in name or '문어' in name:
            result.append(name)
    return result

def get_all_menus():
    all_menus = {
        "burgerking": get_menu_from_burgerking(),
        "subway": get_menu_from_subway(),
        "kimbabcheonguk": get_menu_from_kimbabcheonguk(),
        "kimgane": get_menu_from_kimgane(),
        "hansot": get_menu_from_hansot()
    }
    return all_menus

if __name__ == "__main__":
    menus = get_all_menus()
    print(menus)
