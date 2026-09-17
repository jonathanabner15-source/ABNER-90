import time
import math

def run_iss_tracker():
    print("==================================================")
    print("    ABNER-90 GEOSPATIAL STABILITY ENGINE v1.0     ")
    print("    SATELLITE SECTOR: ISS (ZARYA) OVER BEREA, KY   ")
    print("==================================================")
    
    f_beacon = 145800000.0   # 145.800 MHz VHF Downlink
    c = 299792458.0          # Speed of light (m/s)
    v_orbital = 7660.0       # Cruise velocity (m/s)
    
    steps = [
        {"time": "-3m 00s", "ele": 10, "state": "HORIZON ENTRY", "dir": "SW"},
        {"time": "-2m 00s", "ele": 25, "state": "ASCENDING    ", "dir": "WSW"},
        {"time": "-1m 00s", "ele": 52, "state": "APPROACHING  ", "dir": "WNW"},
        {"time": " 0m 00s", "ele": 68, "state": "MAX ELEVATION", "dir": "OVERHEAD"},
        {"time": "+1m 00s", "ele": 45, "state": "RECEDING     ", "dir": "ENE"},
        {"time": "+2m 00s", "ele": 18, "state": "DESCENDING   ", "dir": "NE"},
        {"time": "+3m 00s", "ele": 10, "state": "HORIZON EXIT ", "dir": "NNE"},
    ]
    
    for pt in steps:
        angle_rad = math.radians(pt["ele"])
        v_relative = v_orbital * math.cos(angle_rad)
        
        if "+" in pt["time"]:
            v_relative = -v_relative
        elif "0m 00s" in pt["time"]:
            v_relative = 0.0
            
        f_shifted = f_beacon * (1 + v_relative / c)
        doppler_delta = f_shifted - f_beacon
        
        print(f"[{pt['time']}] {pt['state']} | Dir: {pt['dir']:<8} | El: {pt['ele']}° | Freq: {f_shifted/1e6:.6f} MHz ({doppler_delta/1000:+0.3f} kHz)")
        time.sleep(1.0)

if __name__ == "__main__":
    run_iss_tracker()

