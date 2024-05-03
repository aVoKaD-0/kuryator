import tkinter as tk

win = tk.Tk()

import math
ch = 1 # Если число с плавающей надо проверить снова, переменная меняется на 2 и число не проверяется на sqrt, используется в f вынос целого и не целого числа

def vynos_celogo_chisla(number): # выносит целое число
    global ch
    number2 = math.sqrt(number)
    if str(number2).find(".") == len(str(number2))-2 and ch == 1:
        ch = 1
        return int(str(number2)[:-2]), 0
    vne_kornya = 1
    pod_kornem = number
    false = 0
    while false != 1:
        if pod_kornem % 4 == 0:
            pod_kornem = pod_kornem//4
            vne_kornya *= 2
        elif pod_kornem % 9 == 0:
            pod_kornem = pod_kornem//9
            vne_kornya *= 3
        elif pod_kornem % 25 == 0:
            pod_kornem = pod_kornem//25
            vne_kornya *= 5
        else:
            false = 1
    if false == 1 and pod_kornem != number:
        return vne_kornya, pod_kornem
    else:
        return 0, 0

def vynos_NeCelogo_chisla(number): # выносит не целое число
    number2 = number
    decrease = "1"
    global ch
    dlina_number = 1
    for i in range(len(str(number2))-1, 0, -1):
        if str(number2)[i] == "e":
            decrease += "0"*int(str(number2)[i+2:])
            if str(number2).find(".") != -1:
                dlina_number = int(str(number2)[i+2:])+1
            else:
                dlina_number = int(str(number2)[i+2:])
            break
    number2 *= float(decrease)
    decrease = 1/int(decrease)
    dlina = len(str(number2)[(str(number2).find("."))+1:])
    if dlina_number == 1:
        dlina_number = dlina
    if decrease != 1.0:
        number2 = round(number2, 1)
    decrease = check_e(decrease)
    decrease = str(decrease)
    while str(number2)[-1] != "0" or str(number2)[-2] != ".":
        number2 *= 10
        decrease = "0.0" + decrease[2:]
        dlina -= 1
        number2 = round(number2, dlina)
    number3, number4 = vynos_celogo_chisla(int(number2))
    if number4 == 0 and number3 != 0:
        if dlina_number%2 == 0:
            number3 /= int("1"+("0"*((dlina_number//2))))
        else:
            ch = 2
            number3, number4 = vynos_celogo_chisla(int(number2))
    if number4 != 0 and number3 != 0:
        flag = True
        for t in range(0, len(str(decrease))): # Смотрим длину после точки у первого числа
            for i in range(0, len(str(decrease))//2): # Смотрим длину после точки у второго числа
                if round(round(((number3/int("1"+"0"*t))**2), t*2)*round((number4/int("1"+"0"*i)), i*2), i*2+t*2) == number:
                    number3 = number3/int("1"+"0"*t)
                    number4 = number4/int("1"+"0"*i)
                    if t == 0:
                        number3 = str(number3)[:-2]
                    if i == 0:
                        number4 = str(number4)[:-2]
                    flag = False
                    break
            if flag == False:
                break
        if flag == True:
            number3, number4 = 0, 0
    return number3, number4

def proverka_dlin_chisla(number):
    flag = True
    number = str(number)
    tochka = str(number).find(".")
    for t in range(tochka+2, len(str(number[tochka+1:]))): # Смотрим длину после точки у первого числа
        if t != len(number)-2:
            if  number[t+1] == number[t]:
                for i in range(t+2, len(str(number[tochka+1:]))):
                    if number[i] == number[t+2]:
                        if i-t >= 3:
                            if int(number[t+2]) > 5:
                                number = number[:t-1]+str(int(number[t-1])+1)
                                flag = False
                            else:
                                number = number[:t]
                                flag = False
                            break
                    else:
                        break
        if flag == False:
            break
    if number[-1] == "0" and number[-2] == ".":
        number = number[:-2]
    return number

def check_e(number):
    number2 = number
    if str(number).find("e") != -1:
        number2 = "0." + "0"*(int(str(number)[str(number).find("e")+2:])-1)
        if str(number).find(".") != -1:
            number2 += str(number)[:str(number).find(".")] + str(number)[str(number).find(".")+1:str(number).find("e")]
        else:
            number2 += str(number)[:str(number).find("e")]
    return number2

def VynosIzPodKoren(koren): #вынос из под корня
    try:
        c = 0 # проверка правильно ли стоит знак корня в строке
        f = 0 # проверка правильно ли стоит знак деления
        g = 0 # проверка правильно ли стоят числа с плавающей запятой
        f2 = 0 # проверка не стоит ли знак деления в конце или в начале
        g2 = 0 # проверка не стоит ли точка в конце или в начале  
        c2 = 0 # проверка не стоит ли знак корня в конце 
        for i in range(0, len(koren)-1):
            if koren[i] == "√":
                c += 1
            if koren[i] == "/":
                f += 1
            if koren[i] == ".":
                g += 1
            if koren[i] == "√" and i == len(koren):
                c2 += 1
            if koren[i] == "." and (i != 0 and i != len(koren)-1) and koren[i-1].isdigit() and koren[i+1].isdigit():
                g2 += 1
            if koren[i] == "/" and (i != 0 and i != len(koren)-1) and koren[i-1].isdigit() and koren[i+1].isdigit():
                f2 += 1
        if g > 4 or c != 1 or f > 2 or f != f2 or g != g2 or c2 != 0:
            return "Проверьте правильность ввода"
        elif len(koren) == 1:
            return "Проверьте правильность ввода"
        else:
            a = str(koren).find("√")
            NeKPL = True # проверяет есть ли число с плавающей запятой вне корня
            KPL = True # проверяет есть ли число с плавающей запятой под корнем
            KDR = True # проверяет есть ли дробь под корняем
            NeKDR = True # проверяет есть ли дробь вне корня
            Drob_Ne = 0
            Drob_V = 0
            for i in range(a+1, len(koren)):
                if koren[i] == ".":
                    KPL = False  
            for i in range(a):
                if koren[i] ==".":
                    NeKPL = False
            for i in range(a+1, len(koren)):
                if koren[i] == "/":
                    KDR = False
                    Drob_V = i
            for i in range(a):
                if koren[i] == "/":
                    NeKDR = False
                    Drob_Ne = i
            if KDR == True and (KPL == True or KPL == False):
                if str(koren[a+1:]).find(".") == -1:
                    number, number2 = vynos_celogo_chisla(int(koren[a+1:]))
                else:
                    number, number2 = vynos_NeCelogo_chisla(float(koren[a+1:]))
                if NeKDR == True and (NeKPL == True or NeKPL == False): # если вне корня либо целое число, либо числа нету
                    if number == 0 and number2 == 0: 
                        return f"Число иррациональное"
                    else:
                        if a != 0:
                            if str(koren[:a]).isdigit() == True: # если число вне корня целое
                                numerator = proverka_dlin_chisla(float(number*int(koren[:a])))
                            elif a != 0: # если число вне корня не целое
                                if str(number*float(koren[:a]))[-1] == "0" and str(number*float(koren[:a]))[-2] == ".":
                                    numerator = str(number*float(koren[:a]))[:-2]
                                else:
                                    numerator = proverka_dlin_chisla(float(number*float(koren[:a])))
                        else:
                            numerator = number
                        numerator = check_e(numerator)
                        number2 = check_e(number2)
                        if number2 == 0: # если вне дроби есть число и число расскладывается нацело
                            return f"{numerator}"
                        elif number2 != 0: # если вне дроби есть число и число расскладывается нацело
                            return f"{numerator}√{number2}"
                        else:
                            if number2 == 0:
                                return f"{number}"
                            else:
                                return f"{number}√{number2}"
                elif NeKDR == False and (NeKPL == True or NeKPL == False): # если вне корня дробь
                    if number == 0 and number2 == 0:
                        return f"Число иррациональное"
                    else:
                        if str(koren[:Drob_Ne]).isdigit() == True: # если число вне корня целое
                            numerator = proverka_dlin_chisla(float(number*int(koren[:Drob_Ne])))
                        elif a != 0: # если число вне корня не целое
                            if str(number*float(koren[:Drob_Ne]))[-1] == "0" and str(number*float(koren[:Drob_Ne]))[-2] == ".":
                                numerator = str(number*float(koren[:Drob_Ne]))[:-2]
                            else:
                                numerator = proverka_dlin_chisla(float(number*float(koren[:Drob_Ne])))
                        numerator = check_e(numerator)
                        number2 = check_e(number2)
                        if koren[:a] != "" and number2 == 0: # если вне дроби нету числа и число расскладывается нацело
                            return f"{numerator}/{koren[Drob_Ne+1:a]}"
                        elif koren[:a] != "" and number2 != 0 : # если вне дроби есть число и число расскладывается нацело
                            return f"{numerator}√{number2}/{koren[Drob_Ne+1:a]}"
            elif KDR == False and (KPL == False or KPL == True):
                if koren[a+1:Drob_V].find(".") == -1:
                    number, number2 = vynos_celogo_chisla(int(koren[a+1:Drob_V]))
                else:
                    number, number2 = vynos_NeCelogo_chisla(float(koren[a+1:Drob_V]))
                if koren[Drob_V+1:].find(".") == -1:
                    number3, number4 = vynos_celogo_chisla(int(koren[Drob_V+1:]))
                else:
                    number3, number4 = vynos_NeCelogo_chisla(float(koren[Drob_V+1:]))
                if NeKDR == True and (NeKPL == True or NeKPL == False):  # если вне корня либо целое число, либо числа нету
                    if (number == 0 and number2 == 0) or (number3 == 0 and number4 == 0):
                        return f"Число иррациональное"
                    else:
                        if a != 0:
                            if str(koren[:a]).isdigit() == True: # если число вне корня целое
                                numerator = proverka_dlin_chisla(float(number*int(koren[:a])))
                            elif a != 0: # если число вне корня не целое
                                if str(number*float(koren[:a]))[-1] == "0" and str(number*float(koren[:a]))[-2] == ".":
                                    numerator = str(number*float(koren[:a]))[:-2]
                                elif a != 0:
                                    numerator = proverka_dlin_chisla(float(number*float(koren[:a])))
                        else:
                            numerator = number
                        numerator = check_e(numerator)
                        number2 = check_e(number2)
                        number3 = check_e(number3)
                        number4 = check_e(number4)
                        if number2 == 0 and number4 == 0: # если исло расскладывается нацело и знаменатель расскадывается нацело
                            return f"{numerator}/{number3}" 
                        elif number2 == 0 and number4 != 0: # если число расскладывается нацело, но знаменатель расскадывается не нацело
                            return f"{numerator}/{number3}√1/{number4}" 
                        elif number2 != 0 and number4 == 0: # если число расскладывается нацело, но знаменатель расскадывается нацело
                            return f"{numerator}/{number3}√{number2}"
                        elif number2 != 0 and number4 != 0: # если число расскладывается нацело и знаменатель расскадывается не нацело
                            return f"{numerator}√{number2}/{number3}√{number4}"
                elif NeKDR == False and (NeKPL == False or NeKPL == True): # если вне корня либо дробь с целыми числами, либо дробь с числа с плавающей запятой, либо смешаная дробь
                    if (number == 0 and number2 == 0) or (number3 == 0 and number4 == 0):
                        return f"Число иррациональное"
                    else:
                        if str(koren[:Drob_Ne]).isdigit() == True: # если число вне корня целое
                            numerator = proverka_dlin_chisla(float(number*int(koren[:Drob_Ne])))
                        elif a != 0: # если число вне корня не целое
                            if str(number*float(koren[:Drob_Ne]))[-1] == "0" and str(number*float(koren[:Drob_Ne]))[-2] == ".":
                                numerator = str(number*float(koren[:Drob_Ne]))[:-2]
                            else:
                                numerator = proverka_dlin_chisla(float(number*float(koren[:Drob_Ne])))
                        if str(koren[Drob_Ne+1:a]).isdigit() == True: # если число в корне целое
                            denominator = proverka_dlin_chisla(float(number3*int(koren[Drob_Ne+1:a])))
                        elif a != 0: # если число в корне не целое
                            if str(number3*float(koren[Drob_Ne+1:a]))[-1] == "0" and str(number3*float(koren[Drob_Ne+1:a]))[-2] == ".":
                                denominator = str(number3*float(koren[Drob_Ne+1:a]))[:-2]
                            else:
                                denominator = proverka_dlin_chisla(float(number3*float(koren[Drob_Ne+1:a])))
                        numerator = check_e(numerator)
                        number2 = check_e(number2)
                        number3 = check_e(number3)
                        number4 = check_e(number4)
                        if number2 == 0 and number4 == 0: # если число расскладывается нацело и знаменатель расскадывается нацело
                            return f"{numerator}/{denominator}" 
                        elif number2 == 0 and number4 != 0: # если число расскладывается нацело, но знаменатель расскадывается не нацело
                            return f"{numerator}/{denominator}√1/{number4}" 
                        elif number2 != 0 and number4 == 0: # если число расскладывается нацело, но знаменатель расскадывается нацело
                            return f"{numerator}/{denominator}√{number2}"
                        elif number2 != 0 and number4 != 0: # если число расскладывается нацело и знаменатель расскадывается не нацело
                            return f"{numerator}√{number2}/{denominator}√{number4}"
    except:
        return "Проверьте правильность ввода"
        
def VnosPodKoren(koren):
    try:
        c = 0
        f = 0
        g = 0
        f2 = 0
        g2 = 0
        c2 = 0
        for i in range(0, len(koren)-1):
            if koren[i] == "√":
                c += 1
            if koren[i] == "/":
                f += 1
            if koren[i] == ".":
                g += 1
            if koren[i] == "√" and i == 0:
                c2 += 1
            if koren[i] == "." and (i != 0 and i != len(koren)-1) and koren[i-1].isdigit() and koren[i+1].isdigit():
                g2 += 1
            if koren[i] == "/" and (i != 0 and i != len(koren)-1) and koren[i-1].isdigit() and koren[i+1].isdigit():
                f2 += 1
        if koren[len(koren)-1] == "√":
            c += 1
        if g > 4 or c != 1 or f > 2 or f != f2 or g != g2 or c2 != 0:
            return "Проверьте правильность ввода"
        elif len(koren) == 1:
            return "Проверьте правильность ввода"
        else:
            a = str(koren).find("√")
            Drob_Ne = a
            Drob_V = len(koren)
            number2 = 0
            for i in range(a+1, len(koren)):
                if koren[i] == "/":
                    Drob_V = i
            for i in range(a):
                if koren[i] == "/":
                    Drob_Ne = i
            if str(koren[:Drob_Ne]).isdigit() == True:
                number = int(koren[:Drob_Ne])**2
            else:
                number = float(koren[:Drob_Ne])**2
            if Drob_Ne != a:
                if str(koren[Drob_Ne+1:a]).isdigit() == True:
                    number2 = int(koren[Drob_Ne+1:a])**2
                else:
                    number2 = float(koren[Drob_Ne+1:a])**2
            if str(koren[a+1:Drob_V]).isdigit() == True and len(koren[a+1:Drob_V]) != 0:
                number *= int(koren[a+1:Drob_V])
            elif str(koren[a+1:Drob_V]).isdigit() != True and len(koren[a+1:Drob_V]) != 0:
                number *= float(koren[a+1:Drob_V])
            if Drob_V != len(koren):
                if number2 == 0:
                    number2 = 1
                if str(koren[Drob_V+1:]).isdigit() == True and len(koren[Drob_V+1:]) != 0:
                    number2 *= int(koren[Drob_V+1:])
                elif str(koren[Drob_V+1:]).isdigit() != True and len(koren[Drob_V+1:]) != 0:
                    number2 *= float(koren[Drob_V+1:])
            if type(number) == float:
                if str(number)[-1] == "0" and str(number)[-2] == ".":
                    number = int(str(number)[:-2])
            if type(number2) == float:
                if str(number2)[-1] == "0" and str(number2)[-2] == ".":
                    number2 = int(str(number2)[:-2])
            if number2 == 0:
                return f"√{number}"
            else:
                return f"√{number}/{number2}"
    except:
        return "Проверьте правильность ввода"

def add_digit(digit):
    if calc.get() == "Проверьте правильность ввода" or calc.get() == "Число иррациональное" or calc.get() == "":        
        value = str(digit)
    else:
        value = calc.get() + str(digit)
    calc.delete(0, tk.END)
    calc.insert(0, value)

def delet():
    value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, value[:len(value)-1])

def nachinka1():
    value = VynosIzPodKoren(calc.get())
    calc.delete(0, tk.END)
    calc.insert(0, value)

def nachinka2():
    value = VnosPodKoren(calc.get())
    calc.delete(0, tk.END)
    calc.insert(0, value)

def deleter():
    calc.delete(0, tk.END)

def manual():
    window = tk.Tk()
    window.title("Инструкция пользования")
    window.geometry("300x300")
    window.minsize(300, 300)
    label=tk.Label(window, text="Если требуется внести число под корень\nставим знак корня в конце, либо там, где нужно.\nЕсли требуется вынести число из под корня ставим\nзнак корня впереди числа, либо там, где нужно.\nПример вноса:\n2.5√, 2/3√43, 0.67/23√3/35.6\nПример выноса:\n√256, 0.5√256, 0.67/23√4/0.25\nМожно вводить числа:\nс плавающей запятой, дробные числа, целые числа.")
    label.pack(anchor="center", expand=1)

win.geometry(f"300x350")
win["bg"] = "#D4D4D4"
win.title("kuryator")
win.minsize(300, 350)

calc = tk.Entry(win, justify=tk.RIGHT, font=("Arial", 15), width=15)
calc.grid(row=0, column=0, columnspan=3, stick="we")

tk.Button(text="     C     ", bd=5, font=("Arial", 13), command=lambda: deleter()).grid(row=1, column=0, sticky="wens", padx=5, pady=5)
tk.Button(text="    Del    ", bd=5, font=("Arial", 13), command=lambda: delet()).grid(row=1, column=1, sticky="wens", padx=5, pady=5)
tk.Button(text="√", bd=5, font=("Arial", 13), command=lambda: add_digit("√")).grid(row=1, column=2, sticky="wens", padx=5, pady=5)

tk.Button(text="/", bd=5, font=("Arial", 13), command=lambda: add_digit("/")).grid(row=2, column=0, sticky="wens", padx=5, pady=5)
tk.Button(text=".", bd=5, font=("Arial", 13), command=lambda: add_digit(".")).grid(row=2, column=1, sticky="wens", padx=5, pady=5)
tk.Button(text="инструк", bd=5, font=("Arial", 13), command=lambda: manual()).grid(row=2, column=2, sticky="wens", padx=5, pady=5)

tk.Button(text="7", bd=5, font=("Arial", 13), command=lambda: add_digit(7)).grid(row=3, column=0, sticky="wens", padx=5, pady=5)
tk.Button(text="8", bd=5, font=("Arial", 13), command=lambda: add_digit(8)).grid(row=3, column=1, sticky="wens", padx=5, pady=5)
tk.Button(text="9", bd=5, font=("Arial", 13), command=lambda: add_digit(9)).grid(row=3, column=2, sticky="wens", padx=5, pady=5)

tk.Button(text="4", bd=5, font=("Arial", 13), command=lambda: add_digit(4)).grid(row=4, column=0, sticky="wens", padx=5, pady=5)
tk.Button(text="5", bd=5, font=("Arial", 13), command=lambda: add_digit(5)).grid(row=4, column=1, sticky="wens", padx=5, pady=5)
tk.Button(text="6", bd=5, font=("Arial", 13), command=lambda: add_digit(6)).grid(row=4, column=2, sticky="wens", padx=5, pady=5)

tk.Button(text="1", bd=5, font=("Arial", 13), command=lambda: add_digit(1)).grid(row=5, column=0, sticky="wens", padx=5, pady=5)
tk.Button(text="2", bd=5, font=("Arial", 13), command=lambda: add_digit(2)).grid(row=5, column=1, sticky="wens", padx=5, pady=5)
tk.Button(text="3", bd=5, font=("Arial", 13), command=lambda: add_digit(3)).grid(row=5, column=2, sticky="wens", padx=5, pady=5)

tk.Button(text="Внести", bd=5, font=("Arial", 13), command=lambda: nachinka2()).grid(row=6, column=0, sticky="wens", padx=5, pady=5)
tk.Button(text="0", bd=5, font=("Arial", 13), command=lambda: add_digit(0)).grid(row=6, column=1, sticky="wens", padx=5, pady=5)
tk.Button(text="Вынести", bd=5, font=("Arial", 13), command=lambda: nachinka1()).grid(row=6, column=2, sticky="wens", padx=5, pady=5)

win.grid_columnconfigure(0, minsize=50, weight=1)
win.grid_columnconfigure(1, minsize=50, weight=1)
win.grid_columnconfigure(2, minsize=50, weight=1)

win.grid_rowconfigure(1, minsize=50, weight=1)
win.grid_rowconfigure(2, minsize=50, weight=1)
win.grid_rowconfigure(3, minsize=50, weight=1)
win.grid_rowconfigure(4, minsize=50, weight=1)
win.grid_rowconfigure(5, minsize=50, weight=1)
win.grid_rowconfigure(6, minsize=50, weight=1)

win.mainloop()
