def Q1(arr1,arr2):
    arr3=[]
    for i in range(len(arr1)):
        x=max(arr1[i],arr2[i])
        arr3.append(x)
    return arr3

def Q2(arr):
    size=len(arr)//2
    for i in range(size):
        if arr[i]!=arr[size+i]:
            return False
    return  True


def Q3():
    arr=[]
    x=0
    while x != -1:
        x=int(input('Enter a number:'))
        if x==-1:
            break
        y=1
        z=x//10
        while z>1:
            y=y+1
            z=z/10
        arr.append(y)
    return arr


def Q4():
    array=[]
    size=int(input('how many words you want?:'))
    for i in range(size):
        y=input('enter a word:')
        array.append(y)

    t=array[::-1]
    s=''
    for i in t:
        s+=i
        s+=' '
    print(s)

def Q5(arr1,arr2):
    for i in range(len(arr1)):
        if arr1[i] not in arr2:
            return False
    return True


def Q6(arrStu,arrGrades):
    o={}
    for i in range(len(arrStu)):
        o[arrStu[i]]=arrGrades[i]
    return o

def Q7(dic):
    for i in dic:
        x=sum(dic[i])
        print(i,x/len(dic[i]))

def Q8(arr):
    temp=0
    for i in arr:
        y=0
        z=i
        while int(z)>1:
            y=y+1
            z=z//10
        if temp<y:
            temp=y
            maximum=i
    return maximum

def Q9(str):
    st=''
    su=''
    arr1=set()
    leter='abcdefghijkmnlopqrstuvwxyz'
    for i in range(len(str)):
        if str[i] in leter:
            arr1.add(str[i])
            leter=leter.replace(f'{str[i]}','')
    for i in arr1:
        st+=i
        st+=','
    for i in leter:
        su+=i
        su+=','
    print('Used letters:',st)
    print('Unused letters:',su)







def Q11(n):
    string='123456789'*n
    str=iter(string)
    y=int(n/2)+1

    for i in range(y+1):
        print(" "*(y-i),end='')
        for j in range(i*2-1):
            print(next(str),end='')
        print('')
    for i in range(y-1,0,-1):
        print(" " * (y - i), end='')
        for j in range(i * 2 - 1):
            print(next(str), end='')
        print('')
Q11(11)

def Q12(arr):
    def ispoli(u):
        x = -1
        for i in range(int(len(u)/2)):
            if u[i]!=u[x]:
                return False
            else:
                x-=1
        return True
    count = 0
    for j in range(len(arr)):
        y=arr[j]
        p=str(y)
        if ispoli(p):
            count=count+1
    return count



def Q13(arr,dic):

    for i in range(len(arr)):
        temp=0
        for j in dic:
            if arr[i] is dic[j]:
                temp+=1
        if temp>0:
            arr[i]=True
        else:
            arr[i]=False
    return arr




def Q14(arr,dic):
    while len(arr)>len(dic):
        t=arr.pop(0)
        dic[f'{t}']=len(arr)
    print(arr,dic)



