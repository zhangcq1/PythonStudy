import random

class SimulateLanding(object):
    
    def __init__(self):
        self.Database = dict()
        
    def Register(self):
        username = input('Please input the username you want to register:').strip()
        password = input('Please input the password you want to register:').strip()
        if username in self.Database:
            print('The user name you registered already exists\n')
        else:
            new_Data = {username:password}
            self.Database.update(new_Data)

            
    def Landing(self):
        count = 3
        while count>0:
            username = input('Please input your username:').strip()
            if username in self.Database:
                
                password = input('Please input your password:').strip()
                if password == self.Database[username]:

                    state = self.VerificationCode()
                    if state is 'Pass':
                        print('Landing success\n')
                        break
                    else:
                        count = count-1
                        print('The verification failed,Number of remaining inputs:%s'%count)
                else:
                    count = count-1
                    print('The password error,Number of remaining inputs:%s'%count)
                    continue
            else:
                count = count-1
                print('The username error,Number of remaining inputs:%s'%count)
                continue
        

            
    def VerificationCode(self,state='Failed'):
        a='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789'
        count = 3
        while count>0:
            VerificationCode = random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a)
            print('The verification code is:%s' %VerificationCode)
            UserInput=input('Please input verification code:').strip()
            if UserInput.upper() == VerificationCode.upper():
                print('verification success\n')
                state='Pass'
                break
            else:
                count = count-1
                print('verification failed,Number of remaining inputs:%s'%count)
        return state

user = SimulateLanding()
for i in range(1):
    user.Register()
    print(user.Database)
    user.Landing()
end = input('Enter any key to return')
