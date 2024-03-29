<picture>
    <source height="100px" srcset="https://user-images.githubusercontent.com/22857002/173680960-5e82161d-0e0b-45a8-b35f-26be5539eeb2.svg#gh-dark-mode-only" media="(prefers-color-scheme: dark)">
    <img height="100px" src="https://user-images.githubusercontent.com/28403617/172729236-3578e657-e8a0-4cb8-be7a-0daecfbbd77b.svg#gh-light-mode-only">
</picture>

---

- [Encode](#encode)
- [GPG / PGP](#gpg-/-pgp)
- [Hashcat](#hashcat)
- [Identifier](#identifier)
- [John](#john)
- [PFX](#pfx)
- [RSA](#rsa)
- [Wordlist](#wordlist)
- [XOR](#xor)


# Bruteforce
## John
```bash
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
```

### Sql Hash
```bash
john -format=md5crypt-long --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
```

## Hashcat
### Hash Identifier
```bash
hashid hash.txt
```
[Hashcat Doc](https://hashcat.net/wiki/doku.php?id=example_hashes)

### Dictionnary Attack
```bash
hashcat -m 500 hash.txt /usr/share/wordlists/rockyou.txt
```

# Wordlist
```bash
crunch <minimum length> <maximum length> <charset> -t <pattern> -o wordlist.lst
```

# GPG / PGP
### Buteforce
```bash
gpg2john private.key > hash.txt
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
```

### Decrypt message
```bash
gpg -import private.key
gpg -d msg.txt
```

# Identifier
[Boxentriq](https://www.boxentriq.com/code-breaking/cipher-identifier)

# Encode
### Base64
```bash
echo lol | base64
```
```bash
echo bG9sCg== | base64 -d
```

### Urlencode
```bash
urlencode "url_raw"
```
```bash
urlencode -d "url_encode"
```

### Hexa
```bash
echo 6c6f6c0a | xxd -p -r
```
```bash
echo lol | xxd -p -r
```

# PFX
### Bruteforce
```
crackpkcs12 -d /usr/share/wordlists/rockyou.txt certificate.pfx
```
[Source](https://github.com/crackpkcs12/crackpkcs12)

# RSA
### Common Modulus Attack
Condition:
- Have 2 encrypt message
- Have 2 public keys
If you have this two condition you can found the original message with this program:

[Git - RSA Common Modulus Attack](https://github.com/HexPandaa/RSA-Common-Modulus-Attack)

# Xor
### Basic calcul
```
a ^ b = c
a ^ c = b
```