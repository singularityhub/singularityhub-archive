---
id: 8555
name: "Sylvia-Liang/torch36"
branch: "master"
tag: "latest"
commit: "4e6ff200da5b092167b8e09bc637d02caf05ae85"
version: "a5085a7ff01e42900927acf0019ab767"
build_date: "2019-04-22T21:53:08.846Z"
size_mb: 9012
size: 4232753183
sif: "https://datasets.datalad.org/shub/Sylvia-Liang/torch36/latest/2019-04-22-4e6ff200-a5085a7f/a5085a7ff01e42900927acf0019ab767.simg"
url: https://datasets.datalad.org/shub/Sylvia-Liang/torch36/latest/2019-04-22-4e6ff200-a5085a7f/
recipe: https://datasets.datalad.org/shub/Sylvia-Liang/torch36/latest/2019-04-22-4e6ff200-a5085a7f/Singularity
collection: Sylvia-Liang/torch36
---

# Sylvia-Liang/torch36:latest

```bash
$ singularity pull shub://Sylvia-Liang/torch36:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: marcchpc/pytorch_cuda9

%environment
  # use bash as default shell
  SHELL=/bin/bash
  export SHELL
  
  # add CUDA paths
  CPATH="/usr/local/cuda/include:$CPATH"
  PATH="/usr/local/cuda/bin:$PATH"
  LD_LIBRARY_PATH="/usr/local/cuda/lib64:$LD_LIBRARY_PATH"
  CUDA_HOME="/usr/local/cuda"
  export CPATH PATH LD_LIBRARY_PATH CUDA_HOME
  
  # make conda accessible
  PATH=/opt/conda/envs/pytorch-py3.6.8/bin:$PATH
  export PATH

%setup
  # runs on host - the path to the image is $SINGULARITY_ROOTFS

%post
  # post-setup script

  # load environment variables
  . /environment

  # make environment file executable
  chmod +x /environment

  # default mount paths, files
  mkdir /scratch /data /work-zfs 
  touch /usr/bin/nvidia-smi
  
  # user requests (contact marcc-help@marcc.jhu.edu)
  /opt/conda/bin/conda install opencv scikit-learn scikit-image scipy pandas 
  /opt/conda/bin/conda install -c anaconda numpy pytest flake8 tensorflow-tensorboard
  /opt/conda/bin/conda install -c conda-forge tensorboardx tqdm protobuf onnx spectrum nibabel
  
  # try a pip install
  /opt/conda/bin/pip install torchtext

%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command

%test
  # test that script is a success
```

## Collection

 - Name: [Sylvia-Liang/torch36](https://github.com/Sylvia-Liang/torch36)
 - License: None

