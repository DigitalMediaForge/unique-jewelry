import random

class Category:

    categoryDictionary = {
        'Bez kategorii': 21, 
        'Bransoletki': 79, 
        'Bransoletki na nogę': 86, 
        'Bransoletki z pierścionkiem': 100, 
        'Bransolety skórzane': 95, 
        'Broszki': 105, 
        'Chokery': 90, 
        'Dziecko': 83, 
        'Klipsy': 80, 
        'Kobieta': 77, 
        'Kolczyki': 78, 
        'Kolie': 82, 
        'Łańcuszki': 87, 
        'Łańcuszki do okularów': 94, 
        'Mężczyzna': 88, 
        'Mysterybox': 98, 
        'Naszyjniki': 81, 
        'Naszyjniki warstwowe': 92, 
        'Nausznice': 89, 
        'Nieśmiertelniki': 97, 
        'Opakowania i dodatki': 104, 
        'Paski': 93, 
        'Perfumy': 99, 
        'Pierścionki': 85, 
        'PIN': 91, 
        'Piny': 102, 
        'Spinki': 101, 
        'Vouchery podarunkowe': 103, 
        'Wisiorki': 84, 
        'Zawieszki': 96
    }

    def __init__(self, wcapi) -> None:
        self.wcapi = wcapi

    def retrieve_category_ids(self, csvCategoriesRow):
        list = csvCategoriesRow.split(' > ')
        categoryIds = {}

        for categoryName in list:
            given_id = self.categoryDictionary.get(categoryName)
            # if given_id is None:
            #     given_id = self.create_new(category_name)
            categoryIds[categoryName] = given_id

        return categoryIds

    def create_new(self, name):
        try:
            response = self.wcapi.post("products/categories", {
                "name": name
            }).json()
            print("Category for: " + response['name'] + " was created with ID: " + str(response['id']))
        except Exception as e:
            print(e)

    def get_all_static(self):
        if len(self.categoryDictionary) == 0:
            category_json = self.wcapi.get("products/categories?per_page=100").json()
            
            for category in category_json:
                name = category['name']
                id = category['id']
                self.categoryDictionary[name] = id

        return self.categoryDictionary
    

        