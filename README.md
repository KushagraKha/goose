# goose
## Simplify Your Environment Variable Management
### What is goose?
**goose** is your solution to managing environment variables effortlessly, making it ideal for developers who work across multiple languages and libraries on the same machine. If you've ever found yourself frustrated by the need to constantly rename or recreate environment variables due to updates or conflicting versions, goose is here to save the day.

With goose, you can streamline the process, ensuring that your development environment is always set up exactly the way you need it, without the headaches.

### Key Features

- **Simple Command Management**: Quickly add executables to your environment using a single command.
- **Effortless Execution**: Call your executables from the command line without worrying about environment paths.
- **Version Control Friendly**: Easily switch between different versions of tools or languages without adjusting your environment variables.

### Why the need for goose?

Managing environment variables can be a tedious and error-prone task, especially when working with multiple languages and tools. goose eliminates that hassle, allowing you to focus on what really matters—your code. Whether you're a developer, data scientist, or systems administrator, **goose** is designed to make your workflow more efficient.

### How It Works

Setting up goose is simple:

1. **Add an Executable to goose**:
Use the following command to link an executable to a command name:
```
goose -f <path-to-executable> -n <command-name>
```
- **<path-to-executable>**: The absolute path to the executable you want to add.
- **<command-name>**: The name you want to assign to this command for future use.

2. **Run Your Command**:
Once added, you can execute the command from anywhere in your terminal by typing:

```
goose <command-name>
```

### Example Use Case
Imagine you have multiple versions of Python installed on your machine. With goose, you can easily switch between them without constantly modifying your system's environment variables. Just add each version using a unique command name:

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
Clone the repository.
Ensure Python is installed on your system.
Add goose to your environment variables to use it globally.
