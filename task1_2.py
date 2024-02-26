from HW04 import total_salary, get_cats_info

def main():
    print("**********Завдання №1**********") 
    total, average = total_salary("text.txt")
    print(f"Загальна сума заробітної плати: {total} грн, Середня заробітна плата: {average} грн")


    print("***********Завдання №2**********")    
    info=get_cats_info('cats_info.txt')
    print(info)

#******************************************
if __name__=="__main__":
    main()
    