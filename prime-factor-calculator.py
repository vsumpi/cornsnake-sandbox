leftHand = []
rightHand = []
def division(number):
    for i in range(2,number + 1):
        if number % i == 0:
            leftHand.append(number)
            rightHand.append(i)
            division(int(number / i))
            break

number = int(input("Please enter a number: "))

division(number)

i = 0

# debug
# print(leftHand)
# print(rightHand)

for item in leftHand:
    numstr = str(number)
    bbc = len(numstr)
    intstr = str(item)
    if len(intstr) <= bbc:
        space = (bbc - len(intstr)) * " "
        item = str(space) + str(item)
    print(item, "|", rightHand[i])
    i = i + 1