###############################################################################
# MyGlobals
###############################################################################

class Radar:
    num_of_leds = 78


class Target:
    num_of_targets = 10


class Tracks:
    num_of_tracks = 24
    num_of_leds = 78


class Colors:
    target          = [ 10, 20, 30]
    radar_send      = [ 10, 20, 30]
    radar_receive   = [ 10, 20, 30]


class Values:
    loop_time       = 0.3


# -----------------------------------------------------------------------------
def main_task():
    print(Tracks.num_of_tracks)
    print(Colors.target[1])
    print(Colors.radar_send)


# =============================================================================
if __name__ == '__main__':

    main_task()
    print("=== End of Program ===")
# =============================================================================
