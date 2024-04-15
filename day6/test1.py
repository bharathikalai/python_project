
name = "my name is bharathi thasan"

dicts  = {}

name = name.lower()

for i in name:
    if i.isalpha():
        if i in dicts:
            dicts[i] += 1
        else:
            dicts[i] = 1


for x,y in dicts.items():
    print(f"{x},{y}")