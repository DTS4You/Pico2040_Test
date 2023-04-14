###############################################################################
# MyGlobals
###############################################################################

class Radar:
    num_of_beams    = 4
    num_of_leds     = 78
    target_hit_pos  = 60                # Trefferposition von Links nach Rechts in LEDs gerechnet


class Target:
    num_of_targets = 10


class Tracks:
    num_of_tracks   = 24
    num_of_leds     = 78
    #                   1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24
    track_hit_x     = [ 0,  1,  2,  3,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
    # Gibt die seitliche Position an, auf den der Radar-Strahls die Bahn treffen könnte
    #                   1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24
    track_hit_y     = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
    # Gibt die Höhe an, auf der der Rader-Strahl die Bahn treffen könnte


class Colors:
    target          = [ 10, 20, 30]
    radar_send      = [ 10, 20, 30]
    radar_receive   = [ 10, 20, 30]


class Values:
    loop_time       = 0.3
    wait_cycle_min  = 2                  # Anzahl der min. Radarstrahlenverläufe bis neue Schottteile erzeugt werden
    wait_cycle_max  = 10                 # Anzahl der max. Radarstrahlenverläufe bis neue Schottteile erzeugt werden


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
