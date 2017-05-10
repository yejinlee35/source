def factorial2(count):
    if count > 1:
        count *= factorial2(count -1)
    return count
print(count)

print(factorial2(10))