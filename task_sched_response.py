
##avg response time fixed tiny darknet
from numpy.lib.twodim_base import tril_indices
from pickle import TRUE
import random
import time
import math
import numpy as np
import copy
import math

class Task:
    def __init__(self, id, period, deadline, computation_time, arrival_time,weight):
        self.id = id
        self.period = period
        self.deadline = deadline
        self.computation_time = computation_time
        self.arrival_time = arrival_time
        self.weight=weight


def calculate_hyperperiod(array):
    lcm = np.lcm.reduce(array)
    return lcm

def process(task_num, exec_time):
    # Code for the process
    #print(f"Task {task_num} running...")
    #time.sleep(exec_time)
    x=1

task_set = []
task_set_nt=[]

def per_gen(n):
  task_p=[]
  for i in range(n):
    t=random.randint(1,8)
    task_p.append(t)
  return task_p


##task sched for non TEE


def schedule_tasks_nt(SIMULATION_TIME,n):
    task_i=[]

    #code for response time
    taskr_a=[]
    taskr_com=[]
    taskr_p=[]
    task_ind=[]
    hold=100000000
    # Define the current time
    current_time = 0
    # Initialize the schedulability flag
    schedulable = True
    #SIMULATION_TIME=1000
    # Execute the tasks in the task set until the simulation time is reached
    while current_time < SIMULATION_TIME:
        # Find the task with the earliest deadline
        earliest_deadline = SIMULATION_TIME + 1
        task_index = -1
        #print("n", n)
        for i in range(n):

            #print("for loop", i)
            #print(task_set[i].arrival_time)
            if task_set_nt[i].arrival_time <= current_time:
                if task_set_nt[i].deadline < earliest_deadline:
                    earliest_deadline = task_set[i].deadline
                    task_index = i
                    #print("task index", i)

        # Check if a task is ready to execute

        if task_index != -1:
            task_i.append(task_set_nt[task_index].id)
            # Execute the task
            process(task_set_nt[task_index].id, task_set_nt[task_index].computation_time)
            current_time += task_set_nt[task_index].computation_time

            # Check if the task met its deadline
            if current_time <= task_set_nt[task_index].deadline:
                #print(f"Task {task_set[task_index].id} met its deadline at time {current_time}")
                x=1
            else:
                #print(f"Task {task_set[task_index].id} missed its deadline at time {current_time}")
                schedulable = False
                #current_time = SIMULATION_TIME

            # Update the arrival time of the next instance of the task
            task_ind.append(task_set_nt[task_index].id)
            #taskr_a.append(task_set[i].arrival_time)
            taskr_com.append(current_time)
            taskr_p.append(task_set_nt[task_index].period)
            # Update the arrival time of the next instance of the task
            task_set_nt[task_index].arrival_time += task_set_nt[task_index].period
            task_set_nt[task_index].deadline += task_set_nt[task_index].period
        else:
            # Wait for the next task to arrive
            #current_time += 1
            if hold==current_time:
              if current_time==int(current_time):
                current_time+=1
              else:
                current_time=math.ceil(current_time)
            hold=current_time



    # Print the schedulability of the task set
    if schedulable:
        #print("The task set is schedulable")
        x=1
    else:
        #print("The task set is not schedulable")
        x=1
    # Create an empty dictionary to store counts
    count_dict = {}
    task_arrive=[]
    # Count repetitions
    i=0
    for element in task_ind:
        if element in count_dict:
            task_arrive.append(taskr_p[i]*count_dict[element])
            count_dict[element] += 1
        else:
            task_arrive.append(taskr_p[i]*0)
            count_dict[element] = 1
        i+=1
    # Print the counts
    taskr_a=task_arrive

    #print("task_i",task_i)
    #print("task_ind",task_ind)
    #print("taskr_p", taskr_p)
    #print("taskr_a", taskr_a)

    print("taskr_com non tee", taskr_com,len(taskr_com))
    task_r=[]
    for i in range(len(taskr_p)):
      k=(taskr_com[i]-taskr_a[i])/taskr_p[i]
      if k>1:
        k=0
      task_r.append(k)

    #print("task response", task_r)
    if len(task_r)!=0:
      print("avg response time non TEE:", sum(task_r)/len(task_r))

    return 0


