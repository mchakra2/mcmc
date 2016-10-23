===============================
MCMC
===============================


.. image:: https://img.shields.io/travis/mchakra2/mcmc.svg
        :target: https://travis-ci.org/mchakra2/mcmc

.. image:: https://pyup.io/repos/github/mchakra2/mcmc/shield.svg
	:target: https://pyup.io/repos/github/mchakra2/mcmc/
	:alt: Updates

.. image:: https://coveralls.io/repos/github/mchakra2/mcmc/badge.svg
        :target: https://coveralls.io/github/mchakra2/mcmc




Applying MCMC to generate a sequence of connected graphs


* Free software: MIT license
* Documentation: https://mcmc.readthedocs.io.


Features
--------

* A function to read in tuples from input file
* A function to make an initial connected graph from the given tuples
* A function to either add or remove an edge
* A function to calculate the number of bridges in a graph
* A function to calculate qij and qji
* The main function makes a new graph for every iteration by randomly selecting an edge and either switching it on (if the edge is not present) or switching it off (if the edge is present and is not a bridge) 

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

