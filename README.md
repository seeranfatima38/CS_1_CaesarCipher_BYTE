# CS_1_CaesarCipher_BYTE
(Text Encryption/Decryption)

A simple Python program that encrypts and decrypts text using the Caesar Cipher.
Built for the Arithmatrix Virtual Internship Program (AVIP) 2026, Cybersecurity track, Task 1.

## How It Works
Each letter is shifted forward in the alphabet by a chosen number (the shift/key).
With shift 3: A becomes D, B becomes E, and so on. Decryption shifts the letters back by the same number.

- Letters wrap around: with shift 3, Z becomes C
- Uppercase and lowercase are preserved
- Numbers, spaces, and punctuation stay unchanged
- Any shift value can be used

## How to Run
1. Install Python 3
2. Download `caesar_cipher.py`
3. Run in a terminal:

```
python caesar_cipher.py
```

## Usage Examples

**Encryption**
```
Enter your text: Hello, World!
Enter shift number: 3
Type 'e' to encrypt or 'd' to decrypt: e
Result: Khoor, Zruog!
```

**Decryption**
```
Enter your text: Khoor, Zruog!
Enter shift number: 3
Type 'e' to encrypt or 'd' to decrypt: d
Result: Hello, World!
```

## Sample Files
- `sample_input.txt`: original text (`Hello, World!`)
- `sample_output.txt`: encrypted text with shift 3 (`Khoor, Zruog!`)

## Demo
![Demo screenshot](demo_screenshot.png)

## Limitations
The Caesar Cipher is not secure. There are only 25 possible shifts, so it can be broken by trying all of them (brute force). It is built here to learn the basics of encryption.
