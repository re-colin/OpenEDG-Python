import platform

# Underlying/detailed processor name 
# Intel64 Family 6 Model 142 Stepping 10, GenuineIntel
print("processor()", platform.processor()) 

# Basic processor name e.g AMD64
print("machine()", platform.machine()) 

# Generic OS name as a string (Windows)
print("system()", platform.system())

# Detailed/Underlying OS name
print("platform()", platform.platform()) 

# System version 
print("version()", platform.version()) 

