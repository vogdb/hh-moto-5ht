import nest
import util


nest.Install("research_team_models")

neuron = nest.Create(
    'hh_moto_5ht', params={
        "I_e": 670.0, #pA
        "C_m": 200.0, #pF
        "t_ref": 0.0,
    }
)
multimeter = nest.Create(
    'multimeter',
    params={"record_from": ["V_m"], "withtime": True}
)

nest.Connect(multimeter, neuron)
nest.Simulate(150.)

util.plot_multimeter('V_m', multimeter, 'V_m')
util.display_plots()
