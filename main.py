#*****************Welcome To THE OTHER SIDE*****************



# Created on:   time: 00:13     Date: 19/7/2021
# Programmer: Himanshi




# Importing Global File For working of font Color in Console/Shell 
import os
os.system("cls")

import re
import json
import copy



# Importing local modules
import color as cl



# Importing local module from package Booking
import super_user as sp
import member as mm





# Function to login both members and superuser
# Runs everytime main.py is executed except once in starting
def login():
    while True:
        
        while True:
            print(cl.blue+'Please choose an option to login:\n\n1. Super User\n\n2. Gym Member\n\n3. Exit'+cl.reset)
            try:
                option= int(input())
                if option in [1,2,3]:
                    break
                else:
                    print(cl.blue+'Please Enter either option 1 or 2'+cl.reset)
                    continue
            except:
                print(cl.blue+'Please enter a Number'+cl.reset)
        
        fp = open('login.json','r')
        content = fp.read()
        fp.close()
        user=json.loads(content)
        
        if option==1:
            print(cl.blue+'Enter your email:')
            email1=input()
            print('Enter your password:'+cl.reset)
            passcode = input()
            superuser = user['super_user']
            if superuser['email']==email1 and superuser['password']==passcode:
                print(cl.green+'Welcome back',superuser['name'],'\n\n\n'+cl.reset)
                # Once password email matches Super_User class object is formed for main menu
                obj = sp.Super_User(superuser)
                obj.main_menu()
            else:
                print(cl.red+'Incorrect Email or password.\n\n\nBYE!!!\n\n\n\n'+cl.reset)

        elif option==2:
            if 'members' in user.keys():
                print('Enter your mobile number:')
                mob=input()
                print('Enter your password:')
                passcode = input()
                if mob in user['members'].keys() and user['members'][mob]['password']==passcode:
                    member = copy.deepcopy(user['members'][mob])
                    print('Welcome Back',member['name'])
                    # Once password mob matches Member class object is formed for main_menu
                    mem = mm.Member(member)
                    mem.main_menu()
                else:
                    print(cl.red+'Incorrect Email or password.\n\n\nBYE!!!\n\n\n\n'+cl.reset)
            else:
                print(cl.red+'No member has joined the gym yet.'+cl.reset)
        
        elif option ==3:
            print(cl.red+'BYE!!\n\n\n'+cl.reset)
            break




# Function to setup the Gym Membership System's Super User Profile.
# This runs once in the starting.
def setup():
    print(cl.gold+'\n\nWelcome to Gym Membership System\n\n\nEasy way to manage your customers\n\n')
    print('We need to setup account for Super User\n\n\nLoading...\n\n\n\n'+cl.reset)
    regx_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'     #Regular Expression to detect correct email format
    regx_pass = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"     #Regular Expression to detect correct password format
    
    while True:
        print(cl.blue+'Enter your email:'+cl.reset)
        email = input()
        if re.match(regx_email,email):
            break
        else:
            print(cl.red+'Enter a valid email Id'+cl.reset)
            continue
    
    while True:
        print(cl.bk_blue+'Enter a password:'+cl.reset)
        password = input()
        if re.match(regx_pass,password):
            break
        else:
            print(cl.red+'Password Quality Low. \n\n\nTry to input: At least 8 characters\nUppercase letters: A-Z\nLowercase letters: a-z\nNumbers: 0-9\nAny of the special characters: @#$%^&+=\n\n\n'+cl.reset)
            continue
    print(cl.blue+'Email and Password setup was Successful.\n\n'+cl.reset)
    
    while True:
        try:
            print(cl.blue+'Personal Details Setup:\n\nEnter your Name:'+cl.reset)
            name=input()
            print(cl.blue+'Enter your Age:'+cl.reset)
            age = int(input())
            if age>150 or age<18:
                print(cl.red+'Not a valid age.\nTry Again'+cl.reset)
                continue
            print(cl.blue+'Enter your mobile number:'+cl.reset)
            mob = int(input())
            if len(str(mob))==10:
                break
            else:
                print(cl.red+'Enter a valid Mobile Number'+cl.reset)
                continue
        except:
            print(cl.red+'Enter a valid digit'+cl.reset)
    
    fp = open('login.json','w')
    Login = {'super_user':{'email':email,'password':password,'name':name,'age':age,'mob':int(mob)}}
    login_dump = json.dumps(Login)
    fp.write(login_dump)            #All info of superuser is written in json format in login.json
    fp.close()
    print(cl.cyan+'Super User Setup Successfull!!\n\n\n'+cl.reset)




#Function to run first time main.py is executed
def gym_membership():
    fp = open('login.json','r') #reading info from login.json file
    d = fp.read()
    fp.close()
    if d:
        login()     
    else:
        setup()     #If login.json is empty then setup SuperUser by setup function
        login()




# Calling the function gym_membership()
gym_membership()
