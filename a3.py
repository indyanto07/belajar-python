kata = '   acenbusuk   andre   '
kata2 = 'acenbusuk   '
kata3 = 'acen busuk'
ubahkata2 = kata2.zfill(20)
print(kata.rstrip())
print(kata.lstrip())
print(kata2.rstrip().strip("busuk"))
print(kata3.endswith('acen'))
print('---'.join([kata3,kata2,'!']))
print(kata3.split())
print(kata3.replace('acen','abang'))
print(ubahkata2)
