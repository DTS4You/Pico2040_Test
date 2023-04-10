# #############################################################################
# ### Tracks
# ### V 0.10
# #############################################################################

class Track_Seg:

    def __init__(self, num_pix):
        self.num_pix = num_pix
        self.position = 0
        self.hit_flag = False
        self.start_flag = True
        self.end_flag = False
        self.direction = False

    def next_position(self):
        if self.position > 0:
            self.start_flag = False

    def get_position(self):
        return self.position


# -----------------------------------------------------------------------------

def main():
    print("Start Global Init")
    mg = Radar_Beam(35)
    print(mg.position)
    print(mg.get_position())


# ------------------------------------------------------------------------------
# --- Main
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    main()

# =============================================================================

# Radar Strahlen von Position 0 bis "end_flag"
# Bei Treffer mit Target -> Farbe auf Rot und zurück zur Position 0
