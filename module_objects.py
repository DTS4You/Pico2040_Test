# #############################################################################
# ### Objets
# ### V 0.10
# #############################################################################
import time

import defaults
import module_radar
import module_target
import module_tracks
import random


class State_Machine():

    def __init__(self, wait_cycles=2):
        self.wait_cycles        = wait_cycles
        self.wait_counter       = 0
        self.new_flag           = True
        self.max_target_flag    = False

    def next_step(self):
        if self.wait_counter < self.wait_cycles:
            self.wait_counter += 1
        else:
            self.wait_counter = 0
            self.new_flag = False
            self.wait_cycles = random.randint(defaults.Values.wait_cycle_min, defaults.Values.wait_cycle_max)


def generate_radar_beams():
    my_radar_beams = []
    for i in range(defaults.Radar.num_of_beams):
        my_radar_beams.append(module_radar.Radar_Beam(defaults.Radar.num_of_leds))
    return my_radar_beams


def generate_targets():
    my_targets = []
    for i in range(defaults.Target.num_of_targets):
        my_targets.append(module_target.Target())
    return my_targets


def generate_tracks():
    my_tracks = []
    for i in range(defaults.Tracks.num_of_tracks):
        my_tracks.append(module_tracks.Track_Seg(defaults.Tracks.num_of_leds, defaults.Tracks.track_hit_y[i]))
    return my_tracks


def generate_objects():
    global state_logic, tracks, targets, radar_beams
    tracks = generate_tracks()
    targets = generate_targets()
    radar_beams = generate_radar_beams()
    state_logic = State_Machine()


def check_max_targets():
    num_of_activ_targets = 0
    for i in range(len(targets)):
        if targets[i].activ_flag:
            num_of_activ_targets += 1
    if num_of_activ_targets == len(targets):
        state_logic.max_target_flag = False
    else:
        state_logic.max_target_flag = True


# -----------------------------------------------------------------------------

def main():
    print("Start Objects")
    generate_objects()
    i = 0
    while i < 50:
        check_max_targets()
        state_logic.next_step()
        #print(state_logic.wait_cycles)
        i += 1
        time.sleep(0.3)


# ------------------------------------------------------------------------------
# --- Main
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
    print("=== End of Program ===")

# =============================================================================
