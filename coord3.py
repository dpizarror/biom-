# -*- coding: utf-8 -*-
import btk
from btkTools import *
import numpy as np
from gait_functions import *

filename='JuanDR_Walk01.c3d'

acq=smartReader(filename)
point_unit=acq.GetPointUnit()
point_frec=acq.GetPointFrequency()
marker_names=getMarkerNames(acq)

lmed=acq.GetPoint('LMED').GetValues()
rmed=acq.GetPoint('RMED').GetValues()
lasi=acq.GetPoint('LASI').GetValues()
rasi=acq.GetPoint('RASI').GetValues()


LLL = get_leglen(lmed, lasi)
LLR = get_leglen(rmed, rasi)
print(f'Largo de piernas. Izquierda: {LLL:.2f} mm, derecha {LLR:.2f} mm')

# hip joint centre
HJCleft = get_hjc(LLL) 
HJCright = get_hjc(LLR) 
#print(f'Coordenadas SACR: {sacr[4,:]}')
print(f'Coordenadas HJC izquierdo: {HJCleft}')
print(f'Coordenadas HJC derecho: {HJCright}')