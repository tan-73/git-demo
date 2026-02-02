
# 🔐 AES, RSA, and Network Traffic Analysis using OpenSSL & tcpdump

## 4. Demonstration of ECB Mode of AES on Text (No IV Required)

> ECB (Electronic Codebook) mode does **NOT** use an Initialization Vector (IV).

### Step 1: Create a plaintext file
```bash
echo "This is a sample plaintext for AES ECB mode" > plain.txt
```

### Step 2: Encrypt the plaintext using AES-128-ECB
```bash
openssl enc -aes-128-ecb -e -in plain.txt -out cipher1.bin -k mypassword
```

### Step 3: View encrypted output
```bash
cat cipher1.bin
```

### Step 4: Decrypt the ciphertext
```bash
touch plain.txt

gedit plain.txt

openssl enc -aes-128-ecb -e -in plain.txt -out cipher1.bin -k 00112233445566778899aabbccddeeff

ghex cipher1.bin

openssl enc -aes-128-ecb -d -in cipher1.bin -out output.txt -k 00112233445566778899aabbccddeeff
```

### Step 5: View decrypted text
```bash
cat output.txt
```

---

## 5. Demonstration of ECB and CBC Modes of AES on a Bitmap Image

### 5.1 AES-128-ECB Encryption of Bitmap Image (No IV)
```bash
openssl enc -aes-128-ecb -e -in pic_original.bmp -out pic_ecb.bmp -k 00112233445566778899aabbccddeeff
```

**Observation:** ECB mode leaks image patterns.

---

### 5.2 AES-128-CBC Encryption of Bitmap Image (With IV)
```bash
openssl enc -aes-128-cbc -e -in pic_original.bmp -out pic_cbc.bmp \
-k 00112233445566778899aabbccddeeff \
-iv 0102030405060708090a0b0c0d0e0f

head -c 54 pic_original.bmp > header
tail -c +55 pic_ecb.bmp > body_ecb
cat header body_ecb > new_ecb.bmp
eog new_ecb.bmp
tail -c +55 pic_cbc.bmp > body_cbc
cat header body_cbc > new_cbc.bmp
eog new_cbc.bmp
```

**Observation:** CBC mode removes visible patterns.

---

## 6. Demonstration of Padding in AES

### Encrypt with padding
```bash
echo "12345" > f1.txt
echo "1234567890" > f2.txt
echo "1234567890abcdef" > f3.txt
openssl enc -aes-128-cbc -e -in f1.txt -out f1.bin \
-k 00112233445566778899aabbccddeeff \
-iv 0102030405060708090a0b0c0d0e0f
```

### Decrypt without padding
```bash
openssl enc -aes-128-cbc -d -nopad -in f1.bin -out p1.txt \
-k 00112233445566778899aabbccddeeff \
-iv 0102030405060708090a0b0c0d0e0f
```

---

## 8. RSA Public Key Cryptography Using OpenSSL

### Generate RSA private key
```bash
openssl genrsa -out key.pri 2048
```

### Extract public key
```bash
openssl rsa -in key.pri -out key.pub -pubout
```

### View private key
```bash
openssl rsa -in key.pri -noout -text
```

### View public key
```bash
cat key.pub
```

### Encrypt and decrypt message
```bash
echo "hello" > message.txt
openssl rsautl -encrypt -inkey key.pub -pubin -in message.txt -out message.enc
openssl rsautl -decrypt -inkey key.pri -in message.enc -out message.dec
```

### Secure key exchange
```bash
openssl rand -hex 32 > secret.key
openssl rsautl -encrypt -inkey key.pub -pubin -in secret.key -out secret.key.enc
openssl rsautl -decrypt -inkey key.pri -in secret.key.enc -out secret.key.dec
```

---

## 10. Packet Capture and Analysis using tcpdump

### Basic capture
```bash
tcpdump -i any
```

### Capture and save
```bash
tcpdump -i enp0s3 -w file1.pcap
```

### Read capture file
```bash
tcpdump -r file1.pcap
```

### Capture all packets
```bash
tcpdump -i any -w capture.pcap
```

### Protocol filters
```bash
tcpdump -i any tcp
tcpdump -i any icmp
```

### Host filter
```bash
tcpdump -i enp0s3 icmp and host 192.168.1.100 -w file1.pcap
```

### Port filters
```bash
tcpdump -i any port 80
tcpdump -i any port 443
```

### TCP flag filters
```bash
tcpdump -n -i enp0s3 'tcp[tcpflags] & tcp-syn != 0'
tcpdump -n -i enp0s3 'tcp[tcpflags] & (tcp-syn | tcp-ack) != 0'
```

### Advanced filter
```bash
tcpdump -nn -i enp0s3 -p -e \
'host bnmit.org and port 80 and tcp[tcpflags] & (tcp-syn | tcp-ack) != 0'
```

---

## ✅ Conclusion

- ECB mode is insecure due to pattern leakage  
- CBC mode provides better security using IV  
- Padding is essential for block ciphers  
- RSA is used for secure key exchange  
- tcpdump enables low-level packet analysis
