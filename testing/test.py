import socket

# ip = "192.168.178.116"

# print(socket.inet_aton(ip))


# def ip_to_hex(ip):
#     return ''.join(f"{int(part):02x}" for part in ip.split('.'))

# print(ip_to_hex(ip))

ip_header = bytearray.fromhex(
    '45'      # Version + IHL                0-1
    '00'      # TOS                          1-2
    '0000'    # Total Length                 2-4
    'abcd'    # Identification               4-6
    '0000'    # Flags + Fragment Offset      6-8
    'ff'      # TTL                          8-9
    '06'      # Protocol (TCP)               9-10
    '0000'    # Checksum (to be calculated)  10-12
    '00000000' # Source IP                   1
    '00000000' # Destination IP
)

# for i in range(22):
#     print(f"{i} = {ip_header[i:i+1]}")

tcp_header = bytearray.fromhex(
    'abcd'      # Source Port
    'abcd'      # Destination Port
    '00000000'  # Sequence Number
    '00000000'  # Acknowledgment Number
    '50'        # Data Offset + Reserved + NS flag
    '02'        # Control Flags
    '4000'      # Window Size
    '0000'      # Checksum
    '0000'      # Urgent Pointer
)

print(tcp_header[16:18])