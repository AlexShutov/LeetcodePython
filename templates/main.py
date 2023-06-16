# This is a sample Python script.
from collections import Counter


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def getTestData():
    return [1, 2, 3]

def getTestString():
    return "some test string"

def testLoop():
    n = 20
    for i in range(0, n):
        print(str(i) + " ")

def testCounter():
    values = [0, 0, 0, 1, 4, 5]
    counter = Counter(values)
    print(counter.items())

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print(getTestData())
    print(f'Greetings: ', getTestString())
    testLoop()
    testCounter()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


