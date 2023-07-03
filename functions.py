# user-defined function
def MitMidMorning():
    print("This is Mid-morning class")


MitMidMorning()
MitMidMorning()


def addtwonumbers():
    x = 7
    y = 23
    print("The sum is", x + y)


addtwonumbers()


def productoftwonumbers():
    x = float(input("Enter first number:"))
    y = float(input("Enter second number:"))
    print("The product is", x * y)


productoftwonumbers()


def calculate_average(dataset):
    total = sum(dataset)
    count = len(dataset)
    average = total / count
    return average


dataset = [4, 5, 9, 8, 9]
answer = calculate_average(dataset)
print("The average is ", answer)

calculate_average(dataset)
