import tkinter
from functools import partial
import pickle
from tkinter import END,messagebox
from tkinter import *
from PIL import ImageTk, Image
from tkinter.colorchooser import askcolor
from tkinter import filedialog
import pygame
import os
import mutagen
from mutagen.mp3 import MP3
import random



root=tkinter.Tk()
f1=open('SETTINGS.bin','rb')
po=pickle.load(f1)
print(po)
bgg,txt,flp=po[0],po[1],po[2]
msc,mad,mad2,mad3,mad4,name,temp,ch,bstack,pnf,mdl,temp1,ps=[],[],[],[],[],[],[],[1],[],[],[],[],[]
pygame.init()
pygame.mixer.init()


def wnd():
    f=open('SETTINGS.bin','rb')
    g=pickle.load(f)
    if g[0]=='white':
        bg='white'
    else:
        bg=g[0][1]
    if g[1]=='black':
        tg='black'
    else:
        tg=g[1][1]
    return bg,tg


def bfs(flp1):
    global flp
    flp=filedialog.askdirectory()


def bgcl(bgg1):
    global bgg
    bgg=askcolor()
    

def tcl(txt1):
    global txt
    txt=askcolor()


def tac():
    try:
        if True==bool(stt.winfo_exists()):
            stt.withdraw()
        else:
            pass
    except NameError:
        pass
    bg,tg=wnd()
    global tca
    tca=Toplevel(root)
    tca.title('TERMS AND CONDITIONS')
    tca.geometry("1250x700")
    tca.minsize(1250,700)
    tca.maxsize(1250,700)
    tca.configure(bg=bg)
    
    img1= Image.open("back.png")
    rimg1= img1.resize((30,25))
    nimg1= ImageTk.PhotoImage(rimg1)
    illg1= Label(tca,image=nimg1)
    illg1.photo=nimg1
    button1= Button(tca,image=nimg1,command=lambda:settings(),bg=bg,relief='flat',activebackground=tg).place(x=0,y=0)
    
    lg3=tkinter.Label(tca,text='TERMS AND CONDITIONS',bg=bg,fg=tg,font=('Arial',14)).place(x=550,y=0)
    k="Welcome to MUSIC PLAYER APP These terms and conditions govern your use of our app. By using our app, you agree to abide by these terms. If you do not agree with any part of these terms, please refrain from using our app.\n\n1. License\n\nWe grant you a limited, non-exclusive, and non-transferable license to use our app for personal, non-commercial purposes only. This license does not allow you to modify, reproduce, or distribute the app.\n\n2. User Conduct\n\nYou agree to use our app in compliance with all applicable laws and regulations. You further agree not to engage in any unlawful or prohibited activities, including but not limited to:\n\nUploading or sharing copyrighted material without permission.\nAttempting to disrupt or interfere with the functioning of the app.\nMisrepresenting your identity or affiliation with others.\n\n3. Privacy Policy\n\nYour privacy is important to us. Please review our Privacy Policy to understand how we collect, use, and protect your personal information.\n\n4. Intellectual Property\n\nAll content, trademarks, and intellectual property rights associated with our app are owned by us or our licensors. You agree not to use, reproduce, or distribute any content from our app without our express permission.\n\n5. Limitation of Liability\n\nWe strive to provide a reliable and error-free app, but we cannot guarantee uninterrupted or error-free access. We shall not be liable for any direct, indirect, incidental, or consequential damages arising out of your use of our app.\n\n6. Termination\n\nWe reserve the right to terminate or suspend your access to our app at any time, without prior notice or liability, for any reason whatsoever, including without limitation if you breach these terms.\n\n7. Updates and Modifications\n\nWe may update or modify these terms and conditions from time to time. Your continued use of our app after any such changes constitutes your acceptance of the new terms.\n\n8. Governing Law\n\nThese terms and conditions shall be governed by and construed in accordance with the laws of India, without regard to its conflict of law provisions."
    lg3=tkinter.Label(tca,text=k,bg=bg,fg=tg,font=('Arial',9)).place(x=3,y=60)
    


