import socket
import sys


# sys.path.append(r"C:\Program Files\Python 3.5\lib\site-packages")

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('192.168.0.101', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


def find_name_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print("Your Computer Name is:" + hostname)
    print("Your Computer IP Address is:" + ip_address)


def ip_exists(ip):
    try:
        socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = socket_obj.connect_ex((ip, 22))
        if result == 0:
            print("raspberry pi exists at ip_address: ", ip)
        else:
            print("ip_address " + ip + "does not exist")
        socket_obj.close()

    except:
        print("err")


print(get_ip())
find_name_ip()

for x in range(1, 255):
    ipp = str(x)
    ip_exists('192.168.0.'+ipp)




