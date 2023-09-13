from flask import Flask
from cryptography.fernet import Fernet

app = Flask(__name__)

# Generate a key for encryption and decryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Encrypt the text
def encrypt_text(text):
    encrypted_text = cipher_suite.encrypt(text.encode())
    return encrypted_text

# Decrypt the text
def decrypt_text(encrypted_text):
    decrypted_text = cipher_suite.decrypt(encrypted_text).decode()
    return decrypted_text

@app.route('/')
def index():
    # Your text to encrypt
    plaintext = "OPEN_AI_KEY = 'Himanshu Kumar'"
    
    # Encrypt the text
    encrypted_data = encrypt_text(plaintext)

    # Decrypt the text (for demonstration purposes)
    decrypted_data = decrypt_text(encrypted_data)

    return f"Original Text: {plaintext}<br>Encrypted Text: {encrypted_data}<br>Decrypted Text: {decrypted_data}"

if __name__ == '__main__':
    app.run(debug=True,port = 5001)