def schedule_tasks(SIMULATION_TIME,n,task_p):
    task_i=[]

    #code for response time
    taskr_a=[]
    taskr_com=[]
    taskr_p=[]
    task_ind=[]
    hold=100000000
    # Define the current time
    current_time = 0
    # Initialize the schedulability flag
    schedulable = True
    #SIMULATION_TIME=1000
    # Execute the tasks in the task set until the simulation time is reached
    while current_time < SIMULATION_TIME:
        # Find the task with the earliest deadline
        earliest_deadline = SIMULATION_TIME + 1
        task_index = -1
        #print("n", n)
        for i in range(n):

            #print("for loop", i)
            #print(task_set[i].arrival_time)
            if task_set[i].arrival_time <= current_time:
                if task_set[i].deadline < earliest_deadline:
                    earliest_deadline = task_set[i].deadline
                    task_index = i
                    #print("task index", i)

        # Check if a task is ready to execute

        if task_index != -1:
            task_i.append(task_set[task_index].id)
            # Execute the task
            process(task_set[task_index].id, task_set[task_index].computation_time)
            current_time += task_set[task_index].computation_time

            # Check if the task met its deadline
            if current_time <= task_set[task_index].deadline:
                #print(f"Task {task_set[task_index].id} met its deadline at time {current_time}", "arrival time",task_set[task_index].arrival_time, "deadline",task_set[task_index].deadline )
                x=1
            else:
                #print(f"Task {task_set[task_index].id} missed its deadline at time {current_time}","arrival time",task_set[task_index].arrival_time,"deadline",task_set[task_index].deadline)
                schedulable = False
                #current_time = SIMULATION_TIME

            # Update the arrival time of the next instance of the task
            task_ind.append(task_set[task_index].id)
            #taskr_a.append(task_set[i].arrival_time)
            taskr_com.append(current_time)
            #taskr_p.append(task_set[task_index].period)
            # Update the arrival time of the next instance of the task
            task_set[task_index].arrival_time += task_set[task_index].period
            task_set[task_index].deadline += task_set[task_index].period
        else:
            # Wait for the next task to arrive
            


            current_time += 1

    # Print the schedulability of the task set
    if schedulable:
        #print("The task set is schedulable")
        x=1
    else:
        #print("The task set is not schedulable")
        x=1


    for i in range(len(task_i)):
      taskr_p.append(task_p[task_i[i]-1])

    # Create an empty dictionary to store counts
    count_dict = {}
    task_arrive=[]
    # Count repetitions
    i=0

    for element in task_ind:
        if element in count_dict:
            task_arrive.append(taskr_p[i]*count_dict[element])
            count_dict[element] += 1
        else:
            task_arrive.append(taskr_p[i]*0)
            count_dict[element] = 1
        i+=1



    # Print the counts
    taskr_a=task_arrive

    #print("task_i",task_i)
    #print("task_ind",task_ind)
    #print("taskr_com", taskr_com,len(taskr_com))
    #print("taskr_a", taskr_a)
    #print("taskr_p", taskr_p)


    task_r=[]
    for i in range(len(taskr_p)):
      k=(taskr_com[i]-taskr_a[i])/taskr_p[i]
      if k>1:
        k=k
      task_r.append(k)

    #print("task response", task_r)
    if len(task_r)!=0:
      print(sum(task_r)/len(task_r))
    return schedulable, task_i, taskr_com,taskr_a,taskr_p



def task_ded_fus(k,task_i,task_avl,task_p):
  #a holds task index number
  a=task_i[k]
  #b holds task available time
  b=task_avl[k]
  #print(a,b)
  ded=task_p[a-1]
  task_deadline=b+ded

  return task_deadline
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a




def find_second_smallest(arr):
    unique_numbers = sorted(set(arr))

    if len(unique_numbers) < 2:
        return arr[0]  # Handle case when there are fewer than two unique elements

    return unique_numbers[1]

def cyclic_sched(hold_p):

  T_i=min(hold_p)
  T_j=find_second_smallest(hold_p)

  #print(T_i,T_j,hold_p)
  gcd_hold_p=gcd(T_i,T_j)
  if 2*T_i-gcd_hold_p<T_j:
    return True


#count_dict = {}
def check_and_remove_inner_arrays(arr):
        count_dict = {}
        j=0
        for element in arr:
            if len(element)==0:
              # Check if the element has not been counted yet
              if j not in count_dict:
                  count_dict[j] = 1
              else:
                  count_dict[j] += 1
              j+=1
        #print(count_dict)


def update_task_w_sched(task_i,task_avl,task_w2,len_i,task_w_sched,current_time):

  i=len(task_w_sched)
  #print("i len_i",i,len_i,task_w2)
  while i<len_i:
    #print("inside while",current_time)
    if task_avl[i]<=current_time:
        #p=task_i[i]-1
        task_w_sched.append(task_w2[i])
        #task_avl.pop(0)
        #task_i.pop(0)
        #print("task_avl",task_avl)
        #print("task_i",task_i)
        #print("task_w_sched",task_w_sched)
        #i=i-1
    i+=1

  return task_w_sched


