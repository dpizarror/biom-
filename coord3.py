# -*- coding: utf-8 -*-
import btk
from btkTools import *
import numpy as np

filename='JuanDR_Walk01.c3d'

acq=smartReader(filename)
point_unit=acq.GetPointUnit()
point_frec=acq.GetPointFrequency()
marker_names=getMarkerNames(acq)