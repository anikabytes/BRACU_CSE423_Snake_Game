'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLX import _types as _cs
# End users want this...
from OpenGL.raw.GLX._types import *
from OpenGL.raw.GLX import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLX_VERSION_GLX_1_4'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GLX,'GLX_VERSION_GLX_1_4',error_checker=_errors._error_checker)
GLX_SAMPLES=_C('GLX_SAMPLES',100001)
GLX_SAMPLE_BUFFERS=_C('GLX_SAMPLE_BUFFERS',100000)
@_f
@_p.types(_cs.__GLXextFuncPtr,arrays.GLubyteArray)
def glXGetProcAddress(procName):pass
