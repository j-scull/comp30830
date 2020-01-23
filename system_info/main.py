"""
Created on 22 Jan 2017
@author: Joe
"""

import socket
import os
import platform
import multiprocessing as mp
from psutil import virtual_memory
import timeit
import itertools


def main():
    hostname = socket.gethostname() #gets the the of the current machine
    print('Name:', hostname) 
    print('System:', platform.system(), os.name)
    print('Release:', platform.release())
    print('CPUs:', mp.cpu_count())
    mem = virtual_memory()#returns total memory in bytes
    print('Total Memory:', mem.total)  
    print('Used Memory:', mem.used) #total - used memory does not necessarily = free memory
    print('Free Memory:', mem.free)
    print('IP Address:', socket.gethostbyname(hostname))
    
    
    
    def bench_pidigits(ndigits=100, loops=100):
        
        def calc_ndigits(n):
            
            def gen_x():
                return map(lambda k: (k, 4*k + 2, 0, 2*k +1),itertools.count(1))
    
            def compose(a, b):
                aq, ar, as_, at = a
                bq, br, bs, bt = b
                return (aq*bq, 
                        aq*br + ar*bt, 
                        as_*bq + at*bs, 
                        as_*br + at*bt)
                
            def extract(z, j):
                q, r, s, t = z
                return (q*j + r) // (s*j + t)
            
            def pi_digits():
                z = (1, 0, 0, 1)
                x = gen_x()
                while 1:
                    y = extract(z, 3)
                    while y != extract(z, 4):
                        z = compose(z, next(x))
                        y = extract(z, 3)
                    z = compose((10, -10*y, 0, 1), z)
                    yield y
                
            return list(itertools.islice(pi_digits(), n))
        
        for _ in range(loops):
            calc_ndigits(ndigits)
        #print('PI:', ''.join(map(str, calc_ndigits(ndigits))))
        return
    
        #return perf.perf_counter() - t0
        
    
    t_default = 6.388216104
    start_time = timeit.default_timer()
    bench_pidigits(ndigits=100, loops=1000)
    elapsed_time = timeit.default_timer() - start_time
    print('Relative Elapsed:', elapsed_time/t_default)
    
        
if __name__ == '__main__':
    main()      
            
        
