# This file is part of 
# PyADF - A Scripting Framework for Multiscale Quantum Chemistry.
# Copyright (C) 2006-2012 by Christoph R. Jacob, S. Maya Beyhan,
# Rosa E. Bulo, Andre S. P. Gomes, Andreas Goetz, Karin Kiewisch,
# Jetze Sikkema, and Lucas Visscher 
#
#    PyADF is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    PyADF is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with PyADF.  If not, see <http://www.gnu.org/licenses/>.
"""
 General utilities that are used internally.

 @author:       Christoph Jacob and others
 @organization: Karlsruhe Institute of Technology (KIT)
 @contact:      christoph.jacob@kit.edu
 
"""

from Errors import PyAdfError

newjobmarker = '--- PyADF *** new job *** PyADF ---\n'

class PSE (object):
    def __init__(self):
        import openbabel
        self._OBElementTable = openbabel.OBElementTable()
    
    def get_atomic_number (self, symbol):
        return self._OBElementTable.GetAtomicNum(symbol)
    
    def get_symbol (self, atnum):
        return self._OBElementTable.GetSymbol(atnum)

pse = PSE()

Bohr_in_Angstrom = 0.5291772108
au_in_Debye =  2.54177
au_in_eV = 27.2114

def conversion(inp, out):
    factor = {}
    factor ['Hartree'] = {}
    factor ['Hartree']['kJ/mol'] = 2625.50 #AWG: from NIST
    factor ['Hartree']['kcal/mol'] = 627.090
    factor ['Hartree']['eV'] = 27.2114
    if inp == out:
        return 1
    else:
        if inp in factor:
            if out in factor[inp]:
                return factor[inp][out]
            else:
                raise PyAdfError('conversion does not support output unit for given input unit')
        else:
            raise PyAdfError('conversion does not support input unit')



