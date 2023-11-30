# Exercise:
#
#   a) Using dictionary `info` in `Data.py`, create a second dictionary
#      `fromSymbol` in the same module for converting the symbol of an element
#      to the corresponding atomic number
#
#   b) Define a simple class for holding the following information of an atom
#      as instance variables:
#     * Element (given as the atomic number)
#     * Number of implicit hydrogens
#     * Charge
#
#   c) For class `Atom`, define a function `symbol` that returns the symbol
#      corresponding to the atom's element.
#
#   d) For class `Atom`, define a function `mass` that returns the atom's
#      atomic mass. Make sure to include the mass from implicit hydrogen
#      atoms. Do the same thing for `exactMass`.
#
#   e) For class `Atom`, define a `__str__` function for pretty printing
#      the atom: The symbol followed by an `H` and the number of implicit
#      hydrogens (if any), followed by the charge (if any).
#      Example output:
#        print(Atom(6,0,0))
#        >>> C
#        print(Atom(6,1,0))
#        >>> CH
#        print(Atom(6,2,0))
#        >>> CH2
#        print(Atom(6,0,1))
#        >>> C+
#        print(Atom(6,0,2))
#        >>> C+2
#        print(Atom(6,0,-1))
#        >>> C-
#        print(Atom(6,0,-2))
#        >>> C-2
#        print(Atom(6,2,1))
#        >>> CH2+
#
#   f) Refine the constructor of class `Atom` in such a way that arguments
#      `hydrogens` and `charge` are optional, i.e. that it's possible to create
#      an `Atom` just by writing `Atom(6)`.
#
#   g) Refine the constructor of class `Atom` in such a way that
#      instead of the atomic number, we can also provide an element symbol.
#      You need to perform some runtime type checking for this to work.
