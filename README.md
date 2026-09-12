# NYC Restaurant Inspection Results — Three Data Questions

## Why I chose this dataset
I chose the NYC restaurant inspection results dataset because it contains real inspectation records from restaurants in New York City. It is easy to understand because each row represents a restaurant inspection record, and the columns describe information about the restaurant and its inspection, such as borough, cuisine, inspection date, and grade.

The dataset it also useful for asking questions about restaurant inspection records and comparing different categories, while still having clear limits. For example, the GRADE column contains categories such as A, B, and C, it is a catagory, not a number that can be quantified. Also, the inspectation focuses on a limited dimension.

The dataset is available through NYC Open Data: https://data.cityofnewyork.us/Health/NYC-Restaurant-Inspection-Results/gv23-aida

## Three data questions

# Question: How many restaurant inspection records are in Manhattan?

#count = 0
#for row in restaurants:
#    if row["BORO"] == "Manhattan":
#        count += 1
#print(count)
#output: 109349

Why the data structure supports this question:
This works because the dataset is tabular: each row represents a restaurant inspection record, and the BORO column stores the borough where the restaurant is located. Since each row is one observation, counting the rows where BORO equals "Manhattan" gives the total number of Manhattan restaurant inspection records.

# Question: How many restaurant inspection records received an A grade?

#a_count = 0
#for row in restaurants:
#    if row["GRADE"] == "A":
#        a_count += 1
#print(a_count)
#output: 97795

Why the data structure supports this question:
This works because the GRADE column stores the inspection grade for each record. We can check the value of the GRADE column for every row and count the rows where the grade is "A". The list of dictionaries structure makes it easy to access the GRADE value for each inspection record.

# Question: How many Manhattan restaurant inspection records received an A grade?

#manhattan_a = 0
#for row in restaurants:
#    if row["BORO"] == "Manhattan":
#        if row["GRADE"] == "A":
#            manhattan_a += 1
#print(manhattan_a)
#output: 37968

Why the data structure supports this question:
This works because we can filter rows using two conditions: BORO must be "Manhattan" and GRADE must be "A". The dataset's one-row-per-inspection-record structure makes it possible to combine these conditions and count the inspection records that meet both requirements.

A question I might want to answer is: Are restaurants with an A grade actually safer for customers than restaurants with a B or C grade?
This dataset cannot fully answer that question because it mainly contains information about restaurant inspections and inspection results. It does not include information such as customer food poisoning cases, customer health outcomes, or every safety problem that may occur outside an inspection. The data also contains inspection records rather than guaranteed unique restaurants, so it would be misleading to assume that every row represents a different restaurant or that an A grade means a restaurant is always completely safe.
