

def palindrome(string):

    n = len(string)
    S = set()
    for s in string:
        if s not in S:
            S.add(s)
        else:
            S.remove(s)
    if len(S) <= 1:
        return True
    else:
        return False

print("is test a palindrome ? ", palindrome("test"))
print("is ressasser a palindrome ? ", palindrome("ressasser"))











