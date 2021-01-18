# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 22:00:42 2020

@author: Mounika
"""


processeslist=[]
burstlist=[]
arrivallist=[]


n=int(input("Enter Number of Processes:"))

for i in range(0,n):
    print("Enter ProcessId for process",(i+1),"is:")
    pid=input()
    processeslist.append(pid)
    
    
    
for i in range(0,n):
    print("Enter BurstingTime for ProcessId",processeslist[i],"is:")
    bt1=int(input())
    burstlist.append(bt1)

    

for i in range(0,n):
    print("Enter Arrival Time for ProcessId",processeslist[i],"is:")
    at1=int(input())
    arrivallist.append(at1)
    a_list=sorted(arrivallist)
   
sum = arrivallist[0]
completion_time = []
completion_time.append(sum)
for i in range(0, len(burstlist)):
    sum += burstlist[i]
    completion_time.append(sum)
print("The Gantt chart value is:",completion_time)


wtime = []
tat = []
for i in range(0, len(burstlist)):
    if (completion_time[i] - arrivallist[i]) <= 0:
        wtime.append(0)
    else:
        wtime.append(completion_time[i] - arrivallist[i])
        
    if (completion_time[i+1] - arrivallist[i]) <= 0:
        tat.append(0)
    else:
        tat.append(completion_time[i+1] - arrivallist[i])
    

avgwt = 0
avgtat = 0
for i in range(0, len(wtime)):
    avgwt += wtime[i]
    avgtat += tat[i]
print("Pro\tBT\tAT\tW",  
          "T\tTAT\tCT") 
  
for i in range(n): 
        
        print( processeslist[i], "\t", burstlist[i], "\t", arrivallist[i],  
              "\t", wtime[i], "\t", tat[i], "\t", completion_time[i+1])

print("\nWaiting time:",avgwt)
print("\nAverage of waiting time:",avgwt/len(burstlist))
print("\nTurn around Time:",avgtat)
print("\nAverage of turnover around time:",avgtat/len(burstlist)) 


print("\n\n\nGantt chart")
t=[]
for i in range(0,len(wtime)):
    t.append(completion_time[i+1])
    
    
print(t)
import plotly.graph_objects as go

fig = go.Figure(go.Waterfall(
    name = "20", orientation = "v", measure = ["absolute", "absolute","absolute","absolute","absolute"],
    x = processeslist,
    y = t

   ))
fig.update_layout(
        title = "Gantt chart"
)
fig.write_html('fcfs.html', auto_open=True)

fig.show()
