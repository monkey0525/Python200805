while True:
    print('計算機開機')
    print('1.+')
    print('2.-')
    print('3.*')
    print('4./')
    print('5.close')
    功能=input('請選擇功能:')
    if 功能=='1':
        加法數字1=input('請輸入第一個數字:')
        加法數字1=int(加法數字1)
        加法數字2=input('請輸入第二個數字:')
        加法數字2=int(加法數字2)
        加法答案=加法數字1+加法數字2
        print(加法答案)
    if 功能=='2':
        減法數字1=input('請輸入第一個數字:')
        減法數字1=int(減法數字1)
        減法數字2=input('請輸入第二個數字:')
        減法數字2=int(減法數字2)
        減法答案=減法數字1-減法數字2
        print(減法答案)
    if 功能=='3':
        乘法數字1=input('請輸入第一個數字:')
        乘法數字1=int(乘法數字1)
        乘法數字2=input('請輸入第二個數字:')
        乘法數字2=int(乘法數字2)
        乘法答案=乘法數字1*乘法數字2
        print(乘法答案)
    if 功能=='4':
        除法數字1=input('請輸入第一個數字:')
        除法數字1=int(除法數字1)
        除法數字2=input('請輸入第二個數字:')
        除法數字2=int(除法數字2)
        除法答案=除法數字1/除法數字2
        print(除法答案)
    if 功能=='5':
        print('離開')
        break
        
    