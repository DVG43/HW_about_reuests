
from pprint import pprint

#
import requests
#
# Нужно определить кто самый умный(intelligence) из трех супергероев- Hulk, Captain America, Thanos.
# Для определения id нужно использовать метод /search/name





def get_poverstats (name_of_hero):
        # url = f"https://superheroapi.com/api/2619421814940190/character-'Hulk'/powerstats"
        url = f"https://superheroapi.com/api/2619421814940190/search/{name_of_hero}"
        headers_s = {"Authorization": "2619421814940190"}
        params_s = {'poverstats': 'meaning'}
        response = requests.get(url,params = params_s)
        return response.json()


if __name__ == '__main__':

     name_list = ['Hulk', 'Captain America', 'Thanos']
     index = 0
     super_intelegent = ''
     for name_hero in name_list:

         hero_data = get_poverstats(name_hero)['results']
         hero_data_1 = hero_data[0]
         hero_data_2 = int(hero_data_1['powerstats']['intelligence'])
         #pprint (hero_data_2)
         if hero_data_2 > index:
             super_intelegent = name_hero
             index = hero_data_2
         else:
             index = hero_data_2

     print (f'Самый умный {super_intelegent}')


