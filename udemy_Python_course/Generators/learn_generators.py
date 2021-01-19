def hundred_numbers():
    nums = []
    i = 0
    while i < 100:
        nums.append(i)
        i += 1
    return nums

print(hundred_numbers())

# you can implement the same functionality as above by changing the code a bit

def hundred_numbers():
    i = 0
    while i < 100:
        yield i
        i += 1


# a generator doesn't generate entire list and store to memory. it generates each item in the list,
# each time it's called and then remembers that item until the next time it is called.
# It always only stores in memory the last item it returned.

