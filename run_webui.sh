#!/bin/bash
# Get the directory where this script lives
SCRIPT_DIR=$(dirname "$(readlink -f "$0")")
cd "$SCRIPT_DIR"

source venv/bin/activate

echo "🚀 Starting CosyVoice WebUI..."
echo "👉 Open your browser to: http://127.0.0.1:50000"

# You can change the model_dir below to switch default models
python3 webui.py --port 50000 --model_dir pretrained_models/iic/CosyVoice-300M-Instruct
