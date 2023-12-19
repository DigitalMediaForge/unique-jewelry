import csv

categoryCollection = []
categoryBasicCollection = []


with open('download_eur.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    
    for row in csv_reader:

        categoryName = row[8]

        if categoryName not in categoryCollection and line_count != 0:
            categoryCollection.append(categoryName)
            splitted = categoryName.split(' > ')

            subCategory = splitted[0]
            if len(splitted) != 1:
                subCategory = splitted[1]

            if subCategory not in categoryBasicCollection:
                categoryBasicCollection.append(subCategory)

        line_count += 1


# print(categoryCollection)
print(categoryBasicCollection)