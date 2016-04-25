
import socket
import binascii
import struct
local_ip = '127.0.0.1'
local_port = 18675

#dest_ip = socket.gethostbyname("sogou.com")
dest_port = 34567

f= open("targets.txt", 'r')

for c in range (0, 10, 1):
    dest_ip = f.readline()
    cut = len(dest_ip)-2
    dest_ip dest_ip[0:cut]
    data = r'Lor dolor sit amet, consectetur adipiscing elit.Pellentesque id velit interdum, semper ex id, molestie augue. Aenean vel viverra libero. Integer pharetra enim ipsum, vel feugiat turpis vulputate sit amet. Curabitur non risus nec ante luctus feugiat. Vivamus ac sapien sed lacus venenatis interdum. Nulla pellentesque ultrices massa vitae hendrerit. Proin sit amet porta odio, id blandit magna. Vivamus eget laoreet purus. Proin eu ipsum tellus. Pellentesque quis metus sit amet augue lobortis congue at sed sapien. Vestibulum vel purus ut risus semper cursus aliquam at lacus. Vivamus vitae tellus aliquet, interdum massa vel, hendrerit mauris. Morbi enim massa, aliquam ut nulla eleifend, fermentum scelerisque eros. Mauris suscipit ex sapien, a luctus ex aliquam quis. Ut pulvinar mauris ac mi finibus tempor. Mauris a eleifend lacus. Integer eu velit et lacus tincidunt pharetra non a justo. Nullam fringilla tellus sapien, et consectetur lorem bibendum at. Maecenas facilisis vehicula mi ac tempus. Duis sed dui ac sem sodales fringilla. Nunc magna nibh, maximus at augue vel, consequat cursus erat. Praesent sit amet risus nec sem dignissim sollicitudin imperdiet eu turpis. In at urna et lectus porttitor malesuada. Vivamus a congue augue, ac pellentesque ex.Praesent eu pulvinar tortor. Nunc egestas lacinia dolor eget feugiat. Interdum et malesuada fames ac ante ipsum primis in faucibus. Proin ut cursus mi. Nulla nec feugiat nisl. Etiam ut eleifend urna. Donec i'
    #data="test"

    icmp = socket.getprotobyname('icmp')
    udp = socket.getprotobyname('udp')
    ttl = 32
    #while True:
    # create receiving socket for icmp messages
    recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
    # create outgoing socket to send udp requests
    send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, udp)

    # modify outgoing socket to use desired ttl
    send_socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)

    # bind receiving socket to local port
    recv_socket.bind(("", local_port))

    # send datagram
    send_socket.sendto(data, (dest_ip, dest_port))

    # create variables for incoming data
    data_str = None
    data_addr = None

    # Build the GNU timeval struct (seconds, microseconds)
    timeout = struct.pack("ll", 5, 0)

    # Set the receive timeout so we behave more like regular traceroute
    recv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVTIMEO, timeout)

    try:
        # recvfrom is blocking statement set to 4096 because assuming 1500b file possibility
        # from icmp message
        data_str, data_addr = recv_socket.recvfrom(4096)
        print(data_str)
        print(len(data_str)-28)
    except socket.error:
        print("No Response: ", dest_ip)
        pass
    finally:
        send_socket.close()
        recv_socket.close()



