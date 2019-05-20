#!/usr/bin/env python3
# By Migdal
# Convert homer motif profile to PWM
# Usage: profile2pwm.py bach1.motif

from sys import argv
import numpy as np

profile = argv[1]
pwm = []
with open(profile) as handle:
    line = handle.readline()
    while line:
        if not line.startswith(">"):
            line = line.split()
            pwm.append(line)
        line = handle.readline()

pwm = np.array(pwm, dtype = np.float64)
pwm *= 1000
pwm = pwm.astype('int64')
pwm = pwm.astype('str')
pwm = np.transpose(pwm)

for i in range(pwm.shape[0]):
    print(" ".join(pwm[i, ]))
