import socket

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

tcp_header = bytearray.fromhex(
    'abcd'      # Source Port
    'abcd'      # Destination Port
    '00000001'  # Sequence Number
    '00000000'  # Acknowledgment Number
    '50'        # Data Offset + Reserved + NS flag
    '02'        # Control Flags
    '4000'      # Window Size
    '0000'      # Checksum
    '0000'      # Urgent Pointer
)

payload = "Hello World"

def calculate_total_length():
    ip_header_length = int(ip_header[0:1].hex()[1]) * 4
    tcp_header_length = int(tcp_header[12:13].hex()[0]) * 4
    payload_length = len(payload)

    total_length = ip_header_length + tcp_header_length + payload_length
    print(total_length)
    
    total_length_hex = f"{total_length:04x}"
    print(total_length_hex)

    return total_length_hex

def update_ip_header():
    total_length = calculate_total_length()
    ip_header[2:4] = bytes.fromhex(total_length)

    ip_checksum = f"{calculate_ip_checksum():04x}"
    ip_header[10:12] = bytes.fromhex(ip_checksum)

    dest_ip = ip_to_hex(destination)
    src_ip = ip_to_hex(get_my_ip())

    ip_header[12:16] = bytes.fromhex(src_ip)
    ip_header[16:20] = bytes.fromhex(dest_ip)

def update_tcp_header():
    tcp_checksum = f"{calculate_tcp_checksum():04x}"
    print(tcp_checksum)
    tcp_header[16:18] = bytes.fromhex(tcp_checksum)

def print_ip_packet():
    sum = ip_header.hex()
    print(sum)
    return sum

def print_tcp_packet():
    sum = tcp_header.hex()
    print(sum)
    return sum

def calculate_ip_checksum():
    total = 0
    for i in range(0, 20, 2):
        word = (ip_header[i] << 8) + ip_header[i + 1]
        total += word

        while total > 0xFFFF:
            total = (total & 0xFFFF) + (total >> 16)
    
    print(total)
    checksum = ~total & 0xFFFF
    print(checksum)
    return checksum

def calculate_tcp_checksum():
    placeholder = b'\x00'
    protocol = socket.IPPROTO_TCP
    tcp_length = (len(ip_header) + len(payload)).to_bytes(2, byteorder='big')

    pseudo_header = (
        ip_header[12:15] +
        ip_header[16:19] +
        placeholder + 
        bytes([protocol]) +
        tcp_length
    )

    segment = pseudo_header + tcp_header + payload.encode() 

    if len(segment) % 2 != 0:
        segment += b'\x00'
    
    total = 0

    for i in range(0, len(segment), 2):
        word = (segment[i] << 8) + segment[i+1]
        total += word
        
        while total > 0xFFFF:
            total = (total & 0xFFFF) + (total >> 16)
    
    checksum = ~total & 0xFFFF

    return checksum


def create_packet():
    print_ip_packet()
    print_tcp_packet()
    update_ip_header()
    update_tcp_header()
    print_ip_packet()
    print_tcp_packet()

def ip_to_hex(ip):
    return ''.join(f"{int(part):02x}" for part in ip.split('.'))

def get_my_ip():
    hostname = socket.gethostname()
    source = socket.gethostbyname(hostname)
    print(source)
    return source

destination = "127.0.0.1"

create_packet()


s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
s.sendto(ip_header + tcp_header + payload.encode(), (destination, 0))