def abt():
    pass
    try:
        if True==bool(stt.winfo_exists()):
            stt.withdraw()
        else:
            pass
    except NameError:
        pass
    bg,tg=wnd()
    global atb
    atb=Toplevel(root)
    atb.title('ABOUT')
    atb.geometry("1000x1000")
    atb.minsize(1000,200)
    atb.maxsize(1000,200)
    atb.configure(bg=bg)
    
    img1= Image.open("back.png")
    rimg1= img1.resize((30,25))
    nimg1= ImageTk.PhotoImage(rimg1)
    illg1= Label(atb,image=nimg1)
    illg1.photo=nimg1
    button1= Button(atb,image=nimg1,command=lambda:settings(),bg=bg,relief='flat',activebackground=tg).place(x=0,y=0)
    
    lg3=tkinter.Label(atb,text='ABOUT',bg=bg,fg=tg,font=('Arial',14)).place(x=450,y=0)
    k="THIS APP WAS MADE BY A TEAM OF FOUR PEOPLE USING PYTHON FOR BACK-END AND TKINTER FOR THE FRONT-END.THIS APP USES BINARY FILES FOR STORING DATA\n\nTHE FOLLOWING IS THE DETAILS OF THE PEOPLE WHO IS RESPONSIBLE FOR THIS APP\n1. Dakshin\n2. Hari\n3. Gouri\n4. Harinee"
    lg3=tkinter.Label(atb,text=k,bg=bg,fg=tg,font=('Arial bold',9)).place(x=3,y=60)
    
 
def save_stttings(sbt,pmt):
    d=messagebox.askyesno("CONFIRM","ARE YOU SURE ?") 
    if d==True:
        bt=sbt.get()
        pmo=pmt.get()
        
        f1=open('SETTINGS.bin','rb')
        stts=pickle.load(f1)
        f1.close() 
        bt=0
        if bt is None:
            bt=stts[-2]
        if pmo==0:
            pmo=stts[-1]
        else:
            pass
        
            
        settings_lst=[bgg,txt,flp,bt,pmo]

        l1=tkinter.messagebox.showwarning(Warning,'CHANGES MADE')
        f1=open('SETTINGS.bin','wb')
        pickle.dump(settings_lst,f1)
        f1.close()
        try:
            if True==bool(stt.winfo_exists()):
                stt.withdraw()
            else:
                pass
        except NameError:
            pass
        settings()
        

