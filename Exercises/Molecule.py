# With a data type for molecular formulae implemented, it is time
# to look at molecules themselves.
#
# Now, a molecule is a labeled, undirected graph, where we use integers to
# identify nodes and `Atom`s as their labels. In addition, we
# need to keep track of the neighbors of atoms, plus the
# types of bonds connecting atoms with their neighbors.
#
# We use a simple integer to describe the bond type: 1 for a single
# bond, 2 for a double bond, and 3 for a triple bond.
#
# A molecule can then be viewed as a dictionary linking nodes (integers)
# to pairs consisting of their labels (`Atom`s) and neighbors
# (dictionaries pairing nodes (integers) with bond types (integers)).
#
# As an example, here is ethanol in such a representation:
#
# ```
#   ethanol = { 0: (Atom("C",3), {1:1}),
#               1: (Atom("C",2), {0:1,2:1}),
#               2: (Atom("O",1), {1:1})
#             }
# ```
#
# As you can see, each of the heavy atoms of ethanol has its own node, while
# we keep the hydrogens implicit (if possible). For every node, we give its
# list of neighbors plus the bond order: For instance, atom 2 (the oxygen)
# is bound via a single bond to atom 1 (the central carbon), which itself
# has two neighbors (0 and 2, both bound via single bonds).
#
# a) Define a new class called `Molecule` that encapsulates the representation
#    above in a field called `mol`.
#
# b) Define a constructor for molecules that takes a list of
#    atoms (the node labels) plus a list of edges (triples consisting
#    of the two nodes plus the bond order), and transforms these
#    into the representation given above. Node, assume that the list of
#    edges contains every edge only once!
#
#    Make sure that this works correctly by creating some molecules and verifying
#    their inner representation.
#
#    Here's an example:
#
#    ```
#    test = Molecule([Atom("C",3),Atom("C",2),Atom("O",1)],[(0,1,1),(1,2,1)])
#    ```
#
#    If you run `print test.mol`, you should see output similar to this:
#
#    ```
#    {0: (<Atom.Atom object at 0x7f619772a2d0>, {1: 1}),
#     1: (<Atom.Atom object at 0x7f619772a350>, {0: 1, 2: 1}),
#     2: (<Atom.Atom object at 0x7f619772a390>, {1: 1})}
#    ```
#
#    Note: There is a more complex example of a molecule commented-out at the
#    end of this source file. Feel free to use it to the the functions you are
#    going to implement now.
#
# c) The "order" of a graph is the number of nodes it has. Add function
#    `order` to your `Molecule` class and implement it accordingly.
#
# d) The "size" of a graph is the number of edges it has. Add function
#    `edge` to your `Molecule` class and implement it accordingly.
#    Atention: Make sure you count every edge only once even though
#    edges appear twice in a molecule's adjacency representation.
#
# e) The "degree of a node" describes the number of neighbors it has.
#    Add a function `degree` to class `Molecule`
#    that returns the degree of its node input (given as an integer).
#
# f) A node in a graph is "isolate" if it has degree 0. Implement
#    a function `isIsolate` that returns `true` if the node has no neighbors.
#
# g) A node in a graph is "terminal" if it has degree 1. Implement
#    a function `isTerminal` that returns `true` if the node has no neighbors.
#
# h) Implement functions `mass` and `exactMass` to compute the molar mass
#    (and exact molar mass) of a molecule.
#
# i) Implement function `formula` that computes and returns the
#    molecular formula of a molecule.
#
# j) (hard) You are now going to implement your first graph traversal
#    algorithm.
#
#    A "walk" in a graph is a sequence of nodes, so that every node
#    in the sequence is a neighbor of the previous node in the sequence.
#    For instance, [0,1,2,1] is a walk in ethanol:
#    Atom 0 is a neighbor of atom 1, 1 is a neighbor of 2, and 2
#    is a neighbor of 1. However, [0,1,2,0] is not a walk, since
#    0 is not a neighbor of 2.
#
#    A "trail" is a walk in which no edge is traversed more than once.
#    A "path" is a walk in which no node is visited more than once.
#    If there is a path from node `u` to `v`, the two nodes are said
#    to be "connected". Every node is trivially connected to itself.
#
#    Given a molecule and two of its nodes, write a function that
#    determines if the two nodes are connected.
#
# k) Even if you haven't finished everything, you might want to test
#    your code with the following non-trivial molecule (tyrosine
#    hydro chloride).
#
#
# ```
#    tyrosineHCl = Molecule([ Atom("N",3,1),   #0
#                             Atom("C",1),     #1
#                             Atom("C"),       #2
#                             Atom("O"),       #3
#                             Atom("O",1),     #4
#                             Atom("C",2),     #5
#                             Atom("C"),       #6
#                             Atom("C",1),     #7
#                             Atom("C",1),     #8
#                             Atom("C"),       #9
#                             Atom("C",1),     #10
#                             Atom("C",1),     #11
#                             Atom("O",1),     #12
#                             Atom("Cl",0,-1)],#13
#                           [ (0,1,1),
#                             (1,2,1),
#                             (1,5,1),
#                             (2,3,2),
#                             (2,4,1),
#                             (5,6,1),
#                             (6,7,1),
#                             (6,11,2),
#                             (7,8,2),
#                             (8,9,1),
#                             (9,10,2),
#                             (9,12,1),
#                             (10,11,1) ]
#                           )
# ```
#
#    Its order is 14.
#    Its size is 13.
#    Its mass is 217.694.
#    Its exact mass is 217.050570924.
#    Its formula is C9H12ClNO3.
#    Its terminal nodes are nodes 0, 3, 4, and 12.
#    It hase only once isolte node: Node 13.
#    Node 13 is connected to no other node (it is isolate after all),
#    but all other nodes are connected.
