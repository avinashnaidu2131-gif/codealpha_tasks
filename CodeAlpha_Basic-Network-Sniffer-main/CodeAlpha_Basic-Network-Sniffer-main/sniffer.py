from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

def show_packet(packet):
    if IP in packet:
        print("\n---------------------")
        print("From:", packet[IP].src)
        print("To  :", packet[IP].dst)

        if TCP in packet:
            print("Type: TCP")
        elif UDP in packet:
            print("Type: UDP")
        else:
            print("Type: Other")

print("Simple Network Sniffer Running...")
print("Press CTRL + C to stop")
sniff(prn=show_packet)