def settings():
    try:
        if True==bool(mdw.winfo_exists()):
            mdw.withdraw()
        else:
            pass
    except NameError:
        pass
    try:
        if True==bool(atb.winfo_exists()):
            atb.withdraw()
        else:
            pass
    except NameError:
        pass
    try:
        if True==bool(tca.winfo_exists()):
            tca.withdraw()
        else:
            pass
    except NameError:
        pass

    bg,tg=wnd()


    global stt
    stt=Toplevel(root)
    stt.title('SETTINGS')
    stt.geometry("1000x1000")
    stt.minsize(1000,1000)
    stt.maxsize(1000,1000)
    stt.configure(bg=bg)
    
    img1= Image.open("back.png")
    rimg1= img1.resize((30,25))
    nimg1= ImageTk.PhotoImage(rimg1)
    illg1= Label(stt,image=nimg1)
    illg1.photo=nimg1
    button1= Button(stt,image=nimg1,command=lambda:main_wind(),bg=bg,relief='flat',activebackground=tg).place(x=0,y=0)
    

    sbt,pmo=tkinter.StringVar(),tkinter.IntVar()
    
    lg1=tkinter.Label(stt,text='SETTINGS',bg=bg,fg=tg,font=('Arial bold',22)).place(x=450,y=20)
        
    lg3=tkinter.Label(stt,text='Colour of the window',bg=bg,fg=tg,font=('Arial',14)).place(x=25,y=180)
    lg3=tkinter.Label(stt,text='Colour of the text',bg=bg,fg=tg,font=('Arial',14)).place(x=25,y=260)
    lg3=tkinter.Label(stt,text='Folder to select music',bg=bg,fg=tg,font=('Arial',14)).place(x=25,y=340)
    lg3=tkinter.Label(stt,text='Silence Between tracks',bg=bg,fg=tg,font=('Arial',14)).place(x=25,y=420)
    lg3=tkinter.Label(stt,text='Don\'t play music one after the other',bg=bg,fg=tg,font=('Arial',14)).place(x=25,y=500)
    
    
    erad2=tkinter.Entry(stt,textvariable=sbt,fg=tg,bg=bg,font=('Arial',14),width=3).place(x=290,y=420)
    
    eg1=tkinter.Button(stt,command=lambda:tac(),text='TERMS & CONDITION',bg=bg,fg=tg,bd=2,font=('Arial',12),relief="flat").place(x=280,y=780)
    eg1=tkinter.Button(stt,command=lambda:abt(),text='ABOUT',bg=bg,fg=tg,bd=2,font=('Arial',12),relief="flat").place(x=525,y=780)
    
    co=tkinter.Checkbutton(stt,variable=pmo,onvalue=1,offvalue=0,padx=8,pady=8,fg=tg,bg=bg,font=('Arial',10)).place(x=305,y=500)
    
    
    eg1=tkinter.Button(stt,command=lambda:bgcl(1),text='CHOOSE',bg=bg,fg=tg,bd=2,font=('Arial',14)).place(x=290,y=180)
    eg2=tkinter.Button(stt,command=lambda:tcl(1),text='CHOOSE',bg=bg,fg=tg,bd=2,font=('Arial',14)).place(x=290,y=260)
    eg2=tkinter.Button(stt,command=lambda:bfs(1),text='CHOOSE',bg=bg,fg=tg,bd=2,font=('Arial',14)).place(x=290,y=340)

    sst=partial(save_stttings,sbt,pmo)
    bg2=tkinter.Button(stt,text='SAVE',command=lambda:sst(),bg=bg,fg=tg,font=('Arial',14)).place(x=450,y=650)


def pl_files():
    pnf.clear()
    nm=os.path.dirname(os.path.abspath("GYMKANNA.py"))
    fls=os.listdir(nm)
    msc=[]
    for i in fls:
        if 'pln.bin' in i:
            pnf.append(i)
    global pfront,prear
    prear,pfront=len(pnf)-1,0


def main_wind():
    root.withdraw()
    try:
        if True==bool(stt.winfo_exists()):
            stt.withdraw()
        else:
            pass
    except NameError:
        pass
    try:
        if True==bool(ple.winfo_exists()):
            ple.withdraw()
        else:
            pass
    except NameError:
        pass
    pl_files()
    bg,tg=wnd()
    global mdw
    mdw=Toplevel(root)
    mdw.title('SETTINGS')
    mdw.geometry("1000x1000")
    mdw.minsize(1000,1000)
    mdw.maxsize(1000,1000)
    mdw.configure(bg=bg)
    
    img1= Image.open("back.png")
    rimg1= img1.resize((30,25))
    nimg1= ImageTk.PhotoImage(rimg1)
    illg1= Label(mdw,image=nimg1)
    illg1.photo=nimg1
    button1= Button(mdw,image=nimg1,command=lambda:main_wind(),bg=bg,relief='flat',activebackground=tg,state='disabled').place(x=0,y=0)

    img2= Image.open("SETTINGS.png")
    rimg2= img2.resize((30,25))
    nimg2= ImageTk.PhotoImage(rimg2)
    illg2= Label(mdw,image=nimg2)
    illg2.photo=nimg2
    button1= Button(mdw,image=nimg2,command=lambda:settings(),bg=bg,relief='flat',activebackground=tg).place(x=960,y=0)
    
    button1= Button(mdw,text="EDIT PLAYLIST",command=lambda:pledit_wind(),bg=bg,relief='flat',activebackground=bg,fg=tg,font=('Arial Bold',14)).place(x=430,y=760)
    
    lg3=tkinter.Label(mdw,text='PLAYLISTS',bg=bg,fg=tg,font=('Arial',34)).place(x=350,y=20)
    if len(pnf)==0:
        lg3=tkinter.Label(mdw,text='NO PLAYLIST EXISTS',bg=bg,fg=tg,font=('Arial',34)).place(x=250,y=320)
    xp,yp,te=50,200,0
    for i in pnf:
        button1= Button(mdw,text=i.replace('pln.bin',""),command=lambda:cpl(i),bg=bg,fg=tg,font=('Arial',24)).place(x=xp,y=yp)
        xp+=450
        te+=1
        if te/3==0:
            yp+=250
    
    
