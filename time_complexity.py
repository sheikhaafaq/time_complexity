#Try this code in jupyter notebook
# Compare time complexity 

# fun is a function taking two args x & y , which gives the o/p x is divided by two y times
def fun(x,y):
    
    for _ in range(int(y)):
        z=int(x)/2
        x=z
    return z



#### dis is a module which gives track of manipulation   , works in jupyter

import dis as ds

ds.dis(fun)


# Line profile is a library that code line by line , works in jupyter

%load_ext line_profiler

#calcultes time complexity of a function
%timeit  fun1(1000000000000000000000000000000000000000,10000)



#Implement the same function using lambda and bitwise shift operator
# i >> j implies i is divide by two ,j times

fun2=lambda i,j:i>>j

%timeit fun2(1000000000000000000000000000000000000000,10000)

ds.dis(fun2)


