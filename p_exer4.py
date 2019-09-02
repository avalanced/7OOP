class p_exer4():
    def __init__(self):
        self.items=[]
        self.subs=['OOP','APPDEV', 'PE3', 'SOFTENG', 'NET1', 'MAEL2', 'DISTRU2', 'RPH']
    def push (self,item):
        self.items.insert(0,item)
    def remove(self):
        self.items.remove(enrolled)
    def isEmpty (self):
        return self.items==[]
     

    
n=p_exer4()
name =str(input("Enter your name: "))
print('---------------------------------')
print("Welcome",name)
print('Current Units Enrolled:',len(n.items)*3)
#print(n.subs)
while True:
    if len(n.items)*3<24:
                
            print('---------------------------------')
            print("MAIN CHOICES\n")
            print("[1]ADD SUBJECT\n[2]DROP SUBJECT\n[3]PRINT\n[4]EXIT")
            print('---------------------------------')
                  
            choice =int(input("Enter your choice: "))

            if choice == 1: #ADD
                add = str(input('ADD SUBJECT: ')).upper() 
                if add in n.subs:
                    if add not in n.items:
                        n.push(add)
                        print('Subject Succesfull Added!!')
                        print('Current Units Enrolled:',len(n.items)*3)
                    else:
                        print("already enrolled") 
                                           
                        
                else:
                    print('not in list of subs for 2nd yr 1st sem' ) 
            elif choice == 2: #DROP
                if n.isEmpty():
                        print("------No Enrolled Subjects------")
                        print('Current Units Enrolled:',len(n.items)*3)
                        continue

                else:
                    print('---SUBJECTS CURRENTLY ENROLLED---')
                    count =0
                    for x in n.items:
                        count +=1
                        print('[',count,']',x)
                        
                    print('Current Units Enrolled:',len(n.items)*3)
                    print('---------------------------------')
                    
                    enrolled = int(input('Select which subjects you want to drop: '))
                    n.items.pop(enrolled-1)
                    print('Current Units Enrolled:',len(n.items)*3)
                


            elif choice == 3: #PRINT
                if n.isEmpty():
                    print("------No Enrolled Subjects------")
                    print('Current Units Enrolled:',len(n.items)*3)
                    continue

                else:
                    print('---SUBJECTS CURRENTLY ENROLLED---')
                    for x in n.items:                                        
                        print('|\t',x)
                        
                    print('|   Current Units Enrolled:',len(n.items)*3)
                    print('---------------------------------')
            elif choice == 4: #EXIT
                val = input ("Are you sure you want to quit [Y/N]?")
                if val == "y" or val =="Y":
                    print('Goodbye!',name)
                    print ("---- Program terminated ----")
                    break
                elif val =="N" or val =="n":
                    continue
                
            else:
                print("---- Invalid Input ----\n")
    else:
        print('---------------------------------')
        print("You have exceeded the number of units to be enrolled")
        break
        
