# Importing files to ne used in class
import json
import color as cl




# Class for all member options 
class Member:

    def __init__(self,info):
        self.info = info            #object variable has all details of member logging in
    
    
    # Main menu function to give user panel
    def main_menu(self):
        while True:
            print(cl.green+'\nHello',self.info['name'],'\n\n')
            print('1. View Profile\n\n2. View Regimen\n\n0. Exit\n\n\n\n'+cl.reset)
            option = self.num_input()
            
            if option>2 or option<0:
                print(cl.red+'\nPlease input valid option. Try Again!!\n\n'+cl.reset)
                continue
            
            if option==0:
                print(cl.gold+'\n\nSee You Again!!\n\n\n'+cl.reset)
                break
            
            elif option==1:
                c=1
                for i in self.info.keys():
                    print(c,'. ',i.capitalize(),': ',self.info[i],sep='')
                    c+=1
                print('\n\n\n\n')
            
            elif option==2:
                fp = open('workout_regime.json','r')
                reg = fp.read()
                reg = json.loads(reg)
                fp.close()
                if self.info['regime'] in reg.keys():        #To check if regime exists in workout_regime.json file
                    print(cl.green+'\n\nYour Regime is:\n\n')
                    c=1
                    for i in reg[self.info['regime']].keys():
                        print(c,'. ',i.capitalize(),': ',reg[self.info['regime']][i],'\n',sep='')
                        c+=1
                    print('\n\n\n\n'+cl.reset)
                else:
                    print(cl.red+'\nYour regime has been removed by the SuperUser!!\n\n'+cl.reset)

    
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
                print(cl.red+'\nEnter a digit Value. Try Again.\n\n')