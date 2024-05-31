# palindrome with a param and no print statements so we can test the algorithm:

def palindrome(inp):
    if len(inp) < 3:
        return False
    rev = ''.join(reversed([a for a in inp]))
    if rev == inp:
        return True
    return False 

