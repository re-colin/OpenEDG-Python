# FILE/DATA PROCESSING.
# File operations, operation modes, reading/writing to a binary file. 


# Different systems store file paths differently.
# e.g Windows using backslashes (C:\directory\file), Linux & Unix using forward slashes. (/directory/files)
name = "/dir/file"
name = "\dir\file" # escape codes.
name = "\\dir\\file" # correction for windows file path.

# However Python is smart enough to be able to convert slashes into backslashes when it discovers a path is needed by the OS.
# meaning
name = "/dir/file"
name = "c:/dir/file"
# will also work in Windows.
# Programs communicate with files by the means of entities called *handles* or *streams*.

# ======================================
# File streams
# Ops performed on the file stream
# read
# write

# Modes used to open the stream
# read
# write
# update

# When a stream is read in, its akin to a tape recorder in that the virtual head moves over the stream according to the number of bytes transferred. *Current file position*.

# ======================================
# Diagnosing file stream problems
# A function - strerror() - is offered to drastically simplify the handling of file stream errors. It returns a string describing the error plus the error number.
from os import strerror 
try:
    f = open('c:/files/file.txt')
    f.close()
except Exception as exc:
    print("File could not be opened: ", strerror(exc.errno))

# Reading our file in read text mode
stream = open("pe-2/cols_modules/cools/file.txt", "rt", encoding="utf-8")
# print(stream.read())

# Read in the first character. Cant be called after above stream.read() because the virtual read head will be at the end of the file.
# You can also read in a file character by character or by line, but you need to be sure that its memory safe and you have an appropriate buffer.
print(stream.read(1))

print(stream) # Returns file object class.
# Which is an iterable. Its __next__ method returns the next line read in from the file stream.

stream.close() 

# ======================================
# Writing byte arrays to a binary file
bin_file = "pe-2/cols_modules/cools/bf.bin"

print("=================")
data = bytearray(10)

# print(data)

try:
    bf = open(bin_file, 'wb')
    bf.write(data)
    bf.close()
except IOError as eio:
    print(strerror(eio))

bf = open(bin_file, 'rb')
print(bf.read())  # b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' 

# ======================================
# Reading bytes from a stream
# Requires use of method readinto().
# It doesnt create a new byte array object, rather filling a previously created one.
# returns number of successfully read bytes
# tries to fill the whole space available inside its argument. 

data = bytearray(10)

try:
    bf = open(bin_file, 'rb')
    for b in data:
        print(hex(b), end='\n')
    bf.readinto(data)
    bf.close()
except Exception:
    "An error has occured."

# read() for binary files is similar to bytearray, except its immutable. Without arguments, it tries to read all contents of the file into memory as an instance of the bytes class.
# Shouldnt be unused if theres uncertainty about memory capacity.
# read() argument specifies max amount to be read in.
try:
    bf = open(bin_file, "rb")
    data = bytearray(bf.read(5))

    for byte in range(len(data)):
        data[byte] += (1 + byte)

    bf.close()

    for b in data: 
        print(b, hex(b), sep=': ')
except IOError as eio:
    print(strerror(eio.errno))

