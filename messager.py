class MessagerInterface:
    def __init__(self, connect):
        self.connect = connect

    def process_packet(self, packet):
        if packet is None:
            return
        type = packet[0].lower()
        data = packet[1].lower()
        if type == 'msgpublic':
            self.connect.queue_message(f"Broadcast: {data}", channel=0)
        elif type == 'msgecho':
            self.connect.queue_message(f"Echo: {data}", channel=1)
            