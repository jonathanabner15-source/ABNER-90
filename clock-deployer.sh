#!/data/data/com.termux/files/usr/bin/bash

# ─────────────────────────────────────────────
#  ABNER'S HONEST HARMONICS — Clock Deployer
#  Geometric Clock Construction Visualizer
# ─────────────────────────────────────────────

REPO_DIR="$HOME/harmonics"
FILE="geometric-clock.html"
PORT=8080

echo ""
echo "╔══════════════════════════════════════╗"
echo "║   ABNER'S HONEST HARMONICS           ║"
echo "║   Geometric Clock Deployer           ║"
echo "╚══════════════════════════════════════╝"
echo ""

# ── 1. Dependencies ──────────────────────────
echo "[1/4] Checking dependencies..."

if ! command -v python3 &>/dev/null; then
  echo "  → Installing python..."
  pkg install python -y
else
  echo "  ✓ python3 found"
fi

if ! command -v git &>/dev/null; then
  echo "  → Installing git..."
  pkg install git -y
else
  echo "  ✓ git found"
fi

# ── 2. Setup repo dir ────────────────────────
echo ""
echo "[2/4] Setting up directory..."

mkdir -p "$REPO_DIR"

# Copy the HTML file if it exists in current dir
if [ -f "$FILE" ]; then
  cp "$FILE" "$REPO_DIR/$FILE"
  echo "  ✓ Copied $FILE to $REPO_DIR"
else
  echo "  ⚠ $FILE not found in current directory"
  echo "    Checking for index.html instead..."
  if [ -f "index.html" ]; then
    cp "index.html" "$REPO_DIR/$FILE"
    echo "  ✓ Using index.html as $FILE"
  else
    echo "  ⚠ No source file found. Place geometric-clock.html here first."
    exit 1
  fi
fi

# ── 3. Git init / commit ─────────────────────
echo ""
echo "[3/4] Git integration..."

cd "$REPO_DIR"

if [ ! -d ".git" ]; then
  git init
  echo "  ✓ Git repo initialized"
else
  echo "  ✓ Git repo exists"
fi

# Create a README if none exists
if [ ! -f "README.md" ]; then
cat > README.md << 'EOF'
# Abner's Honest Harmonics — Geometric Clock

A geometric construction demonstrating how a Triangle, Hexagon, and Nonagon
nested together generate all 12 hour positions of a clock face.

## Construction Steps
1. Establish 8-point compass (cardinal + secondary directions)
2. Triangle — zero at East, 120° intervals → hours 3, 7, 11
3. Hexagon — zero at South, 60° intervals → even hours
4. Nonagon — zero at West, 40° intervals → hours 1, 5, 9
5. Two Stars of David (E-W and N-S) induce the full clock face

## Run Locally
```bash
python3 -m http.server 8080

fi

git add .
git commit -m "Deploy geometric clock construction visualizer" 2>/dev/null || \
echo "  ✓ Nothing new to commit"

# ── 4. Serve ─────────────────────────────────
echo ""
echo "[4/4] Launching server..."
echo ""
echo "  ┌─────────────────────────────────────┐"
echo "  │  Open in browser:                   │"
echo "  │  http://localhost:$PORT/$FILE  │"
echo "  │                                     │"
echo "  │  Press Ctrl+C to stop               │"
echo "  └─────────────────────────────────────┘"
echo ""

python3 -m http.server $PORT

