#!/ust/bin/env python3
# -*- coding: utf-8 -*-

import sys, os
a= os.path.normpath(os.path.join(os.path.abspath(__file__), '../../'))
sys.path.insert(0, a)

from .SupCategory import *
from .SupCriteria import *
from .Matrix import *
#from .test2 import *
