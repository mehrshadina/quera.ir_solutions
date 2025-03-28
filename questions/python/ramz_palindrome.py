def is_palindrome(s):
    return s == s[::-1]

def making_palindrome(s):
    before_edithing = s

    s = s.replace('?', '+')
    for i in range(len(s)):
        if s[i] == '+':
            s = s[:i] + s[::-1][i] + s[i+1:]
    if is_palindrome(s):
        return s
    else:
        return before_edithing

def process_string(n, s):
    for i in range(n):
        action = input()
        if action == '-':
            left, right = map(int, input().split())
            s = s[:left] + s[right+1:]

        elif action == '+':
            start, insert_str = input().split()
            start = int(start)
            s = s[:start] + insert_str + s[start+1:]

        s = making_palindrome(s)

        if is_palindrome(s):
            print(f"{s} is palindrome")
        else:
            print(f"{s} not palindrome")


n = int(input())
str_input = input()

process_string(n, str_input)