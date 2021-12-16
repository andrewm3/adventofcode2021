import fileinput

def main():
    hex = next(fileinput.input()).strip()
    packet, _ = process(parse(hex))
    print(versions(packet))
    print(value(packet))

def parse(hex):
    bits = bin(int(hex, 16))[2:].zfill(len(hex) * 4)
    return bits

def process(bits):
    packet = {
        'version': int(bits[0:3], 2),
        'typeid':  int(bits[3:6], 2),
        'subs':    [],
    }
    bits = bits[6:]

    if packet['typeid'] == 4:
        packet['value'], bits = literal(bits)
        return packet, bits

    return process_subs(packet, bits)

def process_subs(packet, bits):
    ltid, bits = bits[0], bits[1:]

    if ltid == '0':
        sublen, bits = int(bits[:15], 2), bits[15:]
        subs,   bits = bits[:sublen],     bits[sublen:]
        while len(subs) > 0:
            sub, subs = process(subs)
            packet['subs'].append(sub)
    else:
        n, bits = int(bits[:11], 2), bits[11:]
        for _ in range(n):
            sub, bits = process(bits)
            packet['subs'].append(sub)

    return packet, bits

def literal(bits):
    value = prefix = ''

    while prefix != '0':
        prefix = bits[0]
        number = bits[1:5]
        bits   = bits[5:]
        value += number

    return int(value, 2), bits

def versions(packet):
    return packet['version'] + sum(versions(sub) for sub in packet['subs'])

def value(packet):
    tid, subs = packet['typeid'], packet['subs']
    if tid == 0:
        return sum(value(sub) for sub in subs)
    if tid == 1:
        return reduce(lambda x, y: x * y, (value(sub) for sub in subs))
    if tid == 2:
        return min(value(sub) for sub in subs)
    if tid == 3:
        return max(value(sub) for sub in subs)
    if tid == 4:
        return packet['value']
    if tid == 5:
        return (0, 1)[value(subs[0]) > value(subs[1])]
    if tid == 6:
        return (0, 1)[value(subs[0]) < value(subs[1])]
    if tid == 7:
        return (0, 1)[value(subs[0]) == value(subs[1])]

if __name__ == '__main__':
    main()