def pledit_wind():
    try:
        if True==bool(mdw.winfo_exists()):
            mdw.withdraw()
        else:
            pass
    except NameError:
        pass
    global ple
    ple=Toplevel(root)
    bg,tg=wnd()
    ple.configure(bg=bg)
    ple.geometry("315x150")
    ple.minsize(315,150)
    ple.maxsize(315,150)
    img1= Image.open("back.png")
    rimg1= img1.resize((30,25))
    nimg1= ImageTk.PhotoImage(rimg1)
    illg1= Label(ple,image=nimg1)
    illg1.photo=nimg1
    button1= Button(ple,image=nimg1,command=lambda:main_wind(),bg=bg,relief='flat',activebackground=tg).place(x=0,y=0)
    
    plnm=tkinter.StringVar()
    
    brad1=tkinter.Button(ple,text='ADD SONGS/CREATE PLAYLIST',fg=tg,bg=bg,font=('Arial',13),command=lambda:files()).place(x=15,y=40)
    brad1=tkinter.Button(ple,text='DELETE SONGS FROM PLAYLIST',fg=tg,bg=bg,font=('Arial',13),command=lambda:ply_del_cho()).place(x=10,y=90)   


def delply(mn):
    temp1.clear()
    f=open(mn,'rb')
    ply=pickle.load(f)
    f.close()
    k,h=0,0;
    for i in mad3:
        if i.get()==0:
            temp1.append(ply[k])
            h=1
        k+=1
    ply.clear()
    for i in temp1:
        ply.append(i)
    if h==0:
        l1=tkinter.messagebox.showwarning(Warning,'NO SONG IS SELECTED')
        try:
            if True==bool(pdc.winfo_exists()):
                pdc.withdraw()
            else:
                pass
        except NameError:
            pass
        ply_del_cho()
    if h==1:
        
        f=open(mn,"wb")
        pickle.dump(ply,f)
        f.close()
        messagebox.showinfo("information","THE SONG IS DELETED")
        try:
            if True==bool(pdc.winfo_exists()):
                pdc.withdraw()
            else:
                pass
        except NameError:
            pass
        try:
            if True==bool(mdw.winfo_exists()):
                mdw.withdraw()
            else:
                pass
        except NameError:
            pass
        try:
            if True==bool(psl.winfo_exists()):
                psl.withdraw()
            else:
                pass
        except NameError:
            pass
        try:
            if True==bool(mvw.winfo_exists()):
                mvw.withdraw()
            else:
                pass
        except NameError:
            pass
        try:
            if True==bool(ple.winfo_exists()):
                ple.withdraw()
            else:
                pass
        except NameError:
            pass
        try:
            if True==bool(ple.winfo_exists()):
                ple.withdraw()
            else:
                pass
        except NameError:
            pass
        main_wind()    


