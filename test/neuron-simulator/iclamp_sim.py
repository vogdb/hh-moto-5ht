from neuron import h

import util

soma = util.create_soma()

iclamp = h.IClamp(soma(0))
iclamp.delay = 5
iclamp.dur = 1
iclamp.amp = 0.1  # nA

util.run_sim(soma)
