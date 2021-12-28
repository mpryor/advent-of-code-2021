import math
from math import inf as INFINITY

with open("input") as input_file:
    hex = input_file.read().strip()


class Pkt:
    def __init__(self, len, val, pkts=None, ver_no=None, type_id=None):
        self.len = len
        self.value = val
        self.pkts = pkts
        self.ver_no = ver_no
        self.type_id = type_id


def parse_literal(bits):
    literal_val = ""
    i = 0
    while bits[i] == "1":
        literal_val += bits[i+1:i+5]
        i += 5
    literal_val += bits[i+1:i+5]    
    return Pkt(len=i + 5 + 6, val=int(literal_val, 2))


def parse_operator(bits):
    length_type_id = bits[0]
    if length_type_id == "0":
        total_length = bits[1:16]
        total_length = int(total_length, 2)
        sub_packets = bits[16:16+total_length]
        pkt = decode_packet(sub_packets, total_length, INFINITY)
        pkt.len += 15 + 7
        return pkt
    else:
        pkt_count = bits[1:12]
        pkt_count = int(pkt_count, 2)
        sub_packets = bits[12:]
        pkt = decode_packet(sub_packets, INFINITY, pkt_count)
        pkt.len += 11 + 7
        return pkt


def hex_to_bin(hex):
    bit_str = ""
    for char in hex:
        bit_str += format(int(char, 16), "04b")

    return bit_str


def decode_packet(bit_str, length, no_pkts, top=False):
    bits_read = 0
    count = 0
    pkts = []
    curr_pkt = Pkt(0, None, [])

    while count < no_pkts and bits_read < length:
        pkt_ver = int(bit_str[bits_read + 0:bits_read + 3], 2)
        type_id = int(bit_str[bits_read + 3:bits_read + 6], 2)
        
        pkt = None
        if type_id == 4:
            pkt = parse_literal(bit_str[bits_read + 6::])
        else:
            pkt = parse_operator(bit_str[bits_read + 6::])
            if type_id == 0:
                pkt.value = sum([p.value for p in pkt.pkts])
            elif type_id == 1:
                pkt.value = math.prod([p.value for p in pkt.pkts])
            elif type_id == 2:
                pkt.value = min([p.value for p in pkt.pkts])
            elif type_id == 3:
                pkt.value = max([p.value for p in pkt.pkts])
            elif type_id == 5:
                pkt.value = 1 if pkt.pkts[0].value > pkt.pkts[1].value else 0
            elif type_id == 6:
                pkt.value = 1 if pkt.pkts[0].value < pkt.pkts[1].value else 0
            elif type_id == 7:
                pkt.value = 1 if pkt.pkts[0].value == pkt.pkts[1].value else 0

        pkt.type_id = type_id
        pkt.ver_no = pkt_ver

        if no_pkts == 1:
            curr_pkt.ver_no = pkt_ver
            curr_pkt.type_id = type_id

        if top:
            return pkt

        pkts.append(pkt)
        bits_read += pkt.len
        count += 1

    curr_pkt.len = bits_read
    curr_pkt.pkts = pkts

    return curr_pkt

bin_val = hex_to_bin(hex)
decoded = decode_packet(bin_val, INFINITY, 1, top=True)

version_sum = 0

q = [decoded]
while q:
    cur = q.pop(0)
    print(f"version: {cur.ver_no}")
    version_sum += cur.ver_no
    print(f"val: {cur.value}")
    if cur.pkts != None:
        for pkt in cur.pkts:
            q.append(pkt)
        
print(decoded.value)