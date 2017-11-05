
from tkinter.filedialog import askopenfilename
from os import path

fin = askopenfilename()
d=path.split(fin)
print(d[0])
print(d[1])