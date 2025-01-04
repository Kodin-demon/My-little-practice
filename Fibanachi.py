# attempt to create a program to calculate fibanachi sequence

firstnum = 0
secondnum = 1
fibseq = []

while firstnum < 100:
    sum = firstnum + secondnum
    fibseq.append(sum)
    firstnum = secondnum
    secondnum = sum

for num in fibseq:
    print(num, end=" ")
