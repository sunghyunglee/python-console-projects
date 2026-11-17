'''
server와 client은 관계에 따라 정해짐
    둘은 언제든지 역할이 바뀔 수 있음 (고정 X)
    해줄게/해줘

소켓 - 연결통로
    서버 소켓
    클라이언트 소켓
    ex) 게임에서 서버 터진다ㅋㅋ
'''

import socket
import threading


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 9876))  #127.0.0.1(localhost)
server_socket.bind(('0.0.0.0', 9886))
server_socket.listen()
print("나 서버소켓인데 연결 대기중...")


conn, addr = server_socket.accept()     #쓰레드가 여기에서 대기중 -> 클라이언트 요청 들어오면 연결해줌
print("접속한 addr: ", addr)


def receive():
    while True:
        try:
            # 수신
            data = conn.recv(1024)
            if not data:
                print("not data: ", data)
                print("상대방 나감")
                break
            print("[상대방]", data.decode())
        except Exception as e:
            print("예외발생!", e)
            break


#수신 쓰레드
threading.Thread(target=receive, daemon=True).start()


while True:
    #발신
    msg = input("보낼 메세지: ")
    conn.send(msg.encode())

