import datetime as dt
import random
import re


def total_salary(path):
    total=0
    count=0
    with open(path,"r+") as f:
        for line in f.readlines():
            count=count+1
            list=line.split(',')
            total=total+int(list[1])

    if total!=0 and count!=0:
       average=total/count
    return {total,average}

           
	   




#******************************************
try:
    def get_cats_info(path):
       
        rezult_list=[]
        with open(path,"r+") as f:
            lines = [el.strip() for el in f.readlines()]
            for el in lines:
                s={}
                el=el.split(",")
                s["id"]=el[0]
                s["name"]=el[1]
                s["age"]=el[2]
                rezult_list.append(s)
       
        return f"{rezult_list}"
except FileNotFoundError:
        print("Файл не знайден")

try:
    def parse_input(str):
        
except ValueError:
    print("Value Error")






 