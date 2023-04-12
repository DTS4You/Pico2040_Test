# #############################################################################
# ### Targets
# ### V 0.10
# #############################################################################

class Target:

    def __init__(self):
        """Schrottteile \n
        Position -> Links nach Rechts \n
        Track_num -> Bahn-Nummer"""
        self.position = 0
        self.track_num = 0
        self.activ_flag = False
        self.end_flag = False

    def next_position(self):
        if self.position > 0:
            self.activ_flag = True

    def get_position(self):
        return self.position


# -----------------------------------------------------------------------------

def main():
    print("Start Global Init")
    mg = Target()
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
