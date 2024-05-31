# palindrome:

def palindrome():
    inp = input('enter a string:\n')
    if len(inp) < 3:
        print('not palindrome')
        return False
    rev = ''.join(reversed([a for a in inp]))
    if rev == inp:
        print('palindrome!')
        return True
    print('not palindrome')
    return False

# palindrome()  
