from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np


class DataSetScrape:

    def description(self, link):
        url = link
        data = requests.get(url)
        soup = BeautifulSoup(data.content, 'html.parser')
        s = soup.findAll('li', {'class': 'main_image'})
        links = []
        for i in s:
            links.append(i.a['href'])
        description = []
        for link in links:
            url = link
            data = requests.get(url)
            soup = BeautifulSoup(data.content, 'html.parser')
            s = soup.find('div', {'class': 'keyword_tag'})
            try:
                description.append(s.text)
            except:
                description.append(np.nan)

        return description

    def healthy(self):
        url = 'https://food.ndtv.com/recipes/healthy-recipes'

        data = requests.get(url)

        soup = BeautifulSoup(data.content, 'html.parser')

        s = soup.findAll('img', {'class': 'lazy'})

        l = []

        for i in s:
            i = str(i)
            t = i.split('title')
            name = t[-1].split('width')[0]
            name = name[2:-8]
            l.append(name)

        nl = l[-21:]
        ll = []
        for i in nl:
            ll.append(i[:-6])

        l = l[:-21] + ll

        healthy = pd.DataFrame(columns=['Name','sub_catagory','description'])

        healthy['Name'] = l

        catagory = ['healthy' for i in range(len(l))]

        healthy['sub_catagory'] = catagory

        healthy['description'] = self.description(url)

        return healthy

    def snacks(self):
        url = 'https://food.ndtv.com/recipes/snacks-recipes'

        data = requests.get(url)

        soup = BeautifulSoup(data.content, 'html.parser')

        s = soup.findAll('img', {'class': 'lazy'})

        l = []

        for i in s:
            i = str(i)
            t = i.split('title')
            name = t[-1].split('width')[0]
            name = name[2:-8]
            l.append(name)

        nl = l[-21:]
        ll = []
        for i in nl:
            ll.append(i[:-6])

        l = l[:-21] + ll

        snacks = pd.DataFrame(columns=['Name', 'catagory', 'description'])

        snacks['Name'] = l

        catagory = ['snacks' for i in range(len(l))]

        snacks['catagory'] = catagory

        snacks['description'] = self.description(url)

        return snacks

    def vegetarian(self):
        url = 'https://food.ndtv.com/recipes/vegetarian-recipes'

        data = requests.get(url)

        soup = BeautifulSoup(data.content, 'html.parser')

        s = soup.findAll('img', {'class': 'lazy'})

        l = []

        for i in s:
            i = str(i)
            t = i.split('title')
            name = t[-1].split('width')[0]
            name = name[2:-8]
            l.append(name)

        nl = l[-21:]
        ll = []
        for i in nl:
            ll.append(i[:-6])

        l = l[:-21] + ll

        vegetarian = pd.DataFrame(columns=['Name','sub_catagory','description'])

        vegetarian['Name'] = l

        catagory = ['vegetarian' for i in range(len(l))]

        vegetarian['sub_catagory'] = catagory

        vegetarian['description'] = self.description(url)

        return vegetarian

    def chicken(self):
        url = 'https://food.ndtv.com/recipes/chicken-recipes'

        data = requests.get(url)

        soup = BeautifulSoup(data.content, 'html.parser')

        s = soup.findAll('img', {'class': 'lazy'})

        l = []

        for i in s:
            i = str(i)
            t = i.split('title')
            name = t[-1].split('width')[0]
            name = name[2:-8]
            l.append(name)
        nl = l[-21:]
        ll = []
        for i in nl:
            ll.append(i[:-6])

        l = l[:-21] + ll

        chicken = pd.DataFrame(columns=['Name', 'catagory', 'description'])

        chicken['Name'] = l

        catagory = ['chicken' for i in range(len(l))]

        chicken['catagory'] = catagory

        chicken['description'] = self.description(url)

        return chicken

    def meat(self):
        url = 'https://food.ndtv.com/recipes/meat-recipes'

        data = requests.get(url)

        soup = BeautifulSoup(data.content, 'html.parser')

        s = soup.findAll('img', {'class': 'lazy'})

        l = []

        for i in s:
            i = str(i)
            t = i.split('title')
            name = t[-1].split('width')[0]
            name = name[2:-8]
            l.append(name)
        nl = l[-21:]
        ll = []
        for i in nl:
            ll.append(i[:-6])

        l = l[:-21] + ll

        meat = pd.DataFrame(columns=['Name', 'catagory', 'description'])

        meat['Name'] = l

        catagory = ['meat' for i in range(len(l))]

        meat['catagory'] = catagory

        meat['description'] = self.description(url)

        return meat

    def seafood(self):
        url = 'https://food.ndtv.com/recipes/seafood-recipes'

        data = requests.get(url)

        soup = BeautifulSoup(data.content, 'html.parser')

        s = soup.findAll('img', {'class': 'lazy'})

        l = []

        for i in s:
            i = str(i)
            t = i.split('title')
            name = t[-1].split('width')[0]
            name = name[2:-8]
            l.append(name)
        nl = l[-21:]
        ll = []
        for i in nl:
            ll.append(i[:-6])

        l = l[:-21] + ll

        seafood = pd.DataFrame(columns=['Name','sub_catagory','description'])

        seafood['Name'] = l

        catagory = ['seafood' for i in range(len(l))]

        seafood['sub_catagory'] = catagory

        seafood['description'] = self.description(url)

        return seafood

    def rice(self):
        url = 'https://food.ndtv.com/recipes/rice-recipes'

        data = requests.get(url)

        soup = BeautifulSoup(data.content, 'html.parser')

        s = soup.findAll('img', {'class': 'lazy'})

        l = []

        for i in s:
            i = str(i)
            t = i.split('title')
            name = t[-1].split('width')[0]
            name = name[2:-8]
            l.append(name)
        nl = l[-21:]
        ll = []
        for i in nl:
            ll.append(i[:-6])

        l = l[:-21] + ll

        rice = pd.DataFrame(columns=['Name', 'catagory', 'description'])

        rice['Name'] = l

        catagory = ['rice' for i in range(len(l))]

        rice['catagory'] = catagory

        rice['description'] = self.description(url)

        return rice

    def bread(self):
        url = 'https://food.ndtv.com/recipes/breads-recipes'

        data = requests.get(url)

        soup = BeautifulSoup(data.content, 'html.parser')

        s = soup.findAll('img', {'class': 'lazy'})

        l = []

        for i in s:
            i = str(i)
            t = i.split('title')
            name = t[-1].split('width')[0]
            name = name[2:-8]
            l.append(name)
        nl = l[-21:]
        ll = []
        for i in nl:
            ll.append(i[:-6])

        l = l[:-21] + ll

        bread = pd.DataFrame(columns=['Name', 'catagory', 'description'])

        bread['Name'] = l

        catagory = ['bread' for i in range(len(l))]

        bread['catagory'] = catagory

        bread['description'] = self.description(url)

        return bread

    def desserts(self):
        url = 'https://food.ndtv.com/recipes/desserts-recipes'

        data = requests.get(url)

        soup = BeautifulSoup(data.content, 'html.parser')

        s = soup.findAll('img', {'class': 'lazy'})

        l = []

        for i in s:
            i = str(i)
            t = i.split('title')
            name = t[-1].split('width')[0]
            name = name[2:-8]
            l.append(name)
        nl = l[-21:]
        ll = []
        for i in nl:
            ll.append(i[:-6])

        l = l[:-21] + ll

        desserts = pd.DataFrame(columns=['Name','sub_catagory','description'])

        desserts['Name'] = l

        catagory = ['desserts' for i in range(len(l))]

        desserts['sub_catagory'] = catagory

        desserts['description'] = self.description(url)

        return desserts

    def durga_puja(self):
        url = 'https://food.ndtv.com/recipes/durga-puja-recipes'

        data = requests.get(url)

        soup = BeautifulSoup(data.content, 'html.parser')

        s = soup.findAll('img', {'class': 'lazy'})

        l = []

        for i in s:
            i = str(i)
            t = i.split('title')
            name = t[-1].split('width')[0]
            name = name[2:-8]
            l.append(name)
        # print(l[-6:])
        nl = l[-6:]
        ll = []
        for i in nl:
            ll.append(i[:-6])

        l = l[:-6] + ll

        durga_puja = pd.DataFrame(columns=['Name', 'sub_catagory', 'description'])

        durga_puja['Name'] = l

        catagory = ['durga puja' for i in range(len(l))]

        durga_puja['sub_catagory'] = catagory

        durga_puja['description'] = self.description(url)

        return durga_puja

    def basic_data_build(self):
        df = pd.concat([self.healthy(), self.snacks()], ignore_index=True)

        df.to_csv('data.csv')
        print('basic_finish')

    def data_vegetarian_build(self):
        df = pd.read_csv('data.csv')
        df_new = pd.concat([df, self.vegetarian()])

        df_new.to_csv('data.csv')
        print('vegetarian_finish')

    def data_chicken_build(self):
        df = pd.read_csv('data.csv')
        df_new = pd.concat([df, self.chicken()])

        df_new.to_csv('data.csv')
        print('chicken_finish')

    def data_meat_build(self):
        df = pd.read_csv('data.csv')
        df_new = pd.concat([df, self.meat()])

        df_new.to_csv('data.csv')
        print('meat_finish')

    def data_seafood_build(self):
        df = pd.read_csv('data.csv')
        df_new = pd.concat([df, self.seafood()])

        df_new.to_csv('data.csv')
        print('seafood_finish')

    def data_rice_build(self):
        df = pd.read_csv('data.csv')
        df_new = pd.concat([df, self.rice()])

        df_new.to_csv('data.csv')
        print('rice_finish')

    def data_bread_build(self):
        df = pd.read_csv('data.csv')
        df_new = pd.concat([df, self.bread()])

        df_new.to_csv('data.csv')
        print('bread_finish')

    def data_desserts_build(self):
        df = pd.read_csv('data.csv')
        df_new = pd.concat([df, self.desserts()])

        df_new.to_csv('data.csv')
        print('desserts_finish')

    def data_durga_puja_build(self):
        df = pd.read_csv('data.csv')
        df_new = pd.concat([df,self.durga_puja()])

        df_new.to_csv('data.csv')
        print('desserts_finish')
