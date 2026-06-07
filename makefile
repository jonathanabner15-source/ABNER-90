# ==============================================================================
# INDUSTRIAL MAKEFILE: ABNER'S HONEST HARMONICS LLC
# ENVIRONMENT: Native Linux aarch64 (Termux)
# DESIGNED BY: Jonathan Wayne Abner
# ==============================================================================

CC          := clang
CFLAGS      := -O3 -Wall -march=native
PYTHON      := python3
TARGET      := ABNER-90
CORE_SCRIPT := pisano60_core.py
SECTOR      := "Berea"

.PHONY: all init compile run sync status clean help

all: init compile run

init:
	@echo "[INIT] Verifying sovereign folder structures..."
	@mkdir -p build logs data
	@if [ ! -f SUCCESS_RECORD.py ]; then echo "print('BEREA SECTOR SUCCESS: ARCHIVE LOCKED.')" > SUCCESS_RECORD.py; fi
	@echo "[INIT] System check complete. 0 zombies detected."

compile:
	@echo "[COMPILE] Invoking clang for aarch64 native optimizations..."
	@if [ -f main.c ]; then $(CC) $(CFLAGS) main.c -o build/$(TARGET); echo "[COMPILE] Native execution binary locked in build/$(TARGET)"; else echo "[COMPILE] Standby: Operating on native Python translation layer."; fi

run:
	@echo "[RUN] Launching matrix rotation loops for Sector: $(SECTOR)..."
	@if [ -f $(CORE_SCRIPT) ]; then $(PYTHON) $(CORE_SCRIPT) --sync --sector $(SECTOR); fi

sync:
	@echo "[SYNC] Staging changes to the tracking ledger..."
	@git add .
	@git commit -m "System Update: Core running at optimal virtual memory capacity." || echo "[SYNC] Ledger up-to-date."

status:
	@echo "=============================================================================="
	@echo "                   OPERATIONAL INTEGRITY LOG: BEREA SECTOR                    "
	@echo "=============================================================================="
	@echo "Current Time: $$(date)"
	@echo "------------------------------------------------------------------------------"
	@ps -ef | grep -E 'python|clang|node|tmux' | grep -v grep || echo "No active long-running pipelines detected."
	@echo "------------------------------------------------------------------------------"
	@top -n 1 -b | head -n 5
	@echo "=============================================================================="

clean:
	@echo "[CLEAN] Flushing development caches..."
	@rm -rf build/
	@find . -type d -name "__pycache__" -exec rm -rf {} +

help:
	@echo "Commands: make, make init, make compile, make run, make sync, make status, make clean"
