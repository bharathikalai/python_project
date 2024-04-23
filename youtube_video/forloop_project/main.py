
def calculate_sum(numbers):
    total = 0

    for num in numbers:
        total +=num
    return total


def main():
    numbers = []
    print("enter numbers to calculate the sum (enter done to finish)")
    while True:
        user_input = input("enter a number: ")

        if user_input.lower()  == 'done':
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("invalid input! please enter a valid number  or done to finish")

        if numbers:
            total_sum = calculate_sum(numbers)
            print("sum of the numbers:",total_sum)
        else:
            print("no number entered. exiting..")

if __name__ == "__main__":
    main()