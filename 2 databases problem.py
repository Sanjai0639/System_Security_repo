n = int(input("Enter a size of array: "))

arr = [0] * n
print("Enter the main array values:")
for i in range(n):
    arr[i] = int(input())

str1 = [0] * n
print("Enter the 1st binary seq")
for i in range(n):
    str1[i] = int(input())

str2=[0]*n
str2=str1.copy()
index=int(input("Enter the index to flip in 2nd binary seq: "))
if 0 <= index < n:
    str2[index] = 1 - str2[index]
print(str1)
print(str2)
result= []
for i in range(n):
    if str1[i] != str2[i]:
        result[i]= arr[i]

if result:
    final_xor = 0
    for i in result:
        final_xor ^= i
    print(final_xor)
else:
    print("No differing bits → nothing to XOR.")
