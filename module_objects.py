# #############################################################################
# ### Objets
# ### V 0.10
# #############################################################################
import defaults
import module_target
import module_tracks


def generate_targets():
    my_targets = []
    my_targets.append(module_target.Target(20))
    return my_targets


def generate_tracks():
    my_tracks =  []
    my_tracks.append(module_tracks.Track_Seg(defaults.Tracks.num_of_leds, defaults.Tracks.track_1_hit))


# -----------------------------------------------------------------------------

def main():
    print("Start Objects")
    print(generate_targets())


# ------------------------------------------------------------------------------
# --- Main
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
    print("=== End of Program ===")

# =============================================================================
