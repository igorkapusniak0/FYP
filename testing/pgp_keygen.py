import gnupg
import os

pgp_sender_path="/home/igor/Nextcloud/College/Year_4/FYP/pgp_stuff_sender"
pgp_receiver_path="/home/igor/Nextcloud/College/Year_4/FYP/pgp_stuff_receiver"
gpg = gnupg.GPG(gnupghome=pgp_sender_path)
gpg.encoding = 'utf-8'

input_data_sender = gpg.gen_key_input(key_type="RSA", 
    key_length=2048, 
    name_real="igor", 
    name_comment="hello world",
    name_email="igor@mail.com", 
    passphrase="secret",
    expire_date="2030-12-31"
)

input_data_receiver = gpg.gen_key_input(key_type="RSA", 
    key_length=2048, 
    name_real="john", 
    name_comment="bye world",
    name_email="john@mail.com", 
    passphrase="password",
    expire_date="2030-12-31"
)

key = gpg.gen_key(input_data_sender)
# data = "Hello world"
# encrypted_ascii_data = gpg.encrypt(data,str(key))
# print("encrypted: "+str(encrypted_ascii_data))
# print("key: " + str(key))
# decrypted_data = gpg.decrypt(str(encrypted_ascii_data))
# print("decrypted: "+str(decrypted_data))

# public_keys = gpg.list_keys() 
# private_keys = gpg.list_keys(True)

# print(public_keys)
# print(private_keys)