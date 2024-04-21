#python problem solving

#first
def mysterious_function(x):
    return [x] + x
result = mysterious_function(5)
print(result)

# output : TypeError: unsupported operand type(s) for +: 'int' and 'list'


# correct  we cant add list with init using +

def mysterious_function(x):
    return [x] + [x]
result = mysterious_function(5)
print(result)
# output : [5,5]


#python problem 2 

x = 10

def func1():
    x = 20
    def func2():
        nonlocal x
        x +=30
    func2()
    return x
print(func1())

