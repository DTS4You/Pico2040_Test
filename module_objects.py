# #############################################################################
# ### Objets
# ### V 0.10
# #############################################################################
import defaults
import module_radar
import module_target
import module_tracks


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


# -----------------------------------------------------------------------------

def main():
    print("Start Objects")
    my_tracks = generate_tracks()
    print(my_tracks[23].num_pix)
    print(len(my_tracks))
    my_targets = generate_targets()
    print(len(my_targets))


# ------------------------------------------------------------------------------
# --- Main
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
    print("=== End of Program ===")

# =============================================================================
