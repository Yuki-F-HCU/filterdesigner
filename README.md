# filterdesigner
A MATLAB-like and simple digital filter design library for python.  
  
**filterdesigner** can make simple digital filters they have numerator and denominator coefficients and returns these characteristics.
This library aims to be able to generate FIR/IIR digital filter, prototype analog filters and convolute the digital filters like MATLAB on python.  
  
  
## Status
It is under construction.  
[![Build Status](https://travis-ci.org/Y-F-Acoustics/filterdesigner.svg?branch=master)](https://travis-ci.org/Y-F-Acoustics/filterdesigner)
![Python package](https://github.com/Y-F-Acoustics/filterdesigner/workflows/Python%20package/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/Y-F-Acoustics/filterdesigner/badge.svg?branch=master)](https://coveralls.io/github/Y-F-Acoustics/filterdesigner?branch=master)
  
## Module
### FIRDesign
  FIR digital filter design module  
  
### IIRDesign
  IIR digital and analog filter design module  
  
### FilterSpec
  Digital filter analysis module  
  
### Transform
  Transform from numerator and denominator to zelos, poles, gain and abcd coefficients  
  
### IO
  Import and export to .npy, .mat, .txt file and so on  
  
## Demos  
It is under construction.

## Requirements(tested)
[Python 3.7.6 or later](https://www.python.org/)  
[Numpy 1.18.1 or later](https://numpy.org/)  
[Scipy 1.3.2 or later](https://www.scipy.org/)  
[Matplotlib 3.1.1 or later](https://matplotlib.org/)  
  
## Licensing and copyright notices  
MATLAB is a registered trademark of The MathWorks, Inc.  

