a = 'abcde'
b = 'cdeab'

x = a[0]
a = a.replace(a[0], "")
a += x
print(a, b, x)