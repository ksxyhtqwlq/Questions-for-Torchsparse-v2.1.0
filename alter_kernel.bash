filename="torchsparse/torchsparse/nn/modules/conv.py"  
pattern="self.kernel.data.uniform_(-std, std)"  
sed -i "/$pattern/s/^/# /; /$pattern/a \\        self.kernel.data.fill_(1.0)" "$filename" 