#
#

import os

'''
p = os.popen('lpr', 'w')
p.write("Hello world!\n")
p.close()
'''

# PostScript

p = os.popen('lpr', 'w')
p.write('%!PS\n')
p.write('/Helvetica findfont 12 scalefont setfont\n')
p.write('/cm { 72 mul 2.54 div } def\n')
p.write('1 cm 28 cm moveto\n')
p.write('(Hello world!) show\n')
p.write('showpage\n')
p.close()

