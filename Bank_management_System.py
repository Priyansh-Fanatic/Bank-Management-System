from tkinter import *
from datetime import date
import random
import mysql.connector
from tkinter import messagebox

try:
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password",
    database="bank_sys"
    )
except:
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password"
    )
    c2=mydb.cursor()
    c2.execute("CREATE DATABASE bank_sys")
    print("Database created successfully.")
    c2.execute("USE bank_sys")


global c1
c1 = mydb.cursor()

try:
    c1.execute("DESCRIBE bank_sys.login")
    myresult = c1.fetchall()
except:
    c1.execute("CREATE TABLE login (username VARCHAR(100),password VARCHAR(20),name VARCHAR(100),number INT,pin INT,money INT)")

#date
global ty
ty=date.today()

#all back
def back():
    a.withdraw()
    main_page()

def back1():
    c.withdraw()
    main_page()

def back2():
    d.withdraw()
    home()

def back3():
    e.withdraw()
    home()

def back4():
    f.withdraw()
    home()

def back5():
    g.withdraw()
    home()

#login logic
def login1():
        global dn
        dn=e1.get()
        en=e2.get()
        
        global result1
        sql = f"SELECT username FROM login Where username='{dn}'"
        c1.execute(sql)
        result1 = c1.fetchall()

        global result2
        sql1 = f"SELECT password FROM login Where password='{en}'"
        c1.execute(sql1)
        result2 = c1.fetchall()

        if result1 and result2 :
            messagebox.showinfo("Info","you are logged in")
            a.withdraw()
            home()

        elif en=="" and dn=="":
            messagebox.showerror("Info","fill the entry") 
        elif dn=="":
            messagebox.showerror("Error","Username can't be blank")
        elif en=="":
            messagebox.showerror("error","Password can't be blank")   
        elif result1 or result2:
            messagebox.showerror("Info","password or username is wrong.")
        else:
            messagebox.showinfo("Info","User not exists,create a new account.")     
        

#create logic
def create1():
    global us
    pas=e4.get()
    us=e3.get()
    nm=e5.get()
    pn=e6.get()
    p=random.randint(10000000,99999999)

    sql2 = f"SELECT username FROM login Where username='{us}'"
    c1.execute(sql2)
    myresult = c1.fetchall()

    if myresult and us!="":
        messagebox.showinfo("Info","Username Already Exists")
    elif us=="" and  pas=="":
        messagebox.showerror("Error","Username and Password can't be blank") 
    elif us=="" and pas=="" and nm=="" and pn=="":
        messagebox.showerror("Error","Fill all the entry")
    elif us=="":
        messagebox.showerror("Error","Username can't be blank")   
    elif pas=="":
        messagebox.showerror("Error","Password can't be blank")
    elif us!="":
        sql3 = "INSERT INTO login (username, password,name,number,pin,money) VALUES (%s, %s,%s,%s,%s,%s)"
        val = (f'{us}', f'{pas}',f'{nm}',f'{p}',f'{pn}','0')
        c1.execute(sql3, val)

        mydb.commit()

        messagebox.showinfo("Info", "New User Registered")

        c1.execute(f"CREATE TABLE {us} ( id int,date varchar(100),amount int,reason varchar(100),balance int)")
        sql6 = f"INSERT INTO {us} (id,date,amount,reason,balance) VALUES (%s,%s, %s,%s,%s)"
        val1 = ('1',f'{ty}', '0','Account created','0')
        c1.execute(sql6, val1)
        mydb.commit()

        c.withdraw()
        main_page()

#login page
def login():
    global a
    a=Tk()
    
    a.title("login")
    a.geometry("370x370")
    a.resizable(False,False)
    b.withdraw()
   
    c1=Canvas(a,bg='#e0cdbe',height=500,width=450).pack()

    a1=Label(a,text="Login",font=("arial",24),bg='#e0cdbe').place(x=60,y=20)
    l1=Label(a,text="Username",font=("arial",12),bg='#e0cdbe').place(x=65,y=80)
    global e1
    e1=Entry(a,width=40)
    e1.place(x=70,y=105)

    l2=Label(a,text="Password",font=("arial",12),bg='#e0cdbe').place(x=65,y=140)
    global e2
    e2=Entry(a,width=40,show="*")
    e2.place(x=70,y=165)
    b1=Button(a,text="Login",width=30,command=login1,bg="#ffdab9").place(x=80,y=210)
    b2=Button(a,width=3,text="Back",border=5,command=back,padx=2,pady=2,bg="#e7c9a9")
    b2.place(x=300,y=25)
    a.mainloop()
    
