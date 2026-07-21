'''
Day03- Loops in python
'''

print("=" * 50)
print("For Loop")
print("=" * 50)


for number in range(1, 6):
    print(number)


print("\n"+ "=" * 50)
print("While Loop")
print("=" * 50)

count  = 1

while count <=5:
    print(count)
    count += 1

print("\n" + "=" * 50)
print("Range")
print("=" * 50)

print(list(range(5)))
print(list(range(2,10)))
print(list(range(1,20,2)))

print("\n"+ "=" * 50)
print("Break")
print("=" * 50)


for i in range(1, 11):
    if i == 5:
        break
    print(i)


print("\n" + "=" * 50)
print("continue")
print("=" * 50)

for i in range(1,11):
    if i == 6:
        continue
    print(i)

print("\n" + "=" * 50)
print("Pass")
print("=" * 50)

for i in range(5):
    if i == 2:
        pass
    print(i)

print("\n" + "=" * 50)
print("Nested Loop")
print("=" * 50)

for row in range(3):
    for col in range(3):
        print(f"({row},{col})", end=" ")
    print()

print("\n" + "=" * 50)
print("Loop Else")
print("=" * 50)

for i in range(5):
    print(i)
else:
    print("Loop finished")


