#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
with open('bill_data.txt','r+') as f:
    lines=f.read() # read as one string 
    a=[]
    b=[]
    c=['Jan','Feb','March','April','May','June','July','Aug','Sep','Oct','Nov','Dec','march','Imp']
    d=[]
    lines=lines.split('\n') #split by \n
    print(lines)
    for i in range(0,len(lines)):
        p=lines[i]
        a.append(p.replace(" ",""))
    
    print(a)
    for j in range(0,len(a)):
        for p in range(0,len(c)):
            if a[j].count(c[p])==0:
                pass
            else:
                b.append(a[j])
                
        
    
    print(d,end='\n')
    print(b)
    df=[]
     
    for z in range(0,len(b)):
        df.append(b[z].split(':'))
    print(df)

    dfd = pd.DataFrame(df,columns=['Month','Total','Food','Transport','Ex'])
    print(type(dfd['Total'][0]))
    
    
    #dfd.fillna(0)
            
    dfd.to_excel('result.xlsx',header=True)


# In[16]:


gh=dfd['Total'][14:]
hj=[]
for i in gh:
    hj.append(i.split('+'))

print(hj[0])
hj1=[]
c=('t','s')
hj2=[]
hj3=[]
print(type(c))
for i in range(0,len(hj)):
    for j in range(0,len(hj[i])):
        if hj[i][j].endswith(c):
            hj1.append(hj[i][j])
        if hj[i][j].endswith('d'):
            hj2.append(hj[i][j])
        if hj[i][j].endswith('x'):
            hj3.append(hj[i][j])
            
            

print(hj1)
print(hj2)
print(hj3)
hj4=[]
hj6=[]
for i in range(0,len(hj1)):
    hj4.append(hj1[i].split('transport'))
    hj6.append(hj1[i].split('bus'))

print(hj4)
print(hj6)
hj5=[]

for i in range(0,len(hj4)):
    if len(hj4[i])==2:
        hj5.append(hj4[i][0])

print(hj5)
hj7=[]
for i in range(0,len(hj6)):
    if len(hj6[i])==2:
        hj7.append(hj6[i][0])

print(hj7)
hj8=hj5+hj7
print(hj8)
sum_t=0
for i in hj8:
    sum_t+=int(i)

print(sum_t)
hj9=[]
for i in range(0,len(hj2)):
    hj9.append(hj2[i].split('food'))
    

print(hj9)

hj10=[]

for i in range(0,len(hj9)):
    if len(hj9[i])==2:
        hj10.append(hj9[i][0])

print(hj10)



sum_f=0
for i in hj10:
    sum_f+=int(i)

print(sum_f)


hj11=[]
for i in range(0,len(hj3)):
    hj11.append(hj3[i].split('ex'))
    

print(hj11)
hj12=[]

for i in range(0,len(hj11)):
    if len(hj11[i])==2:
        hj12.append(hj11[i][0])

print(hj12)



sum_e=0
for i in hj12:
    sum_e+=int(i)

print(sum_e)

tot=sum_t+sum_f+sum_e

dfd1=pd.read_excel('result.xlsx',index_col=0)
dfd1.append({'Month':'March','Total':tot,'Food':sum_f,'Transport':sum_t,'Ex':sum_e},ignore_index='True')

print(dfd1)


# In[10]:





# In[21]:


help(pd.io.excel)


# In[3]:


import xlsxwriter
workbook = xlsxwriter.Workbook('result.xlsx')
print(workbook)
worksheet=workbook.worksheets()
print(worksheet)
chart1 = workbook.add_chart({'type': 'column'})
print(chart1)
chart1.add_series({ 
    'Month':       '= Sheet1!$B$2:$B$11', 
    'Total': '= Sheet1!$C$2:$C$11',
    }) 
chart1.set_title({'name':'Total Expenses'})
chart1.set_x_axis({'name':'Months'})
chart1.set_y_axis({'name':'Total'})
worksheet.insert_chart('H2', chart1)
workbook.close()


# In[ ]:




