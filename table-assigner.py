import csv, random

table_list = [i for i in range(1,50)]
expo_list = ["1", "2"]

#get submissions from csv

with open('data/data.csv', newline='') as csvfile:
    submissions_reader = csv.DictReader(csvfile)
    complete_list = []
    free_expos = expo_list[:]
    expo_free_tables = [table_list[:] for _ in range(len(expo_list))]
    for row in submissions_reader:
        expo = random.randint(0, len(free_expos) - 1)
        table = random.randint(0, len(expo_free_tables[expo]) - 1)
        complete_list.append(row)
        complete_list[-1]["expo"] = expo_list[expo]
        complete_list[-1]["table"] = expo_free_tables[expo][table]
        del expo_free_tables[expo][table]
        if not expo_free_tables[expo]:
            del free_expos[expo]
    
# write all columns filled again

with open('data/data_full.csv', 'w') as csvfile:
    fieldnames = ['expo', 'table', 'project', 'sponsors', 'link', 'category', 'special']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in complete_list:
        writer.writerow(row)
