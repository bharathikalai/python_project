import pandas as pd


data = pd.DataFrame({
    "name":["bharathi","vijay","ajith","kamal","ramesh","babu","ramya","balu"],
    "age":[26,30,80,90,12,23,30,80],
    "city":["new york","chennai","mumbai","madurai","salem","nagarkovil","covai","pune"]
})



#sum method
print(sum(data["age"]))


#min method and max method

print(min(data["age"]))

print(max(data["age"]))


#desc we can find the static of numaeic column
print(data.describe())



print("original dataframe")
print(data)
print()


#edite the single value using indexing

print("modified data")
data.at[1,"age"] = 31
print(data)



print("boolean indexing")
#edit values using boolean indexing
data.loc[data["name"] == "kamal","age"] = 60


print(data)