#create page
def create():
    global c
    c=Tk()
    c.title("sign up")

    c.geometry("370x390")
    c.resizable(False,False)
    b.withdraw()

    c2=Canvas(c,bg='#79cbb8',height=500,width=450).pack()

    a1=Label(c,text="Sign up",font=("arial",24),bg='#79cbb8').place(x=60,y=20)


    l3=Label(c,text="Username",font=("arial",12),bg='#79cbb8').place(x=65,y=80)
    global e3
    e3=Entry(c,width=40)
    e3.place(x=70,y=105)

    l4=Label(c,text="Password",font=("arial",12),bg='#79cbb8').place(x=65,y=140)
    global e4
    e4=Entry(c,width=40,show="*")
    e4.place(x=70,y=165)
    l5=Label(c,text="Name",font=("arial",12),bg='#79cbb8').place(x=65,y=200)
    global e5
    e5=Entry(c,width=40)
    e5.place(x=70,y=225)
    l6=Label(c,text="Pin",font=("arial",12),bg='#79cbb8').place(x=65,y=260)
    global e6
    e6=Entry(c,width=40)
    e6.place(x=69,y=285)

    b3=Button(c,text="Create new account",width=27,command=create1,bg='#c9eae2').place(x=91,y=325)  
    b4=Button(c,width=7,text="Back",border=5,command=back1,bg='#d6efe9').place(x=250,y=20)
    c.mainloop()

#main page
def main_page():
    global b  
    b=Tk()
    b.title("The Maze Bank")
    b.geometry("890x450")
    b.resizable(False,False)
    c3=Canvas(b,height=90,width=1260,bg="#1b6535").pack()
    c4=Canvas(b,bg="#a8c66c",height=650,width=1250).place(x=0,y=92)
    l7=Label(b,text="THE MAZE BANK",bg='#1b6535',font=('Harrington',50)).place(x=165,y=5)
    l8=Label(b,text="Welcome to the application of The Maze Bank.",font=("Arial Black",20),bg="#a8c66c").place(x=107,y=97)
    b5=Button(b,text="Login",bg="#a9c0a6",command=login,padx=100,pady=100,font=("Be Bold",26)).place(x=100,y=165)
    b6=Button(b,text="New user",bg="#a9c0a6",command=create,padx=70,pady=100,font=("Be Bold",26)).place(x=500,y=165)
    b.mainloop()


#Logout
def logout():
    ask1=messagebox.askquestion("Logout", "Are you want to logout?")
    if ask1=="yes":
        root.withdraw()
        main_page()
    else :
        pass

#add money logic
def addpage1():
    try:
        global ad
        ad=int(e7.get())
        sql7 = f"SELECT balance FROM {dn} where id={con11}"
        c1.execute(sql7)
        result6 = c1.fetchall()
        con6=result6[0]
        con7=con6[0]
        if ad>0:
            ev=eval(f"{con7}+{ad}")
            
            sql8 = f"INSERT INTO {dn} (id,date,amount,reason,balance) VALUES (%s,%s,%s,%s,%s)"
            val2 = (f'{con11+1}',f'{ty}',f'{ad}','Money added',f'{ev}')
            c1.execute(sql8, val2)
            mydb.commit()

            sql9= f"UPDATE login SET money = '{ev}' WHERE username = '{dn}'"
            c1.execute(sql9)
            mydb.commit()
            messagebox.showinfo("Info","Money added to your balance")
            d.withdraw()
            home()
        else:
            messagebox.showerror("error","can't enter a negative value or 0")
    except ValueError:
        messagebox.showerror("error","enter only number")

