#!/bin/bash

echo "[*] Installing Spiderecon..."

# Get the absolute path of the directory where the user cloned the repo
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# 1. Create the virtual environment
echo "[*] Creating Python virtual environment..."
python3 -m venv "$DIR/venv"

# 2. Install the required Python packages
echo "[*] Installing dependencies..."
"$DIR/venv/bin/pip" install -r "$DIR/requirements.txt"

# 3. Create the global terminal command
echo "[*] Creating global command 'spiderecon'..."
WRAPPER="/usr/local/bin/spiderecon"

# Write the wrapper script to the system binaries folder
echo "#!/bin/bash" | sudo tee $WRAPPER > /dev/null
echo "source $DIR/venv/bin/activate" | sudo tee -a $WRAPPER > /dev/null
echo "python3 $DIR/main.py" | sudo tee -a $WRAPPER > /dev/null

# 4. Make the new command executable
sudo chmod +x $WRAPPER

echo ""
echo "[+] Installation complete!"
echo "[+] You can now run the tool from anywhere by typing: spiderecon"
