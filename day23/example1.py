import pandas as pd


data = pd.DataFrame({
    "name":["bharathi","vijay","ajith","kamal","ramesh","babu","ramya","balu"],
    "age":[90,30,80,90,12,23,30,80],
    "city":["new york","chennai","mumbai","madurai","salem","nagarkovil","covai","pune"]
})



print(data.head())


# print(data)

# #info methods
print(data.info())

# #describe method  # Display descriptive statistics about numeric columns


print(data.describe())

#single column
print(data["age"])


# #muliple colum
print(data[["city","age"]])


# # Filtering rows based on a condition

print(data[data["age"]== 90])