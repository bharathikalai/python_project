import pandas as pd


data = pd.DataFrame({
    "name":["bharathi","vijay","vijay","kamal","ramesh","babu","ramya","babu"],
    "age":[26,30,30,90,12,23,30,23],
    "area":[100,200,200,80,80,70,40,0]
    # "city":["new york","chennai","chennai","madurai","salem","nagarkovil","covai","nagarkovil"]
})


#group by the data  using mean

#using this mean we can find the value in group by with average value
grouped_data = data.groupby("name").mean()

print(grouped_data)



# how to find duplicate value in data frame


duplicate_groups = data.groupby(data.columns.to_list()).size()

print(duplicate_groups)


# #how to filter duplicate value only 

filtered_data = data[~data.duplicated()]
print(filtered_data,"ddd")

