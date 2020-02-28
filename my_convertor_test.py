#!/usr/bin/env python3
#-*- coding: utf-8-*-

#import sys

# print(format(16,'07b'))
# print('{:07b}'.format(16))

def encoding24bit(aText):
    suffix = ''
    text = ''
    text_len = len(aText)
    if text_len == 8:
        aText += '0000'
        suffix = '=='
    if text_len == 16
        aText += '00'
        suffix = '='
    for i in range(len(aText)):
        pos = i*6
        pos_next = pos+5
        text += code64[int(aText[pos:pos_next],2)]
    text += suffix
    return text

code64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

text_in = 'hello'
text_out = ''

buf = ''
for pos in range(len(text_in)):
    ch = text_in[pos]
    buf += format(ord(ch),'08b')
    if len(buf) == 24:
        text_out += encoding24bit(buf)
        buf = ''

if buf <> '':
    


res = ''.join(format(ord(ch), '08b') for ch in text_in)
#print(res)
text_in_len = len(text_in)
remain = text_in_len % 3
if remain == 2:
    res += '00000000'
elif remain == 1:
    res += '0000000000000000'

text_in = res

new_text = ''
for ch in text_in:
    pos_in_code64 = code64.find(ch)
    simbol = format(pos_in_code64,'06b')
    print(simbol)

res = ''.join(format(code64.find(ch), '06b') for ch in text)
print(res)

'''
text_in =  'TWFuIGlzIGRpc3Rpbmd1aXNoZWQsIG5vdCBvbmx5IGJ5IGhpcyByZWFzb24sIGJ1dCBieSB0aGlzIHNpbmd1bGFyIHBhc3Npb24gZnJvbSBvdGhlciBhbmltYWxzLCB3aGljaCBpcyBhIGx1c3Qgb2YgdGhlIG1pbmQsIHRoYXQgYnkgYSBwZXJzZXZlcmFuY2Ugb2YgZGVsaWdodCBpbiB0aGUgY29udGludWVkIGFuZCBpbmRlZmF0aWdhYmxlIGdlbmVyYXRpb24gb2Yga25vd2xlZGdlLCBleGNlZWRzIHRoZSBzaG9ydCB2ZWhlbWVuY2Ugb2YgYW55IGNhcm5hbCBwbGVhc3VyZS4='
res = ''.join(format(code64.find(ch), '06b') for ch in text_in)

if text_in[-2:] == '==':
    text_in = text_in[:-2]
elif text_in[-1:] == '=' :
    text_in = text_in[:-1]

new_text = ''
pos7 = 0
while pos7 < len(res):
    buf = res[pos7:pos7+23]
    pos7 += 24
    for i in range(3):
        pos8 = i * 8
        ch = chr(int((buf[pos8:pos8+7]),2))
        new_text += ch

print(new_text)
'''
