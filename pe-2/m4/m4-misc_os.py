# OS MODULE
import os
# labs
#  https://edube.org/learn/pe-2/the-os-module-lab-1
# 
# =====================

# os.uname (linux/unix based)
# systemname - OS name
# nodename - machine name on network
# release - OS release
# version - OS version
# machine - Hardware identifier, e.g x86_64

# os.mkdir -- create directory. 
# dir -- cwd
# ./dir -- explicit cwd
# ../dir -- parent dir of cwd
# /dir/ -- root directory. (python directory)

# nt
print(os.name)

# listdir() -- lists files/directories in path arg
print(os.listdir('pe-2\cols_modules'))

# os.makedirs() -- Creating another directory inside of a new directory.
# In Unix / Linux, the equivalent is the mkdir command with the -p flag.

# getcwd() - get current working directory.
print(os.getcwd())

# os.rmdir() -- delete a subdirectory.
os.mkdir("newdir1")
print(os.listdir())
os.rmdir("newdir1")
print(os.listdir())

os.listdir()
# os.removedirs() -- delete a directory and its subdirectories.
os.makedirs("newdir1/newdir2")
print(os.listdir())
print(os.listdir("newdir1"))
os.removedirs("newdir1/newdir2")
print(os.listdir())

# os.system() -- executes a system command. available in Windows and Unix. returns 1 for failure.
val = os.system("mkdir this_dir")
print(os.listdir())
print(val)

os.rmdir("this_dir")