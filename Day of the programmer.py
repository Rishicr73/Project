#Link : https://www.hackerrank.com/challenges/day-of-the-programmer/problem
#CODE :


def dayOfProgrammer(year):
    if ((year < 1918) and (year % 4 == 0)) or ((year > 1918) and ((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0))):
        return('12.09.' + str(year))
    elif (year == 1918):
        return('26.09.' + str(year))
    else:
        return('13.09.' + str(year))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
