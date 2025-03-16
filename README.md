# Caesar Cipher
```python
░█████╗░░█████╗░███████╗░██████╗░█████╗░██████╗░        ░█████╗░██╗██████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗        ██╔══██╗██║██╔══██╗██║░░██║██╔════╝██╔══██╗
██║░░╚═╝███████║█████╗░░╚█████╗░███████║██████╔╝        ██║░░╚═╝██║██████╔╝███████║█████╗░░██████╔╝
██║░░██╗██╔══██║██╔══╝░░░╚═══██╗██╔══██║██╔══██╗        ██║░░██╗██║██╔═══╝░██╔══██║██╔══╝░░██╔══██╗
╚█████╔╝██║░░██║███████╗██████╔╝██║░░██║██║░░██║        ╚█████╔╝██║██║░░░░░██║░░██║███████╗██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝        ░╚════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝   
```

## Project Description  
Caesar Cipher is a classic substitution cipher where each letter in a message is shifted by a specified number of places in the alphabet. 
This program allows both encryption and decryption of messages by shifting characters accordingly.  

## Features  
- Choose between encryption and decryption  
- Input custom messages and shift values  
- Handles spaces in the text  
- Interactive console-based execution  

## Technologies Used
- Python  
- String manipulation  
- Control structures (loops, conditional statements)  

## Installation
1. Clone this repository:
```
git clone https://github.com/vodkawithcola1/python--caesar-cipher.git
cd python--caesar-cipher/caesarcipher
```
2. Run the script:
```
python main.py
```

## Example Usage
Encode:
```python
Type 'encode' to encrypt, type 'decode' to decrypt: encode
Type your message: hello
Type the shift number: 3
Here's the encoded result: khoor
```
Decode:
```python
Type 'encode' to encrypt, type 'decode' to decrypt: decode
Type your message: khoor
Type the shift number: 3
Here's the decoded result: hello
```

Made by Mikołaj Kozłowski based on 100 days of Python by Dr. Angela Yu