def playdel():
    print(pnf)
    k,ch=0,0
    for i in range(0,len(mdl)):
        if k==0 and mdl[i].get()==1:
            print(i)
            mn=i
            k=1
        elif(mdl[i].get()==1 and k==1):
            ch=2
    if ch==2:
        messagebox.showinfo("WARNING","MULTIPLE PLAYLIST IS SELECTED")
    else:
        mn=pnf[mn]
        if os.stat(mn).st_size==0:
            p=1
        else:
            p=0
            
        if p==0:
            global pld
            pld=Toplevel(root)
            pld.state('zoomed')
            bg,tg=wnd()
            pld.configure(bg=bg)
            tf,df=0,0
            f=open(mn,'rb')
            pl=pickle.load(f)
            for i in range(0,len(pl)):
                x=tkinter.IntVar()
                mad3.append(x)
            j=0
            for i in pl:
                co=tkinter.Checkbutton(pld,text=i,variable=mad3[j],onvalue=1,offvalue=0,padx=8,pady=8,fg=tg,bg=bg,font=('Arial',10)).place(x=tf,y=df)
                df+=50
                j+=1
                
            eo1=tkinter.Button(pld,text='DELETE',font=('Arial bold',11),fg=tg,bg=bg,command=lambda:delply(mn)).place(x=450,y=600)
        else:
            messagebox.showinfo("WARNING","PLAYLIST IS EMPTY")
            try:
                if True==bool(pdc.winfo_exists()):
                    pdc.withdraw()
                else:
                    pass
            except NameError:
                pass
            ply_del_cho()
            

def ply_del_cho():
    try:
        if True==bool(ple.winfo_exists()):
            ple.withdraw()
        else:
            pass
    except NameError:
        pass
    pl_files()
    mdl.clear()
    bg,tg=wnd()
    global pdc
    pdc=Toplevel(root)
    pdc.title('PLAYLIST')
    pdc.geometry("500x200")
    pdc.minsize(500,300)
    pdc.maxsize(500,300)
    pdc.configure(bg=bg)
    
    img1= Image.open("back.png")
    rimg1= img1.resize((30,25))
    nimg1= ImageTk.PhotoImage(rimg1)
    illg1= Label(pdc,image=nimg1)
    illg1.photo=nimg1
    button1= Button(pdc,image=nimg1,command=lambda:main_wind(),bg=bg,relief='flat',activebackground=tg,state='disabled').place(x=0,y=0)

    img2= Image.open("SETTINGS.png")
    rimg2= img2.resize((30,25))
    nimg2= ImageTk.PhotoImage(rimg2)
    illg2= Label(pdc,image=nimg2)
    illg2.photo=nimg2
    button1= Button(pdc,image=nimg2,command=lambda:settings(),bg=bg,relief='flat',activebackground=tg).place(x=960,y=0)
    
    lg3=tkinter.Label(pdc,text='PLAYLISTS',bg=bg,fg=tg,font=('Arial',34)).place(x=150,y=20)
    for i in pnf:
        x=tkinter.IntVar()
        mdl.append(x)
    xp,yp,te=50,100,0
    for i in range(0,len(pnf)):
        co=tkinter.Checkbutton(pdc,text=pnf[i].replace("pln.bin",""),variable=mdl[i],onvalue=1,offvalue=0,padx=8,pady=8,fg=tg,bg=bg,font=('Arial',16)).place(x=xp,y=yp)
        xp+=100
        te+=1
        if te/4==0:
            yp+=190
    eo1=tkinter.Button(pdc,text='CHOOSE',font=('Arial bold',11),fg=tg,bg=bg,command=lambda:playdel()).place(x=200,y=250)


def msdl(pl):
    if pl is not None:
        global msd
        msd=Toplevel(root)
        msd.state('zoomed')
        bg,tg=wnd()
        msd.configure(bg=bg)
        tf,df=0,0
        for i in range(0,len(msc)):
            x=tkinter.IntVar()
            mad.append(x)
        for i in range(0,len(msc)):
            co=tkinter.Checkbutton(msd,text=msc[i][0:20],variable=mad4[i],onvalue=1,offvalue=0,padx=8,pady=8,fg=tg,bg=bg,font=('Arial',10)).place(x=tf,y=df)
            df+=50

        eo1=tkinter.Button(msd,text='DELETE',font=('Arial bold',11),fg=tg,bg=bg,command=lambda:plysel()).place(x=450,y=600)
        
    else:
        pass
        

