# Functions

a = "Hello"
print()#любой параметр
leigth = len(a)
count1 = range(44)
count2 = range(3, 44)
count3 = range(2, 44, 53)

#своя функция список элем от 0 до предела (с указанием)
def xxr123(stop, start = 0, step = 1):
    answer = []
    i = start
    while i < stop:
        answer.append(i)
        i += step
    return answer

function = xxr123(34)
print('function', function)