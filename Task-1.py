def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                shifted_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                shifted_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("Welcome to the Caesar Cipher Program!")
    choice = input("Type 'encrypt' to encrypt a message, or 'decrypt' to decrypt a message: ").strip().lower()
    
    if choice not in ['encrypt', 'decrypt']:
        print("Invalid choice. Please type 'encrypt' or 'decrypt'.")
        return

    text = input("Enter the message: ").strip()
    shift = int(input("Enter the shift value: ").strip())
    
    if choice == 'encrypt':
        result = caesar_cipher_encrypt(text, shift)
        print(f"Encrypted message: {result}")
    elif choice == 'decrypt':
        result = caesar_cipher_decrypt(text, shift)
        print(f"Decrypted message: {result}")

if __name__ == "__main__":
    main()
