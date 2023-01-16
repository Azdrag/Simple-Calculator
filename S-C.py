from math import sqrt    
a = input ("Sonni kiriting: ")
b = input ("Sonni kiriting: ")
c = ["/" ,"*" ,"-" ,"+" ,"%" ,"**" , "//" ,"V"]
amal = input(f"Amakni tanlang: {c}: ")
if amal == '+':
    print (f"Siz kirirtgan sonlaringizni qo`shmasi {int(a) + int(b)}")
elif amal == '-':
    print (f"Siz kirirtgan sonlaringizni Ayirmasi {int(a) - int(b)}")    
elif amal == '/':
    print (f"Siz kirirtgan sonlaringizni bo`linmasi {int(a) / int(b)}")    
elif amal == '*':
    print (f"Siz kirirtgan sonlaringizni yig`indisi {int(a) * int(b)}")
elif amal == '%':
    print (f"Siz kirirtgan sonlaringizni foizlaganda {int(a) % int(b)}")  
elif amal == '**':
    print (f"Siz kirirtgan sonlaringizni darajasi {int(a) ** int(b)}")    
elif amal == '//':
    print (f"Siz kirirtgan sonlaringizni qoldiqsiz ko`rinish holida {int(a) // int(b)}") 
elif amal == 'V':
    print (f"Siz kirirtgan sonni ildizi {sqrt(int(a))}, {sqrt(int(b))}") 
