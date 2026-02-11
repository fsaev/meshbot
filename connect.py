import meshtastic
import meshtastic.tcp_interface
from pubsub import pub
from parser import Parser
import time

class Connect:
    def onReceive(self, packet, interface):
        self.receive_queue.append(packet)

    def onConnection(self, interface):
        print("Connected to Meshtastic device")

    def __init__(self, host: str, rate_limit: int = 5):
        try:
            self.interface = meshtastic.tcp_interface.TCPInterface(hostname=host)
        except Exception as e:
            print(f"Failed to connect to Meshtastic device: {e}")
            return
        
        self.receive_queue = []
        self.send_queue = []
        self.rate_limit = rate_limit
        self.prev_send_timestamp = 0

        pub.subscribe(self.onReceive, "meshtastic.receive")
        pub.subscribe(self.onConnection, "meshtastic.connection")

    def pop_next_packet(self):
        if self.receive_queue:
            return self.receive_queue.pop(0)
        return None
    
    def queue_message(self, text, channel):
        if text is None:
            return

        text = str(text)
        max_len = 255

        for i in range(0, len(text), max_len):
            chunk = text[i : i + max_len]
            self.send_queue.append((chunk, channel))

    def tick_send_queue(self):
        if self.send_queue:
            current_time = time.time()
            if current_time - self.prev_send_timestamp >= self.rate_limit:
                text, channel = self.send_queue.pop(0)
                try:
                    self.interface.sendText(text, channelIndex=channel)
                    print(f"Sent message: {text} to channel: {channel}")
                except Exception as e:
                    print(f"Failed to send message: {e}")
                self.prev_send_timestamp = current_time