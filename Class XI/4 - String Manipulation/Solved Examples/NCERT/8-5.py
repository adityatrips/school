def rev(s):
    return s[::-1]


def is_palindrome(st):
    if st.lower() == rev(st.lower()):
        print(f'{st} is palindrome!')
    else:
        print(f'{st} isn\'t palindrome!')
