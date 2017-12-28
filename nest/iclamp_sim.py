import nest
import util

neuron = nest.Create(
    'hh_psc_alpha', params={"I_e": 378.0}
)
multimeter = nest.Create(
    'multimeter',
    params={"record_from": ["V_m", "I_syn_ex", "I_syn_in"], "withtime": True}
)

nest.Connect(multimeter, neuron)
nest.Simulate(150.)

util.plot_multimeter('V_m', multimeter, 'V_m')
util.display_plots()