def find_fusion(task_w, task_c, task_i,task_avl,task_p,SIMULATION_TIME):
  i=0
  current_time=0
  hold=1000000
  cs=0
  delta=8
  #print("task_avl",task_avl)
  #print(task_c)
  #print("task W", task_w)
  task_fuse_i=[]
  sched_fus=True
  #print("len task i", len(task_i))

  task_p_w=[]
  for i in range(len(task_i)):
    task_p_w.append(task_p[task_i[i]-1])

  task_w1=[]
  task_c_sched=[]
  task_p_sched=[]
  task_w_sched=[]

  task_fus_com=[]
  task_fus_a=[]
  task_fus_p=[]

  for i in range(len(task_i)):
        p=task_i[i]-1
        task_w1.append(copy.deepcopy(task_w[p]))
        task_c_sched.append(copy.deepcopy(task_c[p]))
        task_p_sched.append(task_p[p])
  #print(task_w1)
  task_w2=copy.deepcopy(task_w1)
  task_w_sched=copy.deepcopy(task_w2)
  #print("task_w",task_w2)
  #print("task_c_sched",task_c_sched)
  #print("task i", task_i)
  wcet=0
  time_count=0
  task_fin=[]
  count_dict = {}
  task_n_a=[]
  task_n_p=[]
  
  while current_time<SIMULATION_TIME:
    m=0
    c=0
    a=0
    i=0
    hold_p=[]
    #print("current time wcet",current_time,wcet)
    current_time+=wcet
    #print("wcet",wcet)
    time_count+=wcet
    wcet=0
    for index, element in enumerate(task_w_sched):
      #print(index)
      if len(element)==0:
        #print(index)
        #print("tasj_w-sched",current_time,task_w_sched)
      #Check if the element has not been counted yet
        #if j not in count_dict:
        #  count_dict[j] = 1
        #  task_fin.append(current_time)
        #  print("index",index,task_w_sched)
        #  #task_n_a.append(task_avl[index])
        #  #task_n_p.append(task_p_sched[index])
        #j+=1
              #Check if the element has not been counted yet
        if index not in count_dict:
          count_dict[index] = 1
          task_fin.append(current_time)
          #print("index",index,task_w_sched)
          task_n_a.append(task_avl[index])
          task_n_p.append(task_p_sched[index])
        #j+=1


    #print(task_w_sched, count_dict)

    #print("current time", current_time)
    if hold==current_time:
      if current_time==int(current_time):
        current_time+=1
      else:
        current_time=math.ceil(current_time)
    hold=current_time


    ##updating task e sched
    len_i=len(task_avl)
    ##task_w_sched=update_task_w_sched(task_i,task_avl,task_w2,len_i,task_w_sched,current_time)
    #print(task_w_sched)

    while c!=1:
      #print(i)

      #if i>len(task_i)-1:

      if i>len(task_w_sched)-1:
        i=0
        c=1
        if m>0:
          wcet=wcet+0.02
          #print(" first loop fused candidate size: ", m)
          #print("fused candidate computation time: ", wcet)
          #print("task_w_sched",task_w_sched)
          #print("c",c)
          cs=cs+1
          if (current_time+wcet)>fuse_deadline:
              sched_fus= False
          #cyc_ded=cyclic_sched(hold_p)
          #if cyc_ded==False:
          #    sched_fus=False
        break

      elif len(task_w_sched[i])==0:
            #
            #print("i",i)
            i=i+1
      #elif task_avl[i]<=current_time:
      elif task_avl[i]<=current_time:
        m=m+task_w_sched[i][0]
        #print("task w sched i o", task_w_sched[i][0])
        #print("task_c_sched i o",task_c_sched[i][0])
        wcet=wcet+task_c_sched[i][0]
        #print(i,task_w[i][0])
        if m>delta:
          m=m-task_w_sched[i][0]
          wcet=wcet-task_c_sched[i][0]

          #print(task_w[i])
          i=i+1
          #print(m,wcet,i)


        else:
          hold_p.append(task_p_sched[i])
          task_w_sched[i].pop(0)
          #wcet=wcet+task_c_sched[i].pop(0)
          task_c_sched[i].pop(0)
          if a==0:
            task_fuse_i.append(i)
            a+=1
            fuse_deadline=task_ded_fus(i,task_i,task_avl,task_p)
          if len(task_w_sched[i])==0:
            i=i+1
      else:
          i=i+1
          #print(i)
          if i>len(task_i)-1:
            if m>0:
              wcet=wcet+0.02
              #print("fused candidate size: ", m)
              #print("fused candidate computation time: ", wcet)
              #print("task_w_sched",task_w_sched)
              #current_time=current_time+wcet
              cs=cs+1
              cyc_ded=cyclic_sched(hold_p)
              if (current_time+wcet)>fuse_deadline:
                  sched_fus= False
              #cyc_ded=cyclic_sched(hold_p)
              #if cyc_ded==False:
              #  sched_fus=False

            c=1
            i=0
            #print("c",c)
  #print("time_count",time_count)
  #print("count dict",count_dict)
  #print("task_fin",task_fin)
  #print("task_avl",task_avl)
  #print("task_p_w",task_p_w)
  task_r_fus=[]
  task_r_nt=[]
  for i in range(len(task_fin)):
      k1=(task_fin[i]-task_n_a[i])/task_n_p[i]
      k2=(task_fin[i]-task_n_a[i]-2*0.02)/task_n_p[i]
      if k1>1:
        k1=k1
      task_r_fus.append(k1)
      task_r_nt.append(k2)
  #print("task_r_fus",task_r_fus)
  if len(task_r_fus)!=0:
    print(sum(task_r_nt)/len(task_r_nt))
    print(sum(task_r_fus)/len(task_r_fus))
    
  #print("SMC CS",cs)
  return cs, sched_fus


