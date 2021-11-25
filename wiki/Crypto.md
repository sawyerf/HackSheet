# Crypto

- [Identifier](#identifier)
- [GPG](#gpg)
- [John](#john)
- [Hashcat](#hashcat)
- [Wordlist](#wordlist)

## Identifier
[Boxentriq](https://www.boxentriq.com/code-breaking/cipher-identifier)

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

## John
```
john -format=md5crypt-long --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
```
## Hashcat
### Hash Identifier
```
hashid hash.txt
```
### Dictionnary Attack
```
hashcat -m 500 hash.txt /usr/share/wordlists/rockyou.txt
```

## Wordlist
```
crunch <minimum length> <maximum length> <charset> -t <pattern> -o wordlist.lst
```