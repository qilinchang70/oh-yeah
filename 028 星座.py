n=eval(input())

for i in range(0,n,1):
    [month,date]= input().split()
    month= eval(month)
    date= eval(date)
    if month==1 and date >=21:
        print("Aquarius")
    elif month==2 and date <=19:
        print("Aquarius")
    elif month==2 and date >19:
        print("Pisces")
    elif month==3 and date <=20:
        print("Pisces")
    elif month==3 and date >20:
        print("Aries")
    elif month==4 and date <=19:
        print("Aries")
    elif month==4 and date >=20:
        print("Taurus")
    elif month==5 and date <=20:
        print("Taurus")
    elif month==5 and date >=21:
        print("Gemini")
    elif month==6 and date <=21:
        print("Gemini")
    elif month==6 and date >21:
        print("Cancer")
    elif month==7 and date <=22:
        print("Cancer")
    elif month==7 and date >=23:
        print("Leo")
    elif month==8 and date <=22:
        print("Leo")
    elif month==8 and date >=23:
        print("Virgo")
    elif month==9 and date <=22:
        print("Virgo")
    elif month==9 and date >=23:
        print("Libra")
    elif month==10 and date <=23:
        print("Libra")
    elif month==10 and date >=24:
        print("Scorpio")
    elif month==11 and date <=21:
        print("Scorpio")
    elif month==11 and date >=22:
        print("Sagittarius")
    elif month==12 and date <=20:
        print("Sagittarius")
    elif month==12 and date >=21:
        print("Capricorn")
    elif month==1 and date <=20:
        print("Capricorn")
