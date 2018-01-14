from neuron import h
from neuron import gui  # VERY IMPORTANT to include 'gui'! Despite the fact that it is unused.
import numpy
import pylab

RUN_TIME = 150.0


def create_soma():
    soma = h.Section(name='soma')
    soma.L = 200.
    soma.diam = 50. / numpy.pi
    soma.nseg = 1
    h.define_shape()  # Translate into 3D points.
    soma.Ra = 200  # Axial resistance in Ohm * cm
    soma.cm = 2  # Membrane capacitance in micro Farads / cm^2
    soma.insert('motoneuron_5ht')
    return soma


def run_sim(soma):
    v_vec = h.Vector()
    cai_vec = h.Vector()
    t_vec = h.Vector()
    # h_vec = h.Vector()
    # m_vec = h.Vector()
    # n_vec = h.Vector()
    p_vec = h.Vector()
    mc_vec = h.Vector()
    hc_vec = h.Vector()
    v_vec.record(soma(0.5)._ref_v)
    cai_vec.record(soma(0.5)._ref_cai_motoneuron_5ht)

    # h_vec.record(soma(0.5)._ref_h_motoneuron_5ht)
    # m_vec.record(soma(0.5)._ref_m_motoneuron_5ht)
    # n_vec.record(soma(0.5)._ref_n_motoneuron_5ht)
    p_vec.record(soma(0.5)._ref_p_motoneuron_5ht)
    mc_vec.record(soma(0.5)._ref_mc_motoneuron_5ht)
    hc_vec.record(soma(0.5)._ref_hc_motoneuron_5ht)
    t_vec.record(h._ref_t)

    duration = RUN_TIME
    h.tstop = duration
    h.run()


    pylab.figure("Neuron iclamp")

    pylab.subplot(3,1,1)
    pylab.ylabel('V (mV)')
    pylab.plot(t_vec, v_vec, label="V_m")
    pylab.legend()

    pylab.subplot(3,1,3)
    pylab.ylabel('mmol')
    pylab.plot(t_vec, cai_vec, label="cai")
    pylab.legend()

    pylab.subplot(3,1,2)
    pylab.ylabel('particles')
    # plot_parameter(t_vec, h_vec, "h")
    # plot_parameter(t_vec, m_vec, "m")
    # plot_parameter(t_vec, n_vec, "n")
    pylab.plot(t_vec, p_vec, 'r', label="p")
    pylab.plot(t_vec, mc_vec, 'g', label="mc")
    pylab.plot(t_vec, hc_vec, 'b', label="hc")
    pylab.legend()
    pylab.show()
