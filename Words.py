n = int(input("Введите кол-во слов: "))
userstring = ""
for i in range(n):
    prompt = input()
    userstring = userstring + prompt + " "
print(userstring)