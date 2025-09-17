import socket
import gnupg
import os

gpg_path = "/home/igor/Nextcloud/College/Year_4/FYP/pgp_stuff_sender"

gpg = gnupg.GPG(gnupghome=gpg_path)
gpg.encoding = 'utf-8'


with open("/home/igor/Nextcloud/College/Year_4/FYP/receiver_pubkey.asc", "r") as f:
    key_data = f.read()

import_result = gpg.import_keys(key_data)
receiver_key = import_result.fingerprints[0]

print(receiver_key)

public_keys = gpg.list_keys()
private_keys = gpg.list_keys(True)

my_public_key = public_keys[0]["fingerprint"] 
my_private_key = private_keys[0]["keygrip"]

print(my_public_key)
print(my_private_key)


clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 8089))

message = """
hello world
"""

encrypted_ascii_data = gpg.encrypt(message, str(receiver_key), always_trust=True)
print("encrypted: "+str(encrypted_ascii_data))


encoded_message = str(encrypted_ascii_data).encode()
clientsocket.send(encoded_message)