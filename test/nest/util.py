import nest
import pylab


def plot_multimeter(plot_name, multimeter, param_to_display):
    status = nest.GetStatus(multimeter)[0]
    events = status['events']
    times = events['times']
    pylab.figure(plot_name)
    pylab.plot(times, events[param_to_display])


def display_plots():
    pylab.show()
