from neuron import h

import util

soma = util.create_soma()

syn_ = h.ExpSyn(soma(0.5))
syn_.tau = 0.5
syn_.e = 0

stim = h.NetStim()
stim.number = 1
stim.start = util.RUN_TIME / 2
stim.interval = util.RUN_TIME

ncstim = h.NetCon(stim, syn_)
ncstim.delay = 1
ncstim.weight[0] = 1

util.run_sim(soma)
