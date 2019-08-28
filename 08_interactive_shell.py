# This file is not about a new part of the python language. It's
# about aonther way to execute python code.

# Till now we have execute our python scripts by invoking the python
# program from terminal and passing it a script to execute.

# Wouldn't it be great if we could test small pieces of code without
# writing new scripts?
# Fear no more! Because we can!

# If you type in "python" in your terminal and do not give python any
# file to execute, python will start the interactive shell. Now you
# can type pieces of python code and once you press [enter] python
# will execute the code.

# > python
# Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> print("hello")          <-- this you should type
# hello                       <-- this python should display

# How to exit a interactive shell session?
# type "exit()" or press Ctrl+Z[enter]

# In the interactive shell we can do anything we can do in a script:

# > python
# Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> a = 12
# >>> b = 34
# >>> c = a * b
# >>> print(c)
# 408
# >>> c                       <-- to see a variables value we don't
#                                 even need to type print(c)

# Multiline statements
# The interactive shell allows to test multiline statements like for
# loop. After you type the first line of the for loop the shell will
# recoginze that you need to type another line of code so it will
# allow you to type in more line before actually executing the code.
# Python still will be stict about spaces and indents so remeber to
# use the correct indentation level.

# > python
# >>> l = ["A", 42, 24, "monkey"]
# >>> for character in l:
# ...     print(character)
# ...                          <-- at this point if you press [enter]
#                                  leaving an empty line, your for
#                                  loop will be executed.
# A
# 42
# 24
# monkey
# >>> 

# The name "interactive shell" might be somewhat confusing.
# The adjective "interactive" means that we can execute code in the
# terminal and immidiately get results from python. As if talking to
# python.
# The name "shell" should not be confused with a beach shell.
# Although it's a wall. The "interactive shell" is a wall between the
# user (you) and the python interpreter or operating system (OS).
# What ever you type in the "interactive shell" will be passed to the
# python interpreter. The python interpreter will further pass
# commands to the OS.

# Some more general information on "shells"

# There are many different "shells" allowing users to communicate
# with the OS. The "terminal" or "command line" aka "cmd" is one of
# them. But since those shells are old and some operations are
# cubmersome new shells are being created. For example at some point
# Microsoft added a new shell to Windows called "PowerShell".
# PowerShell allows to configure a Windows OS much more easily than
# the old cmd. The PowerShell console looks exactly like the cmd
# console, with the excepiton that it's blue and it "understand" all
# the new commands.
# For example in the PowerShell terminal you could type:
# > Write-Host 'Hello World' -BackgroundColor Red
# This would output the text 'Hello World' on a red background. This
# is nearly impossible in a cmd.
