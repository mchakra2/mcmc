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

* input_arg: function to read in parameters and node tuples from the input file
* dist: function to calculate the distance between two grid points or tuples
* make_init_graph: function to make an initial connected graph from the given tuples
* graph_change: function to either add or remove an edge
* calculate_bridges: function to calculate the number of bridges in a graph
* calculate_q: function to calculate qij and qji
* theta_func: function to calculate theta, which is subsequently used for calculating the relative probability pi_j/pi_i
* MH: function that accepts or rejects the proposed change in graph according to the Metropolis Hastings algorithm
* max_shortest_path: function which return the longest among the shortest paths between vertex 0 and all other vertices
* graph_count: function to keep track of unique graphs encountered during the simulation using a dictionary
* mc_chain_generator: function to generate the markov chain for the given number of iterations
* quantiling: function to return the edge list of 1% most probable graphs  
* main: The main function

Implementation Details
~~~~~~~~~~~~~~~~~~~~~~~

In this implementation of Markov Chain Montecarlo (MCMC), a new connected graph (G2) is generated by mutating the state of a randomly selected edge (from all possible edges for the given nodes) of the existing graph (G1). So, if the selected edge is present in G1, it is removed if removal of that edge does not disconnect the graph. If the randomly selected edge is not present in G1, the edge is added. In the code, random edge selection is done by randomly selecting two node tuples from tuple list M without replacement. qij,qji and the relative probability of pi_j/pi_i are calculated. G2 is either accepted or rejected according to the Metropolis Hastings algorithm. The edge list of unique graph encountered during the simulation is added to a dictionary. For each additional observation of an already observed graph, the value of the key in the dictionary is incremented by 1. Throughout the simulation a running sum of the following are maintained: degree of vertex 0, total number of edges in the G1 and the longest path from vertex 0 to any other vertex. Thoughout the implementation, the first node tuple in the nodelist M is considered as vertex 0. The weight of an edge between two vertices is the Euclidian distance between the two node tuples. The expected values of an attribute is calculated at the end of the simulation by dividing the running sum by the number of iterations. The top 1% of most probable graphs is given in the output file as edge lists. When the number of observed unique graphs is less than 100, only the most likely graph is provided as output. Default parameter values are coded in the **mcmc.py** file in **mcmc** sub-directory of the package. The user has to provide an input file named **input.txt** which contains the following information:


* parameter r (optional)
* parameter T (optional)
* iterations: This is the number of steps in the monte carlo simulation
* location of the output file     
* nodes as tuples (e.g. 2,2 .Each node tuple should be written in a separate line.)

The input file must be saved in the **IOFiles** subdirectory. The **IOFiles** subdirecroty already contains an example input file. Please note that the keys identifying the parameters in the input file should not be altered. To run the script, clone the package by typing this in your command line:
  
git clone https://github.com/mchakra2/mcmc.git


Adjust the **input.txt** file in **IOFiles** subdirectory to your liking. To run the mcmc script, make sure you are in the main **mcmc** package directory (but out of the **mcmc** subdirectory!). Type the following:

python ./mcmc/__init__.py

You will find the output file in the location that you have mentioned in **input.txt** file. If you did not specify the name and location of the output file, you will find the **output.txt**  file under subdirectory **IOFiles** (because that is the default output file location!).   



Credits
---------

* **Maghesree Chakraborty** - **mchakra2@ur.rochester.edu**
Special thanks to Dr. A White for being an excellent guide. 

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
