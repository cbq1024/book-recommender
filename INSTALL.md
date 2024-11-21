# INSTALL

```shell
python.exe -m pip install --upgrade pip setuptools
pip install recommenders
pip install recommenders[spark]
# install if need cuda for torch
conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1
# cuda11.8
pip install recommenders[gpu] -f https://download.pytorch.org/whl/cu118/torch_stable.html
# or used | ref: https://pytorch.org/get-started/locally/#windows-pip
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install DrissionPage
pip install streamlit
pip install pathlib2
```

the nvidia info

```text
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 522.06       Driver Version: 522.06       CUDA Version: 11.8     |
|-------------------------------+----------------------+----------------------+
| GPU  Name            TCC/WDDM | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  NVIDIA GeForce ... WDDM  | 00000000:01:00.0 Off |                  N/A |
| N/A   51C    P8     6W /  N/A |      0MiB /  4096MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+
```

# export and import anaconda env

- https://docs.anaconda.com/working-with-conda/environments/#sharing-an-environment

## export

```shell
# Replace <ENV_NAME> with the name of the environment you want exported
conda activate <ENV_NAME>
conda env export > environment.yml
```

## import

```shell
conda env create -f environment.yml
```
