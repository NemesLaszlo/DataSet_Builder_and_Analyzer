from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import random

class dataSetBasicAnalyze:

    def __init__(self):
        self.df = pd.read_csv('data.csv')

    def base_clean(self):
        l = ['Name', 'catagory', 'description', 'sub_catagory']
        drop = []
        columns = list(self.df.columns)
        for col in columns:
            if col not in l:
                drop.append(col)
        if drop != []:
            self.df = self.df.drop(drop, axis=1)

    def add_veg_nonveg_column(self):
        l = ['chicken', 'wings', 'meat', 'salmon', 'salmons', 'cob', 'cobs', 'kebab', 'kebabs', 'fish', 'snake',
             'gosht', 'bacon', 'mutton', 'lamb', 'egg', 'eggs']
        nv = ['chicken', 'meat']
        vg_nv = []

        for name, cat in zip(self.df.Name, self.df.catagory):
            n = name.split()
            f = 0
            if cat in nv:
                vg_nv.append('non-veg')
            else:
                for i in n:
                    if i.lower() in l:
                        f = 1
                if f == 1:
                    vg_nv.append('non-veg')
                else:
                    vg_nv.append('veg')

        self.df['Veg_Non'] = vg_nv
        print(self.df.Veg_Non.value_counts())

    def add_review_column(self):
        review = []
        for i in range(self.df.shape[0]):
            review.append(random.randint(1, 5))
        self.df['Review'] = review

    def add_price_column(self):
        price = []
        for i in range(self.df.shape[0]):
            price.append(random.randrange(200, 700, 5))
        self.df['Price'] = price

    def add_nutrient_column(self):
        url = 'http://www.englishkitab.com/en/Vocabulary/List-Of-Dry-Fruits.html'

        data = requests.get(url)

        soup = BeautifulSoup(data.content, 'html.parser')

        s = soup.find('td')

        s = s.text.split('\t')[:-1]
        dry_fruits = list(filter(lambda x: x != 'Dry Fruit\n ' and x != '', s))

        url = 'https://www.redcrossblood.org/donate-blood/blood-donation-process/before-during-after/iron-blood-donation/iron-rich-foods.html'

        data = requests.get(url)

        soup = BeautifulSoup(data.content, 'html.parser')

        s = soup.findAll('div', {'class': 'par-33'})

        l = []
        iron = []
        for html in s:
            l = html.ul.text.split('\n')
            l = l[1:-1]

            iron = iron + l

        url = 'https://www.medicalnewstoday.com/articles/322585.php#non-dairy-sources-of-calcium'

        data = requests.get(url)

        soup = BeautifulSoup(data.content, 'html.parser')

        s = soup.findAll('h3')
        calcium = []
        for i in s[:-1]:
            calcium.append(i.text.split('.')[1].strip())

        url = 'https://www.healthline.com/nutrition/foods-high-in-sodium#section1'

        data = requests.get(url)

        soup = BeautifulSoup(data.content, 'html.parser')

        s = soup.findAll('div', {'class': 'css-0'})
        sodium = []
        for i in s[:-1]:
            sodium.append(i.a.text.split('.')[1].strip())

        url = 'https://www.healthline.com/nutrition/iodine-rich-foods#section1'

        data = requests.get(url)

        soup = BeautifulSoup(data.content, 'html.parser')

        s = soup.findAll('div', {'class': 'css-0'})
        iodine = []
        for i in s[:-1]:
            iodine.append(i.a.text.split('.')[1].strip())

        url = 'https://www.healthline.com/nutrition/10-foods-high-in-magnesium#section11'

        data = requests.get(url)

        soup = BeautifulSoup(data.content, 'html.parser')

        s = soup.findAll('div', {'class': 'css-0'})
        magnesium = []
        for i in s[:-1]:
            magnesium.append(i.a.text.split('.')[1].strip())

        url = 'https://www.healthline.com/health/selenium-foods#cashews'

        data = requests.get(url)

        soup = BeautifulSoup(data.content, 'html.parser')

        s = soup.findAll('div', {'class': 'css-0'})
        selenium = []
        for i in s[2:]:
            selenium.append(i.a.text.split('.')[1].strip())
        #     print(i.a.text.split('.')[1].strip())

        url = 'https://www.healthline.com/nutrition/20-delicious-high-protein-foods'

        data = requests.get(url)

        soup = BeautifulSoup(data.content, 'html.parser')

        s = soup.findAll('div', {'class': 'css-0'})
        protien = []
        for i in s[:-1]:
            protien.append(i.a.text.split('.')[1].strip())

        url = 'https://www.medicalnewstoday.com/articles/321522.php#high-protein-foods-for-weight-loss'

        data = requests.get(url)

        soup = BeautifulSoup(data.content, 'html.parser')

        s = soup.findAll('p')

        for p in s:
            if p.strong:
                protien.append(p.strong.text.split('.')[1].strip())

        url = 'https://www.healthline.com/nutrition/12-healthy-high-carb-foods'

        data = requests.get(url)

        soup = BeautifulSoup(data.content, 'html.parser')

        s = soup.findAll('div', {'class': 'css-0'})
        carb = []
        for i in s[:-1]:
            carb.append(i.a.text.split('.')[1].strip())

        url = 'https://www.medicalnewstoday.com/articles/323110.php#dried-fruits'

        data = requests.get(url)

        soup = BeautifulSoup(data.content, 'html.parser')

        s = soup.findAll('h3')

        for i in s[:-1]:
            carb.append(i.text.split('.')[1].strip())

        url = 'https://www.tuasaude.com/en/high-carb-foods/'

        data = requests.get(url)

        soup = BeautifulSoup(data.content, 'html.parser')

        s = soup.findAll('td')

        for i in range(3, len(s), 3):
            carb.append(s[i].text.strip())

        vitamins = ['ham', 'soymilk', 'watermelon', 'acorn squash', 'milk', 'yogurt', 'cheese', 'whole',
                    'enriched grains', 'cereals',
                    'meat', 'poultry, fish', 'fortified', 'whole grains', 'mushrooms', 'potatoes',
                    'chicken', ' whole grains', 'broccoli', ' avocados', 'mushrooms',
                    'meat', 'fish', ' poultry', 'legumes', ' tofu', 'soy', 'bananas',
                    'Whole grains', ' eggs', 'soybeans', 'fish',
                    'Fortified grains', 'cereals', 'asparagus', 'spinach', 'broccoli', 'legumes', 'peas', 'chickpeas',
                    'orange',
                    ]

        B12 = ['Meat', ' poultry', ' fish', ' milk', 'cheese', 'cereals', 'yogurt', 'dahi']

        Vitamin_C = ['margarita', 'Citrus fruit', ' potatoes', 'broccoli', 'bell peppers', 'spinach', 'strawberries',
                     'tomatoes', 'Brussels sprouts']

        Vitamin_A = ['beef', 'liver', 'eggs', 'egg', 'shrimp', 'fish', 'fortified milk', ' sweet potatoes', 'carrots',
                     'pumpkins', 'spinach', ' mangoes']

        Vitamin_A += dry_fruits

        Vitamin_D = ['milk', 'cereals', ' fatty', 'fish']

        Vitamin_E = ['vegetables oils', 'leafy green', 'whole grains', 'nuts']

        Vitamin_K = ['Cabbage', 'eggs', 'egg', ' milk', 'spinach', 'broccoli', ' kale']

        Calcium = ['keer', 'yogurt', 'cheese', 'milk', 'salmon', 'leafy green', 'Cappuccino'] + calcium

        Chloride = ['salt']

        Magnesium = ['chocolate', 'Spinach', 'broccoli', 'legumes', 'seeds'] + magnesium

        Potassium = ['cake', 'meat', 'milk', 'fruits', 'vegetables', 'grains', 'legumes']

        Sodium = ['salt', 'soy sauce', 'vegetables'] + sodium

        Chromium = ['meat', 'poultry', 'fish', 'nuts', 'cheese']

        Copper = ['shellfish', 'nuts', 'seeds', 'beans', ' prunes']

        Fluoride = ['fish', 'teas']

        Iodine = ['salt', 'seafood'] + iodine

        Iron = ['red meat', 'poultry', 'eggs', 'egg', 'fruits', 'green', 'fortified bread'] + iron

        Manganese = ['nuts', 'legumes', 'whole grains', 'tea', 'coffee', 'chai']

        Selenium = ['banana', 'Organ meat', 'seafood', 'walnuts'] + selenium

        Zinc = ['meat', 'shellfish', 'legumes', 'whole grains']

        Protien = protien + ['cookie', 'cookies', 'mutton', 'meat', 'gosht', 'Chicken', 'Wings', 'Meat', 'Salmon',
                             'Cob', 'Kebab', 'Fish', 'Snake', 'Gosht', 'Bacon', 'Mutton', 'Lamb']

        Fiber = ['Salad', 'salad']

        Phosphorus = ['paneer', 'kebab']

        Carbohydrates = carb + ['Poha', 'aloo', 'buttter', 'ghee', 'rice', 'biryani', 'pulao']

        Nutritions = {'Phosphorus': Phosphorus, 'Fiber': Fiber, 'Vitamins': vitamins, 'B12': B12,
                      'Vitamin_C': Vitamin_C, 'Vitamin_A': Vitamin_A, 'Vitamin_D': Vitamin_D, 'Vitamin_E': Vitamin_E,
                      'Vitamin_K': Vitamin_K,
                      'Calcium': Calcium, 'Chloride': Chloride, 'Magnesium': Magnesium, 'Potassium': Potassium,
                      'Sodium': Sodium,
                      'Chromium': Chromium, 'Copper': Copper, 'Fluoride': Fluoride,
                      'Iodine': Iodine, 'Iron': Iron, 'Manganese': Manganese, 'Selenium': Selenium, 'Zinc': Zinc,
                      'Protien': Protien, 'Carbohydrates': Carbohydrates}

        nutrients = []
        for name in self.df.Name:
            name = name.split()
            s = ''
            for i in name:
                for nutrient, food in Nutritions.items():
                    for j in food:
                        if i.lower().strip() == j.lower().strip():
                            if str(nutrient) not in s:
                                s += str(nutrient) + ' '
                            # nutrient.append(s)
            if s == '':
                nutrients.append(np.nan)
                # print('none',name)
            else:
                nutrients.append(s)
                # print(s,name)

        self.df['Nutrient'] = nutrients
        self.df.catagory.unique()
        self.df.sub_catagory.unique()

    def data_fill(self):
        for i in range(self.df.shape[0]):
            if self.df.loc[i, 'catagory'] == 'meat' and self.df.loc[i, 'Nutrient'] == 'none':
                self.df.loc[i, 'Nutrient'] = 'Protien'

        for i in range(self.df.shape[0]):
            if self.df.loc[i, 'catagory'] == 'rice' and self.df.loc[i, 'Nutrient'] == 'none':
                self.df.loc[i, 'Nutrient'] = 'Carbohydrates'

        for i in range(self.df.shape[0]):
            if self.df.loc[i, 'catagory'] == 'chicken' and self.df.loc[i, 'Nutrient'] == 'none':
                self.df.loc[i, 'Nutrient'] = 'Protien'

        for i in range(self.df.shape[0]):
            if self.df.loc[i, 'sub_catagory'] == 'seafood' and self.df.loc[i, 'Nutrient'] == 'none':
                self.df.loc[i, 'Nutrient'] = 'Vitamin_A'

        for i in range(self.df.shape[0]):
            if self.df.loc[i, 'catagory'] == 'bread' and self.df.loc[i, 'Nutrient'] == 'none':
                self.df.loc[i, 'Nutrient'] = 'Protien Vitamins'

        for i in range(self.df.shape[0]):
            if self.df.loc[i, 'sub_catagory'] == 'vegetarian' and self.df.loc[i, 'Nutrient'] == 'none':
                self.df.loc[i, 'Nutrient'] = 'Protien Calcium'

        for i in range(self.df.shape[0]):
            if self.df.loc[i, 'sub_catagory'] == 'navratri' and self.df.loc[i, 'Nutrient'] == 'none':
                self.df.loc[i, 'Nutrient'] = 'Protien Fibre'

        for i in range(self.df.shape[0]):
            if self.df.loc[i, 'sub_catagory'] == 'diwali' and self.df.loc[i, 'Nutrient'] == 'none':
                self.df.loc[i, 'Nutrient'] = 'Protien Carbohydrate'

        for i in range(self.df.shape[0]):
            if self.df.loc[i, 'sub_catagory'] == 'holi' and self.df.loc[i, 'Nutrient'] == 'none':
                self.df.loc[i, 'Nutrient'] = 'Protien Carbohydrate Vitamins'

        for i in range(self.df.shape[0]):
            if self.df.loc[i, 'sub_catagory'] == 'breakfast' and self.df.loc[i, 'Nutrient'] == 'none':
                self.df.loc[i, 'Nutrient'] = 'Fibre Iron Vitamins'

        for i in range(self.df.shape[0]):
            if self.df.loc[i, 'sub_catagory'] == 'healthy' and self.df.loc[i, 'Nutrient'] == 'none':
                self.df.loc[i, 'Nutrient'] = 'Fibre Iron Vitamins Carbohydrates'

        for i in range(self.df.shape[0]):
            if self.df.loc[i, 'sub_catagory'] == 'kids' and self.df.loc[i, 'Nutrient'] == 'none':
                self.df.loc[i, 'Nutrient'] = 'Calcium Iron'

        for i in range(self.df.shape[0]):
            if self.df.loc[i, 'sub_catagory'] == 'eid' and self.df.loc[i, 'Nutrient'] == 'none':
                self.df.loc[i, 'Nutrient'] = 'Protien'

        for i in range(self.df.shape[0]):
            if self.df.loc[i, 'sub_catagory'] == 'christmas' and self.df.loc[i, 'Nutrient'] == 'none':
                self.df.loc[i, 'Nutrient'] = 'Protien Carbohydrates'

        for i in range(self.df.shape[0]):
            if self.df.loc[i, 'sub_catagory'] == 'dinner' and self.df.loc[i, 'Nutrient'] == 'none':
                self.df.loc[i, 'Nutrient'] = 'Protien Carbohydrates'

        for i in range(self.df.shape[0]):
            if self.df.loc[i, 'sub_catagory'] == 'desserts' and self.df.loc[i, 'Nutrient'] == 'none':
                self.df.loc[i, 'Nutrient'] = 'Sugar Carbohydrates'

        for i in range(self.df.shape[0]):
            if self.df.loc[i, 'catagory'] == 'snacks' and self.df.loc[i, 'Nutrient'] == 'none':
                self.df.loc[i, 'Nutrient'] = 'Protien Carbohydrates'

        for i in range(self.df.shape[0]):
            if self.df.loc[i, 'catagory'] == 'easter' and self.df.loc[i, 'Nutrient'] == 'none':
                self.df.loc[i, 'Nutrient'] = 'Protien Carbohydrates'

        for i in range(self.df.shape[0]):
            if self.df.loc[i, 'sub_catagory'] == 'durga puja' and self.df.loc[i, 'Nutrient'] == 'none':
                self.df.loc[i, 'Nutrient'] = 'Protien Carbohydrates'

    def fill_nan_values(self):
        l = ['Cookie', 'Cookies', 'cookie', 'cookies']
        l1 = ['Paneer', 'paneer']
        l2 = ['Salad', 'salad']
        l3 = ['Thandai', 'thandai']
        l4 = ['milk', 'Milk']
        l5 = ['soup', 'Soup']
        l6 = ['Cake', 'cake']

        more = ['chicken', 'almond', 'chocolate', 'kheer', 'cake', 'curry', 'rice', 'biryani', 'halwa', 'fish', 'aloo',
             'mutton',

             'cookies', 'baked', 'kebab', 'christmas', 'ladoo', 'badam', 'strawberry', 'apple', 'salad', 'tikka',
             'lamb',

             'soup', 'banana', 'vada', 'bread', 'sauce', 'kaju', 'paneer', 'prawn', 'barfi', 'mango', 'thandai',
             'coconut',

             'dahi', 'pizza', 'modak', 'rasmalai', 'dal', 'malai', 'gosht', 'kofta', 'gujiya', 'pasta',

             'pulao', 'methi', 'poha', 'butter', 'dosa', 'carrot', 'chaat', 'kebabs', 'kulfi', 'gajar',

             'korma', 'pista', 'gulab', 'khichdi', 'palak', 'roti', 'roast', 'tikki', 'cheese', 'matar', 'smoothie',

             'cranberry', 'sabudana', 'rabdi', 'berry', 'coffee', 'paratha', 'walnut', 'spicy', 'potato', 'beetroot',

             'anjeer', 'samosa', 'kachori', 'gulkand', 'risotto', 'margarita', 'honey', 'corn', 'nuts', 'roasted',

             'spinach', 'sev', 'cardamom', 'dome', 'sangria', 'chawal', 'arbi', 'mushroom', 'tea', 'egg', 'pie',

             'parantha', 'kulcha', 'khaja', 'rabri', 'jalebi', 'bhaji', 'chilli', 'tricolour', 'chikki', 'zucchini',

             'gluten-free', 'barley', 'raspberry', 'chakli', 'dip', 'shankarpali', 'dessert', 'cashew', 'tomato',
             'soya',

             'stuffed', 'chana', 'steam', 'bao', 'peda', 'tiranga', 'pav', 'idli', 'seed', 'saffron', 'love', 'chutney',

             'cocktail', 'mint', 'garlic', 'turkey', 'microwave', 'wrapped', 'keema', 'shami',

             'ghevar', 'pancakes', 'pudding', 'papad', ]

        for i in range(self.df.shape[0]):

            s = self.df.loc[i, 'Name'].split()
            for j in s:
                if j in l:
                    self.df.loc[i, 'catagory'] = 'cookie'

        for i in range(self.df.shape[0]):

            s = self.df.loc[i, 'Name'].split()
            for j in s:
                if j in l1:
                    self.df.loc[i, 'catagory'] = 'paneer'

        for i in range(self.df.shape[0]):

            s = self.df.loc[i, 'Name'].split()
            for j in s:
                if j in l2:
                    self.df.loc[i, 'catagory'] = 'salad'

        for i in range(self.df.shape[0]):

            s = self.df.loc[i, 'Name'].split()
            for j in s:
                if j in l3:
                    self.df.loc[i, 'catagory'] = 'thandai'

        for i in range(self.df.shape[0]):

            s = self.df.loc[i, 'Name'].split()
            for j in s:
                if j in l4:
                    self.df.loc[i, 'catagory'] = 'milk'

        for i in range(self.df.shape[0]):

            s = self.df.loc[i, 'Name'].split()
            for j in s:
                if j in l5:
                    self.df.loc[i, 'catagory'] = 'soup'

        for i in range(self.df.shape[0]):

            s = self.df.loc[i, 'Name'].split()
            for j in s:
                if j in l6:
                    self.df.loc[i, 'catagory'] = 'cake'

        for i in range(self.df.shape[0]):

            if str(self.df.loc[i, 'catagory']) == 'nan':
                s = self.df.loc[i, 'Name'].split()
                for j in s:
                    if j.lower() in more:
                        self.df.loc[i, 'catagory'] = j

    def fill_nans_from_description(self):
        l = ['broccoli', 'shorba', 'gluten', 'scotch', 'lentil', 'kahwa', 'kiwi', 'oats', 'wings', 'momos',

             'gajak', 'salmon', 'appam', 'basil', 'pithe', 'warm', 'kinnu', 'punch', 'spanish', 'milk', 'fresh',
             'cappuccino',

             'plum', 'tawa', 'kadai', 'kofte', 'malabari', 'coriander', 'pistachio', 'kalakand', '(vrat)', 'upma',
             'dundee',

             'gehun', 'sushi', 'khoya', 'panacotta', 'eggless', 'easter', 'kashmiri', 'khus', 'besan', 'sohan',
             'panjiri',

             'malpua', 'payesh', 'imarti', 'atte', 'petha', 'omelette', 'laddu', 'chhena', 'almonds', 'chargrilled',
             'bell',

             'glazed', 'watermelon', 'polenta', 'recipe', 'som', 'tam', 'tangy', 'amaranth', 'moong', 'missi',

             'quesadilla', 'dragon', 'fire', 'argentino', 'belgian', 'chop', 'moonglet', 'lasooni',

             'pakori', 'zaitooni', 'croquettes', 'gujiyas', 'hariyali', 'apricot', 'gokul', 'shower', 'devils', 'onion',

             'gur', 'maple', 'ice', 'desi', 'gobhi', 'mastani', 'drink', 'hot', 'mocha', 'whisky', 'bourbon', 'irish',

             'boondi', 'amritsari', 'cauliflower', 'rum', 'fritters', 'seared', 'crab', 'cajun', 'bacon', 'mongolian',

             'rava', 'pineapple', 'bruschetta', 'breton', 'luchi',

             'parotta', 'poppy', 'brownie', 'macaroons', 'crunch', 'turkish', 'vanilla', 'cinnamon', 'cookie', 'indian',

             'bedmi', 'raseele', 'suji', 'zaffrani', 'nariyal', 'aanarsa', 'assorted', 'yogurt', 'creamy', 'sheer',

             'pakode', 'kele', 'thepla', 'bonda', 'singhare', 'jalapeno', 'makki', 'chole', 'daal', 'pani', 'keerai',

             'vadi', 'basundi', 'dhokli', 'dhokla', 'pohe', 'papdi', 'ras']
        for i in range(self.df.shape[0]):

            if str(self.df.loc[i, 'catagory']) == 'nan':
                if len(str(self.df.loc[i, 'description'])) > 2:
                    s = str(self.df.loc[i, 'description']).split()
                    for j in s:
                        if j.lower() in l:
                            self.df.loc[i, 'catagory'] = j

    def save(self):
        self.df.to_csv('dataset.csv')

    def dataset_clean_prepare(self):
        self.base_clean()
        self.add_veg_nonveg_column()
        self.add_review_column()
        self.add_price_column()
        self.add_nutrient_column()
        self.data_fill()
        self.fill_nan_values()
        self.fill_nans_from_description()
        self.save()
