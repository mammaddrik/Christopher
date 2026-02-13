<div id="top"></div>
<p align="center">
    <a href="https://github.com/mammaddrik/christopher">
    <img src="https://i.postimg.cc/j5X7N8PF/Christopher.png" alt="Christopher logo"></a>
</p>


# Christopher
Christopher is a comprehensive command-line cryptography toolkit designed for learning, experimenting with, and understanding classical encryption algorithms.
It provides a wide collection of historical ciphers, hashing utilities, and encryption mechanisms in a single interactive interface.
This project aims to demonstrate how traditional cryptographic systems work internally by allowing users to encrypt, decrypt, and even attempt to crack various classical ciphers. It serves as an educational resource for students, cybersecurity beginners, and anyone interested in the foundations of cryptography.
Christopher includes implementations of substitution ciphers, transposition ciphers, polyalphabetic systems, hash functions, and even a simulation of the Enigma machine. The tool is built with modular architecture, making it easy to extend with additional algorithms and cryptographic techniques.
> **Note:** The majority of the included ciphers are classical and are intended for educational purposes only. They should not be used for real-world security.
<p align="center">
    <img src="https://i.postimg.cc/VkJkrZtn/christopher.png">
</p>

What is Cryptography? [Here](https://en.wikipedia.org/wiki/Cryptography)<br>

## Features

- 🔐 Implementation of multiple classical encryption algorithms
- 🔄 Support for both encryption and decryption operations
- 🧠 Cipher Cracking and basic cryptanalysis capabilities
- 🧩 Modular architecture for easy extension
-🎓 Educational focus with practical experimentation support
## Including
<details>

- **Atbash Cipher**
- **Caesar Cipher**
  - Encryption
  - Decryption
  - Crack
- **Affine Cipher**
  - Encryption
  - Decryption
  - Crack
- **Vigenère Cipher**
  - Encryption
  - Decryption
  - Crack
- **Reverse Text**
- **Play Fire Cipher**
  - Encryption
  - Decryption
- **Rail Fence Cipher**
  - Encryption
  - Decryption
  - Crack
- **Scytale Cipher**
  - Encryption
  - Decryption
- **Polybius Square**
- **Columnar Cipher**
  - Encryption
  - Decryption
  - Crack
- **Simple Substitution Cipher**
  - Encryption
  - Decryption
  - Crack
- **Baconian Cipher**
- **Morse Code**
- **Rot13 Cipher**
- **One-Time Pad Cipher**
  - Encryption
  - Decryption
- **Hash Function**
  - **Hash Generator**
    - MD2
    - MD4
    - MD5
    - SHA1
    - SHA224
    - SHA256
    - SHA384
    - SHA512
    - sha3-224
    - sha3-256
    - sha3-384
    - sha3-512
    - shake-128
    - shake-256
    - blake2b
    - blake2s
    - NTLM
    - adler32
    - crc32
  - **Hash Cracker**
    - MD5
    - SHA1
    - SHA256
    - SHA384
    - SHA512
- **Enigma Machine**
- **Public Key Cipher**
  - Encryption
  - Decryption
</details>

## Installation
### <img src="https://i.postimg.cc/nLp4jWx0/Windows.png" width="15" height="15" alt="Windows"/> Windows
> **Note:** Christopher isn't compatible with python2, run it with python3 instead.<br>
> I suggest you definitely use [cmder](https://cmder.app/).
```
git clone https://github.com/mammaddrik/christopher.git
cd christopher
python pip install -r requirements.txt
python christopher.py
```

### <img src="https://cdn.simpleicons.org/docker/2496ED" width="15" height="15" alt="docker"/> Docker
install docker on your system. [docker](https://www.docker.com/)
```
docker build -t christopher .
docker run -ti christopher
```

### <img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/linux-colored.svg" width="15" height="15" alt="Linux"/> Linux
> **Note:** Christopher isn't compatible with python2, run it with python3 instead.<br>
```
git clone https://github.com/mammaddrik/christopher.git
cd christopher
python pip install -r requirements.txt
python christopher.py
```
Or you can install it:
```
git clone https://github.com/mammaddrik/christopher.git
cd christopher
python pip install -r requirements.txt
sudo chmod +x setup.sh
sudo bash setup.sh
christopher
```
> **Note:** If you get a permission denied error, use this comment: `bash christopher`<br>

### requirements
| **Requirements**  | **Command**  | **Link**  | **Version**  |
| ------------- | ------------- | ------------- | ------------- |
| pycryptodome  | `python pip install pycryptodome`  | [pypi](https://pypi.org/project/pycryptodome/)  | 3.23.0|
| passlib  | `python pip install passlib`  | [pypi](https://pypi.org/project/passlib/)  | 1.7.4  |

> **Note:** You may encounter an error while installing this requirements. If an error occurs, use the following command.
```
python -m pip install --upgrade pip
python pip install -r requirements.txt
```

## Usage

## Screenshots

## License
Christopher is licensed under [MIT License](https://github.com/mammaddrik/christopher/blob/main/LICENSE).

<p align="right"><a href="#top">back to top</a></p>