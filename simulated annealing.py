import numpy as np

distance_mat=np.array([[0,1,1,2,3],[1,0,2,1,2],[1,2,0,1,2,],[2,1,1,0,1],[3,2,2,1,0]])
flow_mat=np.array([[0,5,2,4,1],[5,0,3,0,2],[2,3,0,0,0],[4,0,0,0,5],[1,2,0,5,0]])

def swap(initial_solution,index1,index2):
    arr=initial_solution.copy()
    arr[index1,:]=initial_solution[index2,:]
    arr[index2,:]=initial_solution[index1,:]
    arr2=arr.copy()
    arr2[:,index1]=arr[:,index2]
    arr2[:,index2]=arr[:,index1]
    return arr2
def cost(solution):
    cost_mat=np.multiply(solution,flow_mat)
    return np.sum(cost_mat)/2

def random_descent(solution):
    valid=False
    index1=np.random.randint(5)
    while valid==False:
        index2=np.random.randint(5)
        if index2!=index1:
            valid=True
    new_solution=swap(solution,index1,index2)
    obj_val=cost(new_solution)
    return[index1,index2,new_solution,obj_val]

def cooling1(t0,tn,n,i):
    ti=t0-(i*(t0-tn)/n)
    return ti

def cooling2(t0,tn,n,i):
    ti=t0*(tn/t0)**(i/n)
    return ti

def Simulated_Annealing(init_solution):
    t0=25
    tn=5
    n=20
    solution_list=[]
    current_sol=init_solution
    [index1,index2,new_solution,obj_val]=random_descent(current_sol)
    for i in range(n):
        if cost(new_solution)<=cost(current_sol):
            print("random descent is better current cost = " +str(cost(current_sol)) + " new cost= " + str(cost(new_solution))+"\n")
            current_sol=new_solution.copy()
            [index1,index2,new_solution,obj_val]=random_descent(current_sol)
        else: 
            print("perfomr SA"+"\n")
            delta=cost(new_solution)-cost(current_sol)
            ti=cooling2(t0,tn,n,i)
            prob=np.exp(-delta/ti)
            rand_num=np.random.rand()
            print("ti= "+ str(ti) +" delta = " + str(delta)+"\n")
            print("Probability = " + str(prob)+ " rand number= "+ str(rand_num)+"\n")
            if prob>rand_num:
                print("accept bad solution. \n")
                print("current cost = " +str(cost(current_sol)) + " new cost= " + str(cost(new_solution))+"\n")
                current_sol=new_solution.copy()
                [index1,index2,new_solution,obj_val]=random_descent(current_sol)
            else:
                print("don't accept bad solution. \n")
                
        solution_list.append([current_sol,cost(current_sol)])
    return solution_list

heuristic_sol_list=Simulated_Annealing(distance_mat)

                
            