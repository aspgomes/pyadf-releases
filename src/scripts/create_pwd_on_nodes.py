#!/usr/bin/env python

# This file is part of 
# PyADF - A Scripting Framework for Multiscale Quantum Chemistry.
# Copyright (C) 2006-2011 by Christoph R. Jacob, S. Maya Beyhan,
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

# This is a helper script for PyADF that creates the
# current directory on all nodes found in the HPMPI machine 
# file. This is needed before calling ADF because otherwise
# it will crash.

import os

if 'TC_HPMPI_MACHINE_FILE' in os.environ :

    f = open(os.environ['TC_HPMPI_MACHINE_FILE'], 'r')
    lines = f.readlines()
    f.close()

    for l in lines:
        node = l.split()[0]
        os.system('ssh %s mkdir -p %s' % (node, os.getcwd()) )