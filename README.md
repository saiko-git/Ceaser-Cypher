🔐 Caesar Cipher Encoder/Decoder (Python)
This is a simple terminal-based Caesar Cipher tool written in Python that allows users to encode and decode messages using a custom shift value. Unlike traditional Caesar ciphers that only handle lowercase letters, this implementation supports:

✅ Lowercase and Uppercase Letters

✅ Numbers (0–9)

✅ Symbols and Punctuation

⚙️ How It Works
The program builds a custom character set using Python’s string module (ascii_lowercase, ascii_uppercase, punctuation, and digits).

Each character in the message is located and shifted based on its type:

Lowercase: shifted within first 26 characters

Uppercase: shifted within the next 26

Symbols: shifted within the next 32 characters

Digits: shifted within the final 10 characters

The user is prompted to choose between encoding and decoding, input a message, and select a shift value.

Encoding uses a positive shift, while decoding uses a negative shift.

🧠 Features
Supports full character sets (letters, symbols, digits)

Easy-to-use interactive command line

Shift logic is modular by character type

Custom handling for wrapping around character groups


