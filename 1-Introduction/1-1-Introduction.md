# Introduction

Before talking about TensorFlow lite, we need to talk briefly what kind of
problem we are trying to solve. Running neural networks model is
typically quite resource intensive.  Not only the training phase require
memory and computational power, but also inference can be quite taxing.
Consider cases when, for example, a real time inference is required from videos
or cameras. Different models can perform at different speeds that are
clearly strongly influenced by the hardware that the model is running on.

Typically one talk about machine learning at the edge when all the
computational tasks are performed on a device, typically with low memory
and power, directly where is needed, without sending data back and forth
to a more powerful server. Edge computing can address the following
issues

- The device must not be connected to the internet to work. You have cases
where the computationals tasks have to be performed in environment where
the internet connection is not existing, or maybe so slow that
exchanging data with a server may be unfeasible.
- Sometime in specific environment, you don't have access to a power
outlet. Meaning your devices need to use batteries. The problem
is that doing machine learning costs, typically, a lot of energy.
Devices must therefore use very low power amounts, meaning that we
need special ways of doing machine learning on such devices that does
not use all the battery. This is where TensorFlow Lite comes into play. Much
more on that later on.
- Everything happens on the device, meaning that there are no latency problems.
Sometime inference in the ms area are necessary, and therefore running
everything on the device becomes a must. Sending data to a server,
waiting for an evaluation and receiving the data back will typically require
lot of time.
- Lastly the data does not need to leave the device, meaning that
privacy is guaranteed. And not having an internet connection means also
that the device is normally quite safe from external attacks.

So to do edge computing we need two main components:
- A device that does not require so much energy and that is able to
run machine learning models
- Software that can be run on the device and that is able to run
machine learning models.
