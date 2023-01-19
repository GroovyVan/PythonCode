# Functions

#*args оператор как tuple
#def a(*args):
#    print(args)
#    print(args[0])
#    print(args[1])
#    print(args[2])
#a (5, 14, 66)

def xxr123(*args, **kwargs):
    answer = []
    count = len(args)
    if count == 1:
        start = 0
        stop = args[0]
        step = 1
    elif count == 2:
        start = args[0]
        stop = args[1]
        step = 1
    elif count == 3:
        start = args[0]
        stop = args[1]
        step = args[2]
    else:
        print('invalid params')
        return None
    i = start
    while i < stop:
        answer.append(i)
        i += step
    if 'format' in kwargs:
        format = kwargs['format']
        if format == 'list':
            return answer
        if format == 'tuple':
            return tuple(answer)
        if format == 'set':
            return set(answer)
        return answer
    else:
        return answer

function = xxr123(1, 10, 2)
print('function', function)