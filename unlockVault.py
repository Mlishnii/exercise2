import decrypt1
print("*"*100)
import solvepuzzle2
print("*"*100)
import  magicnum3
print("*"*100)
import  checkpass3
print("*"*100)
# اصلا خروجیش جوری نبود که بشه باهاش کلمه رمز ساخت برا همین نزاشتمش اصلاexam num نکته: فایل 
#ولی خروجیشو تو خود فایلش میتونید ببینید
# |=هم همینطور turtlee فایل 

def unlock_vault(clues):
    passWord="".join(clues)
    return passWord

l = []

l.append(decrypt1.a[0][0])
#-----------------1--------------

l.append(solvepuzzle2.a[0][0])
#-----------------2--------------

l.append(str(magicnum3.a[0]))
l.append(checkpass3.a[0][0])
#-----------------3--------------
print("The final password is: ", unlock_vault(l))
# این عددی که تو کلمه رمز خروجی میگیریم،با اینی که خود تابع تولید میکنه فرق داره
# چون خب رندومه دیگه، هر دفعه یه عدد جدید تولید میکنه
# [= استفاده کنم ولی خب ظاهر قشنگی نداشتseed البته میتونستم از 

