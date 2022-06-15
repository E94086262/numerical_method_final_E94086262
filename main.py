#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import messagebox
#import random
import os
#import time
win=tk.Tk()
win.title('食物選擇')
win.geometry('600x850')


# In[2]:


import pandas as pd
from pandas import DataFrame
import numpy as np
#from Knapsack_Problem_exercise import *
data = pd.read_excel('最佳清單.xlsx', sheet_name='工作表1') 
def excel_editer (t1:str , t2:str ,t4:str):
    global count
    global list1
    global data
    data = pd.read_excel('最佳清單.xlsx', sheet_name='工作表1')
    t1=t1.strip()
    t2=t2.strip()
    t4=t4.strip()
    count=data.shape[0]
    if((t1=='')or(t2=='')or(t4=='')):
        label_1.config(text='請輸入完整')
    elif((t2.isdigit()==False) or (t4.isdigit()==False)):
        label_1.config(text='第二或第三輸入欄只接受數字')
    else:
        data = pd.read_excel('最佳清單.xlsx', sheet_name='工作表1')
        data.loc[count]=[t1+' /',t2+'元','/ '+t4]
        data.to_excel('最佳清單.xlsx', sheet_name='工作表1' , index=False, header=True)
        print(data)
        data_n=data.iloc[count]
        data_n=np.array(data_n)
        data_n=str(data_n).replace("'"," ")
        data_n=data_n.replace("["," ")
        data_n=data_n.replace("]"," ")
        label_1.config(text='當前輸入:' + data_n)
        count+=1
        list1.append(data_n)
        mylistbox = tk.Listbox(win)
        for i in range(0,count):
            mylistbox.insert(tk.END, str(i+1)+'. '+list1[i])
        mylistbox.place(x=150,y=500,width=150,height=300)
    
def excel_re_enter():
    global count
    global data
    global list1
    count=data.shape[0]
    data = pd.read_excel('最佳清單.xlsx', sheet_name='工作表1')
    if(count>0):
        count=count-1
        data=data.drop([count],axis=0)
        list1.pop()
        data.to_excel('最佳清單.xlsx', sheet_name='工作表1' , index=False, header=True)
        print(data)
        if(count>0):
            data = pd.read_excel('最佳清單.xlsx', sheet_name='工作表1')
            mylistbox = tk.Listbox(win)
            for i in range(0,count):
                mylistbox.insert(tk.END, str(i+1)+'. '+list1[i])
            mylistbox.place(x=150,y=500,width=150,height=300)
            #data_n=data.iloc[count-1]
            #data_n=np.array(data_n)
            #data_n=str(data_n).replace("'"," ")
            label_1.config(text='請重新輸入')
            
        else:
            label_1.config(text='已無商品')
            count=0
            list1=[]
            mylistbox = tk.Listbox(win)
            mylistbox.insert(tk.END, '')
            mylistbox.place(x=150,y=500,width=150,height=300)
            
    else:
        label_1.config(text='已無商品')
def excel_delete(a):
    global count
    global data
    global list1
    count=data.shape[0]
    print(type(a))
    print(isinstance(a,int))
    a=a.strip()
    if((a=='')):
        label_1.config(text='請輸入有效數字(刪除)')
        
    elif(a.isdigit()==False):
        label_1.config(text='請輸入有效數字(刪除)')
        
    else:
        if(count<=0):
            label_1.config(text='已無商品')
        else:
            a=int(a)
            data = pd.read_excel('最佳清單.xlsx', sheet_name='工作表1')
            data=data.drop([a-1],axis=0)
            list1.pop(a-1)
            data.to_excel('最佳清單.xlsx', sheet_name='工作表1' , index=False, header=True)
            count-=1
            data = pd.read_excel('最佳清單.xlsx', sheet_name='工作表1')
            mylistbox = tk.Listbox(win)
            for i in range(0,count):
                mylistbox.insert(tk.END, str(i+1)+'. '+list1[i])

            mylistbox.place(x=150,y=500,width=150,height=300)
            label_1.config(text='已刪除')
    
    
#def open_excel():
   # os.system(r"C:\Users\user\商品價格.xlsx")
    
def excel_clean():
    global data
    global count
    global list1
    data = pd.read_excel('最佳清單.xlsx', sheet_name='工作表1')
    a=data.shape[0]
    for i in range(a-1,-1,-1):
        data=data.drop([i],axis=0)
        data.to_excel('最佳清單.xlsx', sheet_name='工作表1' , index=False, header=True)
    label_1.config(text=' ')
    count=0
    list1=[]
    mylistbox = tk.Listbox(win)
    mylistbox.insert(tk.END, '')
    mylistbox.place(x=150,y=500,width=150,height=300)
    
        


