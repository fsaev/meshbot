from database import MeshBotDB

class Parser:
    def __init__(self):
        self.user_db = MeshBotDB('users.fs')
        self.message_db = MeshBotDB('messages.fs')

    def parse(self, packet):
        # Placeholder parse logic
        print(f"Parsing packet: {packet}")
        if('decoded' not in packet or 'portnum' not in packet['decoded']):
            print("Discarding packet: missing 'decoded' or 'portnum'")
            return
        packet_type = packet['decoded']['portnum']
        if packet_type == 'TEXT_MESSAGE_APP':
            #self.message_db.save_data(self.message_db.get_index(), packet['decoded']['text'])
            print(f"Received text message: {packet['decoded']['text']}")
            # Look for 'CFG' prefix to identify config messages
            if packet['decoded']['text'].startswith('CFG '):
                # Extract config data (this is just a placeholder, actual parsing logic will depend on your config format)
                config_data = packet['decoded']['text'][4:]  # Remove 'CFG ' prefix
                return ('CFG', config_data)
            else:
                return ('MSG', packet['decoded']['text'])
        elif packet_type == 'TRACEROUTE_APP':
            print("Received traceroute packet")
        else:
            pass
