from django.shortcuts import render
from .models import Login
from .form import LoginForm

from django.shortcuts import redirect, render,HttpResponse
from .models import *
from .form import LoginForm
from django.contrib.auth import authenticate, login,logout

from datetime import date
from django.contrib.auth.decorators import login_required
from .DB import DbConnection


# Create your views here.
dbobj=DbConnection(host="localhost",user="root",passwd="",database="caeser_cipher",port=3306)

def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('adminhome')
            except Exception as e:
                form = LoginForm()
                return render(request,'signup.html',{'errmsg':str(e),'form':form})
        else:
            form = LoginForm()
            return render(request,'signup.html',{'errmsg':'Validation Failed','form':form})
    else:
        form = LoginForm()
        return render(request,'signup.html',{'form':form})

def login(request):
    form=LoginForm()
    return render(request,'login.html',{'form':form})

def loginaction(request):
    username=request.POST["username"]
    password=request.POST["password"]
    record=Login.objects.filter(username=username,password=password)
    if record.count()>0:
        record=Login.objects.get(username=username,password=password)
        request.session['username'] = record.username
        request.session['role'] = record.role
        if record.role=="admin":
            return render(request,'adminhome.html')
        else:
            return render(request,'userhome.html')
    else:
        form=LoginForm(initial={'role': 'user'})
        return render(request,'login.html',{'errmsg':'Invlid username or password','form':form})

def adminhome(request):
    return render(request,'adminhome.html')

def userhome(request):
    return render(request,'userhome.html')

# def adhome(request):
#     logins=Login.objects.all()
#     return render(request,'adminhome.html',{'logins':logins})

def adcom(request):
    logins=Message.objects.filter(option=1,status=1)
    return render(request,'common.html',{'logins':logins})

def deletemsg(request,mid):
    sql="delete from message where mid=%s"
    val=(mid,)
    if dbobj.executenonquery(sql,val):
        logins=Message.objects.filter(option=1,status=1)
        return render(request,'common.html',{'logins':logins})
    else:
        logins=Message.objects.filter(option=1,status=1)
        return render(request,'common.html',{'logins':logins})

# def approveuser(request,username):
#     sql="update login set status=1 where username=%s"
#     print(sql)
#     val=(username,)
#     if dbobj.executenonquery(sql,val):
#         logins=Login.objects.filter(status=0)
#         return render(request,'validateuser.html',{'logins':logins})
#     else:
#         logins=Login.objects.filter(status=0)
#         return render(request,'validateuser.html',{'logins':logins})

def rejectuser(request,username):
    sql="delete from login where username=%s"
    val=(username,)
    if dbobj.executenonquery(sql,val):
        logins=Login.objects.filter(status=0)
        return render(request,'validateuser.html',{'logins':logins})
    else:
        logins=Login.objects.filter(status=0)
        return render(request,'validateuser.html',{'logins':logins})

def editusers(request):
    logins=Login.objects.filter(status=1)
    return render(request,'editusers.html',{'logins':logins})

def editlogin(request,username):
    login=Login.objects.get(username=username)
    return render(request,'editlogin.html',{'login':login})

def updatelogin(request, username):
    login = Login.objects.get(username=username)
    form = LoginForm(request.POST, instance = login)
    if form.is_valid():
        form.save()
        logins=Login.objects.all()
        return render(request,'editusers.html',{'logins':logins})
    else:
        login = Login.objects.get(username=username)
        return render(request,'editlogin.html', {'login':login})

def deletelogin(request,username):
    sql="delete from login where username=%s"
    val=(username,)
    if dbobj.executenonquery(sql,val):
        logins=Login.objects.filter(status=1)
        return render(request,'editusers.html',{'logins':logins})
    else:
        logins=Login.objects.filter(status=1)
        return render(request,'editusers.html',{'logins':logins})

def brdmsg(request):
    try:
        errmsg=request.session['encmsg']
    except:
        errmsg=''
    username=request.session['username']
    return render(request,'broadcastmsg.html',{'username':username,'errmsg':errmsg})

def broad(request):
    try:
        errmsg=request.session['encmsg']
    except:
        errmsg=''
    username=request.session['username']
    return render(request,'broadcast.html',{'username':username,'errmsg':errmsg})

def unimsg(request):
    try:
        errmsg=request.session['encmsg']
    except:
        errmsg=''
    username=request.session['username']
    return render(request,'unicastmsg.html',{'username':username})

def unicast(request):
    try:
        errmsg=request.session['encmsg']
    except:
        errmsg=''
    username=request.session['username']
    return render(request,'unicast.html',{'username':username})

