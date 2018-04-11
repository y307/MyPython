
# Time
import time

t1=time.strptime('1:20', '%M:%S')
t2=time.strptime('1:50', '%M:%S')
t3=time.mktime(t2)-time.mktime(t1)
print(t1)
print(t2)
print(t3)

print(time.mktime(t2))
print(time.mktime(t1))
print(time.localtime(t3))
print('\n')

# String
print('String\n')
intg=1
s='{0:02d}'.format(intg)
print(s)
flt=0.5
s='{0:02.3f}'.format(flt)
print(s)

print('  ')
print('OK')
