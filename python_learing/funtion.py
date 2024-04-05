def outer_function():
    def inner_function():
        print("this is the inner fucntion")
    print("this is the outer function")
    inner_function()

outer_function()


def outer_function(x):
    def inner_function(y):
        return y * 2
    result = inner_function(x)
    print("result form inner function",result)
    return result





output = outer_function(5)

print("result from outer function",output)


def factorial(n):
    def calc_factorial(num):
        if num == 0:
            return  1
        else:
            return num * calc_factorial(num - 1)
        
    return calc_factorial(n)


# calculating the factorial(5)
result = factorial(5)

print("factorial of 5 is ",result)