# In[3]:


def get_text_input1(): # event of text input
    
    t1 = text_1.get("1.0", tk.END+"-1c") #to include all text box and not to read \n
    t2 = text_2.get("1.0", tk.END+"-1c")
    t4 = text_4.get("1.0", tk.END+"-1c")
    #print(t1)
    #print(t2)
    print(type(t4))
    text_1.delete("1.0","end")
    text_2.delete("1.0","end")
    text_4.delete("1.0","end")
    
    excel_editer(t1,t2,t4)
    #station_input = t1 + "," + t2 # just one string
    #fare_check(station_input)
def get_text_input2():
    t3=text_3.get("1.0", tk.END+"-1c")
    
    text_3.delete("1.0","end")
    excel_delete(t3)
    
def get_entry():
    t5=text_5.get("1.0", tk.END+"-1c")
    text_5.delete("1.0","end")
    gpa(t5)
    


# In[4]:


def gpa(capacity:str):
    data = pd.read_excel('最佳清單.xlsx', sheet_name='工作表1')
    if(capacity.strip()==''):
        label_1.config(text='請輸入有效數字(預算)')
    elif(capacity.isdigit()==False):
        label_1.config(text='請輸入有效數字(預算)')
    else:
        capacity=int(capacity)
        a=data.shape[0]

        calculate=0
        for i in range(0,a):
            list_item.append(data.iloc[i][0].strip('/'))
            data_fare=data.iloc[i][1].strip('元')
            list_fare.append(int(data_fare))
            list_favor.append(int(data.iloc[i][2].strip('/')))
        for k in range(0,a):
            if(list_fare[k]<=capacity):
                calculate=1
                break
            else:
                pass

        if(calculate==1):
            items_control(a,capacity, list_item , list_fare, list_favor)
        elif((list_item==[])or(list_fare==[])or(list_favor==[])):
            #mylistbox = tk.Listbox(win)
            #mylistbox.insert(tk.END, '    您沒有輸入任何商品')
            #mylistbox.place(x=150,y=500,width=150,height=300)
            label_1.config(text='您沒有輸入任何商品')
        else:
            mylistbox = tk.Listbox(win)
            mylistbox.insert(tk.END, '  預算不足以買任何商品!')
            mylistbox.place(x=150,y=500,width=150,height=300)


# In[5]:


def knapsack(i, j):
    if i == 0 :
        return {}
    if items[i][j] > items[i-1][j]:
        return {i}.union(knapsack(i-1, j-weights[i]))
    else:
        return knapsack( i-1, j)
    
def items_control(numItems:int , capacity:int , foods:list , w:list, v:list): 
    global choose
    global values
    global weights 
    values=[0]
    weights=[0]
    #v=v.insert(0,0)
    #w=w.insert(0,0)
    for i in range(0,numItems):
        values.append(v[i])
        weights.append(w[i])
    
    

    print(values[1:])
    print(weights[1:])
    global items
    items= np.zeros((numItems+1, capacity+1), dtype=int)  #create a null array to receive elements of numItems and capacity

    for i in range(1, numItems+1):    #run objects
        for j in range(capacity+1): # Compare object's weight
            if weights[i] > j : #if new item is bigger than the current weight limit 
                items[i][j] = items[i-1][j]
            else :                
                items[i][j] = max(items[i-1][j], items[i-1][j-weights[i]] + values[i])

    print(items) 
    choose = list(knapsack(numItems,capacity))
    print(choose)
    print(foods)
    print(len(choose))
    print('items {', end = '')
    mylistbox = tk.Listbox(win)
    sum_fare=0
    for i in range(len(choose)):
        print(foods[choose[i]-1], end = '')
        mylistbox.insert(tk.END, str(i+1)+'.  '+foods[choose[i]-1]+' / '+str(weights[choose[i]])+'元'+' / '+str(values[choose[i]]))
        sum_fare=sum_fare+weights[choose[i]]
        if i != len(choose)-1:
            print(', ', end = '')
    print('} selected.')
    mylistbox.place(x=150,y=500,width=150,height=300)
    label_3.config(text='最佳化結果')
    label_1.config(text='共選擇'+str(len(choose))+'項商品 '+'花費'+str(sum_fare)+'元')
        

    #return items[numItems][capacity]


# In[6]:


