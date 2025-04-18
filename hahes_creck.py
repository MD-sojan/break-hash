import hashlib

def crack_hash(hash_to_crack, hash_type, wordlist_file):
    try:
        with open(wordlist_file, 'r', encoding='utf-8', errors='ignore') as file:
            for word in file:
                word = word.strip()
                
                # Generate hash based on type
                if hash_type == 'md5':
                    hash_guess = hashlib.md5(word.encode()).hexdigest()
                elif hash_type == 'sha1':
                    hash_guess = hashlib.sha1(word.encode()).hexdigest()
                elif hash_type == 'sha256':
                    hash_guess = hashlib.sha256(word.encode()).hexdigest()
                else:
                    print("Unsupported hash type.")
                    return

                if hash_guess == hash_to_crack:
                    print(f"[+] Hash Cracked! Password: {word}")
                    return
        
        print("[-] Password not found in wordlist.")
    except FileNotFoundError:
        print("[!] Wordlist file not found.")

def main():
    hash_to_crack = input("Enter the hash to crack: ")
    hash_type = input("Enter the hash type (md5, sha1, sha256): ").lower()
    wordlist_file = input("Enter the path to your wordlist: ")
    
    crack_hash(hash_to_crack, hash_type, wordlist_file)

if __name__ == "__main__":
    main()