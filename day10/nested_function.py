def outer_function():
    print("this is the outer function")

    def inner_function():
        print("this is the inner function")
    inner_function()

outer_function()