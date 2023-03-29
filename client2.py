import socket
import pygame
pygame.init()
HOST = 'localhost'
PORT = 1234
SEND_SIZE=1024
print("\n MUSIC PLAYER USING SOCKET")
print("\n")
print("Please select which song you want to listen to")
print("1) Scared to be lonely")
print("2) I'd love to change the world")
print("3) Encore/Numb")
print("4) Rich Flex")
print("5) Lion Heart")
n=input("Enter your choice number")
message=n

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(message.encode())
    with open('received_music.mp3', 'wb') as f:
        while True:
            data = s.recv(SEND_SIZE)
            if not data:
                break
            f.write(data)    


pygame.mixer.music.load("received_music.mp3")
print("playing....")
pygame.mixer.music.play(1)
message=input()
if message=='pause':
    pygame.mixer.music.pause()
    print("music paused")
while pygame.mixer.music.get_busy():
    continue
