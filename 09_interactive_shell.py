# This file is not about a new part of the python language. It's
# about another way to execute python code.

# Till now we have execute our python scripts by invoking the python
# program from terminal and passing it a script to execute.
# If you use PyCharm and run scripts with "right click" + "Run ...."
# PyCharm invokes python.exe and passes the path to your script file
# to python.exe

# Wouldn't it be great if we could test small pieces of code without
# writing new scripts?
# Fear no more! Because we can!

# If you type "python" in your terminal and do not give python any
# file to execute, python will start the interactive shell. Now you
# can type pieces of python code and once you press [enter] python
# will execute the code.
# Terminal = cmd = Command Prompt

# To run Command Prompt in Windows press Windows key, type "cmd" and
# press [enter]

# > python
# >>> print("hello")          <-- this you should type
# hello                       <-- this python should display

# How to exit a interactive shell session?
# type "exit()" or press Ctrl+Z[enter]

# In the interactive shell we can do anything we can do in a script:

# > python
# >>> a = 12
# >>> b = 34
# >>> c = a * b
# >>> print(c)
# 408
# >>> c                       <-- to see a variables value we don't
#                                 even need to type print(c)

# Multi-line statements
# The interactive shell allows to test multi-line statements like a
# for loop. After you type the first line of the for loop the shell
# will recognize you started a loop and you will be able to type
# more lines before executing your code. Python remains strict about
# spaces and indents so remember to use the correct indentation
# level.

# > python
# >>> my_list = ["A", 42, 24, "monkey"]
# >>> for character in my_list:
# ...     print(character)
# ...                          <-- at this point if you press [enter]
#                                  leaving an empty line, your for
#                                  loop will be executed.
# A
# 42
# 24
# monkey

# The name "interactive shell" might be somewhat confusing.
# The adjective "interactive" means that we can execute code in the
# terminal and immediately get results from python. As if talking to
# python.
# "shell" is a synonym for a layer between the user (you) and the
# python interpreter or operating system (OS).
# What ever you type in the "interactive shell" will be passed to the
# python interpreter. The python interpreter will further pass
# commands to the OS.


# exercise 1: Create a list of numbers and sum them in the
# interactive shell
