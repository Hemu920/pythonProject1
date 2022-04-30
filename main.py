print("please give yor string")
s= input()
name = s
count = 0
for i in name:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        count += 1

print('number of ovewls in string:', count)


