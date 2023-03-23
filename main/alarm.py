from tkinter import *
import datetime
import time
import winsound # звуки виндовс

def alarm(set_alarm_timer):
    """Функция которая отвечает за работу будильника"""
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S") # текущее время
        date = current_time.strftime("%d/%m/%Y") # текущее дата
        #print('Установленная дата:', date)
        #print(now)
        if now == set_alarm_timer:
            print("Доброе утро, время вставать")
            sound = 'C:\Windows\Media\The_Animals_The_House.wav'
            winsound.PlaySound(sound, winsound.SND_FILENAME)
        if date == date:
            print('Установленная дата:', date)
            print(now)
        elif date != date:
            print('Дата отличается от текущей даты!')
            break

def actual_time():
    """Получение текущего времени"""
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

# внешняя оболочка будильника
clock = Tk()
clock.title('Будильник') # Название
clock.geometry('400x200') # размер рабочего окна
time_format = Label(clock, text = "Введите время в формате 24 часов!", fg="red",bg="black",font="Arial").place(x=60,y=120)
addTime = Label(clock,text = "Часы  Mинуты  Секунды",font=60).place(x = 110)
addTimes = Label(clock,text = "Когда вставать?",fg="blue",relief = "solid",font=("Helevetica",8,"bold")).place(x=5, y=29)

hour = StringVar()
min = StringVar()
sec = StringVar()

hourTime = Entry(clock,textvariable = hour,bg = "pink",width = 15).place(x=110,y=30)
minTime = Entry(clock,textvariable = min,bg = "pink",width = 15).place(x=150,y=30)
secTime = Entry(clock,textvariable = sec,bg = "pink",width = 15).place(x=200,y=30)

submit = Button(clock, text= "Поставить будильник",fg="red",width = 20,command = actual_time).place(x =110,y=70)

clock.mainloop()