import sys
import os
import torch
import torchaudio

# 1. Setup Paths
sys.path.append('third_party/Matcha-TTS')
from cosyvoice.cli.cosyvoice import CosyVoice

# 2. Load the "Instruct" Model
print("🔹 Loading CosyVoice Instruct Model...")
model_dir = 'pretrained_models/iic/CosyVoice-300M-Instruct'
cosyvoice = CosyVoice(model_dir)

# 3. Configuration
text_input = "I can't believe we finally got this working. The Linux dependencies were a nightmare, but we won!"
style_instruction = "Happy, relieved, slightly fast speaking rate"
speaker_id = '中文男' # Maps to the default male voice

# 4. Generate
print(f"🔹 Generating Audio...")
print(f"   Text:  {text_input}")
print(f"   Style: {style_instruction}")

# The inference returns a GENERATOR (stream), not a single item.
generator = cosyvoice.inference_instruct(text_input, speaker_id, style_instruction)

# 5. Collect and Concatenate
audio_chunks = []

for i, result in enumerate(generator):
    # 'result' is a dictionary for this specific chunk
    if 'tts_speech' in result:
        print(f"   -> Received chunk {i}")
        audio_chunks.append(result['tts_speech'])

# 6. Save
if audio_chunks:
    # Concatenate all chunks into one audio tensor
    final_audio = torch.cat(audio_chunks, dim=1)
    
    output_filename = "result_happy.wav"
    torchaudio.save(output_filename, final_audio, 22050)
    print(f"✅ Success! Saved to: {output_filename}")
else:
    print("❌ Error: No audio data received from model.")
