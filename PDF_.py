
import PyPDF2
import os
from pdf2image import convert_from_path
import numpy as np
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import scrolledtext
import tkinter.filedialog as fd
from tkinter import messagebox
def list_12(path_1,sw,color) :
    images = convert_from_path(path_1,28,poppler_path=r'C:\Program Files\poppler-24.02.0\Library\bin')
    for image in images:
        img = np.array(image.convert('HSV'))
        hsv_sum = img.sum(0).sum(0)
        if hsv_sum[0] == 0 and hsv_sum[1] == 0:
            sw += 1
        else:
            color += 1
    return sw,color

def edit_click():
    messagebox.showinfo("О программе", "Программа предназначена: \n -для подсчета разных форматов бумаги файлов PDF  \n -для расчета материалов для печати "
                                       "\n -по вопросам и предложениям обращаться на почту:alex265265@yandex.ru")
def clear_click ():
    txt.delete("1.0", "end")
def exit_click ():
    root.destroy()

def calculation(filepath):
    if filepath != "":
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
        path_1=filepath
    file = open(path_1, 'rb')  # открытие файла
    pdfReader = PyPDF2.PdfReader(file)
    totalPages = int(len(pdfReader.pages))  # количество страниц в файле
    for i in range(totalPages):  # цикл по листам
        first_page = pdfReader.pages[i]
        w = ((float(first_page.mediabox.width) * 0.3527778))  # 1 пункт равно 0.352778 миллиметров
        h = ((float(first_page.mediabox.height) * 0.352778))
        totalPages_all = totalPages_all + 1
        # длина и ширена листов по форматом с возможным разбросом 10%-15%
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
    return  a4,a4_3,a4_4,a4_5,a4_6,a4_7,a4_8,a3,a3_3,a3_4,a3_5,a3_6,a3_7,a2,a2_3,a1,a1_3,a0,a_err,roll_length,totalPages_all #21

def output(value_list):
    if value_list[0] != 0:
        print("A4=" + str(value_list[0]))
        txt.insert("1.0", "\nA4 = " + str(value_list[0]) + "\n")
    if value_list[1] != 0:
        print("A4на3=" + str(value_list[1]))
        txt.insert("1.0", "\nA4х3 = " + str(value_list[1]))
    if value_list[2] != 0:
        print("A4на4=" + str(value_list[2]))
        txt.insert("1.0", "\nA4х4 = " + str(value_list[2]))
    if value_list[3] != 0:
        print("A4на5=" + str(value_list[3]))
        txt.insert("1.0", "\nA4х5 = " + str(value_list[3]))
    if value_list[4] != 0:
        print("A4на6=" + str(value_list[4]))
        txt.insert("1.0", "\nA4х6 = " + str(value_list[4]))
    if value_list[5] != 0:
        print("A4на7=" + "\nA4х7 = " + str(value_list[5]))
        txt.insert("1.0", str(value_list[5]))
    if value_list[6] != 0:
        print("A4на8=" + str(value_list[6]))
        txt.insert("1.0", "\nA4х8 = " + str(value_list[6]))
    if value_list[7] != 0:
        print("A3=" + str(value_list[7]))
        txt.insert("1.0", "\nA3 = " + str(value_list[7]))
    if value_list[8] != 0:
        print("A3на3 =" + str(value_list[8]))
        txt.insert("1.0", "\nA3х3 = " + str(value_list[8]))
    if value_list[9] != 0:
        print("A3на4 =" + str(value_list[9]))
        txt.insert("1.0", "\nA3х4 = " + str(value_list[9]))
    if value_list[10] != 0:
        print("A3на5 =" + str(value_list[10]))
        txt.insert("1.0", "\nA3х5 = " + str(value_list[10]))
    if value_list[11] != 0:
        print("A3на6 =" + str(value_list[11]))
        txt.insert("1.0", "\nA3х6 = " + str(value_list[11]))
    if value_list[12]!= 0:
        print("A3на7 =" + str(value_list[12]))
        txt.insert("1.0", "\nA3х7 = " + str(value_list[12]))
    if value_list[13] != 0:
        print("A2=" + str(value_list[13]))
        txt.insert("1.0", "\nA2 = " + str(value_list[13]))
    if value_list[14] != 0:
        print("A2на3=" + str(value_list[14]))
        txt.insert("1.0", "\nA2х3 = " + str(value_list[14]))
    if value_list[15] != 0:
        print("A1=" + str(value_list[15]))
        txt.insert("1.0", "\nA1 = " + str(value_list[15]))
    if value_list[16] != 0:
        print("A1на3=" + str(value_list[16]))
        txt.insert("1.0", "\nA1х3 = " + str(value_list[16]))
    if value_list[17] != 0:
        print("A0=" + str(value_list[17]))
        txt.insert("1.0", "\nA0 = " + str(value_list[17]))
    if value_list[18] != 0:
        print("неизвестный формат = " + str(value_list[18]))
        txt.insert("1.0", "\nнеизвестный формат = " + str(value_list[18]))
    txt.insert("1.0", "\nДлина рулона = " + str(round(value_list[19], 1)) + " мм")
    txt.insert("1.0", "\nВсего листов:" + str(value_list[20]))

