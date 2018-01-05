from neuron import h

import util

soma = util.create_soma()

iclamp = h.IClamp(soma(0.5))
iclamp.delay = 0
iclamp.dur = util.RUN_TIME
iclamp.amp = 0.7  # nA

util.run_sim(soma)
