from tkinter import *
import socket
import gnupg
import os

gpg_path = "/home/igor/Nextcloud/College/Year_4/FYP/pgp_stuff_sender"
gpg = gnupg.GPG(gnupghome=gpg_path)
gpg.encoding = 'utf-8'

public_keys = gpg.list_keys()
private_keys = gpg.list_keys(True)

my_public_key = public_keys[0]["fingerprint"] 
my_private_key = private_keys[0]["keygrip"]
# print(my_public_key)
# print(my_private_key)

import_public_result = gpg.import_keys(public_keys[0]["fingerprint"])
import_private_result = gpg.import_keys(private_keys[0]["keygrip"])

# print(import_public_result)
# print(import_private_result)

def send_message():
    print(dest_ip_entry.get())
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((dest_ip_entry.get(), 8089))

    message = message_entry.get()
    encrypted_ascii_data = gpg.encrypt(message,str(my_public_key))  

    print("encrypted: "+str(encrypted_ascii_data))
    encoded_message = str(encrypted_ascii_data).encode()
    
    clientsocket.send(encoded_message)

window = Tk()

dest_ip_label = Label(window, text="Enter destination IP")
dest_ip_label.pack()

dest_ip_entry = Entry(window)
dest_ip_entry.pack()

message_label = Label(window, text="Enter Message")
message_label.pack()

message_entry = Entry(window)
message_entry.pack()

button = Button(window, text='Send', width=25, command=send_message)
button.pack()

button = Button(window, text='Close', width=25, command=window.destroy)
button.pack()

window.mainloop()