def encryptmsg(request):
    username=request.POST['sendusername']
    msg=request.POST['txtmsg']
    option=request.POST['option']
    suname=request.POST['txttousername']
    cipher=encrypt(msg,5)
    date=datetime.today()
    print('username: ',username)
    mess=Message.objects.create(username=username,msg=cipher,date=date,option=option,suname=suname)
    #mess.save()
    request.session['encmsg']='Message send successfully'
    return redirect(adminhome)
    #return HttpResponse('done')

def encryptms(request):
    username=request.POST['sendusername']
    msg=request.POST['txtmsg']
    option=request.POST['option']
    suname=request.POST['txttousername']
    cipher=encrypt(msg,5)
    date=datetime.today()
    print('username: ',username)
    mess=Message.objects.create(username=username,msg=cipher,date=date,option=option,suname=suname)
    #mess.save()
    request.session['encmsg']='Message send successfully'
    return redirect(userhome)
    #return HttpResponse('done')
    
def encrypt(plaintext,key): 
    encrypted = ""
    for c in plaintext:
        if c.isupper(): #check if it's an uppercase character
            c_index = ord(c) - ord('A')
            # shift the current character by key positions
            c_shifted = (c_index + key) % 26 + ord('A')
            c_new = chr(c_shifted)
            encrypted += c_new
        elif c.islower(): #check if its a lowecase character
            # subtract the unicode of 'a' to get index in [0-25) range
            c_index = ord(c) - ord('a') 
            c_shifted = (c_index + key) % 26 + ord('a')
            c_new = chr(c_shifted)
            encrypted += c_new
        elif c.isdigit():
            # if it's a number,shift its actual value 
            c_new = (int(c) + key) % 10
            encrypted += str(c_new)
        else:
            # if its neither alphabetical nor a number, just leave it like that
            encrypted += c
    return encrypted

def decryptmsg(request,mid):
    ciph=Message.objects.get(mid=mid).msg
    msg=decrypt(ciph,5)
    print('Decrypted:',msg)
    return render(request,'showmessage.html',{'msg':msg})
    #return HttpResponse('done')

def decrypt(cipher,key):
    decrypted = ""
    for c in cipher:
        if c.isupper(): 
            c_index = ord(c) - ord('A')
            # shift the current character to left by key positions to get its original position
            c_og_pos = (c_index - key) % 26 + ord('A')
            c_og = chr(c_og_pos)
            decrypted += c_og
        elif c.islower(): 
            c_index = ord(c) - ord('a') 
            c_og_pos = (c_index - key) % 26 + ord('a')
            c_og = chr(c_og_pos)
            decrypted += c_og
        elif c.isdigit():
            # if it's a number,shift its actual value 
            c_og = (int(c) - key) % 10
            decrypted += str(c_og)
        else:
            # if its neither alphabetical nor a number, just leave it like that
            decrypted += c
    return decrypted

def messg(request):
    return render(request,'messge.html')

def viewmesg(request):
    return render(request,'viewmesg.html')

def sendmesg(request):
    return render(request,'sendmesg.html')

# def cmmesg(request):
#     return render(request,'commonmesg.html')

def cmmesg(request):
    logins=Message.objects.filter(option=1,status=1)
    return render(request,'commonmesg.html',{'logins':logins})

def pernmesg(request):
    username=request.session['username']
    logins=Message.objects.filter(suname=username,status=1)
    return render(request,'pernmesg.html',{'logins':logins})

# def mark(request,mid):
#     sql="update message set status=2 where mid=%s"
#     print(sql)
#     val=(mid,)
#     if dbobj.executenonquery(sql,val):
#         logins=Message.objects.filter(status=1)
#         return render(request,'commonmesg.html',{'logins':logins})
#     else:
#         logins=Message.objects.filter(status=1)
#         return render(request,'commonmesg.html',{'logins':logins})

def prof(request):
     username=request.session['username']
     logins=Login.objects.get(username=username)
     return render(request,'prof.html',{'logins':logins})

def editp(request,username):
     logins=Login.objects.get(username=username)
     return render(request,'editpro.html',{'logins':logins})

def updatelog(request,username):
    login = Login.objects.get(username=username)
    form = LoginForm(request.POST, instance = login)
    if form.is_valid():
        form.save()
        logins=Login.objects.all()
        return render(request,'userhome.html',{'logins':logins})
    else:
        login = Login.objects.get(username=username)
        return render(request,'userhome.html', {'login':login})

def logout(request):
     return render(request,'index.html')


