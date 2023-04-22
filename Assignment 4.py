#Question 1
m = int(input("Enter your marks: "))

if m < 25:
    print("Grade: F")
elif m >= 25 and m < 45:
    print("Grade: E")
elif m >= 45 and m < 50:
    print("Grade: D")
elif m >= 50 and m < 60:
    print("Grade: C")
elif m >= 60 and m < 80:
    print("Grade: B")
else:
    print("Grade: A")

#Question 2
y = int(input("Enter a year: "))

if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
    print(y, "is a leap year.")
else:
    print(y, "is not a leap year.")

#Question 3
import random

correct_answers = 0
for i in range(1, 11):
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    question = f"Question {i}: {x} x {y} = "
    answer = int(input(question))
    if answer == x*y:
        print("Right!")
        correct_answers += 1
    else:
        print("Wrong! The correct answer is", x*y)
print("You got", correct_answers, "questions right out of 10.")

#Question 4
for i in range(200):
    if i % 5 == 2 and i % 6 == 3 and i % 7 == 2:
        print("The number of pieces in the bowl is:", i)
        break
