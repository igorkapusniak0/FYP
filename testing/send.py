import socket
"""
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|Version|  IHL  |Type of Service|        Total Length           |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|         Identification        |Flags|      Fragment Offset    |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|  Time to Live |    Protocol   |         Header Checksum       |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                       Source Address                          |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Destination Address                        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Options (if any)                           |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|          Source Port          |       Destination Port        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                        Sequence Number                        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Acknowledgment Number                      |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|  Data |Rese-|  Control Flags  |                               |
| Offset|rved |URG|ACK|PSH|RST|SYN|FIN|       Window Size        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|       Checksum                |    Urgent Pointer             |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Options (if any)                           |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
"""
# ip header data
version = '4'
IHL = '5'
type_of_service = '00'
total_length = '0000' #calculate with method
identification = 'abcd' #can be random if fragmented keep consistant
flags = '3' #0 has to be 0, 1 dont fragment, 2 more fragments follow
fragment_offset = '000'
TTL = 'ff'
protocol  = '06'
header_checksum = '0000' #calculate with method
src_ip = '00000000' # change later
dest_ip = '00000000' # change later

# tcp data
src_port = '3039'
dest_port = '3039'
sq_num = '00000000' #idk
ack_num = '00000000' #idk
data_offset = '0101000000000010' #idk
window_size = 'ffff' # calculate
checksum = '00000000' # calculate
urgent_ptr = '00000000' # idk

def ip_checksum():
    line1 = version+IHL + type_of_service + total_length
    print(line1)
    line2 = identification + flags + fragment_offset
    print(line2)
    line3 = TTL + protocol + header_checksum
    print(line3)
    line4 = src_ip
    print(line4)
    line5 = dest_ip
    print(line5)

    sum = int(line1) + int(line2) + int(line3) + int(line4) + int(line5)
    print(sum)
    sum += 1
    sum = 0xffffffff - sum
    print(sum)
    return sum


def packet_sum():
    line1 = version+IHL + type_of_service + total_length
    print(line1)
    line2 = identification + flags + fragment_offset
    print(line2)
    line3 = TTL + protocol + header_checksum
    print(line3)
    line4 = src_ip
    print(line4)
    line5 = dest_ip
    print(line5)

    sum = line1 + line2 + line3 + line4 + line5
    print(sum)
    return sum

def ip_to_hex(ip):
    ip_parts = ip.split('.')
    hex0 = str(hex(int(ip_parts[0]))).split('x')
    hex1 = str(hex(int(ip_parts[1]))).split('x')
    hex2 = str(hex(int(ip_parts[2]))).split('x')
    hex3 = str(hex(int(ip_parts[3]))).split('x')
    
    hex_ip = hex0[1] + hex1[1] + hex2[1] + hex3[1]
    print(hex_ip)
    return hex_ip 

def get_my_ip():
    hostname = socket.gethostname()
    source = socket.gethostbyname(hostname)
    print(source)
    return source

destination = input("Enter dest ip: ")

dest_ip = ip_to_hex(destination)
src_ip = ip_to_hex(get_my_ip())

ip_checksum()

#packet_sum()


ip_packet = {
    "version": '4',               # Version, 4 bits
    "ihl": '5',                   # Internet Header Length, 4 bits
    "type_of_service": '00',                  # Type of Service, 8 bits
    "total_length": '0020',       # Total Length, 16 bits

    "identification": 'abcd',     # Identification, 16 bits
    "flags": '0',                 # Flags, 3 bits
    "fragment_offset": '000',     # Fragment Offset, 13 bits

    "time_to_live": 'ff',                  # Time to Live, 8 bits
    "protocol": '06',             # Protocol, 8 bits
    "header_checksum": '0000',    # Header Checksum, 16 bits

    "source_ip": '00000000',      # Source IP, 32 bits
    "destination_ip": '00000000'  # Destination IP, 32 bits
}

tcp_packet = {
    "src_port": '0000',         # Source Port, 16 bits
    "dest_port": '0000',        # Destination Port,16 bits

    "seq_num": '00000000',      # Sequence Number, 32 bits
    "ack_num": '00000000',      # Acknowledgment Number, 32 bits

    "data_offset_reserved": '50',  # Data Offset, 4 bits + Reserved, 3 bits + NS flag, 1 bit
    "flags": '02',              # Control Flags, 8 bits
    "window_size": '4000',      # Window Size, 16 bits

    "checksum": '0000',         # Checksum, 16 bits
    "urgent_pointer": '0000'    # Urgent Pointer, 16 bits
}