# We read the text to be encrypted
original_text = input("Enter the text to be encrypted: ")

# The ciphertext is empty for now; we will add further characters to it
encrypted_text = ''

# In the loop we iterate over each
for character in original_text:

    if 'A' <= character <='Z':  # condition a < x <b is the same as: a < x and x < b
        # We have a capital letter; we calculate its sequence number
        # (so that the letter "A" corresponds to 0)
        code = ord(character) - ord('A')

        # We encrypt the character: add 13 and wrap up to 26 characters (remainder from division)
        new_code = (code + 13) % 26

        # We add a new ciphertext:
        # first "shift" the new code so that the letter "A" has the correct code,
        # then convert it to a character and add it to the string with the result
        encrypted_text += chr(new_code + ord('A'))

    elif 'a' <= character <= 'z':  # we do the same for lower case letters
        code = ord(character) - ord('a')   # subtract lower case code "a"
        new_code = (code + 13) % 26
        encrypted_text += chr (new_code + ord('a'))

    else:
        # Rewrite the remaining characters unchanged
        encrypted_text += character

# Print the results
print(encrypted_text)