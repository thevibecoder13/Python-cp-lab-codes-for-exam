def is_prime(n):
    if n<2:
        return "Input incorrect"
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return "Not prime"
    return "Prime number"
num = int(input("Enter no: "))
result = is_prime(num)
print("", result)