
def get_num():
    while True:
        try:
            n = int(input('enter number :'))
            return n
        except:
            print('not a number')
            continue

result = get_num()
print(result)