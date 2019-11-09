#coding:utf-8
import multiprocessing
import threading
import time
q_queue = multiprocessing.Queue()

def init_queue():
    print("init_g_queue start")
    while not q_queue.empty():
        q_queue.get()
    for _index in range(10):
        q_queue.put(_index)
    print("init q_queue end")
    return


#定义一个io密集型任务
def task_io(task_id):
    print("IOTASK[%s] start"%task_id)
    while not q_queue.empty():
        time.sleep(1)
        try:
            data = q_queue.get(block=True,timeout=1)
            print("IOtask[%s] get data:%s"%(task_id,data))
        except Exception as e:
            print("IOtask[%s] error:%s"%(task_id,str(e)))
    print("IOtask [%s] end"%task_id)
    return
g_search_list = list(range(10000))
#定义一个计算密集型任务，利用一些复杂的加减乘除
def task_cpu(task_id):
    print("CPUTask[%s] start"%task_id)
    while not q_queue.empty():
        count = 0
        for i in range(10000):
            count += pow(3*2,3*2) if i in g_search_list else 0
        try:
            data = q_queue.get(block=True,timeout=1)
            print("CpuTask[%s] get data:%s"%(task_id,data))
        except Exception as e:
            print("CPUtask-[%s] error:%s"%(task_id,str(e)))
        else:
            print("Cputask is runing,this is else")
        finally:
            print("cputask is end,this is finally")
    print("cputask[%s] end "%task_id)
    return task_id


#开始验证
if __name__ == '__main__':
    # print("cpu count:",multiprocessing.cpu_count(),"\n")
    # print("========直接执行io密集型任务========")
    # init_queue()
    # time_0 = time.time()
    # task_io(0)
    # print("结束",time.time() - time_0,"\n")

    # print("========多线程执行io密集型任务=======")
    # init_queue()
    # time_0 = time.time()
    # thread_list = [threading.Thread(target=task_io,args=(i,))for i in range(5)]
    # for t in thread_list:
    #     t.start()
    # for t in thread_list:
    #     if t.is_alive():
    #         t.join()
    # print("结束：",time.time()-time_0,"\n")

    # print("=======多进程执行io密集型任务========")
    # init_queue()
    # time_0 = time.time()
    # process_list = [multiprocessing.Process(target=task_io,args=(i,)) for i in range(multiprocessing.cpu_count()) ]
    # for p in process_list:
    #     p.start()
    # for p in process_list:
    #     if p.is_alive():
    #         p.join()
    # print("结束：",time.time()-time_0,"\n")

    print("*"*30)
    #直接执行cpu密集型任务
    print("======直接执行cpu密集型任务======")
    init_queue()
    time_0 = time.time()
    task_cpu(0)
    print("结束：",time.time()-time_0,"\n")

    print("======多线程执行cpu密集型任务=====")
    init_queue()
    time_0 = time.time()
    thread_list = [threading.Thread(target=task_cpu,args=(i,)) for i in range(5)]
    for t in thread_list:
        t.start()
    for t in thread_list:
        if t.is_alive():
            t.join()
    print("结束：",time.time()-time_0,"\n")

    print("=====对进程执行cpu密集度任务======")
    init_queue()
    time_0 = time.time()
    process_list = [multiprocessing.Process(target=task_cpu,args=(i,))for i in range(multiprocessing.cpu_count())]
    for p in process_list:
        p.start()
    for p in process_list:
        if p.is_alive():
            p.join()
    print("结束：",time.time()-time_0,"\n")
