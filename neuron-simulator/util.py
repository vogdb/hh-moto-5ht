from neuron import h
from neuron import gui  # VERY IMPORTANT to include 'gui'! Despite the fact that it is unused.
from matplotlib import pyplot

RUN_TIME = 25.0


def create_soma():
    soma = h.Section(name='soma')
    soma.L = soma.diam = 12.6157  # microns
    h.define_shape()  # Translate into 3D points.
    soma.Ra = 200  # Axial resistance in Ohm * cm
    soma.cm = 2  # Membrane capacitance in micro Farads / cm^2
    soma.insert('motoneuron_5ht')
    return soma


def plot_vm(t_vec, v_vec):
    pyplot.figure(figsize=(8, 4))
    pyplot.plot(t_vec, v_vec)
    pyplot.xlabel('time (ms)')
    pyplot.ylabel('mV')
    pyplot.show()


def run_sim(soma):
    v_vec = h.Vector()
    t_vec = h.Vector()
    v_vec.record(soma(0)._ref_v)
    t_vec.record(h._ref_t)

    duration = RUN_TIME
    h.tstop = duration
    h.run()

    plot_vm(t_vec, v_vec)
