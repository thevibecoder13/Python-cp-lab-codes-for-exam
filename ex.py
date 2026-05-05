def is_palindrome(num):
    original = num
    reverse = 0
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10
    return original == reverse
def find_palindromes(lst):
    result = []
    
    for num in lst:
        if is_palindrome(num):
            result.append(num)
    return result
lst = list(map(int, input("Enter numbers separated by space: ").split()))
print("Palindrome numbers:", find_palindromes(lst))