def msdp():
    global msp
    msp=Toplevel(root)
    bg,tg=wnd()
    msp.configure(bg=bg)
    msp.geometry("250x100")
    msp.minsize(250,200)
    msp.maxsize(250,200)
    
    pl=tkinter.StringVar()
    
    erad2=tkinter.Entry(msp,textvariable=pl,fg=tg,bg=bg,font=('Bahnschrift SemiLight',11)).place(x=80,y=10)
    lrad1=tkinter.Label(msp,text='PlaylistName',fg=tg,bg=bg,font=('Arial bold',11)).place(x=0,y=10)
    cp=partial(msdl,pl.get())
    brad1=tkinter.Button(msp,text='ADD',fg=tg,bg=bg,font=('Arial',11),command=lambda:cp()).place(x=190,y=40)
    

def files():
    f=open('SETTINGS.bin','rb')
    g=pickle.load(f)
    nm=g[2]
    fls=os.listdir(nm)
    msc=[]
    for i in fls:
        if '.mp3' in i:
            msc.append(i)
    print(msc)
    f.close()
    f=open('MUSIC.bin','wb')
    pickle.dump(msc,f)
    f.close()
    mscvw()

    
def plyadd(pnm):
    f=open('MUSIC.bin','rb')
    msc=pickle.load(f)
    f.close()
    nm=os.path.dirname(os.path.abspath("GYMKANNA.py"))
    fls=os.listdir(nm)
    h=0
    for i in fls:
        if (pnm.get()+'pln.bin')==i:
            h=1
            fl=i
    
    if h==1:
        if os.stat(fl).st_size==0:
            x=[]
        else:
            f=open(fl,'rb')
            x=pickle.load(f)
            f.close()
        
    else:
        x=[]
        fl=pnm.get()+'pln.bin'
        
    for i in range(0,len(msc)):
        if mad[i].get()==1:
            if mad[i] not in x:
                x.append(msc[i])
    
    f=open(fl,'wb')
    pickle.dump(x,f)
    f.close()
    try:
        if True==bool(mdw.winfo_exists()):
            mdw.withdraw()
        else:
            pass
    except NameError:
        pass
    try:
        if True==bool(psl.winfo_exists()):
            psl.withdraw()
        else:
            pass
    except NameError:
        pass
    try:
        if True==bool(mvw.winfo_exists()):
            mvw.withdraw()
        else:
            pass
    except NameError:
        pass
    try:
        if True==bool(ple.winfo_exists()):
            ple.withdraw()
        else:
            pass
    except NameError:
        pass
    main_wind()


def plysel():
    global psl
    psl=Toplevel(root)
    bg,tg=wnd()
    psl.configure(bg=bg)
    psl.geometry("315x110")
    psl.minsize(315,110)
    psl.maxsize(315,110)
    
    plnm=tkinter.StringVar()
    
    erad2=tkinter.Entry(psl,textvariable=plnm,fg=tg,bg=bg,font=('Bahnschrift SemiLight',11))
    erad2.place(x=120,y=10)
    erad2.focus()
    
    lrad1=tkinter.Label(psl,text='PlaylistName',fg=tg,bg=bg,font=('Arial bold',11)).place(x=20,y=10)
    lrad1=tkinter.Label(psl,text='*If the playlist doesn\'t exist, A new one will be created',fg=tg,bg=bg,font=('Arial bold',8)).place(x=5,y=90)
    cp=partial(plyadd,plnm)
    brad1=tkinter.Button(psl,text='ADD',fg=tg,bg=bg,font=('Arial',11),command=lambda:cp()).place(x=130,y=40)


