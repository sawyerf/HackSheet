# Crypto

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
