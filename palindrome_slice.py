# palindrome with string slicing:

def palindrome_slice(inp):
    if len(inp) < 3:
        print('not palindrome')
        return False
    rev = inp[::-1]
    if rev == inp:
        print('palindrome!')
        return True
    print('not palindrome')
    return False


