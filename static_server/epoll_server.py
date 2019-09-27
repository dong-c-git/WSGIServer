#coding:utf-8
import socket
import re
import select

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
    #创建一个epoll对象epoll适用于linux下
    epl = select.epoll()
    #将监听套接字no注册到epoll中
    epl.register(tcp_server.fileno(),select.EPOLLIN)
    fd_event_dict = dict()   #定义事件通知字典
    while True:
        fd_event_list = epl.poll()  #默认会堵塞，知道os监测到数据到来，通过事件通知方式告诉这个程序此时才会解堵塞
        #[(fd,event)](套接字对应描述符，这个文件描述符描述到底是什么事件，例如可以调用recv)
        for fd,event in fd_event_list:
            #等待客户端到来
            if fd == tcp_server.fileno():
                new_socket,new_addr = tcp_server.accept()
                epl.register(new_socket.fileno(),select.EPOLLIN)
                fd_event_dict[new_socket.fileno()] = new_socket
            elif event == select.EPOLLIN:
                #判断已经链接的客户端是否有数据发送过来
                recv_data = fd_event_dict[fd].recv(1024).decode("utf-8")
                if recv_data:
                    # 为客户端服务
                    server_client(fd_event_dict[fd], recv_data)
                else:
                    fd_event_dict[fd].close()
                    epl.unregister(fd)
                    del fd_event_dict[fd]
    #关闭主进程套接字
    tcp_server.close()


if __name__ == '__main__':
    main()