import torch

# Check if GPU is available and use it
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Using device:", device)

# Create tensors and perform matrix multiplication
a = torch.tensor([[1.0, 2.0], [3.0, 4.0]], device=device)
b = torch.tensor([[5.0, 6.0], [7.0, 8.0]], device=device)
c = torch.matmul(a, b)

print(c)

