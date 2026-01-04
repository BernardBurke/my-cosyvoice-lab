# Dev Log: CosyVoice Setup (Jan 2026)

## Context
Started with a fresh Linux Mint 22.2 install (Python 3.12, CUDA 12.5). 
Goal: Get CosyVoice 3 "Instruct Mode" running locally.

## The "Happy Path" (How to reinstall later)
1. System Deps: `sudo apt install git-lfs swig`
2. Python: `pip install grpcio --only-binary=:all:` (Critical fix for 3.12)
3. Torch: Use 2.3.1 to match Torchaudio 2.3.1 (downgraded from 2.6).
4. Models: `snapshot_download` from ModelScope (Instruct-300M).

## The "Gotchas" (Don't repeat these mistakes)
* **grpcio build fail:** Python 3.12 tries to compile grpcio from source and dies. 
  * *Fix:* Install the binary wheel manually before running requirements.
* **Dependency Conflict:** `requirements.txt` forced Torch 2.3.1, but I had Torchaudio 2.6.0 installed.
  * *Fix:* `pip install torchaudio==2.3.1 --index-url https://download.pytorch.org/whl/cu121`
* **Streaming Generator:** The inference API returns a generator, not a file.
  * *Fix:* Must iterate through chunks and `torch.cat` them before saving.

## Useful Commands
* **Launch WebUI:** `./run_webui.sh`
* **Test CLI:** `python test_instruct.py`
