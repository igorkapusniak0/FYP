import socket
import gnupg
import os

pgp_sender_path="/home/igor/Nextcloud/College/Year_4/FYP/pgp_stuff_sender"
pgp_receiver_path="/home/igor/Nextcloud/College/Year_4/FYP/pgp_stuff_receiver"

gpg = gnupg.GPG(gnupghome=pgp_receiver_path)
gpg.encoding = 'utf-8'

public_keys = gpg.list_keys()
private_keys = gpg.list_keys(True)

my_public_key = public_keys[0]["fingerprint"] 
my_private_key = private_keys[0]["keygrip"]
print(my_public_key)
print(my_private_key)


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 8089))
serversocket.listen(5)

try:
    while True:
        connection, address = serversocket.accept()
        buf = connection.recv(10**9)
        print(buf)
        print(len(buf))
        decrypted_data = gpg.decrypt(buf.decode('utf-8'), passphrase="password")
        print("decrypted: "+str(decrypted_data))
except KeyboardInterrupt:
    serversocket.close()
