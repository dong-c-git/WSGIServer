#coding:utf-8
import socket
import time

tcp_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcp_server.bind(("",7890))
tcp_server.listen(128)
tcp_server.setblocking(False) #设置套接字为非堵塞模式
client_cocket_list = list()

while True:
    #time.sleep(0.5)
    try:
        new_scoket,new_addres = tcp_server.accept()
    except Exception as ret:
        print("没有顾客到来")
    else:
        print("---只要没有产生异常，那么也就意味着 来了一个新的客户端----")
        new_scoket.setblocking(False) #设置套接字为非堵塞模式
        client_cocket_list.append(new_scoket)
    for client_cocket in client_cocket_list:
        try:
            recv_data = client_cocket.recv(1024)
        except Exception as ret:
            print(ret)
            print("----这个客户端没有发送过来数据----")
        else:
            print("______没有异常——————————")
            print(recv_data)
            if recv_data:
                #对方发送过来数据
                print("______客户端发送过来了数据————————")
            else:
                #对方调用了close导致recv返回
                client_cocket.close()
                client_cocket_list.remove(client_cocket)
                print("客户端已经关闭")