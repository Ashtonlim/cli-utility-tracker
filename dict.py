import csv

to_csv = [
    {'name': 'bob', 'age': 25, 'weight': 200},
    {'name': 'jim', 'age': 31, 'weight': 180},
]

keys = to_csv[0].keys()
print(keys)

with open('people.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(to_csv)

with open('people.csv', newline='') as output_file:
    dictReader = csv.DictReader(output_file, delimiter=',')
    line_count = 0
    # print(dictReader)
    for row in dictReader:
        print(f'\t{row["name"]} works in the {row["age"]} department, and was born in {row["weight"]}')
