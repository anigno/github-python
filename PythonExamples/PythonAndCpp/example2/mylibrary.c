#include <stdio.h>

// Define a simple C structure
struct MyStruct {
    int field1;
    double field2;
};

// Function that takes a pointer to the structure as a parameter
int process_struct(struct MyStruct *my_struct) {
    printf("C Function: Received MyStruct: field1=%d, field2=%.2lf\n", my_struct->field1, my_struct->field2);

    // Modify the structure fields
    my_struct->field1 *= 2;
    my_struct->field2 += 1.0;

    return my_struct->field1;
}

//# Compile the C code into a shared object (DLL)
//gcc -shared -o mylibrary.so mylibrary.c
