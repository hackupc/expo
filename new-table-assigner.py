import csv, random

table_list = [i for i in range(1,120)]
expo_list = ["1"]

#get submissions from csv
title_col = "Submission Title"
description_col = "Plain Description"
sponsors_row = "Desired Prizes"
link_col = "Submission Url"

input_path = 'data/data.csv'
output_full_path = 'data/data_full.csv'
output_gavel_path = 'data/data_gavel.csv'

gavel = []
full  = []

with open(input_path, newline='') as csvfile:
    submissions_reader = csv.DictReader(csvfile)
    free_tables = table_list[:]
    print(table_list)
    for row in submissions_reader:
        print(row)
        table = random.randint(0, len(free_tables)-1)
        full.append(row)
        gavel.append({'project': row[title_col], 'location': table, 'description':
        row[description_col][:200]})
        # complete_list[-1]["expo"] = expo_list[expo]
        full[-1]['table'] = table_list[table]
        del free_tables[table]

# write full file (for expo website)

with open(output_full_path, 'w') as csvfile:
    fieldnames = ['table', 'project', 'sponsors', 'link']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in full:
        writer.writerow(
        {
            'table': row['table'],
            'project': row[title_col],
            'sponsors': row[sponsors_row],
            'link': row[link_col]
            #'category': ',
        })


# write gavel file (to paste to gavel)

with open(output_gavel_path, 'w') as csvfile:
    fieldnames = ['project', 'location', 'description']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in gavel:
        writer.writerow(row)