def mscvw():
    global mvw
    mvw=Toplevel(root)
    mvw.state('zoomed')
    bg,tg=wnd()
    mvw.configure(bg=bg)
    tf,df=0,0
    f=open('MUSIC.bin','rb')
    msc=pickle.load(f)
    samp=tkinter.IntVar()
    for i in range(0,len(msc)):
        x=tkinter.IntVar()
        mad.append(x)
    for i in range(0,len(msc)):
        co=tkinter.Checkbutton(mvw,text=msc[i][0:20],variable=mad[i],onvalue=1,offvalue=0,padx=8,pady=8,fg=tg,bg=bg,font=('Arial',10)).place(x=tf,y=df)
        df+=50
    
    eo1=tkinter.Button(mvw,text='ADD',font=('Arial bold',11),fg=tg,bg=bg,command=lambda:plysel()).place(x=450,y=600)


def shufbck():
    tp=bstack.pop(-1)
    pygame.mixer.music.load(tp)
    pygame.mixer.music.play()
    audio = MP3(tp)
    audio_info = audio.info 
    length = int(audio_info.length)
    bstack.append(tp)
    f=open("SETTINGS.bin","rb")
    g=pickle.load(f)
    g=int(g[-2])
    root.after(1000*length+g, check_music_end)


def back_button():
    global sh,qu
    if sh==1:
        lrad2.destroy()
        shufbck()
    if qu==1:
        global front
        front-=1
        if (front+1)!=rear+1:
            button123.config(state=NORMAL)
        if front==0:
            button456.config(state="disabled")
        lrad1.destroy()
        play()


def forw_button():
    global sh,qu
    if sh==1:
        lrad2.destroy()
        play()
    if qu==1:
        global front
        front+=1
        if front!=0:
            button456.config(state=NORMAL)
        lrad1.destroy()
        play()
   

def pause():
    if len(ps)%2==0:
        pygame.mixer.music.pause()	
    else:
        pygame.mixer.music.unpause()
    ps.append(1)
    

def check_music_end():
    f=open('SETTINGS.bin','rb')
    g=pickle.load(f)
    f.close()
    if g[-1]==0:
        global front,rear
        if front!=0:
            button456.config(state=NORMAL)
        if (front+1)!=rear+1:
            button123.config(state=NORMAL)
        if front==0:
            button456.config(state="disabled")
        lrad1.destroy()
        lrad2.destroy()
        play()
        front+=1
    else:
        pass
    

def play():
    bg,tg=wnd()
    global lrad1,lrad2
    lrad2=tkinter.Label(pwd,text='',fg=tg,bg=bg,font=('Arial bold',10))
    lrad2.place(x=100,y=7)
    lrad1=tkinter.Label(pwd,text='',fg=tg,bg=bg,font=('Arial bold',10))
    lrad1.place(x=100,y=7)
    if ch[0]==1:
        global front,length
        if(front<rear+1):
            lrad2.destroy()
            pygame.mixer.music.load(temp[front])
            pygame.mixer.music.play()
            lrad1['text']=temp[front]
            audio = MP3(temp[front])
            audio_info = audio.info 
            length = int(audio_info.length)
            tp=front+1
            if tp==rear+1:
                button123.config(state="disabled")
            f=open("SETTINGS.bin","rb")
            g=pickle.load(f)
            print("223",g[-2])
            h=int(g[-2])
            root.after(1000*length+h, check_music_end)
                
    elif ch[0]==0:
        lrad1.destroy()
        rnd=random.randint(0,len(temp)-1)
        pygame.mixer.music.load(temp[rnd])
        pygame.mixer.music.play()
        lrad2["text"]=temp[rnd]
        audio = MP3(temp[rnd])
        audio_info = audio.info 
        length = int(audio_info.length)
        bstack.append(temp[rnd])
        f=open("SETTINGS.bin","rb")
        g=pickle.load(f)
        h=int(g[-2])
        root.after(1000*length+h, check_music_end)


