Description of the project AirBnB
The project AirBnB deploys a command line interpreter
that enables interaction with the frontend of an HTML server
using python scripts. The command line interpreter uses features
from the web server in order to gather information and data
of objects that contain attributes for the featured objectives
when interacting with the HTML server.

Description of the command interpreter
The command line interpreters aim, is essential when collecting data
from the web server in order to manage, update and maniputate
information after creating a source or account that is descptive
in regards with a particular attribute.

How to start it
The command interpreter handles commands associated with input
and output. So to validate the commands interactions interactively,
you will need all the class attributes that can be used when
gathering information from the web server. The command interpreter
will collect data associated with the web server from the command
interpreter, enabled by the commands made available from the
console application.

How to use it
The command interpreter works in interactive mode and non-interactive mode.

`Interactive`
The interactive command interpreter is a command line shell which enables
interactions on the command interpreter from a prompt in order to
simulate a command directly from the command interpreter.

Example:
When a prompt appear, then a command can be interpreted as a command is entered
and the output of the command simulates from the prompt until the program
is terminated.

root@user:/# ./console.py
(prompt) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

Undocumented commands:
======================
create

(hbnb)quit
root@user:/#

`Non-Interactive`
The non-interactive command interpreter works on the command interpreter by
simulating a command without a prompt.

Example:
When a command is composed with a pipe symbol, the command interpreter simulates
the output of the command entered before the prompt appears as it would in
interactive mode.

root@user:/# echo "help" | ./console.py
(prompt)

Documented commands (type help <topic>):
========================================
EOF  help  quit

Undocumented commands:
======================
create

(hbnb)quit
root@user:/#

Authors
Orateng Maila
Youssef EL BOUDALI
