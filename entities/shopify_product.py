from converters.colibra_product import ColibraProduct
from entities.colibra_category_parser import ColibraCategoryParser

class ShopifyProduct:
    
    def __init__(self) -> None:
        self.rows = []

    def __kilogramToGram(self, weight):
        return str(float(weight) * 1000)

    def createRows(
            self, 
            product: ColibraProduct,
            category: ColibraCategoryParser,
            conditionedVendor = 'Colibra',
            conditionedPublished = 'TRUE',
            conditionedOption1Name = 'Title',
            conditionedInventoryQty = '100',
            conditionedInvetoryPolicy = 'deny',
            conditionedFulfillmentService = 'manual',
            conditionedRequiresShipping = 'TRUE',
            conditionedTaxable = 'TRUE',
            conditionedGiftCard = 'FALSE',
            conditionedCondition = 'new',
            conditionedWeightUnit = 'g',
            conditionedStatus = 'active'
        ):

        self.handle = product.productId
        self.title = '' if not product.name else product.name
        self.bodyHTML = '' if not product.description else product.description
        self.vendor = conditionedVendor
        self.productCategory = category.taxonomy
        self.type = category.type
        self.tags = category.tags
        self.published = conditionedPublished
        self.option1Name = conditionedOption1Name
        self.option1Value = '' if not product.name else product.name
        self.option2Name = ''
        self.option2Value = ''
        self.option3Name = ''
        self.option3Value = ''
        self.variantSKU = '' if not product.ean else product.ean
        self.variantGrams = '' if not product.weight else self.__kilogramToGram(product.weight)
        self.variantInventoryTracker = ''
        self.variantInventoryQty = conditionedInventoryQty
        self.variantInventoryPolicy = conditionedInvetoryPolicy
        self.variantFulfillmentService = conditionedFulfillmentService
        self.variantPrice = product.price
        self.variantCompareAtPrice = ''
        self.variantRequiresShipping = conditionedRequiresShipping
        self.variantTaxable = conditionedTaxable
        self.variantBarcode = ''
        self.imageSrc = '' if not product.img1 else product.img1
        self.imagePosition = '1'
        self.imageAltText = '' if not product.name else product.name
        self.giftCard = conditionedGiftCard
        self.seoTitle = '' if not product.name else product.name
        self.seoDescription = '' if not product.shortDescription else product.shortDescription
        self.googleShoppingGoogleProductCategory = ''
        self.googleShoppingGender = category.gender
        self.googleShoppingAgeGroup = category.ageGroup
        self.googleShoppingMPN = ''
        self.googleShoppingAdWordsGrouping = category.adWordsGrouping
        self.googleShoppingAdWordsLabels = '' if not product.name else product.name
        self.googleShoppingCondition = conditionedCondition
        self.googleShoppingCustomProduct = ''
        self.googleShoppingCustomLabel0 = ''
        self.googleShoppingCustomLabel1 = ''
        self.googleShoppingCustomLabel2 = ''
        self.googleShoppingCustomLabel3 = ''
        self.googleShoppingCustomLabel4 = ''
        self.variantImage = '' if not product.img1 else product.img1
        self.variantWeightUnit = conditionedWeightUnit 
        self.variantTaxCode = ''
        self.costPerItem = ''
        self.priceInternational = ''
        self.compareAtPriceInternational = ''
        self.status = conditionedStatus

        self.rows.append(self.__getDataRow())

        if product.img2 != '':
            self.imageSrc = product.img2
            self.imagePosition = '2'
            self.rows.append(self.__getDataRow())

        if product.img3 != product.img3:
            self.imageSrc = ''
            self.imagePosition = '3'
            self.rows.append(self.__getDataRow())

        if product.img4 != '':
            self.imageSrc = product.img4
            self.imagePosition = '4'
            self.rows.append(self.__getDataRow())

        if product.img5 != '':
            self.imageSrc = product.img5
            self.imagePosition = '5'
            self.rows.append(self.__getDataRow())

        if product.img6 != '':
            self.imageSrc = product.img6
            self.imagePosition = '6'
            self.rows.append(self.__getDataRow())
            
        if product.img7 != '':
            self.imageSrc = product.img7
            self.imagePosition = '7'
            self.rows.append(self.__getDataRow())

        return self.rows

    def __getDataRow(self):
        return [
            self.handle,
            self.title,
            self.bodyHTML,
            self.vendor,
            self.productCategory,
            self.type,
            self.tags,
            self.published,
            self.option1Name,
            self.option1Value,
            self.option2Name,
            self.option2Value,
            self.option3Name,
            self.option3Value,
            self.variantSKU,
            self.variantGrams,
            self.variantInventoryTracker,
            self.variantInventoryQty,
            self.variantInventoryPolicy,
            self.variantFulfillmentService,
            self.variantPrice,
            self.variantCompareAtPrice,
            self.variantRequiresShipping,
            self.variantTaxable,
            self.variantBarcode,
            self.imageSrc,
            self.imagePosition,
            self.imageAltText,
            self.giftCard,
            self.seoTitle,
            self.seoDescription,
            self.googleShoppingGoogleProductCategory,
            self.googleShoppingGender,
            self.googleShoppingAgeGroup,
            self.googleShoppingMPN,
            self.googleShoppingAdWordsGrouping,
            self.googleShoppingAdWordsLabels,
            self.googleShoppingCondition,
            self.googleShoppingCustomProduct,
            self.googleShoppingCustomLabel0,
            self.googleShoppingCustomLabel1,
            self.googleShoppingCustomLabel2,
            self.googleShoppingCustomLabel3,
            self.googleShoppingCustomLabel4,
            self.variantImage,
            self.variantWeightUnit,
            self.variantTaxCode,
            self.costPerItem,
            self.priceInternational,
            self.compareAtPriceInternational,
            self.status
        ]