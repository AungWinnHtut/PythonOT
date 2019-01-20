#!/usr/bin/python3
# This program is for Python Networking basic lessons collection
# By Dr. Aung Win Htut (Green Hackers)
# Date: 2019-01-20


import socket
# import sys


# sys.path.append(r"C:\Program Files\Python 3.5\lib\site-packages")


# TCP almost always uses SOCK_STREAM and UDP uses SOCK_DGRAM.
# TCP/SOCK_STREAM is a connection-based protocol.
# The connection is established and the two parties have a conversation until
# the connection is terminated by one of the parties or by a network error.
# UDP/SOCK_DGRAM is a datagram-based protocol.
# You send one datagram and get one reply and then the connection terminates.
# If you send multiple packets, TCP promises to deliver them in order.
# UDP does not, so the receiver needs to check them, if the order matters.
# If a TCP packet is lost, the sender can tell. Not so for UDP.
# UDP datagrams are limited in size, from memory I think it is 512 bytes.
# TCP can send much bigger lumps than that.
# TCP is a bit more robust and makes more checks.
# UDP is a shade lighter weight (less computer and network stress).
# Choose the protocol appropriate for how you want to interact with the other computer.


def get_ip_from_address(web_address):
    try:
        print('ip address of ' + web_address + ' is ', end="")
        print(socket.gethostbyname(web_address))
    except socket.gaierror:  # given host name invalid error - gai -> getaddrinfo()
        print('Cannot resolve address ', web_address, socket.gaierror)
    print()


def get_own_ip():
    # This fun is to find own ip address
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        # you can use any ip address
        s.connect(('192.168.0.1', 1))
        ip = s.getsockname()[0]
    except:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip


def find_name_and_ip():
    # This function will find out computer name and ip address
    # gethostbyname_ex() function returns a tuple
    # 1 Host name,
    # 2 Alias names of the hostname,
    # 3 Other IP address of the host name

    hostname = socket.gethostname()
    ip_address = socket.gethostbyname_ex(hostname) # socket.gethostbyname() will give ipv6 address

    print("full data is " + str(ip_address))
    print("ipv4 only is " + str(ip_address[2][3]))
    print("Computer Name from data is: " + str(ip_address[0]))
    print("Your Computer Name from hostname is:" + hostname)
    print("Your Computer IPv4 Address is: " + str(ip_address[len(ip_address) - 1][len(ip_address[len(ip_address) - 1]) - 1]))
    print("Ipv6 address by socket.getaddrinfo() is " + str(socket.getaddrinfo(hostname, 80))) # will return tuple
    print("Ipv6 address by socket.gethostbyname() is " + str(socket.gethostbyname(hostname)))
    print()


def ip_exists(ip):
    try:
        socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = socket_obj.connect_ex((ip, 22))
        if result == 0:
            print('**************************************************')
            print("raspberry pi exists at ip_address: ", ip)
            print('**************************************************')
            print()
            socket_obj.close()
            return True
        else:
            # print("ip_address " + ip + " is not raspberry pi")
            socket_obj.close()
            return False
    except:
        print("err")


def main():
    # Main function start here
    get_ip_from_address('www.google.com')
    get_ip_from_address('www.facebook.com')
    get_ip_from_address('www.dfkadjfadkjfdfk.com')
    print(get_own_ip())
    find_name_and_ip()

    for x in range(100, 120):
        ipp = str(x)
        result = ip_exists('192.168.0.'+ipp)
        if result:
            break


if __name__ == "__main__":
    main()

