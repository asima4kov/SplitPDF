
def list_12(path_1,sw,color) :
    images = convert_from_path(path_1,28,poppler_path=r'C:\Program Files\poppler-24.02.0\Library\bin')
    for image in images:
        img = np.array(image.convert('HSV'))
        hsv_sum = img.sum(0).sum(0)
        if hsv_sum[0] == 0 and hsv_sum[1] == 0:
            sw += 1
        else:
            color += 1
    print(f'цветные  {color}' )
    print(f'черно-белые {sw}')
    return sw,color






import PyPDF2
import os
from pdf2image import convert_from_path
import numpy as np
from tkinter import *
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
from tkinter import scrolledtext
import tkinter.filedialog as fd
from tkinter import messagebox

def edit_click():
    messagebox.showinfo("О программе", "Программа предназначена: \n -для подсчета разных форматов бумаги файлов PDF  \n -для расчета материалов для печати \n -по вопросам и предложениям обращаться на почту:alex265265@yandex.ru")
def clear_click ():
    txt.delete("1.0", "end")
def exit_click ():
    root.destroy()
def open_fail():
    filepath = filedialog.askopenfilename()
    file_name = os.path.basename(filepath)
    if filepath != "":
            a4 = 0
            a4_3=0
            a4_4=0
            a4_5=0
            a4_6=0
            a4_7=0
            a4_8=0
            a3=0
            a3_3=0
            a3_4=0
            a3_5=0
            a3_6=0
            a3_7=0
            a2=0
            a2_3=0
            a1=0
            a1_3=0
            a0=0
            a_err=0
            sw=0
            color=0
            total_sw=0
            total_color=0

            roll_length=0
            totalPages_all=0
            total_sw=0
            total_color=0
            path_1=filepath
            if enabled.get()==1:
                list_12(path_1,sw,color)
                total_sw1=list_12(path_1,sw,color)
                total_sw=total_sw+total_sw1[0]
                total_color = total_color + total_sw1[1]

            file = open(path_1, 'rb') # открытие файла
            pdfReader = PyPDF2.PdfReader(file)
            totalPages =int( len(pdfReader.pages)) #количество страниц в файле
            for i in range(totalPages): # цикл по листам
                first_page =pdfReader.pages[i]
                w =((float(first_page.mediabox.width)*2.54)/72)*10
                h =((float(first_page.mediabox.height)*2.54)/72)*10
                totalPages_all=totalPages_all+1
                if (w<219 and h<314) or (w<314 and h<219):
                    a4=a4+1
                elif 600 < w < 660 and 280<h < 310:
                    a4_3 = a4_3 + 1
                    roll_length = roll_length + w
                elif 600 < h < 660 and 280<w < 310:
                    a4_3 = a4_3 + 1
                    roll_length = roll_length + h
                elif 750 < w < 900 and  280<h < 310:
                    a4_4 = a4_4 + 1
                    roll_length = roll_length + w
                elif 750 < h < 900 and  280<w < 310:
                    a4_4 = a4_4 + 1
                    roll_length = roll_length + h
                elif 280 < w < 310 and 1000<h < 1100 :
                    a4_5 = a4_5 + 1
                    roll_length = roll_length + h
                elif  280 < h < 310 and 1000 < w < 1100:
                    a4_5 = a4_5 + 1
                    roll_length = roll_length + w
                elif 1200 < w < 1300 and 280<h < 310:
                    a4_6 = a4_6 + 1
                    roll_length = roll_length + w
                elif 280 < w < 310 and 1400<h < 1500:
                    a4_7 = a4_7 + 1
                    roll_length = roll_length + h
                elif 1600 < h < 1700 and 280<w < 310:
                    a4_8 = a4_8 + 1
                    roll_length = roll_length + h
                elif (400 < w < 440 and 280< h < 310) or (280<w<360 and 400<h<450):
                    a3 = a3 + 1
                elif 400<w < 440 and 840<h <920:
                    a3_3 = a3_3 + 1
                    roll_length = roll_length + h
                elif 400<h < 440 and 850<w <920:
                    a3_3 = a3_3 + 1
                    roll_length = roll_length + w
                elif 400<w < 440 and 1100<h < 1250:
                    a3_4 = a3_4 + 1
                    roll_length = roll_length + h
                elif 400<w < 440 and 1400<h < 1510:
                    a3_5 = a3_5 + 1
                    roll_length = roll_length + h
                elif 400<w < 440  and 1700 < h < 1810:
                    a3_6 = a3_6 + 1
                    roll_length = roll_length + h
                elif 400 < w < 440 and 2000 < h < 2150:
                    a3_7 = a3_7 + 1
                    roll_length = roll_length + h
                elif 550 < w < 610 and 400< h < 450:
                    a2=a2+1
                    roll_length = roll_length + w
                elif 550 < h < 610 and 400 < w < 450:
                    a2 = a2 + 1
                    roll_length = roll_length + h
                elif 550 < w < 610 and 1200< h < 1300:
                    a2_3=a2_3+1
                    roll_length = roll_length + h
                elif 550 < h < 610 and 1200 < w < 1300:
                    a2_3 = a2_3 + 1
                    roll_length = roll_length + w
                elif 800 < w < 860 and 550< h < 620:
                    a1=a1+1
                    roll_length = roll_length + w
                elif 800 < h < 860 and 550< w < 620:
                    a1=a1+1
                    roll_length = roll_length + h
                elif 800 < w < 860 and 1700< h < 1810:
                    a1_3=a1_3+1
                    roll_length = roll_length + h
                elif (1100 < w < 1220 and 800 < h <860) or (1100 < h < 1220 and 800 < w <860):
                    a0 =  a0  + 1
                    roll_length = roll_length + w
                elif (1100 < h < 1220 and 800 < w <860):
                    a0 = a0  + 1
                    roll_length = roll_length + h
                else:
                    a_err=a_err+1
                    roll_length = roll_length + w
    if filepath != "":
        if a4!=0:
            print("A4="+ str(a4))
            txt.insert("1.0", "\nA4 = "+str(a4)+"\n")
        if a4_3!=0:
            print("A4на3="+ str(a4_3))
            txt.insert("1.0", "\nA4х3 = "+str(a4_3))
        if a4_4 != 0:
            print("A4на4="+ str(a4_4))
            txt.insert("1.0", "\nA4х4 = "+ str(a4_4))
        if a4_5 != 0:
            print("A4на5="+ str(a4_5))
            txt.insert("1.0", "\nA4х5 = "+str(a4_5))
        if a4_6 != 0:
            print("A4на6="+ str(a4_6))
            txt.insert("1.0","\nA4х6 = "+str(a4_6))
        if a4_7 != 0:
            print("A4на7="+ "\nA4х7 = "+str(a4_7))
            txt.insert("1.0", str(a4_7))
        if a4_8 != 0:
            print("A4на8="+ str(a4_8))
            txt.insert("1.0", "\nA4х8 = "+str(a4_8))
        if a3!=0:
            print("A3="+ str(a3))
            txt.insert("1.0","\nA3 = " +str(a3))
        if a3_3!=0:
            print("A3на3 ="+ str(a3_3))
            txt.insert("1.0", "\nA3х3 = " +str(a3_3))
        if a3_4!=0:
            print("A3на4 ="+ str(a3_4))
            txt.insert("1.0","\nA3х4 = "+ str(a3_4))
        if a3_5!=0:
            print("A3на5 ="+ str(a3_5))
            txt.insert("1.0", "\nA3х5 = "+str(a3_5))
        if a3_6!=0:
            print("A3на6 ="+ str(a3_6))
            txt.insert("1.0", "\nA3х6 = "+str(a3_6))
        if a3_7!=0:
            print("A3на7 ="+ str(a3_7))
            txt.insert("1.0", "\nA3х7 = "+str(a3_7))
        if a2!=0:
            print("A2="+ str(a2))
            txt.insert("1.0", "\nA2 = "+str(a2))
        if a2_3!=0:
            print("A2на3="+ str(a2_3))
            txt.insert("1.0",  "\nA2х3 = " +str(a2_3))
        if a1!=0:
            print("A1="+ str(a1))
            txt.insert("1.0", "\nA1 = " + str(a1))
        if a1_3!=0:
            print("A1на3="+ str(a1_3))
            txt.insert("1.0", "\nA1х3 = " +str(a1_3))
        if a0!=0:
            print("A0="+ str(a0))
            txt.insert("1.0", "\nA0 = " +str(a0))
        if a_err!=0:
            print("неизвестный формат = "+ str(a_err))
            txt.insert("1.0", "\nнеизвестный формат = " +str(a_err))
        print("длина рулона="+ str(round(roll_length,1))+" мм")
        print(f"черно-белых листов: { total_sw}")
        print(f"цветных листов: { total_color}")
        print(f"Total Pages: { totalPages_all}")
        txt.insert("1.0", "\nДлина рулона = "+str(round(roll_length,1))+" мм")
        txt.insert("1.0", "\nВсего листов:" + str(totalPages_all) )
        if enabled.get()==1:
            txt.insert("1.0", "\nЧерно-белые:" + str(total_sw))
            txt.insert("1.0", "\nЦветные:" + str(total_color))
        txt.insert("1.0", "\nИмя файла:" + str(file_name))
        txt.insert("1.0", "-------------------------" )
