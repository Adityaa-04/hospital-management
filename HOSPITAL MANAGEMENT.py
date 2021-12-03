import pyttsx3
from prettytable import PrettyTable
from prettytable import from_db_cursor
from datetime import datetime
from datetime import date
import random
print("..................WELCOME TO SUNSHINE'S HOSPITAL..................")
A=datetime.now()
print(A.strftime("               %B %d,%Y %I:%M%p   %A"))
print()
print()
def clr():
      print ('\n'*2)
def clr1():
      print ('\n'*1)
def clr3():
      print ('\n'*3)
def empatient():
      global c1
      b=1;
      while b==1:
            print("====================================")
            print("*ENTER 1 IF YOU ARE AN EMPLOYEE")
            print("*ENTER 2 IF YOU ARE A PATIENT")
            print("====================================")
            print()
            user=int(input("Please Enter Your Response:"))
            if user==1:
                  c1=1
                  clr1()
                  open1()
            elif user==2:
                  c1=0
                  clr1()
                  patient()
                  break

def yupp():
      en = pyttsx3.init()
      en.say("WELCOME TOO SUNSHINE HOSPITAL")
      en.runAndWait()
      empatient()

def open2():
      open1()
      
def open1():
      a="aditya"
      b="******"
      employee=input("EMPLOYEE ID:")
      password=input("PASSWORD:")  
      if employee==a and password==b:
            print("LOG-IN SUCCESSFUL")
            clr1()
            menu()
      elif "a!=aditya":
            print("INCORRECT ID OR PASSWORD")
            print("TRY AGAIN")
            clr1()
            open1()
            
def patient():
      d=1
      while d==1:
            print("ENTER 1 FOR APPOINTMENT")
            print("ENTER 2 FOR DIAGONISTIC TEST")
            print("ENTER 3 FOR TEST REPORT COLLECTION") 
            print("ENTER 4 LOG-OUT")
            print()
            choicee=int(input("Enter Your Choice:"))
            if choicee==1:
                  clr1()
                  appointment()
            elif choicee==2:
                  clr1()
                  diagonistic()
            elif choicee==3:
                  clr1()
                  report()
            elif choicee==4:
                  clr1()
                  empatient()
            else:
                  print("wrong input")
                  break
            
def table4():
      import mysql.connector
      mydb=mysql.connector.connect(host="localhost",user="root",passwd="aditya"\
                                   ,database='Sunshine_hospital')
      mycursr=mydb.cursor()
      mycursr.execute("create table if not exists report(Test_Type varchar(70) \
                           ,Report_Status varchar(15),Amount int);")
      print("Table Created")
      
def addrecord2():
      import mysql.connector
      mydb=mysql.connector.connect(host="localhost",user="root",passwd="aditya"\
                                   ,database='Sunshine_hospital')
      mycursor=mydb.cursor()
      query=("insert into report(Test_Type,Report_Status,Amount) \
                                    values('Amylase Test','PREPARED',500),\
                                   ('ANA(Antinuclear Antibody','PREPARED',700),\
                                   ('Blood Sugar test)','NOT PREPARED',1000),\
                                   ( 'CT Scans','PREPARED',2000),\
                                   ('CBC (Complete Blood Count)','PREPARED',800),\
                                   ('CRP (C – Reactive protein)','NOT PREPARED',950),\
                                   ('Hemoglobin A1C (HbA1c)','PREPARED',450),\
                                   ('MRI Scans','NOT PREPARED',5000),\
                                   ('PET Scans','PREPARED',4000),\
                                   ('Thyroid Function test – TSH, T3 and T4','PREPARED',1750);")
      mycursor.execute(query)
      mydb.commit()
      mydb.close()
      print("Data Successfully Installed")
      
def table5():
      import mysql.connector
      mydb=mysql.connector.connect(host="localhost",user="root",passwd="aditya",\
                                   database='Sunshine_hospital')
      mycursr=mydb.cursor()
      mycursr.execute(" create view view_report as select diagonostic.*,report.Report_Status ,\
                                                       report.Amount from diagonostic,\
                                                       report where diagonostic.Test_Type=\
                                                       report.Test_Type;")
      print("Table Created")
      
