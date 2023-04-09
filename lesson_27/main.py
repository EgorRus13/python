nach=input("Начало первого урока (чч:мм):")
dlur=int(input("Длительность урока (мин):"))
dlp=int(input("Длительность перемен (мин):"))
n=int(input("На сколько уроков нужно расписание:"))
# split=nach.split(":")
# h = split[0]
# m=split[1]
h, m = nach.split(":")
h, m=int(h),int(m)
time=h*60+m
for i in range(n):
    print(f"Урок {i+1}:", end="")
    h=time//60
    m=time%60
    print(f"{str(h).rjust(2,'0')}:{str(m).rjust(2,'0')} - ",end="")
    time=time+dlur
    h = time // 60
    m = time % 60
    print(f"{str(h).rjust(2, '0')}:{str(m).rjust(2, '0')}")
    time=time+dlp