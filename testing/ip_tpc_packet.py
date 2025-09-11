import socket

ip_header = bytearray.fromhex(
    '45'      # Version + IHL
    '00'      # TOS
    '0000'    # Total Length
    'abcd'    # Identification
    '0000'    # Flags + Fragment Offset
    'ff'      # TTL
    '06'      # Protocol (TCP)
    '0000'    # Checksum (to be calculated)
    '00000000' # Source IP
    '00000000' # Destination IP
)

tcp_header = bytearray.fromhex(
    '0000'      # Source Port
    '0000'      # Destination Port
    '00000000'  # Sequence Number
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

    ip_checksum = str(calculate_ip_checksum())
    ip_header[10:12] = bytes.fromhex(ip_checksum)

    dest_ip = ip_to_hex(destination)
    src_ip = ip_to_hex(get_my_ip())

    ip_header[12:16] = bytes.fromhex(src_ip)
    ip_header[16:20] = bytes.fromhex(dest_ip)

def print_ip_packet():
    sum = ip_header[0:20].hex()
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

def create_packet():
    print_ip_packet()
    update_ip_header()
    print_ip_packet()

def ip_to_hex(ip):
    return ''.join(f"{int(part):02x}" for part in ip.split('.'))


def get_my_ip():
    hostname = socket.gethostname()
    source = socket.gethostbyname(hostname)
    print(source)
    return source

destination = input("Enter dest ip: ")



create_packet()