#withdrawl money logic
def withdrawlpage1():
    try:
        av=int(e8.get())

        if av<con9 and av>0:
            ev=eval(f"{con9}-{av}")

            sql11 = f"INSERT INTO {dn} (id,date,amount,reason,balance) VALUES (%s,%s, %s,%s,%s)"
            val3 = (f'{con11+1}',f'{ty}', f'{av}','Money withdrawl',f'{ev}')
            c1.execute(sql11, val3)
            mydb.commit()

            sql12= f"UPDATE login SET money = '{ev}' WHERE username = '{dn}'"
            c1.execute(sql12)
            mydb.commit()
            messagebox.showinfo("Info","Money withdrawl from your balance")
            e.withdraw()
            home()
        elif av<0:
            messagebox.showerror("Error","can't enter a negative value or 0") 
        else:
            messagebox.showerror("Error","not enough money in your account  ") 
    except ValueError:
            messagebox.showerror("error","enter only number")

#transfer money logic
def transfer1():
    try:
        ab=int(e9.get())
        af=int(e10.get())

        try:
            sql13 = f"SELECT number FROM login Where number='{ab}'"
            c1.execute(sql13)
            result8 = c1.fetchall()
            con12=result8[0]
            con13=int(con12[0])

            
        
            if ab==con13 and af<con9 and af>0:
                #reciver username
                sql14 = f"SELECT username FROM login Where number='{ab}'"
                c1.execute(sql14)
                result9 = c1.fetchall()
                con14=result9[0]
                con15=con14[0]
                print(con15)

                sql19 = f"SELECT id FROM {con15} ORDER BY id desc LIMIT 0, 1"
                c1.execute(sql19)
                result12 = c1.fetchall()
                con20=result12[0]
                con21=con20[0]

                #sender
                sql15 = f"SELECT money FROM login Where username='{dn}'"
                c1.execute(sql15)
                result10 = c1.fetchall()
                con16=result10[0]
                con17=con16[0]
                #reciver
                sql16 = f"SELECT money FROM login Where username='{con15}'"
                c1.execute(sql16)
                result11 = c1.fetchall()
                con18=result11[0]
                con19=con18[0]

                et=eval(f"{con17}-{af}")
                et1=eval(f"{con19}+{af}")

                sql17 = f"INSERT INTO {dn} (id,date,amount,reason,balance) VALUES (%s,%s, %s,%s,%s)"
                val4 = (f'{con11+1}',f'{ty}', f'{af}','Money transferd',f'{et}')
                c1.execute(sql17, val4)
                mydb.commit()

                sql18 = f"INSERT INTO {con15} (id,date,amount,reason,balance) VALUES (%s,%s, %s,%s,%s)"
                val5 = (f'{con21+1}',f'{ty}', f'{af}','Money transferd',f'{et1}')
                c1.execute(sql18, val5)
                mydb.commit()

                sql19= f"UPDATE login SET money = '{et}' WHERE username = '{dn}'"
                c1.execute(sql19)
                mydb.commit()

                sql20= f"UPDATE login SET money = '{et1}' WHERE username = '{con15}'"
                c1.execute(sql20)
                mydb.commit()

                messagebox.showinfo("info","Money has transfered")
                f.withdraw()
                home()
            elif af<0:
                messagebox.showerror("Error","can't enter a negative value or 0")
            else :
                messagebox.showerror("error","entered account no. is wrong")
            
        except IndexError:
            messagebox.showerror("Error","entered account no. is wrong!!")

    except ValueError:
        messagebox.showerror("Error","entered wrong credentials!!")

#add money
def addpage():
    global d
    d=Tk()
    d.geometry("900x300")
    d.title("Add money")
    d.resizable(FALSE,FALSE)
    root.withdraw()
    c7=Canvas(d,height=90,width=1260,bg="#1b6535").pack()
    c8=Canvas(d,bg="#a8c66c",height=650,width=1250).place(x=0,y=92)
    l9=Label(d,text="THE MAZE BANK",bg='#1b6535',font=('Harrington',50)).place(x=185,y=5)
    b12=Button(d,width=7,text="Back",relief="groove",bg="#a7beae",pady=8,command=back2)
    b12.place(x=827,y=28)
    l19=Label(d,text="Add Money",font="arial 34 underline",bg="#a8c66c")
    l19.place(x=308,y=120)
    
    global e7
    e7=Entry(d,width=55)
    e7.place(x=255,y=195)
    b13=Button(d,padx=40,pady=7,text="Add money to balance",command=addpage1,bg="#daf2dc").place(x=320,y=230)
    d.mainloop()


