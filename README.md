# NYC Restaurant Inspection Results — Three Data Questions

## Why I chose this dataset
I chose the NYC restaurant inspection results dataset because it contains real inspectation records from restaurants in New York City. It is easy to understand because each row represents a restaurant inspection record, and the columns describe information about the restaurant and its inspection, such as borough, cuisine, inspection date, and grade.

The dataset it also useful for asking questions about restaurant inspection records and comparing different categories, while still having clear limits. For instance, the grading for some restaurants remain empty, that is unknown to us. Another thing is that the GRADE column contains categories such as A, B, and C, it is a catagory, not a number that can be quantified. Also, the inspectation focuses on a limited dimension. 

The dataset is available through NYC Open Data: https://data.cityofnewyork.us/Health/NYC-Restaurant-Inspection-Results/gv23-aida

## Three data questions

# Question: How many restaurant inspection records are in Manhattan?

#count = 0
#for row in restaurants:
#    if row["BORO"] == "Manhattan":
#        count += 1
#print(count)
#output: 425

Why the data structure supports this question:
This works because the dataset is tabular: each row represents a restaurant inspection record, and the BORO column stores the borough where the restaurant is located. Since each row is one observation, counting the rows where BORO equals "Manhattan" gives the total number of Manhattan restaurant inspection records.

# Question: How many restaurant inspection records received an A grade?

#a_count=0
#not_a_count=0
#for row in restaurants:
#    grade=row["GRADE"]
#    if grade=="A":
#        a_count+=1
#print("A grade:", a_count)
#output: 64

Why the data structure supports this question:
This works because the GRADE column stores the inspection grade for each record. We can check the value of the GRADE column for every row and count the rows where the grade is "A". The list of dictionaries structure makes it easy to access the GRADE value for each inspection record.

# Question: How many Manhattan restaurant inspection records received an A grade?

#manhattan_a=0
#manhattan_not_a=0
#for row in restaurants:
#    if row["BORO"]=="Manhattan":
#        if row["GRADE"]=="A":
#            manhattan_a+=1
#        else:
#            manhattan_not_a+=1
#print("Manhattan A grade:",manhattan_a)
#print("Manhattan not A grade:",manhattan_not_a)
#output: Manhattan A grade: 21, manhattan not A grade: 404


Why the data structure supports this question:
This works because we can filter rows using two conditions: BORO must be "Manhattan" and GRADE must be "A". The dataset's one-row-per-inspection-record structure makes it possible to combine these conditions and count the inspection records that meet both requirements.

What the Data Cannot Answer

A question I might want to answer is: “Which restaurant is the best restaurant in New York City?” This dataset cannot answer that because the grading is based on simple letter rather than exact scores to compare. So it is hard to compare restaurants with the same letter grade. Some grading results as well as grading details are missing, making it confusing for the grading criteria. The simple way of grading with letter could be confusing because many restaurants shares the same grading results and it is hard for the consumers to tell what exactly are they good at or better than others.
