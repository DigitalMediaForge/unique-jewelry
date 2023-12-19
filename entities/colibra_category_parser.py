class ColibraCategoryParser:

    categories = [
        # 'Earrings', 
        # 'Bracelets', 
        # 'Clips', 
        # 'Necklaces', 
        # 'Pendants', 
        # 'Rings', 
        # 'Anklets', 
        # 'Chains', 
        # 'Earmuffs', 
        # 'Chokers', 
        # 'PIN', 
        # 'Layered Necklaces', 
        # 'Belts', 
        # 'Chains for glasses', 
        # 'Dog tags', 
        # 'Mysterybox', 
        # 'Perfume', 
        # 'Bracelets with a ring', 
        # 'Cufflinks', 
        # 'Pins', 
        # 'Gift Vouchers', 
        # 'Packaging and accessories', 
        # 'Brooches'
    ]

    taxonomies = {
        'Chains': 'Apparel & Accessories > Jewelry',
        'Mysterybox': 'Apparel & Accessories > Jewelry',
        'Anklets': 'Apparel & Accessories > Jewelry > Anklets',
        'Chokers': 'Apparel & Accessories > Jewelry > Body Jewelry',
        'Bracelets': 'Apparel & Accessories > Jewelry > Bracelets',
        'Leather bracelets': 'Apparel & Accessories > Jewelry > Bracelets',
        'Bracelets with a ring': 'Apparel & Accessories > Jewelry > Bracelets',
        'Pins': 'Apparel & Accessories > Jewelry > Brooches & Lapel Pins',
        'PIN': 'Apparel & Accessories > Jewelry > Brooches & Lapel Pins',
        'Brooches': 'Apparel & Accessories > Jewelry > Brooches & Lapel Pins',
        'Cufflinks': 'Apparel & Accessories > Jewelry > Brooches & Lapel Pins',
        'Pendants': 'Apparel & Accessories > Jewelry > Charms & Pendants',
        'Earrings': 'Apparel & Accessories > Jewelry > Earrings',
        '': 'Apparel & Accessories > Jewelry > Jewelry Sets',
        'Layered Necklaces': 'Apparel & Accessories > Jewelry > Necklaces',
        'Necklaces': 'Apparel & Accessories > Jewelry > Necklaces',
        'Rings': 'Apparel & Accessories > Jewelry > Rings',
        'Belts': 'Apparel & Accessories > Clothing Accessories > Belts',
        'Clips': 'Apparel & Accessories > Clothing Accessories > Hair Accessories > Hair Pins, Claws & Clips',
        'Chains for glasses': 'Health & Beauty > Personal Care > Vision Care > Eyewear Accessories > Eyewear Straps & Chains',
        'Earmuffs': 'Apparel & Accessories > Clothing Accessories > Earmuffs',
        'Perfume': 'Health & Beauty > Personal Care > Cosmetics > Perfume & Cologne',
        'Gift Vouchers': 'Gift Cards',
        'Packaging and accessories': 'Arts & Entertainment > Party & Celebration > Gift Giving',
        'Dog tags': 'Animals & Pet Supplies > Pet Supplies > Dog Supplies',
    }


    def __init__(self, 
    category) -> None:
        self.categoryCollection = []
        self.originName = category

        list = category.split(' > ')

        self.adWordsGrouping = list[0]

        if len(list) != 1:
            self.type = list[1]
            self.tags = list[1]
            self.taxonomy = self.taxonomies[list[1]]

            if list[0] != 'Baby':
                self.gender = list[0]
                self.ageGroup = 'Adult'
            else: 
                self.gender = ''
                self.ageGroup = 'Child'
        
        else:
            self.type = list[0]
            self.tags = list[0]
            self.gender = ''
            self.ageGroup = 'Adult'
            self.taxonomy = self.taxonomies[list[0]]


    def addCategory(self, categoryName):
        self.categoryCollection.append(categoryName)

