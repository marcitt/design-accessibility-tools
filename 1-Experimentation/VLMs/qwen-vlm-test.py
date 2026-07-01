import torch
from PIL import Image
from transformers import AutoProcessor, AutoModelForVision2Seq

device = "mps" if torch.backends.mps.is_available() else "cpu"
print(f"Using device: {device}") 

"""
huggingface.co/Qwen/Qwen2-VL-2B-Instruct
"""

qwen_id = "Qwen/Qwen2-VL-2B-Instruct"
# qwen_id = "Qwen/Qwen2-VL-1.5B-Instruct"  # smaller fallback
 
qwen_processor = AutoProcessor.from_pretrained(qwen_id)
qwen_model = AutoModelForVision2Seq.from_pretrained(
    qwen_id,
    torch_dtype=torch.float32,
    trust_remote_code=True,       # required for Qwen
    attn_implementation="eager",  # required for MPS
).to(device)

image = Image.open("example.jpg").convert("RGB")
messages = [
    {
        "role": "user",
        "content": [
            {"type": "image"},
            {"type": "text", "text": "Describe the image."}
        ]
    }
]
inputs = qwen_processor(
    messages=messages,
    images=[image],
    return_tensors="pt"
).to(device)
with torch.no_grad():
    output = qwen_model.generate(**inputs, max_new_tokens=100)
print(qwen_processor.batch_decode(output, skip_special_tokens=True)[0])