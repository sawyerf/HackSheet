<picture>
    <source height="100px" srcset="https://user-images.githubusercontent.com/28403617/172728813-44af208a-978d-4ef1-a6e6-ff724d5baf0f.svg" media="(prefers-color-scheme: dark)">
    <img height="100px" src="https://user-images.githubusercontent.com/28403617/172728814-0628eea3-922e-4011-8411-51c562f4e576.svg#">
</picture>

---

- [Encode](#encode)
- [GPG](#gpg)
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

# GPG
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