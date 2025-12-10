import os
model_dir = os.getenv("UNS_INFERENCE_MODEL_DIR", "models")
print(f"Model directory: {model_dir}")
print(f"Exists: {os.path.exists(model_dir)}")
print(f"YOLOX exists: {os.path.exists(os.path.join(model_dir, 'yolox'))}")