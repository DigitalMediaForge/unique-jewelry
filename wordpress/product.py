IMAGES_URL_WP_CONTENT = 'https://uniquejewelry.pl/woocommerce/wp-content/uploads/2023/importfoto'

class Product:

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

    def create(self, data):
        print(self.wcapi.post("products", data).json())

    def body(self, product_code, name, price, description, externalImages, categories: dict):

        category_data_object = []
        for key in categories:
            category_data_object.append({ "id": categories[key] })

        external_images_object = []
        for externalImage in externalImages:
            external_images_object.append({
                "src": externalImage,
                "name": name,
                "alt": name
            })

        return {
            "name": name,
            "sku": product_code,
            "regular_price": price,
            "description": description,
            "short_description": description,
            "categories": category_data_object,
            "images": external_images_object
        }
    
    def get_all(self):
        print(self.wcapi.get("products").json())
