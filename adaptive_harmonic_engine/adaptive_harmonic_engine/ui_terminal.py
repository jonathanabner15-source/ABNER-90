# ui_terminal.py
# Jonathan Wayne Abner — Terminal UI for Harmonic Engine

import harmonic_engine_part3 as cosmic
import harmonic_engine_part4 as perpetual

def menu():
    print("\n=== Harmonic Engine Terminal UI ===")
    print("1) Quasar Profile")
    print("2) Event Horizon Profile")
    print("3) Accretion Disk Profile")
    print("4) Perpetual Motion Engine")
    print("0) Exit")

def run():
    while True:
        menu()
        choice = input("Select option: ").strip()

        if choice == "1":
            print(cosmic.quasar_profile())
        elif choice == "2":
            print(cosmic.event_horizon_profile())
        elif choice == "3":
            print(cosmic.accretion_disk_profile())
        elif choice == "4":
            perpetual.run_perpetual_engine()
        elif choice == "0":
            break
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    run()
