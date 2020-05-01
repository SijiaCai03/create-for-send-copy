import csv
import pandas as pd

infile = open('Holiday Schedule Ranking 2019.csv','r')

#read data from infile
open_file = csv.reader(infile, delimiter=',')
header = next(open_file)

emp_dic = {}
for record in open_file:
    for x in range(1,14):
        record[x] = int(record[x])
    emp_dic[record[0]] = record[1:14]
 

#create the data frame
emp_data = pd.DataFrame(emp_dic)

emp_data.index = header[1:14]

emp_data['Col_sum'] = emp_data.apply(lambda x: x.sum(), axis=1)

emp_data = emp_data.sort_values(by='Col_sum', ascending=False)


#create a list for date
date = []
for x in range(13):
    date.append(emp_data.index[x])

#create dict and list for employees
empdict = {}
emplist = []
for x in range(20):
    empdict[emp_data.T.index[x]] = 0
    emplist.append(emp_data.T.index[x])


for x in range(13):
    for w in range(13):
        emp = emp_data.iloc[x].nsmallest(3)
        v1=emp.index[0]
        v2=emp.index[1]
        v3=emp.index[2]
    
    #check if there three employee already have two work days
        if empdict[v1]>=2:
            emp_data.at[date[x],v1]=100
        if empdict[v2]>=2:
            emp_data.at[date[x],v2]=100
        if empdict[v3]>=2:
            emp_data.at[date[x],v3]=100
        
    #change no work employee to 0, work employee to 1
    for y in range(20):
        emp_data.at[date[x],emplist[y]]=0
    emp_data.at[date[x],v1]=1
    emp_data.at[date[x],v2]=1
    emp_data.at[date[x],v3]=1

    #add 1 in dict by loop
    empdict[v1] += 1
    empdict[v2] += 1
    empdict[v3] += 1

#create output
print("0 = no work at that day")
print("1 = work at that day")

emp_data = emp_data.drop(['Col_sum'],axis=1).sort_index(ascending=True)
print(emp_data.T)    

emp_data.T.to_csv('Holiday Schedule By Employee.csv')








 
            










