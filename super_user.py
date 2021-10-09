# Importing files to ne used in class
import json
import color as cl




# Class for all super user functions
class Super_User:


    # init function initialise class object info containing all details of super user
    def __init__(self,info):
        self.info = info

    

    # For CRUD Function on members in Gym
    def member_option(self):
        
        while True:
            print(cl.bold+cl.cyan+'\n\n\n\n1. Create Member\n\n2. View Member\n\n3. Update Member\n\n4. Delete Member\n\n0. Exit\n\n\n'+cl.reset)
            opt = self.num_input()
            if opt == 0:
                break
            
            elif opt == 1:
                while True:
                    fp=open('login.json','r')
                    data=fp.read()
                    data = json.loads(data)
                    fp.close()
                    print(cl.bold+cl.cyan+"\nEnter Member's mobile number:\n\n"+cl.reset)
                    mob = self.num_input()
                    if len(str(mob))!=10:
                        print(cl.red+'\n\nEnter a valid 10 Digit Number\n\n'+cl.reset)
                        continue
                    
                    print(cl.blue+"\n\nEnter Member's email:\n"+cl.reset)
                    email = input()
                    print(cl.blue+"\n\nEnter Member's password:\n"+cl.reset)
                    password = input()
                    print(cl.blue+"\n\nEnter Member's Full Name:\n"+cl.reset)
                    name = input()
                    print(cl.blue+"\n\nEnter Member's Age:\n"+cl.reset)
                    age = self.num_input()
                    if age<15 or age>100:
                        print(cl.red+'\nPlease Enter Valid Input!\n\n'+cl.reset)
                        continue
                    
                    print(cl.blue+"\n\nEnter Member's Gender:\n"+cl.reset)
                    gender=input()
                    print(cl.blue+"\n\nEnter Member's Weight(in Kg):\n"+cl.reset)
                    weight = self.num_input()
                    print(cl.blue+"\n\nEnter Member's Height(in m):\n"+cl.reset)
                    height = float(input())
                    bmi1 = weight/(height*height)
                    bmi = round(bmi1,1)
                    fp1 = open('workout_regime.json','r')
                    reg = fp1.read()
                    reg = json.loads(reg)
                    reg_exist=list(reg.keys())
                    fp1.close()
                    m = 0
                    if reg_exist:
                        for i in range(len(reg_exist)):
                            if bmi>=float(reg_exist[i][0:4]) and bmi<float(reg_exist[i][5:]):
                                regime = reg_exist[i]
                                m+=1
                        if not m:
                            print(cl.red+"\n\nRegimen for this BMI doesn't exist. Please try creating one\n\n"+cl.reset)
                            break
                    
                    else:
                        print(cl.red+'\n\nThere is no existing Regimen. Please try creating one.\n\n'+cl.reset)
                        break
                    
                    print(cl.blue+"\n\nEnter Member's mebership duration(in months):\n"+cl.reset)
                    time = self.num_input()
                    if 'members' not in data.keys():
                        data['members']={mob:{'name':name,'age':age,'email':email,'password':password,'gender':gender,'bmi':bmi,'membership':time,'regime':regime}}
                    
                    else:
                        data['members'][mob]={'name':name,'age':age,'email':email,'password':password,'gender':gender,'bmi':bmi,'membership':time,'regime':regime}
                    fp = open('login.json','w')
                    j_data = json.dumps(data)
                    fp.write(j_data)
                    fp.close()
                    print(cl.gold+cl.bold+'\n\n\nMember added successfully!!\n\n\n'+cl.reset)
                    break
            
            elif opt == 2:
                fp = open('login.json','r')
                user_info = fp.read()
                user_info = json.loads(user_info)
                fp.close()
                if 'members' in user_info.keys():
                    print(cl.cyan+cl.bold+'\n\nEnter a valid mobile number of the member:\n')
                    mob = self.num_input()
                    member_info = user_info['members']
                    mob = str(mob)
                    if mob in member_info.keys():
                        print("\n\nMember's Name:",member_info[mob]['name'])
                        print("Member's Email:",member_info[mob]['email'])
                        print("Member's Password:",member_info[mob]['password'])
                        print("Member's Age:",member_info[mob]['age'])
                        print("Member's Gender:",member_info[mob]['gender'])
                        print("Member's BMI:",member_info[mob]['bmi'])
                        print("Member's Regimen of BMI range:",member_info[mob]['regime'])
                        print("Member's membership duration(in months):",member_info[mob]['membership'])
                        print('\n\nChoose other option\n\n\n'+cl.reset)
                    else:
                        print(cl.red+"\n\nMember's mobile number doesn't match with existing data\n\n\n"+cl.reset)
                    continue
                
                else:
                    print(cl.red+'\nNo existing member Information present.\n\n'+cl.reset)

            elif opt == 3:
                fp = open('login.json','r')
                user_info = fp.read()
                user_info = json.loads(user_info)
                fp.close()
                if 'members' in user_info.keys():
                    print(cl.blue+'\n\nEnter a valid mobile number of the member:\n'+cl.reset)
                    mob = self.num_input()
                    member_info = user_info['members']
                    mob = str(mob)
                    if mob in member_info.keys():
                        while True:
                            print(cl.bold+cl.blue+'\n\nPlease choose valid option to update information or 0 to Exit')
                            print("1. Member's Name:",member_info[mob]['name'])
                            print("2. Member's Email:",member_info[mob]['email'])
                            print("3. Member's Password:",member_info[mob]['password'])
                            print("4. Member's Age:",member_info[mob]['age'])
                            print("5. Member's Gender:",member_info[mob]['gender'])
                            print("6. Member's BMI:",member_info[mob]['bmi'])
                            print("7. Member's membership duration(in months):",member_info[mob]['membership'])
                            print("8. Member's mobile number:",mob)
                            print('0. Exit'+cl.reset)
                            select = self.num_input()
                            if select == 0:
                                break
                            
                            elif select == 1:
                                print(cl.blue+"\n\nEnter Member's updated Full Name:\n"+cl.reset)
                                name = input()
                                user_info['members'][mob]['name']=name
                            
                            elif select == 2:
                                print(cl.blue+"\n\nEnter Member's new email:\n"+cl.reset)
                                email = input()
                                user_info['members'][mob]['email']=email
                            
                            elif select ==3:
                                print(cl.blue+"\n\nEnter Member's new password:\n"+cl.reset)
                                password = input()
                                user_info['members'][mob]['password']=password
                            
                            elif select ==4:
                                print(cl.blue+"\n\nEnter Member's latest Age:\n"+cl.reset)
                                age = self.num_input()
                                user_info['members'][mob]['age']=age
                            
                            elif select ==5:
                                print(cl.blue+"\n\nEnter Member's changed Gender:\n"+cl.reset)
                                gender=input()
                                user_info['members'][mob]['gender']=gender
                            
                            elif select == 6:
                                print(cl.blue+"\n\nEnter Member's new BMI:\n"+cl.reset)
                                bmi=float(input())
                                user_info['members'][mob]['bmi']=bmi
                            
                            elif select==7:
                                print(cl.blue+"\n\nDo you want to increase or revoke membership duration(in months):\n1. Increase\n2. Revoke\n\n"+cl.reset)
                                ms = self.num_input()
                                if ms ==1:
                                    print(cl.green+'\nEnter the duration(in Months) you want to increase membership for:'+cl.reset)
                                    dur = self.num_input()
                                    if dur<0 or dur>100:
                                        print(cl.red+'\nWrong Input.\n\n'+cl.reset)
                                    else:
                                        time = member_info[mob]['membership']+dur
                                
                                elif ms==2:
                                    print(cl.green+'\n\nEnter the duration(in Months) you want to revoke membership for:\n'+cl.reset)
                                    dur = self.num_input()
                                    if dur<0 or dur>int(member_info[mob]['membership']):
                                        print(cl.red+'\nWrong Input.\n\n'+cl.reset)
                                    
                                    else:
                                        time = member_info[mob]['membership']-dur
                                        if time==0:
                                            del user_info['members'][mob]
                                            print(cl.red+'\nMember has been removed since Membership Duration became less than 1 month.\n\n'+cl.reset)
                                            break
                                        
                                        else:
                                            user_info['members'][mob]['membership']=time
                            
                            elif select ==8:
                                print(cl.blue+"\n\nEnter Member's new mobile number:\n"+cl.reset)
                                mob1 = self.num_input()
                                user_info['members'][mob1]={'name':member_info[mob]['name'],'age':member_info[mob]['age'],'email':member_info[mob]['email'],'password':member_info[mob]['password'],'gender':member_info[mob]['gender'],'bmi':member_info[mob]['bmi'],'membership':member_info[mob]['membership'],'regime':member_info[mob]['regime']}
                                del user_info['members'][mob]
                            fp=open('login.json','w')
                            new_data = json.dumps(user_info)
                            fp.write(new_data)
                            fp.close()
                            print(cl.bold+cl.green+'\n\n\nMember Information Successfully Updated!!\n\n'+cl.reset)
                            break
                    
                    else:
                        print(cl.red+"\nMember's mobile number doesn't match with existing data!\n\n"+cl.reset)

                else:
                    print(cl.red+'\nNo existing member Information present.\n\n'+cl.reset)

            elif opt == 4:
                fp = open('login.json','r')
                data = fp.read()
                data = json.loads(data)
                fp.close()
                if 'members' in data.keys():
                    print(cl.blue+'\n\nEnter the mobile Number of member whose membership is to be cancelled:\n'+cl.reset)
                    mob = self.num_input()
                    member_data = data['members']
                    mob = str(mob)
                    if mob in member_data.keys():
                        del data['members'][mob]
                        if not data['members']:
                            del data['members']
                        fp=open('login.json','w')
                        new_data = json.dumps(data)
                        fp.write(new_data)
                        fp.close()
                        print(cl.bold+cl.green+'\n\n\nMember Information Successfully Deleted!!\n\n'+cl.reset)

                    else:
                        print(cl.red+"\nMember's mobile number doesn't match with existing data!\n\n"+cl.reset)
                
                else:
                    print(cl.red+'\nNo existing member Information present.\n\n'+cl.reset)
            
            else:
                print(cl.red+'\nWrong input. Try Again!!\n\n'+cl.reset)


    
    # Object Function for CRUD of Regimen
    def regime_option(self):
        
        while True:
            print(cl.bold+cl.gold+'\n\n\nChoose an option:\n\n1. Create Regimen\n\n2. View Regimen\n\n3. Delete Regimen\n\n4. Update Regimen\n\n0. Exit\n\n'+cl.reset)
            option = self.num_input()
            if option == 0:
                break
            
            elif option == 1:
                while True:
                    fp = open('workout_regime.json','r')
                    reg = fp.read()
                    reg = json.loads(reg)
                    fp.close()
                    l_reg = list(reg.keys())
                    if l_reg:
                        print(cl.blue+'\nExisting regimes are:\n\nIn BMI range:'+cl.reset)
                        for i in range(len(l_reg)):
                            print(i+1,'. ',l_reg[i],sep='')
                            day_reg = list(reg[l_reg[i]].keys())
                            c=65
                            for j in range(len(day_reg)):
                                print('\t\t\t\t',chr(c),'. ',day_reg[j],': ',reg[l_reg[i]][day_reg[j]])
                                c+=1
                            print(cl.blue+'\t\t----------------------------------------------------\n\n'+cl.reset)
                    
                    else:
                        print(cl.red+'\nNo regimen created yet.\n\n'+cl.reset)
                    
                    while True:
                        try:
                            print(cl.blue+'\n\nEnter exclusive upper limit for bmi range:\n'+cl.reset)
                            upper = float(input())
                            upper = round(upper,1)
                            print(cl.blue+'\n\nEnter inclusive lower limit for bmi range:\n'+cl.reset)
                            lower = float(input())
                            lower =  round(lower,1)
                            final = {}
                            for i in ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']:
                                while True:
                                    work = {1:'Rest',2:'Chest',3:'Bicep',4:'Back',5:'Tricep',6:'Legs',7:'Cardio',8:'Abs',9:'Glutes'}
                                    print(cl.cyan+'\n\nAvailable option for',i,'\n\n1. Rest\n2. Chest\n3. Bicep\n4. Back\n5. Tricep\n6. Legs\n7. Cardio\n8. Abs\n9. Glutes\n'+cl.reset)
                                    print('\n\nInput number of workout on',i,':\n')
                                    n=self.num_input()
                                    if n<1 or n>3:
                                        print(cl.red+'\n\nPlease Choose maximum Three and minimum One workout for 1 day!!\n'+cl.reset)
                                        continue
                                    else:
                                        w=[]
                                        for j in range(n):
                                            print('Choose',j+1,'option for',i,':\n\n1. Rest\n2. Chest\n3. Bicep\n4. Back\n5. Tricep\n6. Legs\n7. Cardio\n8. Abs\n9. Glutes')
                                            num = self.num_input()
                                            if num<1 or num>9:
                                                print(cl.red+'\nWrong Input. Try Again!!\n\n'+cl.reset)
                                                continue
                                            else:
                                                w.append(work[num])
                                        workout = '/'.join(w)
                                    final[i]=workout
                                    print(i,'workout successfully created')
                                    break
                            key = str(lower)+'-'+str(upper)
                            reg[key]=final
                            fp = open('workout_regime.json','w')
                            new_regime = json.dumps(reg)
                            fp.write(new_regime)
                            fp.close()
                            print(cl.bold+cl.green+'\n\n\nNew Regimen successfully created!!\n\n'+cl.reset)
                            break
                        except:
                            print(cl.red+'\nTry to input decimal value\n\n'+cl.reset)
                    break

            elif option==2:
                fp = open('workout_regime.json','r')
                reg = fp.read()
                reg = json.loads(reg)
                fp.close()
                if not reg:
                    print(cl.red+'\nThere is no existing Regimen\n\n'+cl.reset)
                else:
                    serial = list(reg.keys())
                    for i in range(len(reg.keys())):
                        print('Regime ',i+1,':','\n\n','BMI Range: ',serial[i],'\n',sep='')
                        workout = list(reg[serial[i]].keys())
                        for j in range(len(workout)):
                            print(workout[j],':',reg[serial[i]][workout[j]])
                        print('----------------------------------------------------\n\n\n\n')
            
            elif option==3:
                while True:
                    try:
                        print(cl.blue+'\n\nEnter exclusive upper limit for bmi range you want to delete:\n')
                        upper = float(input())
                        upper = round(upper,1)
                        print('\n\nEnter inclusive lower limit for bmi range you want to delete:\n'+cl.reset)
                        lower = float(input())
                        lower =  round(lower,1)
                        key = str(lower)+'-'+str(upper)
                        fp = open('workout_regime.json','r')
                        reg = fp.read()
                        reg = json.loads(reg)
                        fp.close()
                        if key not in reg.keys():
                            print(cl.red+'\nThis BMI range doesnt exists. Try to enter different range Regimen!\n\n'+cl.reset)
                            continue
                        else:
                            del reg[key]
                            fp = open('workout_regime.json','w')
                            new_reg = json.dumps(reg)
                            fp.write(new_reg)
                            fp.close()
                            print('\n\nRegimen of range',key,'successfully deleted!!\n\n')
                            break
                    except:
                        print(cl.red+'\nEnter a decimal value(Upto 1 decimal place).\n\n'+cl.reset)
                
            elif option == 4:
                while True:
                    try:
                        print(cl.blue+'\n\nEnter exclusive upper limit for bmi range you want to update Regimen:\n')
                        upper = float(input())
                        upper = round(upper,1)
                        print('\n\nEnter inclusive lower limit for bmi range you want to update Regimen:\n'+cl.reset)
                        lower = float(input())
                        lower =  round(lower,1)
                        key = str(lower)+'-'+str(upper)
                        fp = open('workout_regime.json','r')
                        reg = fp.read()
                        reg = json.loads(reg)
                        fp.close()
                        if key not in reg.keys():
                            print(cl.red+'\nThis BMI range doesnt exists. Try to enter different range Regime!\n\n'+cl.reset)
                            continue
                        else:
                            while True:
                                day = list(reg[key])
                                print(cl.blue+'\n\nEnter the Day option you want to update:\n'+cl.reset)
                                for i in range(len(day)):
                                    print(i+1,'.',day[i],':',reg[key][day[i]])
                                update = self.num_input()
                                if update<1 or update>7:
                                    print('Wrong Input.')
                                    continue
                                else:
                                    while True:
                                        work = {1:'Rest',2:'Chest',3:'Bicep',4:'Back',5:'Tricep',6:'Legs',7:'Cardio',8:'Abs',9:'Glutes'}
                                        print(cl.blue+'\n\nAvailable option are','\n\n1. Rest\n2. Chest\n3. Bicep\n4. Back\n5. Tricep\n6. Legs\n7. Cardio\n8. Abs\n9. Glutes\n'+cl.reset)
                                        print('Input number of workout')
                                        n=self.num_input()
                                        if n<1 or n>3:
                                            print(cl.blue+'\n\nPlease Choose maximum Three and minimum One workout for 1 day\n'+cl.reset)
                                            continue
                                        else:
                                            w=[]
                                            work = {1:'Rest',2:'Chest',3:'Bicep',4:'Back',5:'Tricep',6:'Legs',7:'Cardio',8:'Abs',9:'Glutes'}
                                            for j in range(n):
                                                while True:
                                                    print('\n\nChoose',j+1,'option from:','\n\n1. Rest\n2. Chest\n3. Bicep\n4. Back\n5. Tricep\n6. Legs\n7. Cardio\n8. Abs\n9. Glutes\n')
                                                    num = self.num_input()
                                                    if num<1 or num>9:
                                                        print(cl.red+'\nWrong Input. Try Again!!\n\n'+cl.reset)
                                                        continue
                                                    else:
                                                        w.append(work[num])
                                                        break
                                        workout = '/'.join(w)
                                        reg[key][day[update-1]]=workout
                                        fp = open('workout_regime.json','w')
                                        data = json.dumps(reg)
                                        fp.write(data)
                                        fp.close()
                                        print(cl.bold+cl.green+'\n\n\nRegimen Successfully updated!!\n\n'+cl.reset)
                                        break
                                break
                        break
                    except:
                        print(cl.red+'\nEnter a decimal value(Upto 1 decimal place)!\n\n'+cl.reset)


    
    
    # Main menu gives all option to Super User
    # This is first object function to run when Super_User class is called
    def main_menu(self):
        
        while True:
            print(cl.bold+cl.cyan+'\n\nChoose an Activity:\n\n\n\n1. Member Options\n\n2. Regimen Options\n\n3. Your details\n\n4. Exit\n\n\n')
            option = self.num_input()
            
            if option==1:
                self.member_option()        #calling member_option function to CRUD member
            
            elif option == 2:
                self.regime_option()          #calling regime_option function to CRUD regime
            
            elif option == 3:
                print(cl.bold+cl.gold+'\n\nYour Details:\n')
                c=1
                for i in list(self.info.keys()):    # Displaying Super User information from object variable info of Dict type
                    print(c,': ',i,': ',self.info[i],'\n',sep='')
                    c+=1
                print('\n\n\n'+cl.reset)
            
            elif option == 4:
                print(cl.bold+cl.cyan+'\n\nSee You Again!!\n\n\n'+cl.reset)
                break
            
            else:
                print(cl.red+'Enter a valid option'+cl.reset)

    


    # static method to except only integer input
    @staticmethod
    def num_input():
        while(True):
            try:
                num = int(input())
                if num>=0:
                    return num
                else:
                    print(cl.red+'\nEnter a Whole Number\n\n'+cl.reset)
                    continue
            except ValueError:
                print(cl.red+'\nEnter a digit Value. Try Again.\n\n'+cl.reset)