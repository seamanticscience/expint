# expint

Python function for evaluation of exponential integrals, E<sub>n</sub>(x), with real values, _not just integers_, of the order "n" from the paper by Navas-Palencia (2018) in the journal Numerical Algorithms, doi:[10.1007/s11075-017-0331-z](http://doi.org/10.1007/s11075-017-0331-z). 

The exponential integral (see also `scipy.special.expn`) can be related to the upper incomplete gamma function:

![\begin{align*}
\Gamma(s,x) = x^s E_{(1-s)}(x) \equiv x^s E_n(1-s,x),
\end{align*}
](https://render.githubusercontent.com/render/math?math=%5CLarge+%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A%5CGamma%28s%2Cx%29+%3D+x%5Es+E_%7B%281-s%29%7D%28x%29+%5Cequiv+x%5Es+E_n%281-s%2Cx%29%2C%0A%5Cend%7Balign%2A%7D%0A)

`scipy.special.expn` can only cope with integer values of the order, and most (all?) gamma function routines I tried also relied on positive integer order, so forget about calculating `Γ(-0.8,x)`, if that's something you find you need to do...

My main reason for posting this here, _since the code is available on the journal website as a supplement_, was because I needed to make a few tweaks in order to install the package successfully:
1. Replace the includes path in `expint.i`.
1. The code is written in `C++` and then wrapped for Python using `swig`, so I run `swig -c++ -python expint.i` to generate `expint.py`.
1. Create a `setup.py` script.
1. Compile using python: `python setup.py build_ext --inplace`
1. Put the pyexpint folder somewhere in my `PYTHONPATH` and link `expint.py` to `__init__.py`
1. `import expint` as usual, and success! 

Here's their copyright notice, if you find this useful then please [cite their paper!](http://doi.org/10.1007/s11075-017-0331-z):
```
/*Copyright (c) 2017 Guillermo Navas-Palencia

Permission is hereby granted, free of charge, to any person obtaining a copy of 
this software and associated documentation files (the "Software"), to deal in 
the Software without restriction, including without limitation the rights to 
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies 
of the Software, and to permit persons to whom the Software is furnished to do 
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all 
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN 
THE SOFTWARE.*/
```
