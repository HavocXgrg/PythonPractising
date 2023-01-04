# this is all copy and paste from the chatGpt, I just wanted to have the knowledge of sha-1 function in python.

import hashlib


def get_sha1_hash(userinput):
    # Encode the input string as bytes
    input_bytes = userinput.encode()

    # Create a new hash object
    hash_object = hashlib.sha1()

    # Use the hash object to compute the hash code
    hash_object.update(input_bytes)

    # Get the hash code as a hexadecimal string
    hash_code = hash_object.hexdigest()

    return hash_code


# Example usage
userinput = input("write the string to convert into hash code: ")
hash_code = get_sha1_hash(userinput)
print(hash_code)
