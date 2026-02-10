
class AdminInterface:
    def __init__(self):
        pass

    def show_help(self):
        print("Admin Interface Help:")
        print("1. View Logs")
        print("2. Manage Users")
        print("3. System Settings")
        print("4. Exit")

    def process_command(self, command):
        print(f"Processing admin command: {command}")
        if command == 'help':
            self.show_help()
        elif command == 'view_logs':
            self.view_logs()
        elif command == 'manage_users':
            self.manage_users()
        elif command == 'system_settings':
            self.system_settings()
        else:
            print("Unknown command")
    def handle_choice(self, choice):
        if choice == '1':
            self.view_logs()
        elif choice == '2':
            self.manage_users()
        elif choice == '3':
            self.system_settings()
        elif choice == '4':
            print("Exiting Admin Interface.")
            return False
        else:
            print("Invalid choice. Please try again.")
        return True

    def view_logs(self):
        print("Viewing logs... (placeholder)")

    def manage_users(self):
        print("Managing users... (placeholder)")

    def system_settings(self):
        print("Accessing system settings... (placeholder)")