# goose
## Simplify Your Environment Variable Management
### What is goose?
**goose** is an environment and PATH management tool intended to streamline the process of setting up and managing PATH variables. This tool will be most helpful for beginners until they become more familiar with PATH editing and management.  

### Key Features

- **Simple Command Management**: Quickly add executables to your environment using a single command.
- **Effortless Execution**: Call your executables from the command line without worrying about environment paths.
- **Version Control Friendly**: Easily switch between different versions of tools or languages without adjusting your environment variables.

### Commands and setup

1. **Add an Executable to goose**:
Use the following command to link an executable to a command name:
```
goose -f <path-to-executable> -n <command-name>
```
- **`<path-to-executable>`**: The absolute path to the executable you want to add.
- **`<command-name>`**: The name you want to assign to this command for future use.

2. **Run Your Command**:
Once added, you can execute the command from anywhere in your terminal by typing:

```
goose <command-name>
```

### Example Use Case
Imagine you have multiple versions of Python installed on your machine. With goose, you can easily switch between them without constantly modifying your system's environment variable order. Just add each version using a unique command name:

```
goose -f /path/to/python3.8 -n python38
goose -f /path/to/python3.9 -n python39
```

Now, whenever you need to run Python 3.8 or Python 3.9, you can simply use:

```
goose python38 -m my_script.py
```
or

```
goose python39 -m my_script.py
```

### Getting Started
goose comes with the executable (located inside the dist folder) and an installer for Windows (located inside the Output folder). Simply run the Installer as admin and then restart your computer to be able to use it through the command line. Alternatively, you can try to compile locally using the goose.py file.
