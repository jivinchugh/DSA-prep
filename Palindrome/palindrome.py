'''Write the following function recursively:

def is_palindrome(word)
word is a character string. This function returns true if word is a palindrome. A palindrome is a string that reads the same forwards and backwards. Thus: noon, mom, dad are all palindromes. table, texture, glass are not palindromes.

the above function can be a wrapper to a function that actually does the work

Try to write the function to O(n) run time where n is the length of s.'''

def is_palindrome(word):
    # Wrapper function to initiate the recursion
    def check_palindrome(s, left, right):
        # Base case: If left index is greater than or equal to right index, it's a palindrome
        if left >= right:
            return True
        # Check if the characters at the current indices are the same
        if s[left] != s[right]:
            return False
        # Recur for the next pair of characters
        return check_palindrome(s, left + 1, right - 1)

    # Call the recursive function with initial indices
    return check_palindrome(word, 0, len(word) - 1)

# Example usage
print(is_palindrome("noon"))    # True
print(is_palindrome("mom"))     # True
print(is_palindrome("dad"))     # True
print(is_palindrome("table"))   # False
print(is_palindrome("texture"))  # False
print(is_palindrome("glass"))   # False
