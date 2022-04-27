from hashlib import md5
from Cryptodome.Cipher import AES
from os import urandom
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


def encrypt(key,plaintext):
    aesblock=AES.block_size






if __name__=='__main__':
    password=int(input("enter the password"))
    text=input("enter the text")

    encrypt(password,text)
