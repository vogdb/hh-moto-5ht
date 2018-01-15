from neuron import h
from neuron import gui  # VERY IMPORTANT to include 'gui'! Despite the fact that it is unused.
import numpy
import pylab

soma = h.Section(name='soma')
soma.L = 200.
soma.diam = 50. / numpy.pi
soma.nseg = 1
h.define_shape()  # Translate into 3D points.
soma.Ra = 200  # Axial resistance in Ohm * cm
soma.cm = 2  # Membrane capacitance in micro Farads / cm^2
soma.insert('motoneuron_5ht')

iclamp = h.IClamp(soma(0.5))
iclamp.delay = 0
iclamp.dur = 10000.0
iclamp.amp = 0.7  # nA

v_vec = h.Vector()
cai_vec = h.Vector()
t_vec = h.Vector()
h_vec = h.Vector()
m_vec = h.Vector()
n_vec = h.Vector()
p_vec = h.Vector()
mc_vec = h.Vector()
hc_vec = h.Vector()

v_vec.record(soma(0.5)._ref_v)
cai_vec.record(soma(0.5)._ref_cai_motoneuron_5ht)
h_vec.record(soma(0.5)._ref_h_motoneuron_5ht)
m_vec.record(soma(0.5)._ref_m_motoneuron_5ht)
n_vec.record(soma(0.5)._ref_n_motoneuron_5ht)
p_vec.record(soma(0.5)._ref_p_motoneuron_5ht)
mc_vec.record(soma(0.5)._ref_mc_motoneuron_5ht)
hc_vec.record(soma(0.5)._ref_hc_motoneuron_5ht)
t_vec.record(h._ref_t)

h.tstop = 150.0
h.run()

pylab.figure()
pylab.title('Neuron iclamp sim')

pylab.subplot(4, 1, 1)
pylab.ylabel('Membrane Voltage')
pylab.plot(t_vec, v_vec, label="V_m")
pylab.legend()

pylab.subplot(4, 1, 2)
pylab.ylabel('Ca inside')
pylab.yticks(numpy.arange(0.0001, 0.0010, 0.0002))
pylab.plot(t_vec, cai_vec, label="Ca_in")
pylab.legend()

pylab.subplot(4, 1, 3)
pylab.ylim(0, 1)
pylab.ylabel('h, m, n particles')
pylab.plot(t_vec, h_vec, 'r', label="h")
pylab.plot(t_vec, m_vec, 'g', label="m")
pylab.plot(t_vec, n_vec, 'b', label="n")
pylab.legend()

pylab.subplot(4, 1, 4)
pylab.ylim(0, 1)
pylab.ylabel('p, mc, hc particles')
pylab.plot(t_vec, p_vec, 'r', label="p")
pylab.plot(t_vec, mc_vec, 'g', label="mc")
pylab.plot(t_vec, hc_vec, 'b', label="hc")
pylab.legend()

pylab.show()

