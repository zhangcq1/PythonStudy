import re
shopping_cart={}
def Register():
    u_ask=re.compile(r'^\w+$')
    p_ask=re.compile(r'^[a-zA-Z0-9]{6,}$')
    r_name=re.compile(r"{'username':.+?}",re.S)
    while 1:
        page='======注册页面======'
        print(format(page,'^40',))
        try:
            username=input('请输入同户名(字母数字下划线):')
            password=input('请输入密码(至少六位字母和数字):')
            if u_ask.findall(username)[0]==username and \
               p_ask.findall(password)[0]==password:
                with open('C:/Users/Administrator/Desktop/A-Python/databases.txt','r',encoding='utf-8') as f:
                    usernames=f.read()
                    if "{'username': '%s'}" % username in \
                       r_name.findall(usernames):
                        print('用户名已存在,请重新输入')
                        N=input('是否继续注册(输入是继续,其他退出):').strip()
                        if N=="是":
                            continue
                        else:
                            break
                Databases(username,password)
                print('注册成功')
                break
            else:
                print('注册失败,用户名或密码格式错误')
                N=input('是否继续注册(输入是继续,其他退出):').strip()
                if N=="是":
                    continue
                else:
                    break
        except:
            print('注册失败,密码长度不合要求')
            print('注册失败,用户名或密码格式错误')
            N=input('是否继续注册(输入是继续,其他退出):').strip()
            if N=="是":
                continue
            else:
                break

def Landing():
    while 1:
        page='======登录页面======'
        print(format(page,'^40',))
        username=input('请输入同户名:')
        password=input('请输入密码:')
        Re_Str=r"{'username':.+?'(%s)'}.+?{'password':.+?'(%s)'}"%(username,password)
        userdata=re.compile(Re_Str,re.S)
        try:
            with open('C:/Users/Administrator/Desktop/A-Python/databases.txt','r',encoding='utf-8') as f:
                usernames=f.read()
                if userdata.findall(usernames):
                    print('登录成功')
                    return 1
                else:
                    print('用户名或密码错误\n')
                    N=input('重新登录请输入1,输入任意键退出:')
                    if N=='1':
                        continue
                    else:
                        return -1      
        except:
            print('用户名或密码错误')
            N=input('重新登录请输入1,输入任意键退出:')
            if N=='1':
                continue
            else:
                return -1

def Databases(Username,Password):
    data=[{'username':Username},{'password':Password}]
    with open('C:/Users/Administrator/Desktop/A-Python/databases.txt','a',encoding='utf-8') as f:
        f.write('\n'+str(data))
    
def P1():
    page='======系统页面======'
    tab1='1.用户注册'
    tab2='2.用户登录'
    tab3='3.退出系统'
    print(format(page,'^40',))#字符串拉长到20,然后居中对齐
    print(format(tab1,'^40',))
    print(format(tab2,'^40',))
    print(format(tab3,'^40',))
    
    
def P2():
    page='======用户页面======'
    tab1='1.添加商品'
    tab2='2.查看购物车'
    tab3='3.购买商品'
    tab4='4.退出登录'
    print(format(page,'^40',))#字符串拉长到20,然后居中对齐
    print(format(tab1,'^40',))
    print(format(tab2,'^40',))
    print(format(tab3,'^40',))
    print(format(tab4,'^40',))

def P3():
    page='======商品页面======'
    print(format(page,'^40',))
    with open('C:/Users/Administrator/Desktop/A-Python/goods.txt','r',encoding='utf-8') as f:
        for line in f.readlines():
            lst=line.strip('\n').split('|')
            print('商品序号: %s\n商品名称: %s\n商品价格: %s\n'%(lst[0],lst[1],lst[2]))
def Add_goods():
    while 1:
        P3()
        N=input('请输入要添加的商品序号(输入q退出):').strip(' ')
        if N.upper()=='Q':
            break
        else:
            with open('C:/Users/Administrator/Desktop/A-Python/goods.txt','r',encoding='utf-8') as f1:
                for line in f1.readlines():
                    lst=line.strip('\n').split('|')
                    if N==lst[0]:
                        if lst[1] in shopping_cart.keys():
                            shopping_cart[lst[1]][1]+=1
                            print('成功加入购物车')
                            break
                                
                        else:
                            shopping_cart[lst[1]]=[int(lst[2]),1]
                            print('成功加入购物车')
                            break
                else:
                    print('商品序号输入错误')

def Show():
    if len(shopping_cart)==0:
        print('你的购物车是空的')
    else:
        for ele in shopping_cart.keys():
            print('商品名称:',ele)
            print('商品价格:',shopping_cart[ele][0])
            print('商品数量:',shopping_cart[ele][1],'\n')
        
def Buy():
    while 1:
        print('你要购买的商品如下')
        Show()
        N=input('确认购买请输入1(退出输入q):').strip()
        if N=='1':
            Sum=0
            for ele in shopping_cart.keys():
                Sum=Sum+shopping_cart[ele][0]*shopping_cart[ele][1]
            print('你好,你一共消费%s元'%Sum)
            shopping_cart.clear()
            break
        elif N.upper()=='Q':
            break
        else:
            print('你输入的指令有误')
        
def page_landing():
    P2()
    while 1:   
        search=input('请输入要选择的操作序号:').strip(' ')
        if search=='1':
            Add_goods()
            return 1
        if search=='2':
            Show()
            return 1
        if search=='3':
            Buy()
            return 1
        if search=='4':
            return -1
            
        else:
            print('你的输入的操作有误')
            continue
def main():
    while 1:
        P1()
        search1=input('请输入要选择的操作序号:').strip(' ')
        if search1=='1':
            Register()
            continue
        if search1=='2':
            N=Landing()
            if N==1:
                while 1:
                    n=page_landing()
                    if n==-1:
                        break
                    if n==1:
                        continue
                    
            else:
                continue
        if search1=='3':
            break
        else:
            print('输入错误,没有对应操作')
main()
