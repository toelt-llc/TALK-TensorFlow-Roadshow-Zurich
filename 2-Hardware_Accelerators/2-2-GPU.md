# How a [Graphics Processing Units (GPU)](https://en.wikipedia.org/wiki/Graphics_processing_units) is working - some notes

A GPU does almost the same thing as the [CPU](https://en.wikipedia.org/wiki/Central_processing_unit) but has thousands of [ALU](https://en.wikipedia.org/wiki/Arithmetic_logic_unit)'s to perform its calculations.
Basically a [GPU](https://en.wikipedia.org/wiki/Graphics_processing_units) can do many matrix multiplication at the same time,
but each matrix multiplication will be done as the [CPU](https://en.wikipedia.org/wiki/Central_processing_unit) does it, in a sequential
way.

 Their highly parallel structure makes them more efficient than general-purpose central processing units (CPUs) for algorithms that process large blocks of data in parallel [2].

In short, a [GPU](https://en.wikipedia.org/wiki/Graphics_processing_units) drastically increases its throughput by parallelising its computation in exchange for an increase in its latency [1]. And as formulated in [1]

> A CPU is a Spartan warrior which is strong and well-trained while the GPU is like a giant army of peasants which can defeat the Spartan because they are with that many.

[1] [https://blog.ml6.eu/googles-edge-tpu-what-how-why-945b32413cde](https://blog.ml6.eu/googles-edge-tpu-what-how-why-945b32413cde)

[2] [https://en.wikipedia.org/wiki/Graphics_processing_unit](https://en.wikipedia.org/wiki/Graphics_processing_unit)

[<< (Previous) Section 2.1](2-1-CPU.md) | [ (Up) Chapter 2](README.md) |
[>> (Next) Section 2.3](2-3-TPU.md)
