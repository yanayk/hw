import time #Молодець
class Student:
    timer=10
    month=0
    day=0
    work=""
    age=int(input("Введіть свій вік: "))
    money=300
    if 14<=age<=80:
        health=100
        IQ=90
        Happyness=int(input("Наскільки ви щасливі 1-100: "))
        alive=True
        def life(self):
            for i in range(10):
                self.day+=3
                time.sleep(1)
                self.timer-=1
                print("*")
            if self.day==30:
                self.day=0
                self.month=self.month+1
            if self.timer==0:
                print(f"Дні {self.day}    Місяці {self.month}")
                print("----------------------------------------------------")
                self.Happyness-=10
                self.health-=10
                print(f"Здоров'я студента :{self.health}")
                print(f"IQ студента :{self.IQ}")
                print(f"Щастя студента :{self.Happyness}")
                print(f"Гроші студента :{self.money}")
                print("----------------------------------------------------")
                self.work=input("Чи хоче студент заробити гроші? Так/Ні")
                if self.work=="Так":
                    job=int(input("Скільки годин працює студент ?"))
                    time.sleep(3)
                    print(f"Студент отримує  {job*3}")
                    self.money+=job*3
                self.timer=10
                if self.Happyness<=0 or self.health<=0 or self.IQ<=0:
                    print("Студент не вижив")
                    self.alive=False
                    time.sleep(3)
                    exit()
                print(f"Дні {self.day}",f"Місяці {self.month}")
                global answ
                print("Щоб покращити здоров'я студента введіть 1","Щоб покращити IQ студента введіть 2","Щоб покращити щастя студента введіть 3" ,sep='\n')
                answ=input()
                
        def improvehealth(self):
            print("Виберіть метод","1:випити таблетки(+10 до здоров'я ;-5 від щастя;-20 від грошей)","2:піти в спортзал (+15 до здоров'я;-10 від грошей)","3:поїхати до моря (+30 до здоров'я;-100 від грошей)","4:пропустити",sep='\n')
            option=int(input("Відповідь: "))
            if option==1:
                if self.Happyness>=5 and self.money>=20:
                    self.health=self.health+10
                    self.Happyness=self.Happyness-5
                    self.money=self.money-20
                    print(f"Здоров'я студента :{self.health}"
                            f"IQ студента :{self.IQ}"
                            f"Щастя студента :{self.Happyness}"
                            f"Гроші студента :{self.money}")
                else:
                    print("Недостатньо ресурсів")
            elif option==2:
                if self.money>=10:
                    self.health=self.health+15
                    self.money=self.money-10
                    print(f"Здоров'я студента :{self.health}"
                        f"IQ студента :{self.IQ}"
                        f"Щастя студента :{self.Happyness}"
                        f"Гроші студента :{self.money}")
                else:
                    print("Недостатньо ресурсів")
            elif option==3:
                if self.money>=100:
                    self.health=self.health+30
                    self.money=self.money-100
                    print(f"Здоров'я студента :{self.health}"
                            f"IQ студента :{self.IQ}"
                            f"Щастя студента :{self.Happyness}"
                            f"Гроші студента :{self.money}")
                else:
                    print("Недостатньо ресурсів")
            elif option==4:
                pass
                
        def improveiq(self):
            print("Виберіть метод","1:починати наукову книжку(+5 до IQ ;-5 від щастя;-30 від грошей)","2:розвязати задачу (+10 до IQ;-10 від грошей)","3:Зіграти в гру (+10 до IQ;-10 від грошей)","4:пропустити",sep='\n')
            option=int(input("Відповідь: "))
            if option==1:
                if self.money>=30 and self.Happyness>=5:
                    self.IQ=self.IQ+10
                    self.Happyness=self.Happyness-5
                    self.money=self.money-30
                    print(f"Здоров'я студента :{self.health}"
                            f"IQ студента :{self.IQ}"
                            f"Щастя студента :{self.Happyness}"
                            f"Гроші студента :{self.money}")
                else:
                    print("Недостатньо ресурсів")
            elif option==2:
                if self.money>=10:
                    self.IQ=self.IQ+10
                    self.money=self.money-10
                    print(f"Здоров'я студента :{self.health}"
                        f"IQ студента :{self.IQ}"
                        f"Щастя студента :{self.Happyness}"
                        f"Гроші студента :{self.money}")
                else:
                    print("Недостатньо ресурсів")
            elif option==3:
                if self.money>=10:
                    self.IQ=self.IQ+10
                    self.money=self.money-10
                    print(f"Здоров'я студента :{self.health}"
                        f"IQ студента :{self.IQ}"
                        f"Щастя студента :{self.Happyness}"
                        f"Гроші студента :{self.money}")
                else:
                    print("Недостатньо ресурсів")
            elif option==4:
                pass

        def improveh(self):
            print("Виберіть метод","1:погуляти(+5 до щастя)","2:зайнятись улюбленою справою(+10 до щастя)","3:поїхати відпочивати (+20 до щастя;-200 від грошей)","4:пропустити",sep='\n')
            option=int(input("Відповідь: "))
            if option==1:
                self.Happyness=self.Happyness+5
                print(f"Здоров'я студента :{self.health}"
                        f"IQ студента :{self.IQ}"
                        f"Щастя студента :{self.Happyness}"
                        f"Гроші студента :{self.money}")
            elif option==2:
                self.Happyness=self.Happyness+10
                print(f"Здоров'я студента :{self.health}"
                        f"IQ студента :{self.IQ}"
                        f"Щастя студента :{self.Happyness}"
                        f"Гроші студента :{self.money}")
            elif option==3:
                if self.money>=200:
                    self.Happyness=self.Happyness+10
                    self.money=self.money-100
                    print(f"Здоров'я студента :{self.health}"
                            f"IQ студента :{self.IQ}"
                            f"Щастя студента :{self.Happyness}"
                            f"Гроші студента :{self.money}")
                else:
                    print("Недостатньо ресурсів")
            elif option==4:
                pass
            
                    

    else:
        print("Некоректний вік")
times=0
St=Student()
for i in range(12):
    times=times+1
    St.life()
    if answ=="1":
        St.improvehealth()
    elif answ=="2":
        St.improveiq()
    elif answ=="3":
        St.improveh()
if times==12:
    print("Пройшов один рік")
    exit()











