class Layer4Segment:
    def __init__(self, src_port, dst_port, data, seq=0, segment_type="DATA"):
        self.src_port = src_port
        self.dst_port = dst_port
        self.data = data
        self.seq = seq
        self.type = segment_type
        self.length = 8 + len(data)
        self.checksum = self.compute_checksum()

    def compute_checksum(self):
        total = self.src_port + self.dst_port + self.length + self.seq
        total += 0 if self.type == "DATA" else 1
        for char in self.data:
            total += ord(char)
        return total % 65535

    def is_valid(self):
        return self.checksum == self.compute_checksum()


class Layer3Packet:
    def __init__(self, src_ip, dst_ip, payload, ttl=100):
        self.src_ip = src_ip
        self.dst_ip = dst_ip
        self.ttl = ttl
        self.protocol = 17
        self.payload = payload
        self.total_length = 20 + payload.length


class Layer2Frame:
    def __init__(self, src_mac, dst_mac, payload):
        self.src_mac = src_mac
        self.dst_mac = dst_mac
        self.type = "0x0800"
        self.payload = payload