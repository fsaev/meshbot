import sys
import os
import subprocess

class AdminInterface:
    def __init__(self, connect):
        self.connect = connect

    def reply_help(self):
        help_message = "Available commands:\n"
        help_message += "CFG HELP - Show this help message\n"
        help_message += "CFG <command> - Execute a configuration command\n"
        self.connect.queue_message(help_message, channel=1)

    def process_packet(self, packet):
        if packet is None:
            return
        type = packet[0].lower()
        data = packet[1].lower()
        if type == 'cfg':
            if data == 'help':
                self.reply_help()
            elif data == 'upgrade':
                source_dir = os.path.dirname(os.path.abspath(__file__))
                subprocess.run(['git', 'pull'], cwd=source_dir)
                os.execv(sys.executable, [sys.executable] + sys.argv)
            