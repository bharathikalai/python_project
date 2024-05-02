if __name__ == '__main__':
    n = int(input("enter the input"))
    student_marks = {}
    for _ in range(n):
        name, *line = input("enter the name and mark").split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input("enter the name you want to find the average")
    y = student_marks[query_name]
    leng = len(y)
    print(leng,"the leng value")

    aver = sum(y) / len(y)

   
    print("{:.2f}".format(aver))




if __name__ == '__main__':
    n = int(input())  # Input: Number of students
    student_marks = {}  # Dictionary to store student names and their scores
    for _ in range(n):
        name, *line = input().split()  # Input: student's name followed by space-separated scores
        scores = list(map(float, line))  # Convert the scores from strings to floats
        student_marks[name] = scores  # Store the student's name and scores in the dictionary
    
    query_name = input()  # Input: Name of the student for whom the average score is queried
    
    # Check if the query name exists in the dictionary
    if query_name in student_marks:
        # Calculate the average score for the queried student
        average_score = sum(student_marks[query_name]) / len(student_marks[query_name])
        print("{:.2f}".format(average_score))  # Print the average score rounded to two decimal places
    else:
        print("Student not found in the records.")  # Print a message if the student is not found






# name, *line = input().split()
# print("name",name)
# print("line")
# scores = list(map(float,line))

# print(scores,"the value of scores ")


# name, *line = input("again enter the input").split()
# scores = list(map(float, line))
# print("score",scores)

# print("name",name)
# print("line",line)



# x = [10,90,80]

# y = x + x
# print("value of y is",y)
# b = []
# for y in x:
#     print("the value of y is ",y)
#     c = y + y
#     b.append(c)
# b.split(" ",+)
# print(b,"the value of ")



# x = {"bharathi":80,"kalai":80,"arun":70}

# y = x["bharathi"]

# print("the value of y",y)



a = 10 / 2
print("the value of a",a)