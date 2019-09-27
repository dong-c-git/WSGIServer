#coding:utf-8
import socket
import time
import re

def server_client(new_socket,request):
    """为这个客户端返回数据"""
    # 1. 接收浏览器发送过来的请求 ，即http请求
    # GET / HTTP/1.1
    # .....
    # request = new_socket.recv(1024).decode("utf-8")
    # print(">>>"*50)
    # print(request)
    request_lines = request.splitlines()
    print(request_lines)
    # GET /index.html HTTP/1.1
    # get post put del
    file_name = ""
    ret = re.match(r"[^/]+(/[^ ]*)",request_lines[0])
    if ret:
        file_name = ret.group(1)
        if file_name == "/":
            file_name = "/index.html"
    #2、返回http数据给浏览器
    try:
        f = open("./html"+file_name,"rb")
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "------file not found-----"
        new_socket.send(response.encode("utf-8"))
    else:
        html_content = f.read()
        f.close()
        response_body = html_content
        response_header = "HTTP/1.1 200 OK\r\n"
        response_header += "Content-Length:%d\r\n"%len(response_body)
        response_header += "\r\n"

        response = response_header.encode("utf-8") + response_body
        new_socket.send(response)

def main():
    """用来完成整体控制"""
    tcp_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_server.bind(("",7890))
    tcp_server.listen()
    tcp_server.setblocking(False)  #将套接字变成非堵塞模式
    client_socket_list = list()       #定义一个客户端列表非堵塞模式
    while True:
        #等待客户端到来
        try:
            new_socket,new_addr = tcp_server.accept()
        except Exception as ret:
            pass
        else:
            new_socket.setblocking(False)
            client_socket_list.append(new_socket)
        for client_socket in client_socket_list:
            try:
                recv_data = client_socket.recv(1024).decode("utf-8")
            except Exception as ret:
                pass
            else:
                if recv_data:
                    #为客户端服务
                    server_client(client_socket,recv_data)
                else:
                    client_socket.close()
                    client_socket_list.remove(client_socket)
    #关闭主进程套接字
    tcp_server.close()




if __name__ == '__main__':
    main()