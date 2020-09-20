import sys
import math

n = int(input())
invalid = []
invalidCount = 0
for i in range(n):
    isbn = input()
    total = 0

    try:
        float(isbn[0:-1])
    except ValueError:
        invalid.append(isbn)
        invalidCount += 1
        continue

    else:
        if(len(isbn) == 10):
            for i in range(0, 9, 1):
                total += int(isbn[i]) * (10 - i)
            if(not (str(abs((total % 11) - 11)) == isbn[-1])
            and not (abs((total % 11) - 11) == 10 and isbn[-1] == 'X')
            and not (total % 11 == 0 and isbn[-1] == '0')):
                invalid.append(isbn)
                invalidCount += 1
        elif(len(isbn) == 13):
            for i in range(0, 12, 1):
                if(i % 2 == 0):
                    total += int(isbn[i]) * 1
                else:
                    total += int(isbn[i]) * 3
            if(not (str(abs((total % 10) - 10)) == isbn[-1])
            and not (total % 10 == 0 and isbn[-1] == '0')):
                invalid.append(isbn)
                invalidCount += 1
        else:
            invalid.append(isbn)
            invalidCount += 1

print(invalidCount, "invalid:")
for i in range(invalidCount):
    print(invalid[i])
