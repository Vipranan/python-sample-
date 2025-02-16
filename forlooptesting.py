import torch

# Check if CUDA is available
if torch.cuda.is_available():
    print(f"CUDA is available. Using GPU: {torch.cuda.get_device_name(0)}")
else:
    print("CUDA is not available. Using CPU.")

# Create a tensor on the GPU (if available)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
tensor = torch.randn(3, 3).to(device)

# Perform a simple tensor operation
result = tensor * 2

# Print the result and the device it's located on
print(f"Tensor result:\n{result}")
print(f"Tensor is on device: {result.device}")