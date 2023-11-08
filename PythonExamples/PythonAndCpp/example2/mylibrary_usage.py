import ctypes

# Load the shared object (DLL)
my_library = ctypes.CDLL("./mylibrary.so")  # Replace with the actual path to your shared object

# Define the C structure in Python
class MyStruct(ctypes.Structure):
    _fields_ = [
        ("field1", ctypes.c_int),
        ("field2", ctypes.c_double),
    ]

# Create an instance of the structure
my_instance = MyStruct()
my_instance.field1 = 10
my_instance.field2 = 3.14

# Call the C function from the shared object
result = my_library.process_struct(ctypes.byref(my_instance))
print(f"Python: Received Result: {result}")
print(f"Python: Modified MyStruct: field1={my_instance.field1}, field2={my_instance.field2:.2f}")