def back():
    global list1
    global count
    mylistbox = tk.Listbox(win)
    for i in range(0,count):
        mylistbox.insert(tk.END, str(i+1)+'. '+list1[i])
    mylistbox.place(x=150,y=500,width=150,height=300)
    label_3.config(text='目前的清單')
def introduction():
    messagebox.showinfo('說明書', '基本操作: 在商品、價格和喜好度的輸入欄，將商品資訊輸入完成，價格和喜好度只接受阿拉伯數字的輸入，並且請自行決定喜好度區間，如 1~10，10代表最大喜好度。修改資料的部分，只有兩種，刪除當前輸入鈕和刪除鈕，前者可以直接刪掉剛輸入進去的資料，後者可以藉由看下面資訊欄給出的列指標，去針對某一列刪除。若想清除所有資料則只需按下。經過一系列輸入的操作後，資料數已達到需求時需求時，則可以開始最佳化，請先在預算欄輸入預算金額，再按下最佳化鈕。倘若最佳化結果出來後，覺得不符，想再修改的話，則只要按下返回鈕，就能回到最佳化之前的狀態。當最佳化結果確定之後，已不須在做修改時，則可以按下輸出鈕，此時會將結果輸出為excel檔，並關閉程式。以上感謝您的閱讀')


# In[7]:


def output():
    global choose
    global list_item
    global list_fare
    global list_favor
    excel_clean()
    data = pd.read_excel('最佳清單.xlsx', sheet_name='工作表1')
    for i in range(len(choose)):
        data.loc[i]=[list_item[choose[i]-1],str(list_fare[choose[i]-1])+'元',str(list_favor[choose[i]-1])]
        data.to_excel('最佳清單.xlsx', sheet_name='工作表1' , index=False, header=True)
    win.destroy()
    os.system('最佳清單.xlsx')
    
    
    
    
    


# In[8]:


text_1=tk.Text(win,font=('Arial',15))
text_1.place(x=110,y=50,width=250,height=50)
text_4=tk.Text(win,font=('Arial',15))
text_4.place(x=110,y=250,width=250,height=50)
text_2=tk.Text(win,font=('Arial',15))
text_2.place(x=110,y=150,width=250,height=50)
label_2=tk.Label(win,text='商品 :',font=('Arial',15))
label_2.place( x=10, y =60)
label_4=tk.Label(win,text='價格 :',font=('Arial',15))
label_4.place( x=10, y =160)
label_5=tk.Label(win,text='喜好度 :',font=('Arial',15))
label_5.place( x=10, y =260)
label_6=tk.Label(win,text='預算 :',font=('Arial',15))
label_6.place( x=370, y =520)



text_3=tk.Text(win,font=('Arial',20))
text_3.place(x=430,y=410,width=70,height=40)


text_5=tk.Text(win,font=('Arial',15))
text_5.place(x=370,y=550,width=100,height=30)

button_1=tk.Button(win,text='輸入',font=('Arial',15), command=get_text_input1)
button_1.place(x=170,y=330,width=100,height=70)
button_2=tk.Button(win,text='刪掉當前輸入',font=('Arial',15), command=excel_re_enter)
button_2.place(x=400,y=75,width=150,height=70)
button_3=tk.Button(win,text='清除所有資料',font=('Arial',15), command=excel_clean)
button_3.place(x=400,y=180,width=150,height=70)
button_4=tk.Button(win,text='刪除',font=('Arial',15), command=get_text_input2)
button_4.place(x=510,y=400,width=70,height=50)

button_5=tk.Button(win,text='最佳化',font=('Arial',15), command=get_entry)
button_5.place(x=375,y=600,width=90,height=50)

button_6=tk.Button(win,text='返回',font=('Arial',15), command=back)
button_6.place(x=375,y=675,width=90,height=50)

button_7=tk.Button(win,text='輸出',font=('Arial',15), command=output)
button_7.place(x=375,y=750,width=90,height=50)

button_8=tk.Button(win,text='說明書',font=('Arial',15), command=introduction)
button_8.place(x=475,y=10,width=70,height=40)

label_1=tk.Label(win,text=' ',font=('Arial',13))
label_1.place( x=320, y = 350)

label_3=tk.Label(win,text='目前的清單',font=('Arial',15))
label_3.place(x=175,y=460)
    
list1=[]

list_item=[]
list_fare=[]
list_favor=[]
choose=[]

excel_clean()


count=0
mylistbox = tk.Listbox(win)
mylistbox.insert(tk.END, '')
mylistbox.place(x=150,y=500,width=150,height=300)


# In[9]:


win.mainloop()


# In[ ]:




