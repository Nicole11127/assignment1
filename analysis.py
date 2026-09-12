import csv

def load_csv(filepath):
    data = []

    with open (filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)

    return data

restaurants=load_csv("Restaurant Inspection.csv")

print(restaurants[:2])

print(restaurants[0])

print(restaurants[10:20])

print(restaurants[0].keys())

for row in restaurants[:10]:
    print(row["STREET"])

for row in restaurants[:10]:
    print(
        row["DBA"], row["STREET"], row["ZIPCODE"]
    )

#show me all the restaurants in Manhattan
for row in restaurants:
    if row["BORO"]=="Manhattan":
        print(row["DBA"])

#how many restaurant records are in Manhattan?
count=0
for row in restaurants:
    if row["BORO"]=="Manhattan":
        count+=1
print(count)

# how many restaurant records received an A grade?
a_count=0
not_a_count=0
for row in restaurants:
    if row["GRADE"]=="A":
        a_count+=1
print("A grade:", a_count)

# how many Manhattan restaurants received an A grade?
manhattan_a=0
manhattan_not_a=0
for row in restaurants:
    if row["BORO"]=="Manhattan":
        if row["GRADE"]=="A":
            manhattan_a+=1
        elif row["GRADE"]!="A":
            manhattan_not_a+=1
print("Manhattan A grade:",manhattan_a)
print("Manhattan not A grade:",manhattan_not_a)
