# loops
print("meow\n"*4)
while True:
    n = int(input("Whats n?"))
    if n > 0:
        break
    for i in range(1, n+1):
        print(i)


def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("What's n?"))
        if n > 0:
            break
        return n


def meow(n):
    for i in range(n):
        print("meow")


student = ["Hermine", "Harry", "Ron"]

for student in student:
    print(student)
