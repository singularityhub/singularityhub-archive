---
id: 8557
name: "Sylvia-Liang/torch37"
branch: "master"
tag: "latest"
commit: "3492c23464151d76e48f83997cd947c127634c6a"
version: "d7d530723f8f90ee46e44332336f4142"
build_date: "2019-04-22T21:53:08.860Z"
size_mb: 9012
size: 4232753183
sif: "https://datasets.datalad.org/shub/Sylvia-Liang/torch37/latest/2019-04-22-3492c234-d7d53072/d7d530723f8f90ee46e44332336f4142.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Sylvia-Liang/torch37/latest/2019-04-22-3492c234-d7d53072/
recipe: https://datasets.datalad.org/shub/Sylvia-Liang/torch37/latest/2019-04-22-3492c234-d7d53072/Singularity
collection: Sylvia-Liang/torch37
---

# Sylvia-Liang/torch37:latest

```bash
$ singularity pull shub://Sylvia-Liang/torch37:latest
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
  PATH=/opt/conda/envs/pytorch-py3.7/bin:$PATH
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

 - Name: [Sylvia-Liang/torch37](https://github.com/Sylvia-Liang/torch37)
 - License: None

