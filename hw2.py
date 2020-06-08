# -*- coding: utf-8 -*-
#Этой строкой разрешаем писать русские буквы в скрипте
import pandas as pd

%pylab inline
import matplotlib.pyplot as plt

import sys          # библиотека нужна для получения аргументов запуска (в аргументе предаем имя файла для разбора)
def main(args=False):   #запускам основную программу, args = список аргументов
    #-------------------------------------------------------------обработка параметров запуска--------------------------
    
    args.insert(1,"MissingMigrants-Global-2020-05-28T22-12-38.csv")  #если скрипт запущен без аргументов - вставляем на место первого имя файла по умолчанию
    try:
        all_data = pd.read_csv(args[1]) #ЗАГРУЖАЕМ ДАННЫЕ ИЗ ФАЙЛА В data
    except (FileExistsError,FileNotFoundError) as e: #обработка ошибки, если нет файла для анализа
        print(f'Нет файла для анализа, Ошибка:{e}')
        quit(1)

    all_data.groupby("Reported Year").sum()["Number Dead"].plot(kind='bar')
    plt.show(block=True)
    all_data.groupby("Region").sum()["Number Dead"].plot(kind='bar')
    plt.show(block=True)
    all_data.loc[all_data["Region"] == "Mediterranean"].groupby("Reported Year").sum()["Number Dead"].plot(kind='bar')
    plt.show(block=True)
    all_data.loc[all_data["Region"] == "Mediterranean"].groupby("Reported Year").sum().plot(kind='bar',
                                                                                            y=["Number of Males",
                                                                                               "Number of Females",
                                                                                               "Number of Children"])
    plt.show(block=True)
main(sys.argv)