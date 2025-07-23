import csv

vorodi = r'C:\Users\Administrator\Desktop\Python-exercises\1741502118270796.csv'
khorogi = 'Result.csv'  

products = []

with open(vorodi, encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for i in reader:
        name = i['Product Name']
        price = int(i['Price'])
        quantity = int(i['Quantity'])
        total = price * quantity

        products.append({
            'Product Name': name,
            'Price': price,
            'Quantity': quantity,
            'Total Price': total
        })

nsme_field = ['Product Name', 'Price', 'Quantity', 'Total Price']

with open(khorogi,'w', encoding='utf-8') as csvfile:
    sazande = csv.DictWriter(csvfile, fieldnames=nsme_field)
    sazande.writeheader()
    sazande.writerows(products)

print("ba movafaghiat fille (Result.csv) sakhte shod.")
