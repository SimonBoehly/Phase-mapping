# Phase-mapping
In this repository we explore the idea of a technique called phase mapping.

It has two aspects:
Firstly, we want to have a method that makes it redundant to look for "best" mappings. Instead, we create a superposition of the results of running different layouts in a clever way.
This is convenient since it stabilizes the process and we don't have to rely on finding the best mapping.

Secondly, it does not only take the mean of the respective results but introduces a way of postprocessing which aims at effectively reducing noisy counts in the output/results. This can also be
applied to running the same circuit multiple times to improve fidelity.
