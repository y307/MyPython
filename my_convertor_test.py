#!/usr/bin/env python3
#-*- coding: utf-8-*-

import sys


text = 'ABC'
code64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

for ch in text:
    print(format(ord(ch), '08b'))

res = ''.join(format(ord(ch), '08b') for ch in text)
print(res)

new_text = ''
for ch in text:
    pos_in_code64 = code64.find(ch)
    simbol = format(pos_in_code64,'06b')
    print(simbol)

res = ''.join(format(code64.find(ch), '06b') for ch in text)
print(res)

text_in =  'TWFuIGlzIGRpc3Rpbmd1aXNoZWQsIG5vdCBvbmx5IGJ5IGhpcyByZWFzb24sIGJ1dCBieSB0aGlzIHNpbmd1bGFyIHBhc3Npb24gZnJvbSBvdGhlciBhbmltYWxzLCB3aGljaCBpcyBhIGx1c3Qgb2YgdGhlIG1pbmQsIHRoYXQgYnkgYSBwZXJzZXZlcmFuY2Ugb2YgZGVsaWdodCBpbiB0aGUgY29udGludWVkIGFuZCBpbmRlZmF0aWdhYmxlIGdlbmVyYXRpb24gb2Yga25vd2xlZGdlLCBleGNlZWRzIHRoZSBzaG9ydCB2ZWhlbWVuY2Ugb2YgYW55IGNhcm5hbCBwbGVhc3VyZS4='
res = ''.join(format(code64.find(ch), '06b') for ch in text_in)

pos7 = 0
while pos7 < len(res):
    buf = res[pos7:pos7+23]
    pos7 += 24
    for i in range(3):
        pos8 = i * 8
        ch_code = int(buf[pos8:pos8+7])
        new_text = new_text + chr(ch_code)

print(new_text)


# print(format(16,'07b'))
# print('{:07b}'.format(16))