#withdrawl money
def withdrawl():
    global e
    e=Tk()
    e.geometry("900x300")
    e.title("Withdrawl money")
    e.resizable(FALSE,FALSE)
    root.withdraw()
    c9=Canvas(e,height=90,width=1260,bg="#1b6535").pack()
    c10=Canvas(e,bg="#a8c66c",height=650,width=1250).place(x=0,y=92)
    l20=Label(e,text="THE MAZE BANK",bg='#1b6535',font=('Harrington',50)).place(x=185,y=5)
    b14=Button(e,width=7,text="Back",relief="groove",bg="#a7beae",pady=8,command=back3)
    b14.place(x=827,y=28)
    l21=Label(e,text="Withdrawl Money",font="arial 34 underline",bg="#a8c66c")
    l21.place(x=275,y=120)
    global e8
    e8=Entry(e,width=55)
    e8.place(x=275,y=195)
    b15=Button(e,padx=40,pady=7,text="withdrawl money from balance",command=withdrawlpage1,bg="#daf2dc").place(x=320,y=230)
    e.mainloop()



#transfer money
def transfer():
    global f
    f=Tk()
    f.geometry("900x450")
    f.title("Transfer money")
    f.resizable(FALSE,FALSE)
    root.withdraw()
    c9=Canvas(f,height=90,width=1260,bg="#1b6535").pack()
    c10=Canvas(f,bg="#a8c66c",height=650,width=1250).place(x=0,y=92)
    l20=Label(f,text="THE MAZE BANK",bg='#1b6535',font=('Harrington',50)).place(x=185,y=5)
    b14=Button(f,width=7,text="Back",relief="groove",bg="#a7beae",pady=8,command=back4)
    b14.place(x=827,y=28)
    l21=Label(f,text="transfer Money",font="arial 34 underline",bg="#a8c66c")
    l21.place(x=285,y=105)
    l22=Label(f,text="account number",font="arial 30 ",bg="#a8c66c").place(x=300,y=160)
    global e9
    e9=Entry(f,width=55)
    e9.place(x=280,y=220)
    l23=Label(f,text="Money amount",font="arial 30 ",bg="#a8c66c").place(x=300,y=250)
    global e10
    e10=Entry(f,width=55)
    e10.place(x=280,y=305)
    b15=Button(f,padx=40,pady=7,text="transfer money from balance",command=transfer1,bg="#daf2dc").place(x=320,y=340)
    f.mainloop()


def history():
    global g
    g=Tk()
    g.geometry("900x500")
    g.title("history")
    g.resizable(FALSE,TRUE)
    root.withdraw()
    c11=Canvas(g,height=90,width=1260,bg="#1b6535").pack()
    c12=Canvas(g,bg="#a8c66c",height=1800,width=1250)
    c12.place(x=0,y=92)
    l24=Label(g,text="THE MAZE BANK",bg='#1b6535',font=('Harrington',50)).place(x=185,y=5)  
    l25=Label(g,text="S.No.",font="arial 30 ",bg="#a8c66c").place(x=20,y=120)
    l26=Label(g,text="date",font="arial 30 ",bg="#a8c66c").place(x=180,y=120)
    l27=Label(g,text="amount",font="arial 30 ",bg="#a8c66c").place(x=340,y=120)
    l28=Label(g,text="description",font="arial 30 ",bg="#a8c66c").place(x=505,y=120)
    l29=Label(g,text="Balance",font="arial 30 ",bg="#a8c66c").place(x=710,y=120)
    b16=Button(g,width=7,text="Back",relief="groove",bg="#a7beae",pady=8,command=back5)
    b16.place(x=827,y=28)
