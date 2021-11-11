#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 14:17:32 2021

@author: yuyingren
"""


import pynini
from pynini.lib import pynutil


words = pynini.string_map("EngList_cmu.txt")


matcher = pynutil.join(words, " ").optimize()



preModel_KataEng=pynini.Fst.read("fstModels/NKP_kataEng.fst")
preModel_CMUEng=pynini.Fst.read("fstModels//NKP_CMUEng.fst")
preModel_romaEng=pynini.Fst.read("fstModels//NKP_romaEng.fst")

newModel_KataEng= preModel_KataEng @ matcher
newModel_CMUEng= preModel_CMUEng @ matcher
newModel_romaEng= preModel_romaEng @ matcher



newModel_KataEng.write("KataEngNEW.fst")
newModel_CMUEng.write("CMUEngNEW.fst")
newModel_romaEng.write("romaEngNEW.fst")
