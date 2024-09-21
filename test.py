import torchsparse.nn as spnn
import torch

in_channels = 1
out_channels = 1

model = spnn.Conv3d(in_channels, out_channels, kernel_size=3, stride=1)

model.cuda()
model.eval()

feats = torch.ones(27, in_channels, out_channels, dtype=torch.float32)

import itertools  
combinations = list(itertools.product(range(3), repeat=3))  
coords = torch.tensor(combinations, dtype=torch.int)  

from torchsparse import SparseTensor
inputs = SparseTensor(feats, coords)
inputs.to('cuda')

print("in_feats:")
print(feats)

print("coords:")
print(coords)

print('out_feats:')
print(model(inputs).feats)