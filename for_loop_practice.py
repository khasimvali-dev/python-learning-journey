# Program 1: Print Numbers from 1 to 10
for i in range(1, 11):
    print(i)
print("------------------")

# Program 2: Print Odd Numbers from 1 to 100
for i in range(1, 101):
    if i % 2 != 0:
        print(i)
print("------------------")

# Program 3: Print Multiples of 5
for i in range(1, 101):
    if i % 5 == 0:
        print(i)
print("------------------")

# Program 4: Print Multiples of 3 and 7
for i in range(1, 101):
    if i % 3 == 0 and i % 7 == 0:
        print(i)