def startallprogressbar(caunt_failov,count_):
    pgr.step(300 / caunt_failov)
    root.update()
def startallprogressbar_1():
        root.update()

def open_directory():
    directory = fd.askdirectory(title="Открыть папку", initialdir="/")
    if directory:
        print(directory)
        path = directory  # путь к папке в которой находятся PDF
        a4=0
        a4_3=0
        a4_4=0
        a4_5=0
        a4_6=0
        a4_7=0
        a4_8=0
        a3=0
        a3_3=0
        a3_4=0
        a3_5=0
        a3_6=0
        a3_7=0
        a2=0
        a2_3=0
        a1=0
        a1_3=0
        a0=0
        a_err=0
        roll_length=0
        totalPages_all=0
        total_sw=0
        total_color=0
        sw = 0
        color = 0
        count_=0


        for i in os.listdir(path): # цикл по всему содержимому в папке
            print(i)
            path_col=os.listdir(path)
            caunt_failov=len(path_col)
            if i.endswith(".pdf"): # отбор pdf файлов
                count_=count_+1
                startallprogressbar(caunt_failov,count_)
                file_name = os.path.basename(path)
                path_1=path+"\\"+i
                if enabled.get() == 1:
                    list_12(path_1, sw, color)
                    total_sw1 = list_12(path_1, sw, color)
                    total_sw = total_sw + total_sw1[0]
                    total_color = total_color + total_sw1[1]
                file = open(path_1, 'rb') # открытие файла
                pdfReader = PyPDF2.PdfReader(file)
                totalPages =int( len(pdfReader.pages)) #количество страниц в файле
                for i in range(totalPages): # цикл по листам
                    first_page =pdfReader.pages[i]
                    w =((float(first_page.mediabox.width)*2.54)/72)*10
                    h =((float(first_page.mediabox.height)*2.54)/72)*10
                    totalPages_all=totalPages_all+1
                    if (w < 219 and h < 314) or (w < 314 and h < 219):
                        a4 = a4 + 1
                    elif 600 < w < 660 and 280 < h < 310:
                        a4_3 = a4_3 + 1
                        roll_length = roll_length + w
                    elif 600 < h < 660 and 280 < w < 310:
                        a4_3 = a4_3 + 1
                        roll_length = roll_length + h
                    elif 750 < w < 900 and 280 < h < 310:
                        a4_4 = a4_4 + 1
                        roll_length = roll_length + w
                    elif 750 < h < 900 and 280 < w < 310:
                        a4_4 = a4_4 + 1
                        roll_length = roll_length + h
                    elif 280 < w < 310 and 1000 < h < 1100:
                        a4_5 = a4_5 + 1
                        roll_length = roll_length + h
                    elif 280 < h < 310 and 1000 < w < 1100:
                        a4_5 = a4_5 + 1
                        roll_length = roll_length + w
                    elif 1200 < w < 1300 and 280 < h < 310:
                        a4_6 = a4_6 + 1
                        roll_length = roll_length + w
                    elif 280 < w < 310 and 1400 < h < 1500:
                        a4_7 = a4_7 + 1
                        roll_length = roll_length + h
                    elif 1600 < h < 1700 and 280 < w < 310:
                        a4_8 = a4_8 + 1
                        roll_length = roll_length + h
                    elif (400 < w < 440 and 280 < h < 310) or (280 < w < 360 and 400 < h < 450):
                        a3 = a3 + 1
                    elif 400 < w < 440 and 840 < h < 920:
                        a3_3 = a3_3 + 1
                        roll_length = roll_length + h
                    elif 400 < h < 440 and 850 < w < 920:
                        a3_3 = a3_3 + 1
                        roll_length = roll_length + w
                    elif 400 < w < 440 and 1100 < h < 1250:
                        a3_4 = a3_4 + 1
                        roll_length = roll_length + h
                    elif 400 < w < 440 and 1400 < h < 1510:
                        a3_5 = a3_5 + 1
                        roll_length = roll_length + h
                    elif 400 < w < 440 and 1700 < h < 1810:
                        a3_6 = a3_6 + 1
                        roll_length = roll_length + h
                    elif 400 < w < 440 and 2000 < h < 2150:
                        a3_7 = a3_7 + 1
                        roll_length = roll_length + h
                    elif 550 < w < 610 and 400 < h < 450:
                        a2 = a2 + 1
                        roll_length = roll_length + w
                    elif 550 < h < 610 and 400 < w < 450:
                        a2 = a2 + 1
                        roll_length = roll_length + h
                    elif 550 < w < 610 and 1200 < h < 1300:
                        a2_3 = a2_3 + 1
                        roll_length = roll_length + h
                    elif 550 < h < 610 and 1200 < w < 1300:
                        a2_3 = a2_3 + 1
                        roll_length = roll_length + w
                    elif 800 < w < 860 and 550 < h < 620:
                        a1 = a1 + 1
                        roll_length = roll_length + w
                    elif 800 < h < 860 and 550 < w < 620:
                        a1 = a1 + 1
                        roll_length = roll_length + h
                    elif 800 < w < 860 and 1700 < h < 1810:
                        a1_3 = a1_3 + 1
                        roll_length = roll_length + h
                    elif (1100 < w < 1220 and 800 < h < 860) or (1100 < h < 1220 and 800 < w < 860):
                        a0 = a0 + 1
                        roll_length = roll_length + w
                    elif (1100 < h < 1220 and 800 < w < 860):
                        a0 = a0 + 1
                        roll_length = roll_length + h
                    else:
                        a_err = a_err + 1
                        roll_length = roll_length + w
        if a4 != 0:
            print("A4=" + str(a4))
            txt.insert("1.0", "\nA4 = " + str(a4) + "\n")
        if a4_3 != 0:
            print("A4на3=" + str(a4_3))
            txt.insert("1.0", "\nA4х3 = " + str(a4_3))
        if a4_4 != 0:
            print("A4на4=" + str(a4_4))
            txt.insert("1.0", "\nA4х4 = " + str(a4_4))
        if a4_5 != 0:
            print("A4на5=" + str(a4_5))
            txt.insert("1.0", "\nA4х5 = " + str(a4_5))
        if a4_6 != 0:
            print("A4на6=" + str(a4_6))
            txt.insert("1.0", "\nA4х6 = " + str(a4_6))
        if a4_7 != 0:
            print("A4на7=" + "\nA4х7 = " + str(a4_7))
            txt.insert("1.0", str(a4_7))
        if a4_8 != 0:
            print("A4на8=" + str(a4_8))
            txt.insert("1.0", "\nA4х8 = " + str(a4_8))
        if a3 != 0:
            print("A3=" + str(a3))
            txt.insert("1.0", "\nA3 = " + str(a3))
        if a3_3 != 0:
            print("A3на3 =" + str(a3_3))
            txt.insert("1.0", "\nA3х3 = " + str(a3_3))
        if a3_4 != 0:
            print("A3на4 =" + str(a3_4))
            txt.insert("1.0", "\nA3х4 = " + str(a3_4))
        if a3_5 != 0:
            print("A3на5 =" + str(a3_5))
            txt.insert("1.0", "\nA3х5 = " + str(a3_5))
        if a3_6 != 0:
            print("A3на6 =" + str(a3_6))
            txt.insert("1.0", "\nA3х6 = " + str(a3_6))
        if a3_7 != 0:
            print("A3на7 =" + str(a3_7))
            txt.insert("1.0", "\nA3х7 = " + str(a3_7))
        if a2 != 0:
            print("A2=" + str(a2))
            txt.insert("1.0", "\nA2 = " + str(a2))
        if a2_3 != 0:
            print("A2на3=" + str(a2_3))
            txt.insert("1.0", "\nA2х3 = " + str(a2_3))
        if a1 != 0:
            print("A1=" + str(a1))
            txt.insert("1.0", "\nA1 = " + str(a1))
        if a1_3 != 0:
            print("A1на3=" + str(a1_3))
            txt.insert("1.0", "\nA1х3 = " + str(a1_3))
        if a0 != 0:
            print("A0=" + str(a0))
            txt.insert("1.0", "\nA0 = " + str(a0))
        if a_err != 0:
            print("неизвестный формат = " + str(a_err))
            txt.insert("1.0", "\nнеизвестный формат = " + str(a_err))
        txt.insert("1.0", "\nДлина рулона = " + str(round(roll_length, 1)) + " мм")
        txt.insert("1.0", "\nВсего листов:" + str(totalPages_all))
        if enabled.get() == 0:
            txt.insert("1.0", "\nИмя паки:" + str(file_name))
            txt.insert("1.0", "-------------------------")
        if enabled.get() == 1:
            txt.insert("1.0", "\nЧерно-белые:" + str(total_sw))
            txt.insert("1.0", "\nЦветные:" + str(total_color))
            txt.insert("1.0", "\nИмя паки:" + str(file_name))
            txt.insert("1.0", "-------------------------")
        startallprogressbar_1()


root = Tk()
root.title("SplitPDF")
root.geometry("500x600")

main_menu = Menu()
main_menu.add_cascade(label="О программе", command=edit_click)
main_menu.add_cascade(label="Отчистить поле", command=clear_click)
main_menu.add_cascade(label="Выйти" , command=exit_click)

root.config(menu=main_menu)

enabled = IntVar()
enabled_checkbutton = ttk.Checkbutton(text="Выполнять расчет по черно-белым и цветным листам ", variable=enabled)
enabled_checkbutton.place(x=10, y=65)

pgr= DoubleVar(value=0)
pgr=ttk.Progressbar(orient="horizontal",mode='determinate', length=200, maximum=300,variable=pgr)
pgr.place(x=10, y=560,width=480, height=15)


btn = ttk.Button(text="Загрузить файл PDF", command=open_fail)
btn.place(x=10, y=10,width=230, height=40)
btn = ttk.Button(text="Выбрать папку с файлами",command=open_directory)
btn.place(x=260, y=10,width=230, height=40)
txt = scrolledtext.ScrolledText( width=40, height=10)
txt.place(x=10, y=100,width=480, height=450)





root.mainloop()
