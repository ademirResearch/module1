import parameters as pmsg
from control.matlab import *
import control
import matplotlib.pyplot as plt


def test(u):
    time_vector = []
    input_vector = list(u.array)
    for i in range(len(input_vector)):
        time_vector.append(i)

    num = 1
    den = [pmsg.LD, pmsg.RS]
    pmsg_transfer_function = TransferFunction(num, den)
    print(sys)
    time, mechanical_power, x_out = control.forced_response(pmsg_transfer_function, time_vector, input_vector)
    plt.plot(time, mechanical_power)
    plt.plot(input_vector)
    plt.show()


def d_axis_loop(ids_ref):
    """
    PMSG First Loop, D-Axis
    :param ids_ref: d-axis current reference value
    :type ids_ref: int
    :return: (ids) Actual d-axis current value
    :rtype: float
    """
    num = [1]
    den = [pmsg.LD, pmsg.RS]
    d_axis_transfer_function = TransferFunction(num, den)
    print(d_axis_transfer_function)

    pi_transfer_function = TransferFunction([pmsg.KP_d, pmsg.KI_d], [1, 0])
    d_axis_closed_loop_system = series(d_axis_transfer_function, pi_transfer_function)
    d_axis_closed_loop_system = feedback(d_axis_closed_loop_system * ids_ref, 1)
    print(d_axis_closed_loop_system)
    time, ids = control.step_response(d_axis_closed_loop_system)
    plt.plot(ids)
    plt.show()
    return ids




