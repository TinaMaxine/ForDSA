
# //Given a string, print all possible substrings of the given string.

# str=input("Give a string to print all of it's substrings: ")
# n = len(str)
# print ("The Given String is : ", str)
# for num in range (1<<n):
#     sub=""
#     for i in range (n):
#         if(num&(1<<i)):
#             sub+=str[i]
#     print(sub)


    


    # time complexity O(2^n X n)
    # space complexity O(n)


str=input("Give a string to print all of it's substrings: ")
n = len(str)
print ("The Given String is : ", str)
substr=[]
for num in range (1<<n):
    sub=""
    for i in range (n):
        if(num&(1<<i)):
            sub+=str[i]
    substr.append(sub)


for s in substr:
    print(s)

# print("Top Element:", substr[-1])
