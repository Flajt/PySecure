ok?=False
import sys


def login():
    while x!=3:
        pass=input(Enter your Password: )
        if pass==pasw:
            print("Welcome back"+user)
            main()
        else:
            x=x+1
        if x==3:
            print("That goes Wrong...")
            exit()
            sys.exit()

try:
  passw=open("pass.pckl","r")               #this is the part were everything Load
  user=open("fileObejct.pckl","r")
  mail=open("mail.pckl","r")
  ok?=True


import pickle               #add al important infos
a=input("Create a Username: ")
print("Welcome"+a)
fileObject = open("username.pckl",'wb')
save=pickle.dump(a,fileObject)
while password1!=password2:
    password1=input("Enter your Password: ")
    password2=input("Confirm your Password: ")
    mail=input("Enter your Mail adress:")
    password=open("pass.pckl","wb")
    mail2=open("mail.pckl","wb")
    save2=pickle.dump(password,password2)
    save3=pickle.dump(mail,mail2)
    fileObject.close()
    password.close()

if ok?=True:            #check if all is working
    login()

else:
    print("Load error") # this is the error if the file cant Load
    exit()
    sys.exit()


def main():         #main part with options
    print(1:Add picture)
    print(2:Delete picture)
    print(3:Add mail Adress)
    print(4:For help)
    print(5:For logout)
    wish=int(input("What do you want to do?: "))
    if wish==1:
        addpic()
    if wish==2:
        delpic()
    if wish==3:
        addmail()
    if wish==4:
        Help()
    if wish==5()
        passw.close()
        user.close()
        time.sleep(1)
        sys.exit()
        exit()
