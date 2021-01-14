def check_palindrome(name):
    name = name.upper()
    if name[0:] == name[: : -1]:
        return True
    else:
        return False


print(check_palindrome('Kajak'))
print(check_palindrome('Radar'))
print(check_palindrome('Dupa'))
print(check_palindrome('Lupul'))