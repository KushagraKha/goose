# goose
## What is goose?
goose is meant to be a command line tool to assist in streamlining environment variable usage. Anybody that has worked in multiple languages and libraries on the same device understands the hassle of dealing with multiple environment variables. The constant renaming as well as recreating variables as different language versions are updated can really cause a headache at times. goose is a solution to deal with this issue. Simply add goose to the environment variables and then, whenever you want to add something to command use:
```
goose -f <path-to-executable> -n <command-name>
```
Then, whenever there is a need to call the executable from the command line, simply type:
```
goose <command-name>
```
The path to executable needs to be the absolute path in order for goose to work.
