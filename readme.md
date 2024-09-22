1. create virtual environment
```shell
conda create -n torchsparse-env
conda activate torchsparse-env
```

2. install packages and compile
```shell
bash compile.bash
```

3. make all kernel values = 1.0
```shell 
bash alter_kernel.bash
```

4. test
```py
python test.py
```

some explains about the inputs:
1. in_channels = out_channels = 1
2. kernel shape = 3 * 3 * 3, with default padding = 1, stride = 1, all kernel values = 1.0
3. have 27 points in all, all features = 1.0 (printed)
4. coordinates of all 27 points in three dimensions are between 0 to 2.

Q. In my opinion, I think the outputs should be:
[8, 12, 8, 12, 18, 12, 8, 12, 8, 12, 18, 12, 18, 27, 18, 12, 18, 12, 8, 12, 8, 12, 18, 12, 8, 12, 8]