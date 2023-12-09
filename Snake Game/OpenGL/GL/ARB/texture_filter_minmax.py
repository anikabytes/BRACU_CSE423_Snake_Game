'''OpenGL extension ARB.texture_filter_minmax

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.texture_filter_minmax to provide a more 
Python-friendly API

Overview (from the spec)
	
	In unextended OpenGL, minification and magnification filters such as
	LINEAR allow texture lookups to returned a filtered texel value produced
	by computing an weighted average of a collection of texels in the
	neighborhood of the texture coordinate provided.
	
	This extension provides a new texture and sampler parameter
	(TEXTURE_REDUCTION_MODE_ARB) which allows applications to produce a
	filtered texel value by computing a component-wise minimum (MIN) or
	maximum (MAX) of the texels that would normally be averaged.  The
	reduction mode is orthogonal to the minification and magnification filter
	parameters.  The filter parameters are used to identify the set of texels
	used to produce a final filtered value; the reduction mode identifies how
	these texels are combined.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/texture_filter_minmax.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.ARB.texture_filter_minmax import *
from OpenGL.raw.GL.ARB.texture_filter_minmax import _EXTENSION_NAME

def glInitTextureFilterMinmaxARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION