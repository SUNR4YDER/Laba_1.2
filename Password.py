aWord = input()
bWord = input()
if aWord != bWord:
    print("Пароли не совпадают :(")
else:
    if aWord == bWord:
        if len(aWord) < 8:
            print("Слишком короткий пароль :(")
        else:
            print("Пароль принят :)")