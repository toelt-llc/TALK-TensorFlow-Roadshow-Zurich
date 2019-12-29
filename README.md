# Edge computing with TensorFlow

![](https://img.shields.io/badge/dependencies-TensorFlow20-blue)
![](https://img.shields.io/badge/dependencies-Jupyter-red)
[![license MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
<!--![](https://img.shields.io/github/forks/toelt-lcc/Bootcamp-Deep-Learning-on-Edge-Devices?label=Fork)
![](https://img.shields.io/github/last-commit/toelt-Michelucci/Bootcamp-Deep-Learning-on-Edge-Devices.svg)
![](https://img.shields.io/github/stars/michelucci/oreilly-london-ai.svg)
![](https://img.shields.io/github/issues/michelucci/oreilly-london-ai.svg)-->

**Author**: Umberto Michelucci (umberto.michelucci@toelt.ai) - (C) 2020 - TOELT llc

This repository contains material, notebooks, scripts about Edge Computing and TensorFlow Lite.

Note that this repository will use relative linking. That means that
all the documentations (markdown files) can be accessed directly
from your laptop without the need of having access to internet
to get files from [GitHub](https://github.com/michelucci/Edge-computing-with-TensorFlow), once you have cloned the repository
on your machine. Of course it can be completely accessed directly
online from [GitHub](https://github.com/michelucci/Edge-computing-with-TensorFlow).

The material is divided in sections, each having its own folder.
In each folder you will find a `README.md` with a table of content and instructions of what you can find in the folder. Here you will find a high level table of content that should help you in navigating the material and finding what you need or search.

Mostly the material is presented with three different media types:

1. **Jupyter notebooks or Python scripts**:  those are scripts that can
be used to try and learn. The notebooks and scripts are mostly used for
the hands-on sessions.

2. **Google Slides**: the slides linked in this repository are not meant
to contain all the material in details, but are used as a guideline.
They show the reader/learner the main points that are important.

3. **Markdown files in the repository**: for some more technical material,
that is important and that requires more explanation I have provided
some markdown files that can be accessed directly online with more information
on specific technical issues.

## Difficulty Tiers

All the material (inlcuding slides) is divided in difficulties Tiers.
At the beginning of each section, notebooks or readme file you will find
indication of its difficulty. In this way you can skip the most
challenging sections in case you are not experiences and want to
concentrate on beginner material.

Here is a short description of each difficulty tier.

**Difficulty Tier 1**: the material is really easy and no previous
experience is required. Typically in this tier no programming or
mathematics is used. Concepts are explained only at a very high level.
No hands-on sessions are necessary.

**Difficult Tier 2**: the material requires some experience. Basic programming
(mostly Python) and mathematics know-how is necessary to understand and profit from the material.
Only basic concepts are used in this tier, and mostly only simple problems
are analyzed to keep the level friendly enough.

**Difficulty Tier 3**: the material requires previous experience in
both programming and machine learning. Advanced programming skills in Python
and mathematics are necessary to completely grasp the concepts and
use them efficiently. Material in this Tier is only used to solve
problems that normally cannot be solved by pre-ready standard solutions.
The problems present several challenges in parallel that needs to be
addressed by different techniques from different fields.

## Table of Content

### Chapter 1 - Introduction and setup

[1.1 Introduction](1-Introduction/1-1-Introduction.md)

[1.2 Setup of Coral Device on MAC OS Catalina](1-Introduction/1-2-Setup-of-Coral-Catalina.md)



### Chapter 2 - Hardware Accelerators


[2.1 How a TPU works: a very high level overview](2-Hardware_Accelerators/2-1-TPU.md)

### Chapter 3 - Quantization of models

[3.1  Quantization](3-1-quantization.md)

### Chapter 4 - TensorFlow Lite

[4.1 Introduction](4-1-Introduction.md)

[4.2  Optimization Techniques in TensorFlow Lite](4-2-Optimization-in-TFLite.md)

[4.3  Saving and converting a model](4-3-saving-converting-models.md)

[4.4  TF-Lite end to end example](4-4-TFLite-end-to-end-example.md)

[4.5  Post-training quantization](4-5-post-training-optimization.md)

[4.6  Conversion with unsupported operations](4-6-conversion-with-unsupported-operations.md)

[4.7  Optimization paths](4-7-optimization-paths.md)

[4.8  Running models](4-8-running-models.md)

[4.9  Transfer Learning](4-9-transfer-learning.md)
