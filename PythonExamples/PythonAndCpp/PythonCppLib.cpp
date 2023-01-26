// PythonCppLib.cpp : Defines the exported functions for the DLL application.
//

#include "stdafx.h"
#include <thread>
#include <iostream>
#include <string>
#include <math.h>

using namespace std;

#define LIBDLL extern "C" __declspec(dllexport)

LIBDLL int sum(int a, int b) 
{
	return a + b;
}

