import nest
import pylab


def plot_parameter(device, param_to_display, label, style='-'):
    status = nest.GetStatus(device)[0]
    events = status['events']
    times = events['times']
    pylab.plot(times, events[param_to_display], style, label)


nest.Install("research_team_models")
nest.SetKernelStatus(dict(resolution=0.1))

neuron = nest.Create(
    'hh_moto_5ht', params={
        "I_e": 700.0,  # pA
        "C_m": 100.0,  # pF
        "t_ref": 2.0,
    }
)
multimeter = nest.Create(
    'multimeter',
    params={
        "record_from": [
            "V_m",
            "Ca_in",
            "Act_m",
            "Act_h",
            "Inact_n",
            "Act_mc",
            "Act_hc"
        ],
        "withtime": True,
        "interval": 0.1
    }
)

nest.Connect(multimeter, neuron)
nest.Simulate(150.)

pylab.figure("Nest iclamp")

pylab.subplot(3, 1, 1)
pylab.ylabel('V (mV)')
plot_parameter(multimeter, 'V_m', 'V_m')
pylab.legend()

pylab.subplot(3, 1, 3)
pylab.ylabel('mmol')
plot_parameter(multimeter, 'Ca_in', 'Ca_in')
pylab.legend()

pylab.subplot(3, 1, 2)
pylab.ylabel('particles')
plot_parameter(multimeter, 'Act_p', 'p', 'r')
plot_parameter(multimeter, 'Act_mc', 'mc', 'g')
plot_parameter(multimeter, 'Act_hc', 'hc', 'b')
pylab.legend()

pylab.show()