def open_file():
    filepath = filedialog.askopenfilename()
    file_name = os.path.basename(filepath)
    if filepath != "":
            sw=0
            color=0
            total_sw=0
            total_color=0
            path_1=filepath
            if enabled.get()==1:
                list_12(path_1,sw,color)
                total_sw1=list_12(path_1,sw,color)
                total_sw=total_sw+total_sw1[0]
                total_color = total_color + total_sw1[1]
            calculation(filepath)
            value_list=calculation(filepath)
    if filepath != "":
        output(value_list)
        if enabled.get()==1:
            txt.insert("1.0", "\nЧерно-белые:" + str(total_sw))
            txt.insert("1.0", "\nЦветные:" + str(total_color))
        txt.insert("1.0", "\nИмя файла:" + str(file_name))
        txt.insert("1.0", "-------------------------")
def startallprogressbar(caunt_failov):
    pgr.step(300 / caunt_failov)
    root.update()
def startallprogressbar_1():
        root.update()

def open_directory():
    arr_b=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    directory = fd.askdirectory(title="Открыть папку", initialdir="/")
    if directory:
        path = directory  # путь к папке в которой находятся PDF
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
                startallprogressbar(caunt_failov)
                file_name = os.path.basename(path)
                path_1=path+"\\"+i
                if enabled.get() == 1:
                    list_12(path_1, sw, color)
                    total_sw1 = list_12(path_1, sw, color)
                    total_sw = total_sw + total_sw1[0]
                    total_color = total_color + total_sw1[1]
                calculation(path_1)
                value_list = calculation(path_1)
                arr_a= value_list
                arr_b=np.array(arr_b)+np.array(arr_a)
        if path_1 != "":
            output(arr_b)
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
main_menu.add_cascade(label="Выйти", command=exit_click)

root.config(menu=main_menu)

enabled = IntVar()
enabled_checkbutton = ttk.Checkbutton(text="Выполнять расчет по черно-белым и цветным листам ", variable=enabled)
enabled_checkbutton.place(x=10, y=65)

pgr= DoubleVar(value=0)
pgr=ttk.Progressbar(orient="horizontal",mode='determinate', length=200, maximum=300,variable=pgr)
pgr.place(x=10, y=560,width=480, height=15)

btn = ttk.Button(text="Загрузить файл PDF", command=open_file)
btn.place(x=10, y=10,width=230, height=40)
btn = ttk.Button(text="Выбрать папку с файлами",command=open_directory)
btn.place(x=260, y=10,width=230, height=40)
txt = scrolledtext.ScrolledText( width=40, height=10)
txt.place(x=10, y=100,width=480, height=450)

root.mainloop()
