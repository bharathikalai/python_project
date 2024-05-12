# #part 1
import json


data = {'name': 'bharathi', 'age': 26, 'city': 'chennai'}


json_string = json.dumps(data)

print(json_string)


#part 2


#sample json string


json_string = '{"name": "John", "age": 30, "city": "New York"}'



data = json.loads(json_string)

print(data["name"])
print(data["age"])
print(data["city"])

# print(data)


#part 3

#read the json file


with open("/home/bharathibk/github/python_project/devops_python_package/data.json","r") as file:
    data = json.load(file)
    print(data)


# #write 

# data = {
#     "name":"vijay",
#     "age":54,
#     "city":"channei"
# }

# with open("/home/bharathibk/github/python_project/devops_python_package/data.json","w") as file:
#     data = json.dump(data,file)





    