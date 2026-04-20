def sum_avg(marks):
    total = sum(marks)
    avg = total / len(marks)
    return total, avg

marks = list(map(int, input().split()))
total, avg = sum_avg(marks)

print(total, avg)