def task_avlf(task_i,task_p,n):
  task_avl = []
  availability = {task: 0 for task in range(1, n + 1)}

  for task in task_i:
      duration = task_p[task - 1]  # Subtract 1 to align with 0-based indexing of task_p
      task_avl.append(availability[task])
      availability[task] += duration
  return task_avl

def initialize_task_set(task_per):
    # Define the task parameters
    #n = random.randint(3,10)
    n=15
    task_w=[]
    task_c=[]
    task_c_sum=[]
    task_c_sum_nt=[]
    task_p=[]

    smc=0
    c_total=0
    ##put value of C and W
    C=[]
    W=[]

    for i in range(n):
      #t=random.randint(1,8)
      #task_p.append(t)
      Layer_n=random.randint(3,22)
      Layer_n=22
      task_w.append(W)
      task_c.append(C)
      task_c_sum.append(round(sum(C)))
      task_c_sum_nt.append(round(sum(C)))
      
    task_p=copy.deepcopy(task_per)
    #print("task_p",task_p)
    #SIMULATION_TIME=calculate_hyperperiod(task_p)
    SIMULATION_TIME=max(task_p)*2
    #print("sim time", SIMULATION_TIME)
    util=0
    #for i in range(0,n):
    #    util=util+task_c_sum[i]/task_p[i]
    #    util= round(util, 2)
    ##print("util", util)
    for i in range(n):
        task_set.append(Task(i+1, task_p[i], task_p[i], task_c_sum[i], 0,task_w[i]))
        task_set_nt.append(Task(i+1, task_p[i], task_p[i], task_c_sum_nt[i], 0,task_w[i]))

    #print(task_set)
    return SIMULATION_TIME,n, task_c, task_c_sum, task_p, task_w

def util_g(n):
  utill=0
  while utill!=0.80:
    task_per=[]
    utill=0
    for  i in range(n):
      t=random.randint(1,96)
      task_per.append(t)
      utill=round(utill+sum(C)/t,2)
  return task_per   
    
def main():
  edf_sched=[]
  edf_sched_c=0
  fus_sched=[]
  fus_sched_c=0
  u_test=0
  delta=8

  while u_test<1:
    n=15
    task_per=util_g(n)
    SIMULATION_TIME,n, task_c, task_c_sum, task_p, task_w=initialize_task_set(task_per)
    util=0

    for i in range(0,n):
        util=util+(sum(task_c[i]))/task_p[i]
    util= round(util, 2)
    #print(util)
    if (util>0):
        #print("task_task_p)
        u_test=u_test+1
        #schedule_tasks_nt(SIMULATION_TIME,n)
        sched, task_i,taskr_com,taskr_a,taskr_p=schedule_tasks(SIMULATION_TIME,n,task_p)
        if sched == True:
          edf_sched.append(1)
          edf_sched_c+=1
        if sched == False:
          edf_sched.append(0)
        task_avl=task_avlf(task_i,task_p,n)
        cont_swic, sched_fus=find_fusion(task_w, task_c, task_i,task_avl,task_p,SIMULATION_TIME)
        if sched_fus:
             fus_sched.append(1)
             fus_sched_c+=1
        if sched_fus== False:
            fus_sched.append(0)

    #print(util, u_test)
  return edf_sched, edf_sched_c, fus_sched, fus_sched_c

cont_swi = 0
counter_edf=0
counter_fus=0
avg_edf=0
avg_fus=0
for i in range(1):
    edf_sched, edf_sched_c, fus_sched, fus_sched_c=main()
    counter_edf+=edf_sched_c
    counter_fus+=fus_sched_c

print(counter_edf)
print(counter_fus)
