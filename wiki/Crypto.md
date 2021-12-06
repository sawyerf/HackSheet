# 🔒 Crypto

- [Encode](#encode)
- [GPG](#gpg)
- [Hashcat](#hashcat)
- [Identifier](#identifier)
- [John](#john)
- [Wordlist](#wordlist)


## John
```
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
```
### Sql Hash
```
john -format=md5crypt-long --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
```

## Hashcat
### Hash Identifier
```
hashid hash.txt
```
[Hashcat Doc](https://hashcat.net/wiki/doku.php?id=example_hashes) 
### Dictionnary Attack
```
hashcat -m 500 hash.txt /usr/share/wordlists/rockyou.txt
```

## Wordlist
```
crunch <minimum length> <maximum length> <charset> -t <pattern> -o wordlist.lst
```

## GPG
### Buteforce
```
gpg2john private.key > hash.txt
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
```

### Decrypt message
```
gpg -import private.key
gpg -d msg.txt
```

## Identifier
[Boxentriq](https://www.boxentriq.com/code-breaking/cipher-identifier)

## Encode
### Base64
```
echo lol | base64
```
```
echo bG9sCg== | base64 -d
```

### Urlencode
```
urlencode "url_raw"
```
```
urlencode -d "url_encode"
```

### Hexa
```
echo 6c6f6c0a | xxd -p -r
```
```
echo lol | xxd -p -r
```
