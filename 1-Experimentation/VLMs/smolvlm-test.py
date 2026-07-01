import torch
from PIL import Image
from transformers import AutoProcessor, AutoModelForVision2Seq

device = "mps" if torch.backends.mps.is_available() else "cpu"
print(f"Using device: {device}") 

"""
huggingface.co/HuggingFaceTB/SmolVLM-256M-Instruct
"""

smolvlm_id = "HuggingFaceTB/SmolVLM-256M-Instruct"
 
smolvlm_processor = AutoProcessor.from_pretrained(smolvlm_id)
smolvlm_model = AutoModelForVision2Seq.from_pretrained(
    smolvlm_id,
    torch_dtype=torch.float32,  
).to(device)

image = Image.open("example.jpg").convert("RGB")
prompt = "Describe this image."
inputs = smolvlm_processor(images=image, text=prompt, return_tensors="pt")
inputs = {k: v.to(device) for k, v in inputs.items()}
with torch.no_grad():
    output = smolvlm_model.generate(**inputs, max_new_tokens=64)
print(smolvlm_processor.decode(output[0], skip_special_tokens=True))


