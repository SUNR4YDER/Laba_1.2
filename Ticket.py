SeatNum = int(input())

if(SeatNum > 36):
    print("Ваше место на боковушке")
elif(SeatNum == 0):
    print("Вы проводник? ಠ_ಠ")
else:
    if SeatNum % 2:
        print("Ваше место - нижняя полка в купе")
    else:
        print("Ваше место - верхняя полка в купе")