import csv

def filter_houses(filters: dict):
    filtered_rows = []

    file =  open('housePrice.csv', mode='r', encoding='utf-8')
    cs_reader = csv.DictReader(file)
    for row in cs_reader:
        row['Area'] = int(row['Area'])
        row['Room'] = int(row['Room'])

        if row['Parking'] == 'True':
            row['Parking'] = True
        else:
            row['Parking'] = False

        if row['Warehouse'] == 'True':
            row['Warehouse'] = True 
        else:
            row['Warehouse'] = False

        if row['Elevator'] == 'True':
            row['Elevator'] = True 
        else:
            row['Elevator'] = False
            
        row['Price'] = int(row['Price'])

        match = True

        if 'room' in filters: 
            if row['Room'] != filters['room']:
                match = False
        
        if 'area' in filters:
            if row['Area'] < filters['area']:
                match = False

        if 'address' in filters: 
            if row['Address'] != filters['address']:
                match = False

        if 'parking' in filters:
            if row['Parking'] != filters['parking']:
                match = False

        if 'elevator' in filters: 
            if row['Elevator'] != filters['elevator']:
                match = False

        if 'address' in filters: 
            if row['Address'] != filters['address']:
                match = False

        if 'price' in filters: 
            if row['Price'] > filters['price']:
                match = False

        if 'warehouse' in filters: 
            if row['Warehouse'] != filters['warehouse']:
                match = False

        if match:
            filtered_rows.append(row)

    out_file = open('result.csv', mode='w', encoding='utf-8', newline='')
    out_file2 = csv.DictWriter(out_file, fieldnames=['Area', 'Room', 'Parking', 'Warehouse', 'Elevator', 'Address', 'Price'])
    out_file2.writeheader()
    out_file2.writerows(filtered_rows)