#scroll bar
    scrollbar = Scrollbar(g)
    scrollbar.pack( side = RIGHT, fill = Y )
    scrollbar.config(command=c12.yview)
    c12.config(yscrollcommand=scrollbar.set)
    c12.pack(expand=True,side=LEFT,fill=BOTH)


    sql21 = f"SELECT id FROM {dn}"
    c1.execute(sql21)
    result12 = c1.fetchall()
    
    k=180
    for x in result12:
        con20=x[0]
        l30=Label(g,text=f"{con20}",font="arial 16 ",bg="#a8c66c").place(x=50,y=k)
        k=k+40
    
    sql22 = f"SELECT date FROM {dn}"
    c1.execute(sql22)
    result13 = c1.fetchall()
    
    l=180
    for y in result13:
        con21=y[0]
        l31=Label(g,text=f"{con21}",font="arial 16 ",bg="#a8c66c").place(x=170,y=l)
        l=l+40

    sql23 = f"SELECT amount FROM {dn}"
    c1.execute(sql23)
    result14 = c1.fetchall()
    
    m=180
    for z in result14:
        con22=z[0]
        l31=Label(g,text=f"{con22}",font="arial 16 ",bg="#a8c66c").place(x=380,y=m)
        m=m+40

    sql24 = f"SELECT reason FROM {dn}"
    c1.execute(sql24)
    result15 = c1.fetchall()
    
    n=180
    for z in result15:
        con23=z[0]
        l31=Label(g,text=f"{con23}",font="arial 16 ",bg="#a8c66c").place(x=520,y=n)
        n=n+40
    
    sql25 = f"SELECT balance FROM {dn}"
    c1.execute(sql25)
    result16 = c1.fetchall()
    
    p=180
    for q in result16:
        con24=q[0]
        l31=Label(g,text=f"{con24}",font="arial 16 ",bg="#a8c66c").place(x=740,y=p)
        p=p+40
        
    g.mainloop()
    
#account details
def home():
    global root
    root=Tk()
    root.title("HOME")
    root.geometry("650x600")
    root.resizable(FALSE,FALSE)
    c5=Canvas(root,height=90,width=1260,bg="#1b6535").pack()
    c6=Canvas(root,bg="#a8c66c",height=650,width=1250).place(x=0,y=92)
    l18=Label(root,text="THE MAZE BANK",bg='#1b6535',font=('Harrington',50)).place(x=50,y=5)

    global con11
    sql14 = f"SELECT id FROM {dn} ORDER BY id desc LIMIT 0, 1"
    c1.execute(sql14)
    result10 = c1.fetchall()
    con10=result10[0]
    con11=con10[0]

    global con9
    sql10 = f"SELECT balance FROM {dn} where id={con11} "
    c1.execute(sql10)
    result7 = c1.fetchall()
    con8=result7[0]
    con9=int(con8[0])

    
#logout,home button
    b8=Button(root,width=6,text="Logout",border=5,relief="groove",bg="#FFA500",command=logout)
    b8.place(x=585,y=110)
#account number
    sql3 = f"SELECT number FROM login Where username='{dn}'"
    c1.execute(sql3)
    result3 = c1.fetchall()
    con=result3[0]
    con1=(con[0])
#account holder
    sql4 = f"SELECT name FROM login Where username='{dn}'"
    c1.execute(sql4)
    result4 = c1.fetchall()
    con2=result4[0]
    con3=str(con2[0]).title()
#money amount
    sql5 = f"SELECT money FROM login Where username='{dn}'"
    c1.execute(sql5)
    result5 = c1.fetchall()
    con4=result5[0]
    con5=(con4[0])
#labels
    l10=Label(root,text="ACCOUNT",font="arial 34 underline",bg="#a8c66c").place(x=210,y=120)
    l11=Label(root,text="Account holder",font="arial 20 underline",bg="#a8c66c").place(x=40,y=190)
    l12=Label(root,text=f"{con3} ",font=("arial",24),bg="#a8c66c").place(x=45,y=240)
    l13=Label(root,text="Account number",font="arial 20 underline",bg="#a8c66c").place(x=415,y=190)
    l14=Label(root,text=f"{con1} ",font=("arial",24),bg="#a8c66c").place(x=425,y=240)
    l15=Label(root,text="Balance",font="arial 20 underline",bg="#a8c66c").place(x=260,y=300)
    l16=Label(root,text="Rs",font=("arial",24),bg="#a8c66c").place(x=260,y=350)
    l17=Label(root,text=f"{con5} ",font=("arial",24),bg="#a8c66c").place(x=305,y=350)
#buttons
    b9=Button(root,text="Add money",width=27,command=addpage,pady=10,bg="#daf2dc").place(x=100,y=430)
    b10=Button(root,text="Withdrawl money",width=27,command=withdrawl,pady=10,bg="#daf2dc").place(x=350,y=430)
    b11=Button(root,text="Tranfer money",width=27,command=transfer,pady=10,bg="#daf2dc").place(x=100,y=500)
    b12=Button(root,text="history",width=27,command=history,pady=10,bg="#daf2dc").place(x=350,y=500)
    root.mainloop()

main_page()




