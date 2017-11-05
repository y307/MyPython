
from tkinter.filedialog import askopenfilename
from os import path

fin = askopenfilename()
d = path.split(fin)
print(d[0])
print(d[1])
c = path.join(d[0], d[1])
print(c)