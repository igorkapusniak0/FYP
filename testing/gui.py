from tkinter import *
import socket
import gnupg
import os

gpg_path = "/home/igor/Nextcloud/College/Year_4/FYP/pgp_stuff_sender"
gpg = gnupg.GPG(gnupghome=gpg_path)
gpg.encoding = 'utf-8'

with open("/home/igor/Nextcloud/College/Year_4/FYP/pgp_stuff_receiver/receiver_pubkey.asc", "r") as f:
    key_data = f.read()

import_result = gpg.import_keys(key_data)
receiver_key = import_result.fingerprints[0]

print(receiver_key)

public_keys = gpg.list_keys()
private_keys = gpg.list_keys(True)

my_public_key = public_keys[0]["fingerprint"] 
my_private_key = private_keys[0]["keygrip"]

import_public_result = gpg.import_keys(public_keys[0]["fingerprint"])
import_private_result = gpg.import_keys(private_keys[0]["keygrip"])

def send_message():
    print(dest_ip_entry.get())
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((dest_ip_entry.get(), 8089))

    message = message_entry.get()
    encrypted_ascii_data = gpg.encrypt(message, str(receiver_key), always_trust=True)


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