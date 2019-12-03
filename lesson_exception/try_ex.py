import  os
file = None
try:
    file = open(r'C:/tmp/asdadasd.txt')
    data = file.read()
except FileNotFoundError as d:
    print(f'---->{d.strerror}')
else:
    print('all right')
finally:
    print('finnally')
    if file:

        file.close()
print('///////////////////////////////////')