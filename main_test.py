# *****************************************************************************
# *** Gestra V2                                                             ***
# *** Ausführung DLR                                                        ***
# *** V 0.11                                                                ***
# *****************************************************************************

import time
import module_globals

x = module_globals.Global.age

# -----------------------------------------------------------------------------
def main_loop():

    print("Main Loop")

    try:
        while True:
            print("Wait_Loop")
            time.sleep(1.0)
    except KeyboardInterrupt:
        print("Main loop ended!")


# =============================================================================
if __name__ == '__main__':

    main_loop()
    print("=== End of Program ===")
# =============================================================================
