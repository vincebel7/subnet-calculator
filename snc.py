import re, sys

def add_preceding_zeros(bin_octet): # for octets
    if(len(bin_octet) >= 8):
        return bin_octet
    return(add_preceding_zeros('0' + str(bin_octet)))

def add_trailing_zeros(bin_mask): # for binary subnet mask
    if(len(bin_mask) >= 32):
        return bin_mask
    return(add_trailing_zeros(str(bin_mask) + '0'))

def decimal_to_binary(dec):
    bin_octet = bin(dec).replace("0b", "")
    return add_preceding_zeros(bin_octet)

def binary_to_decimal(bin_octet):
    dec = int(bin_octet,2)
    return dec

def decimal_ip_to_binary(decip):
    if not re.match('(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}', decip):
        print("Error: Invalid IPv4 address detected -", decip)
        return

    decip_list = decip.split('.')
    binip_list = []
    for octet in decip_list:
        binip_list.append(decimal_to_binary(int(octet)))
    return binip_list

def binary_ip_to_decimal(binip):
    if(len(binip) != 32):
        print("Error: Invalid binary address detected -", binip)
        return

    oct1 = str(binip[0:8])
    oct2 = str(binip[8:16])
    oct3 = str(binip[16:24])
    oct4 = str(binip[24:32])
    return(str(binary_to_decimal(oct1)) + "." + str(binary_to_decimal(oct2)) + "." + str(binary_to_decimal(oct3)) + "." + str(binary_to_decimal(oct4)))

def get_network_address(binaddr, mask):
    for i in range(32):
        if(i >= int(mask)):
            binaddr = binaddr[:i] + "0" + binaddr[i+1:]
    return binaddr

def is_CIDR(arg):
    if re.match('(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\/(3[0-2]|[1-2][0-9]|[0-9]))$', arg):
    #if re.match('(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]).){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])', arg):
        handle_CIDR(arg)
    else:
        print("subnet-calculator: Invalid CIDR. Use format aaa.bbb.ccc.ddd/xx")

def handle_CIDR(arg):
    arg_list = arg.split('/')
    addr = arg_list[0]
    mask = arg_list[1]

    binaddr_list = decimal_ip_to_binary(addr)
    binaddr = binaddr_list[0] + binaddr_list[1] + binaddr_list[2] + binaddr_list[3]

    binmask = ""
    for i in range(int(mask)):
        binmask = binmask + "1"
    binmask = add_trailing_zeros(binmask)
    networkaddr_binary = get_network_address(binaddr, mask)
    networkaddr = binary_ip_to_decimal(networkaddr_binary)
    print("\nResults for",arg,"\n")
    print("IP address:\t\t\t", addr)
    print("Subnet mask:\t\t\t", binary_ip_to_decimal(binmask))
    print("Network address:\t\t", networkaddr)
    print("# of valid hosts:\t\t", (2**(32-int(mask)))-2)

    print("\n-- Binary values ------------------------------------------------")
    print("IP address (binary):\t\t", binaddr)
    print("Subnet mask (binary):\t\t", binmask)
    print()

def call_version():
    print("subnet-calculator v0.1")
    print("Author: https://github.com/vincebel7\n")

def call_help():
    print("usage: python3 snc.py [--help] <CIDR-notation addr> [<args>]\n")
    #print("view networks")
    #print("\tview\tShows all addresses and prefixes")

if(len(sys.argv) == 1):
    call_help()
if(len(sys.argv) == 2):
    if(sys.argv[1] == "--help"):
        call_help()
    elif(sys.argv[1] == "--version"):
        call_version()
    else:
        is_CIDR((sys.argv[1]))
