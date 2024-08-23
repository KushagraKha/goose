import os
import sys
import json

# Define the location where goose will store its data
GOOSE_CONFIG_PATH = "goose_config.json"

# Load or initialize the configuration
def load_config():
    if os.path.exists(GOOSE_CONFIG_PATH):
        with open(GOOSE_CONFIG_PATH, "r") as file:
            return json.load(file)
    else:
        return {}

def save_config(config):
    with open(GOOSE_CONFIG_PATH, "w") as file:
        json.dump(config, file)

# Add a new command to the config
def add_command(path, name):
    config = load_config()
    if name in config:
        print(f"Command '{name}' already exists in goose.")
        overwrite = input("Would you like to overwrite it? (Y/N): ").strip().lower()
        if overwrite == 'y':
            config[name] = path
            save_config(config)
            print(f"Command '{name}' has been overwritten with path '{path}'.")
        else:
            print("Please choose a different name.")
            sys.exit(1)
    else:
        config[name] = path
        save_config(config)
        print(f"Command '{name}' added with path '{path}'.")

# Execute the command
def run_command(name, *args):
    config = load_config()
    if name in config:
        command = [config[name]] + list(args)
        os.execv(command[0], command)
    else:
        print(f"Command '{name}' not found in goose. Please add it first.")

# Main function to handle arguments
def run():
    if len(sys.argv) < 2:
        print("Usage: goose -f <path_to_executable> -n <command_name>")
        print("       goose <command_name> [args...]")
        sys.exit(1)

    if sys.argv[1] == "-f" and len(sys.argv) >= 4:
        path = sys.argv[2]
        name = sys.argv[4]
        add_command(path, name)
    else:
        name = sys.argv[1]
        args = sys.argv[2:]
        run_command(name, *args)

if __name__ == "__main__":
    run()