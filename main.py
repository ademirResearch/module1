from wind import Wind
import pmsg


def main():
    """
    Main program function
    """
    wind = Wind()
    u = wind.get_wind_array()
    # pmsg.test(u)
    pmsg.d_axis_loop(1)


if __name__ == "__main__":
    main()
