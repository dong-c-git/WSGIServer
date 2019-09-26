#coding:utf-8
import socket
import re

def handle_client(client_socket):
    """作为一个客户端进行服务"""
    recv_data = client_socket.recv(1024).decode("utf-8")
    request_header_lines = recv_data.splitlines()
    print(request_header_lines)
    """
        1、使用了正则匹配方式；
        2、捕获了读取服务器上文件的异常；
    """
    for line in request_header_lines:
        print(line)
    http_request_line = request_header_lines[0]
    get_file_name = re.match("[^/]+(/[^ ]*)",http_request_line).group(1)
    print("file name is ==>%s"%get_file_name)     #for test
    #如果没有指定访问的那个页面，例如index.html
    #GET / HTTP/1.1
    if get_file_name == "/":
        get_file_name = DOCUMENTS_ROOT + "/index.html"
    else:
        get_file_name = DOCUMENTS_ROOT + get_file_name
    print("file name is ===2>%s"%get_file_name)   #for test
    try:
        f = open(get_file_name,"rb")
    except IOError:
        #404表示没有这个页面
        response_headers = "HTTP/1.1 404 not found\r\n"
        response_headers += "\r\n"
        response_body = "====sorry,file not found===="
    else:
        response_headers = "HTTP/1.1 200 OK\r\n"
        response_headers += "\r\n"
        response_body = f.read()
        f.close()
    finally:
        # 因为头信息在组织的时候，是按照字符串组织的，不能与以二进制打开文件读取的数据合并，因此分开发送
        # 先发送response的头信息
        client_socket.send(response_headers.encode("utf-8"))
        client_socket.send(response_body)
        client_socket.close()
    # request_file = request_header_lines[0].split(" ")[1]
    # print(request_file)
    # body_content = ""
    # if request_file == "/":
    #     content = "hello world"
    # elif request_file.endswith(".ico"):
    #     content = "this is ico"
    # else:
    #     with open(request_file,"rb") as fp:
    #         content = fp.write()
    # print(request_file)
    # #组织相应的头部信息(herader)
    # response_headers = "HTTP/1.1 200 OK\r\n"  #200表示找到这个资源
    # response_headers += "\r\n"                #用一个换行表示表示下方内容是body内容
    # #组织 内容(body)
    # response_body = body_content + content
    # response = response_headers + response_body
    # client_socket.send(response.encode("utf-8"))
    # client_socket.close()



def main():
    """作为程序的祝控制入口"""
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 设置当服务器先close 即服务器端4次挥手之后资源能够立即释放，这样就保证了，下次运行程序时 可以立即绑定7788端口
    server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server_socket.bind(("",7788))
    server_socket.listen(128)
    while True:
        client_socket,client_addr = server_socket.accept()
        handle_client(client_socket)

"""增加一个服务器读取文件公共配置"""
DOCUMENTS_ROOT = "./html"

if __name__ == '__main__':
    main()