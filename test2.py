def is_palindrome(s):
    # Keeping only alphanumeric characters and converting to lower case
    cleaned_str = ''.join(ch for ch in s if ch.isalnum()).lower()
    # Checking if the cleaned string is equal to its reverse
    return cleaned_str == cleaned_str[::-1]

input_str = input("Enter the string: ")

if is_palindrome(input_str):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")