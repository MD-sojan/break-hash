import re

def identify_hash(hash_string):
    hash_types = [
        (r'^[a-fA-F0-9]{32}$', 'MD5'),
        (r'^[a-fA-F0-9]{40}$', 'SHA1'),
        (r'^[a-fA-F0-9]{64}$', 'SHA256'),
        (r'^[a-fA-F0-9]{128}$', 'SHA512'),
        (r'^[a-fA-F0-9]{56}$', 'SHA224'),
        (r'^[a-fA-F0-9]{96}$', 'SHA384'),
        (r'^[a-fA-F0-9]{16}$', 'MySQL 323'),
        (r'^[a-fA-F0-9]{48}$', 'Haval-192'),
        (r'^[a-fA-F0-9]{32}:[a-fA-F0-9]{32}$', 'MySQL 41'),
        (r'^[a-fA-F0-9]{13}$', 'DES (Unix)'),
        (r'^[a-fA-F0-9]{34}$', 'CRC32'),
    ]

    for pattern, hash_type in hash_types:
        if re.match(pattern, hash_string):
            return f"Hash identified as: {hash_type}"

    return "Unknown hash type"

def main():
    hash_input = input("Enter the hash to identify: ")
    result = identify_hash(hash_input)
    print(result)

if __name__ == "__main__":
    main()