def report():
      import mysql.connector
      x=PrettyTable()
      mydb=mysql.connector.connect(host="localhost",user="root",passwd="aditya",\
                                   database="Sunshine_hospital") 
      mycursr=mydb.cursor()
      a=input("Enter The Patient ID:")
      mycursr.execute("select * from view_report where patient_id=%s;",(a,))
      mytable=from_db_cursor(mycursr)
      print(mytable)
      mydb.close()
      print("YOU CAN COLLECT YOUR REPORT FROM THE RECEPTION DESK")
      clr()
      
def diagonistic():
      global a,b,c,d,e,f
      import mysql.connector
      mydb=mysql.connector.connect(host="localhost",user="root",passwd="aditya"\
                                   ,database='Sunshine_hospital')
      mycursor=mydb.cursor()
      file = open("id.txt","r")
      z=file.read()
      ino=(z[2:6])
      ino=int(ino)
      if int(ino)==9999:
          if (z[1])=="Z":
              alpha=ord(z[0])+1
              newnumber=chr(alpha)+'A'+'0000'
              print(newnumber)
          else:
              gama=ord(z[1])+1
              newnumber=z[0]+chr(gama)+'0000'
              print(newnumber)
      else:
          beta=int(ino)+1
          beta=str(beta)
          newnumber=z[0:2]+beta.zfill(3)
        
      file.close()
      file = open("id.txt","w")
      file.write(newnumber)
      file.close()
      a=newnumber
      b=input("Enter The Patient Name:")
      c=input("Enter Gender:")
      d=input("Enter Age:")
      e=input("Enter City:")
      f=input("Enter Address:")
      g=input("Enter The Phone Number:")
      today = date.today()
      h=today.strftime("%d/%m/%y")
      print()
      print("Choose The Type Of Test Among The Following:")
      print()
      print("1.Amylase Test")
      print("2.ANA(Antinuclear Antibody)")
      print("3.Blood Sugar test ")
      print("4.CT Scans ")
      print("5.CBC (Complete Blood Count) ")
      print("6.CRP (C – Reactive protein)")
      print("7.Hemoglobin A1C (HbA1c)")
      print("8.MRI Scans")
      print("9.PET Scans")
      print("10.Thyroid Function test – TSH, T3 and T4")
      t=int(input("Enter your choice:"))
      if t==1:
            clr1()
            print("===============================")
            print("Total Amount:1700")
            print("TEST NO:",random.randint(0,35))
            print("===============================")
            clr3()
            i="Amylase Test"
            query=("insert into diagonostic values(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
            data=(a,b,c,d,e,f,g,h,i)
            mycursor.execute(query,data)
            mydb.commit()
            mydb.close()
      elif t==2:
            clr1()
            print("===============================")
            print("Total Amount:1700")
            print("TEST NO:",random.randint(0,35))
            print("===============================")
            clr3()
            i="ANA(Antinuclear Antibody"
            query=("insert into diagonostic values(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
            data=(a,b,c,d,e,f,g,h,i)
            mycursor.execute(query,data)
            mydb.commit()
            mydb.close()
      elif t==3:
            clr1()
            print("===============================")
            print("Total Amount:1700")
            print("TEST NO:",random.randint(0,35))
            print("===============================")
            clr3()
            i="Blood Sugar test"
            query=("insert into diagonostic values(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
            data=(a,b,c,d,e,f,g,h,i)
            mycursor.execute(query,data)
            mydb.commit()
            mydb.close()
      elif t==4:
            clr1()
            print("===============================")
            print("Total Amount:1700")
            print("TEST NO:",random.randint(0,35))
            print("===============================")
            clr3()
            i="CT Scans"
            query=("insert into diagonostic values(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
            data=(a,b,c,d,e,f,g,h,i)
            mycursor.execute(query,data)
            mydb.commit()
            mydb.close()
      elif t==5:
            clr1()
            print("===============================")
            print("Total Amount:1700")
            print("TEST NO:",random.randint(0,35))
            print("===============================")
            clr3()
            i="CBC (Complete Blood Count)"
            query=("insert into diagonostic values(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
            data=(a,b,c,d,e,f,g,h,i)
            mycursor.execute(query,data)
            mydb.commit()
            mydb.close()
      elif t==6:
            clr1()
            print("===============================")
            print("Total Amount:1700")
            print("TEST NO:",random.randint(0,35))
            print("===============================")
            clr3()
            i="CRP (C – Reactive protein)"
            query=("insert into diagonostic values(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
            data=(a,b,c,d,e,f,g,h,i)
            mycursor.execute(query,data)
            mydb.commit()
            mydb.close()
      elif t==7:
            clr1()
            print("===============================")
            print("Total Amount:1700")
            print("TEST NO:",random.randint(0,35))
            print("===============================")
            clr3()
            i="Hemoglobin A1C (HbA1c)"
            query=("insert into diagonostic values(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
            data=(a,b,c,d,e,f,g,h,i)
            mycursor.execute(query,data)
            mydb.commit()
            mydb.close()
      elif t==8:
            clr1()
            print("===============================")
            print("Total Amount:1700")
            print("TEST NO:",random.randint(0,35))
            print("===============================")
            clr3()
            i="MRI Scans"
            query=("insert into diagonostic values(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
            data=(a,b,c,d,e,f,g,h,i)
            mycursor.execute(query,data)
            mydb.commit()
            mydb.close()
      elif t==9:
            clr1()
            print("===============================")
            print("Total Amount:1700")
            print("TEST NO:",random.randint(0,35))
            print("===============================")
            clr3()
            i="PET Scans"
            query=("insert into diagonostic values(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
            data=(a,b,c,d,e,f,g,h,i)
            mycursor.execute(query,data)
            mydb.commit()
            mydb.close()
      elif t==10:
            clr1()
            print("===============================")
            print("Total Amount:1700")
            print("TEST NO:",random.randint(0,35))
            print("===============================")
            clr3()
            i="Thyroid Function test – TSH, T3 and T4"
            query=("insert into diagonostic values(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
            data=(a,b,c,d,e,f,g,h,i)
            mycursor.execute(query,data)
            mydb.commit()
            mydb.close()
      else:
                clr()
                print("Wrong Input")
def table3():
      import mysql.connector
      mydb=mysql.connector.connect(host="localhost",user="root",passwd="aditya",\
                                   database='Sunshine_hospital')
      mycursr=mydb.cursor()
      mycursr.execute("create table diagonostic\
                           ( Patient_ID varchar(30) primary key,\
                            Patient_Name varchar(30),Gender char(10),\
                            Age varchar(30),City varchar(30),\
                             Address varchar(30),Phone_Number int(11)\
                             ,Date_Of_Test varchar(10),\
                              Test_Type varchar(40));")
      print("table created")
def display2():
      import mysql.connector
      x=PrettyTable()
      mydb=mysql.connector.connect(host="localhost",user="root",passwd="aditya",\
                                   database="Sunshine_hospital") 
      mycursor=mydb.cursor()
      mycursor.execute("select*from diagonostic")
      mytable=from_db_cursor(mycursor)
      print(mytable)
      mydb.close()
      
def appointment():
      global a,b,c,d,e,f,c1
      import mysql.connector
      mydb=mysql.connector.connect(host="localhost",user="root",passwd="aditya",\
                                   database='Sunshine_hospital')
      mycursor=mydb.cursor()
      file = open("id.txt","r")
      z=file.read()
      ino=(z[2:6])
      ino=int(ino)
      if int(ino)==9999:
          if (z[1])=="Z":
              alpha=ord(z[0])+1
              newnumber=chr(alpha)+'A'+'0000'
              print(newnumber)
          else:
              gama=ord(z[1])+1
              newnumber=z[0]+chr(gama)+'0000'
              print(newnumber)
      else:
          beta=int(ino)+1
          beta=str(beta)
          newnumber=z[0:2]+beta.zfill(3)
        
      file.close()
      file = open("id.txt","w")
      file.write(newnumber)
      file.close()
      print("ENTER THE FOLLOWING DETAILS")
      a=newnumber
      b=input("Patient's Name:")
      c=input("Age:")
      d=input("Gender:")
      e=input("City:")
      f=input("Address:")
      g=input("Phone Number:")
      today = date.today()
      h=today.strftime("%d/%m/%y")
      clr1()
      print("Select The Doctor You Want To Visit:")
      print("1.ENT")
      print("2.Orthhopedic")
      print("3.Dermatologist")
      print("4.Cardiologist")
      print("5.Endocrinologist")
      print("6.General Physician")
      print("7.Gastroenterologist")
      print("8.Neurologist")
      print("9.Ophthalmologist")
      print("10.Psychiatrist")
      print("11.Dentist")
      print("12.Pediatrician")
      print("13.Gynaecologist")
      v=int(input("Enter Your Choice:"))
      if v==1:
            clr()
            print("===============================")
            print("APPOINTMENT NO:",random.randint(1,45))
            print("Doctor's Name: Dr Sanjay")
            print("TIMINGS 5:00pm-7:00pm Daily")
            print("===============================")
            i='ent'
            query=("insert into patient values(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
            data=(a,b,c,d,e,f,g,h,i)
            mycursor.execute(query,data)
            mydb.commit()
            mydb.close()
            clr1()
            if c1==1:
                  option()
      elif v==2:
            clr()
            print("===============================")
            print("APPOINTMENT NO:",random.randint(1,45))
            print("Doctor's Name: Dr Mishra")
            print("TIMINGS 6:00pm-9:00pm (wed,sat)")
            print("===============================")
            i='Orthhopedic'
            query=("insert into patient values(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
            data=(a,b,c,d,e,f,g,h,i)
            mycursor.execute(query,data)
            mydb.commit()
            mydb.close()
            clr()
            if c1==1:
                  option()
      elif v==3:
            clr()
            print("===============================")
            print("APPOINTMENT NO:",random.randint(1,45))
            print("Doctor's Name: Dr Sinha")
            print("TIMINGS 7:00pm-9:00pm Daily")
            print("===============================")
            i='Dermatologists'
            query=("insert into patient values(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
            data=(a,b,c,d,e,f,g,h,i)
            mycursor.execute(query,data)
            mydb.commit()
            mydb.close()
            clr()
            if c1==1:
                  option()
      elif v==4:
            clr()
            print("===============================")
            print("APPOINTMENT NO:",random.randint(1,45))
            print("Doctor's Name: Dr Sengupta")
            print("TIMINGS 6:00pm-8:00pm (mon,tue)")
            print("===============================")
            i='Cardiologists'
            query=("insert into patient values(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
            data=(a,b,c,d,e,f,g,h,i)
            mycursor.execute(query,data)
            mydb.commit()
            mydb.close()
            clr()
            if c1==1:
                  option()
      elif v==5:
            clr()
            print("===============================")
            print("APPOINTMENT NO:",random.randint(1,45))
            print("Doctor's Name: Dr Das")
            print("TIMINGS 12:00pm-3:00pm (wed,thu)")
            print("===============================")
            i='Endocrinologists'
            query=("insert into patient values(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
            data=(a,b,c,d,e,f,g,h,i)
            mycursor.execute(query,data)
            mydb.commit()
            mydb.close()
            clr()
            if c1==1:
                  option()
      elif v==6:
            clr()
            print("===============================")
            print("APPOINTMENT NO:",random.randint(1,45))
            print("Doctor's Name: Dr sharma")
            print("TIMINGS 5:00pm-7:00pm (fri,sat)")
            print("===============================")
            i='General Physician'
            query=("insert into patient values(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
            data=(a,b,c,d,e,f,g,h,i)
            mycursor.execute(query,data)
            mydb.commit()
            mydb.close()
            clr()
            if c1==1:
                  option()
      elif v==7:
            clr()
            print("===============================")
            print("APPOINTMENT NO:",random.randint(1,45))
            print("Doctor's Name: Dr Kumari")
            print("TIMINGS 4:00pm-6:00pm Daily")
            print("===============================")
            i='Gastroenterologists'
            query=("insert into patient values(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
            data=(a,b,c,d,e,f,g,h,i)
            mycursor.execute(query,data)
            mydb.commit()
            mydb.close()
            clr()
            if c1==1:
                  option()
      elif v==8:
            clr()
            print("===============================")
            print("APPOINTMENT NO:",random.randint(1,45))
            print("Doctor's Name: Dr Agarwal")
            print("TIMINGS 10:00am-12:00pm Daily")
            print("         8.00pm-10.00pm      ")
            print("===============================")
            i='Neurologists'
            query=("insert into patient values(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
            data=(a,b,c,d,e,f,g,h,i)
            mycursor.execute(query,data)
            mydb.commit()
            mydb.close()
            clr()
            if c1==1:
                  option()
      elif v==9:
            clr()
            print("===============================")
            print("APPOINTMENT NO:",random.randint(1,45))
            print("Doctor's Name: Dr Mohpal")
            print("TIMINGS 5:00pm-7:00pm Daily")
            print("===============================")
            i='Ophthalmologist'
            query=("insert into patient values(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
            data=(a,b,c,d,e,f,g,h,i)
            mycursor.execute(query,data)
            mydb.commit()
            mydb.close()
            clr()
            if c1==1:
                  option()
      elif v==10:
            clr()
            print("===============================")
            print("APPOINTMENT NO:",random.randint(1,45))
            print("Doctor Name: Dr Attri")
            print("TIMINGS 5:00pm-7:00pm (Thrs,Fri)")
            print("===============================")
            i='Psychiatrist'
            query=("insert into patient values(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
            data=(a,b,c,d,e,f,g,h,i)
            mycursor.execute(query,data)
            mydb.commit()
            mydb.close()
            clr()
            if c1==1:
                  option()
      elif v==11:
            clr()
            print("===============================")
            print("APPOINTMENT NO:",random.randint(1,45))
            print("Doctor's Name: Dr singh")
            print("TIMINGS 5:00pm-8:00pm Daily")
            print("===============================")
            i='Dentist'
            query=("insert into patient values(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
            data=(a,b,c,d,e,f,g,h,i)
            mycursor.execute(query,data)
            mydb.commit()
            mydb.close()
            clr()
            if c1==1:
                  option()
      elif v==12:
            clr()
            print("===============================")
            print("APPOINTMENT NO:",random.randint(1,45))
            print("Doctor's Name: Dr prasad")
            print("TIMINGS 8:00pm-10:00pm (mon,,thu)")
            print("===============================")
            i='Pediatrician'
            query=("insert into patient values(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
            data=(a,b,c,d,e,f,g,h,i)
            mycursor.execute(query,data)
            mydb.commit()
            mydb.close()
            clr()
            if c1==1:
                  option()
      elif v==13:
            clr()
            print("===============================")
            print("APPOINTMENT NO:",random.randint(1,45))
            print("Doctor's Name: Dr chatterjee")
            print("TIMINGS 10:00am-12:00pm Daily")
            print("        6:00pm-8:00pm")
            print("===============================")
            i='Gynecologist'
            query=("insert into patient values(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
            data=(a,b,c,d,e,f,g,h,i)
            mycursor.execute(query,data)
            mydb.commit()
            mydb.close()
            clr()
            if c1==1:
                  option()
      else:
            clr()
            print("wrong choice")

def  table2():
      
      import mysql.connector
      mydb=mysql.connector.connect(host="localhost",user="root",passwd="aditya",\
                                   database='Sunshine_hospital')
      mycursr=mydb.cursor()
      mycursr.execute("create table patient( Patient_ID varchar(30) primary key,\
                                          Patient_Name varchar(30),Age int(3)\
                                          ,Gender varchar(10),City varchar(30)\
                                          ,Address varchar(30),\
                                      Phone_Number int(10),\
                                      Date_Of_Joining varchar(30)\
                                ,Department char(30));")
      

def displaya1():
      import mysql.connector
      x=PrettyTable()
      mydb=mysql.connector.connect(host="localhost",user="root",passwd="aditya",\
                                   database="Sunshine_hospital") 
      mycursor=mydb.cursor()
      mycursor.execute("select*from patient")
      mytable=from_db_cursor(mycursor)
      print(mytable)
      mydb.close()

def menu():
     c=1;
     while c==1:
             
             print()
             print("ENTER 1 FOR NEW APPOINTMENT")
             print("ENTER 2 TO GO TO THE PATIENT PORTAL")
             print("ENTER 3 TO VIEW THE PATIENTS' RECORD")                                                                      
             print("ENTER 4 TO VIEW THE DIAGONOSTIC LIST")
             print("ENTER 5 TO SEARCH FOR A PATIENT'S RECORD")
             print("ENTER 6 TO UPDATE A PATIENT'S RECORD")
             print("ENTER 7 TO DELETE A PATIENT'S RECORD")
             print("ENTER 8 TO VIEW THE LIST OF DOCTORS")
             print("ENTER 9 TO VIEW THE REPORT OF A PATIENT")
             print("ENTER 10 TO LOG-OUT")
             clr1()
             choice=int(input("Enter Your Choice:"))
             if choice==1:
                   clr1()
                   appointment()
                   clr1()
             elif choice==2:
                   patient()
                   clr1()
             elif choice==3:
                   displaya1()
                   clr1()
             elif choice==4:
                   display2()
                   clr1()
             elif choice==5:
                   clr1()
                   search()
                   clr1()
             elif choice==6:
                   updaterecord()
                   clr1()
             elif choice==7:
                   deleterecord()
                   clr1()
             elif choice==8:
                   doctor()
                   clr1()
             elif choice==9:
                   report()
                   clr1()
             elif choice==10:
                        clr1()
                        print("THANK YOU!!")
                        print("Application closed")
                        clr()
                        empatient()
                        break
                        
             c=int(input("Enter 1 To Continue....."))
def option():
      global c1
      a=1
      while a==1:
            print("ENTER 1 TO CONTINUE")
            print("ENTER 2 TO GO PATIENT PORTAL")
            print("ENTER 3 TO LOG-OUT")
            a=int(input("Enter Your Choice:"))
            if a==1:
                  clr1()
                  menu()
            elif a==2:
                  cl=0
                  clr1()
                  patient()
            elif a==3:
                  clr1()
                  empatient()
            else:
                  print("INVALID INPUT")
                  
def  createdatabase():
      import mysql.connector
      mydb=mysql.connector.connect(host="localhost",user="root",passwd="aditya")
      mycursor=mydb.cursor()
      mycursor.execute("create database Sunshine_hospital")
      print("database created")
      
def search():
    c=1
    while c==1:
             print("SEARCH DATA BY THE FOLLOWING:")
             print("                    1* BY PATIENT ID")
             print("                    2* BY NAME")
             print("                    3* BY AGE")
             print("                    4* BY CITY")                                                                      
             print("                    5* BY GENDER")
             print("                    6* BY ADDRESS")
             print("                    7* BY phone number")
             print("                    8* BY DATE_OF JOINING")
             print("                    9* BY DEPARTMENT")
             print("ENTER 10 TO RETURN TO PREVIOUS PAGE")
             clr1()
             c=int(input("Enter Your Choice:"))
             if c==1:
                 search0()
                 clr1()
             elif c==2:
                 search1()
                 clr1()
             elif c==3:
                 search2()
                 clr1()
             elif c==4:
                 search8()
                 clr1()
             elif c==5:
                 search3()
                 clr1()
             elif c==6:
                 search4()
                 clr1()
             elif c==7:
                 search5()
                 clr1()
             elif c==8:
                 search6()
                 clr1()
             elif c==9:
                 search7()
                 clr1()
             elif c==10:
                 menu()
             else:
                 print("INVALID INPUT")
                 
def search0():
      import mysql.connector
      x=PrettyTable()
      mydb=mysql.connector.connect(host="localhost",user="root",passwd="aditya",\
                                   database="Sunshine_hospital") 
      mycursr=mydb.cursor()
      a=input("Enter The Patient ID:")
      mycursr.execute("select * from patient where Patient_ID=%s;",(a,))
      mytable=from_db_cursor(mycursr)
      print(mytable)
      mydb.close()                 
def search1():
      import mysql.connector
      x=PrettyTable()
      mydb=mysql.connector.connect(host="localhost",user="root",passwd="aditya",\
                                   database="Sunshine_hospital") 
      mycursr=mydb.cursor()
      a=input("Enter The Patient Name:")
      mycursr.execute("select * from patient where Patient_Name=%s;",(a,))
      mytable=from_db_cursor(mycursr)
      print(mytable)
      mydb.close()                 
def search2():
      import mysql.connector
      x=PrettyTable()
      mydb=mysql.connector.connect(host="localhost",user="root",passwd="aditya"\
                                   ,database="Sunshine_hospital") 
      mycursr=mydb.cursor()
      a=input("Enter The Patient Age:")
      mycursr.execute("select * from patient where Age=%s;",(a,))
      mytable=from_db_cursor(mycursr)
      print(mytable)
      mydb.close()
def search3():
      import mysql.connector
      x=PrettyTable()
      mydb=mysql.connector.connect(host="localhost",user="root",passwd="aditya"
                                   ,database="Sunshine_hospital") 
      mycursr=mydb.cursor()
      a=input("Enter The Patient Gender:")
      mycursr.execute("select * from patient where Gender=%s;",(a,))
      mytable=from_db_cursor(mycursr)
      print(mytable)
      mydb.close()
def search4():
      import mysql.connector
      x=PrettyTable()
      mydb=mysql.connector.connect(host="localhost",user="root",passwd="aditya",\
                                   database="Sunshine_hospital") 
      mycursr=mydb.cursor()
      a=input("Enter The Patient Address:")
      mycursr.execute("select * from patient where Address=%s;",(a,))
      mytable=from_db_cursor(mycursr)
      print(mytable)
      mydb.close()
def search5():
      import mysql.connector
      x=PrettyTable()
      mydb=mysql.connector.connect(host="localhost",user="root",passwd="aditya",\
                                   database="Sunshine_hospital") 
      mycursr=mydb.cursor()
      a=input("Enter The Patient Phone Number:")
      mycursr.execute("select * from patient where Phone_Number=%s;",(a,))
      mytable=from_db_cursor(mycursr)
      print(mytable)
      mydb.close()      
                 
def search6():
      import mysql.connector
      x=PrettyTable()
      mydb=mysql.connector.connect(host="localhost",user="root",passwd="aditya",\
                                   database="Sunshine_hospital") 
      mycursr=mydb.cursor()
      a=input("Enter The Patient Date_Of_Joining:")
      mycursr.execute("select * from patient where Date_Of_Joining=%s;",(a,))
      mytable=from_db_cursor(mycursr)
      print(mytable)
      mydb.close()
def search7():
      import mysql.connector
      x=PrettyTable()
      mydb=mysql.connector.connect(host="localhost",user="root",passwd="aditya",\
                                   database="Sunshine_hospital") 
      mycursr=mydb.cursor()
      a=input("Enter The Patient Department :")
      mycursr.execute("select * from patient where Department =%s;",(a,))
      mytable=from_db_cursor(mycursr)
      print(mytable)
      mydb.close()
def search8():
      import mysql.connector
      x=PrettyTable()
      mydb=mysql.connector.connect(host="localhost",user="root",passwd="aditya"\
                                   ,database="Sunshine_hospital") 
      mycursr=mydb.cursor()
      a=input("Enter The Patient City:")
      mycursr.execute("select * from patient where City=%s;",(a,))
      mytable=from_db_cursor(mycursr)
      print(mytable)
      mydb.close()      
                          
def updaterecord():
      import mysql.connector
      mydb=mysql.connector.connect(host="localhost",user="root",passwd="aditya",\
                                   database='Sunshine_hospital')
      mycursor=mydb.cursor()
      g=input("Enter The Patient ID To Be Updated:")
      a=input("Enter The Patient Name:")
      b=input("Enter Age:")
      c=input("Enter Gender:")
      d=input("Enter City:")
      e=input("Enter Phone Number:")
      query=("update patient set Patient_Name=%s,Age=%s,gender=%s,city=%s,phone_number=%s \
                                     where patient_id=%s;")
      data=(a,b,c,d,e,g)
      mycursor.execute(query,data)
      mydb.commit()
      mydb.close()
      print("DATA UPDATED SUCCESSFULLY")
def deleterecord():
            import mysql.connector
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="aditya"\
                                         ,database="Sunshine_hospital")
            mycursor=mydb.cursor()
            pid=input("Enter The Patient_ID To Be Deleted:")
            query=("delete from patient where patient_id=%s")
            data=(pid,)
            mycursor.execute(query,data)
            print("DATA DELETED SUCCESSFULLY")
            mydb.commit()
            mydb.close()
def table1():
      import mysql.connector
      mydb=mysql.connector.connect(host="localhost",user="root",passwd="aditya",\
                                   database='Sunshine_hospital')
      mycursr=mydb.cursor()
      mycursr.execute("create table doctor(Doctors_ID varchar(30) primary key,\
                                Doctor_Name varchar(30),Age int(3)\
                                          ,Gender varchar(10),Address varchar(30),\
                                                 Phone_Number int(11),Date_Of_Joining \
                                                 varchar(30)\
                                                                ,Department char(30));")
def addrecord3():
      import mysql.connector
      mydb=mysql.connector.connect(host="localhost",user="root",passwd="aditya",\
                                   database='Sunshine_hospital')
      mycursor=mydb.cursor()
      query=("insert into doctor(doctors_id,doctor_name,age,gender,Address,phone_number,\
                                     date_of_joining,department)\
                                                   values\
         ('DDOO1','Dr Sanjay',37,'MALE','TEEN BATTI',980076543,'27-09-2018','Ent'),\
         ('DDO76','Dr mishra',44,'MALE','SARKAR PARA',987654233,'21-07-2016','Orthhopedic'),\
         ('DDO65','Dr sinha',39,'MALE','JYOTI NAGAR',909876543,'09-01-2017','Dermatologists'),\
         ('DD004','Dr Sengupta',56,'FEMALE','KHAL PARA',912345789,'28-02-2018','Cardiologists'),\
         ('DD032','Dr Das',42,'MALE','PAKURTALA',932145670,'27-05-2018','Endocrinologists'),\
         ('DD023','Dr sharma',41,'MALE','CHECKPOST',919287465,'04-12-2019','General Physician'),\
         ('DD007','Dr Kumari',35,'FEMALE','HAIDAR PARA',659843120,'23-11-2020','Gastroenterologists'),\
         ('DD009','Dr Agarwal',53,'MALE','PUNJABI PARA',796542310,'25-11-2015','Neurologists'),\
         ('DD059','Dr Mohpal',29,'MALE','NORTH CITY',679543120,'19-09-2014','Ophthalmologist'),\
         ('DD087','Dr Attri',33,'FEMALE','SALUGARA',879503421,'12-03-2013','Psychiatrist'),\
         ('DD017','Dr singh',39,'MALE','SALUGARA',908654123,'23-07-2017','Dentist'),\
         ('DD012','Dr prasad',47,'MALE','ASHRAM PARA',900002232,'09-06-2013','Pediatrician'),\
         ('DD093','Dr chatterjee',55,'MALE','UTTRAYAN',800762342,'05-10-2020','Gynecologist');")
      mycursor.execute(query)              
      mydb.commit()
      mydb.close()
            
def doctor():
      import mysql.connector
      x=PrettyTable()
      mydb=mysql.connector.connect(host="localhost",user="root",passwd="aditya",\
                                   database="Sunshine_hospital") 
      mycursor=mydb.cursor()
      mycursor.execute("select*from doctor")
      mytable=from_db_cursor(mycursor)
      print(mytable)
      mydb.close()

#MAIN
      
yupp()



