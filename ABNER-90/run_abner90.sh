#!/data/data/com.termux/files/usr/bin/bash
export OMP_NUM_THREADS=1
taskset -c 0 python3 abner90_state_space_test.py