def playwind(a,b,p):
    try:
        if True==bool(pls.winfo_exists()):
            pls.withdraw()
        else:
            pass
    except NameError:
        pass
    global pwd
    pwd=Toplevel(root)
    lms()
    sh=a.get()
    qu=b.get()
    pwd.geometry("750x50")
    pwd.minsize(750,100)
    pwd.maxsize(750,100)
    bg,tg=wnd()
    pwd.configure(bg=bg)
    
    img= Image.open("back.png")
    rimg= img.resize((40,25))
    nimg= ImageTk.PhotoImage(rimg)
    illg= Label(pwd,image=nimg)
    illg.photo=nimg
    global button456
    button456= Button(pwd,image=nimg,command=lambda:back_button(),bg=bg,relief='flat',activebackground=bg,fg=tg,state="disabled")
    button456.place(x=0,y=7)
    
    img= Image.open("forw.png")
    rimg= img.resize((40,25))
    nimg= ImageTk.PhotoImage(rimg)
    illg= Label(pwd,image=nimg)
    illg.photo=nimg
    global button123
    button123= Button(pwd,image=nimg,command=lambda:forw_button(),bg=bg,relief='flat',activebackground=bg,fg=tg)
    button123.place(x=705,y=7)
    
    
    img= Image.open("pause.png")
    rimg= img.resize((40,25))
    nimg= ImageTk.PhotoImage(rimg)
    illg= Label(pwd,image=nimg)
    illg.photo=nimg
    global button789
    button789= Button(pwd,image=nimg,command=lambda:pause(),bg=bg,relief='flat',activebackground=bg,fg=tg)
    button789.place(x=350,y=60)
    
    f=open(p,'rb')
    ply=pickle.load(f)
    f.close()


def plsh(pl):
    global front,rear
    temp.clear()    
    ch[0]=0
    
    if len(pl)==0:
        l1=tkinter.messagebox.showwarning(Warning,'NO MUSIC IN THE PLAYLIST')
    else:
        for i in pl:
            temp.append(i)
        front=0
        rear=len(temp)-1
        play()


def plqu(pl):
    global front,rear
    temp.clear()    
    ch[0]=1
    
    print(pl)
    if len(pl)==0:
        l1=tkinter.messagebox.showwarning(Warning,'NO MUSIC IN THE PLAYLIST')
    else:
        for i in pl:
            temp.append(i)
        front=0
        rear=len(temp)-1
        play()
                        

def lms():
    global sh,qu
    sh=s.get()
    qu=q.get()
    f=open(p,'rb')
    ply=pickle.load(f)
    f.close()

    if qu==1 and sh==1:
        l1=tkinter.messagebox.showwarning(Warning,'BOTH OPTIONS ARE SELECTED')
    elif qu==0 and sh==0:
        l1=tkinter.messagebox.showwarning(Warning,'NO OPTIONS IS SELECTED')
        main_wind()
    elif qu==1 and sh==0:
        plqu(ply)
    elif sh==1 and qu==0:
        plsh(ply)


def cpl(p1):
    global pls
    pls=Toplevel(root)
    pls.geometry("250x100")
    bg,tg=wnd()
    pls.configure(bg=bg)
    samp=tkinter.IntVar()
    global s,q,p
    p=p1
    s,q=tkinter.IntVar(),tkinter.IntVar()
    co=tkinter.Checkbutton(pls,text="SHUFFLE",variable=s,onvalue=1,offvalue=0,padx=8,pady=8,fg=tg,bg=bg,font=('Arial',10)).place(x=0,y=0)
    co=tkinter.Checkbutton(pls,text="QUEUE",variable=q,onvalue=1,offvalue=0,padx=8,pady=8,fg=tg,bg=bg,font=('Arial',10)).place(x=100,y=0)
    playwnd=partial(playwind,s,q,p)
    eo1=tkinter.Button(pls,text='SELECT',font=('Arial bold',11),fg=tg,bg=bg,command=lambda:playwnd()).place(x=70,y=60)



main_wind()
mainloop()
pygame.QUIT