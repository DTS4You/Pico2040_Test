# #############################################################################
# ### Tracks
# ### V 0.10
# #############################################################################

# Bahnen der Schmutzteile
class Track_Seg:
    """Bahnen der Schmutzteile \n
    Direction = False -> Links nach Rechts \n
    Direction = True  -> Rechts nach Links."""

    def __init__(self, num_pix):
        """Anzahl der LEDs"""
        self.num_pix = num_pix
        self.direction = False

    def get_direction(self):
        return self.direction


# -----------------------------------------------------------------------------

def main():
    print("Start Global Init")
    mg = Track_Seg(20)
    print(mg.direction)
    print(mg.get_direction())


# ------------------------------------------------------------------------------
# --- Main
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    main()

# =============================================================================
