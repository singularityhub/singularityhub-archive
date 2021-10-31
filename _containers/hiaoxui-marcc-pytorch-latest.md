---
id: 4102
name: "hiaoxui/marcc-pytorch"
branch: "master"
tag: "latest"
commit: "0aad269a9041844ff1df079d6e9dfec065fdec20"
version: "a47b20695e53f85931f48fbf326abd84"
build_date: "2019-11-20T14:33:53.589Z"
size_mb: 8619
size: 4057042975
sif: "https://datasets.datalad.org/shub/hiaoxui/marcc-pytorch/latest/2019-11-20-0aad269a-a47b2069/a47b20695e53f85931f48fbf326abd84.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/hiaoxui/marcc-pytorch/latest/2019-11-20-0aad269a-a47b2069/
recipe: https://datasets.datalad.org/shub/hiaoxui/marcc-pytorch/latest/2019-11-20-0aad269a-a47b2069/Singularity
collection: hiaoxui/marcc-pytorch
---

# hiaoxui/marcc-pytorch:latest

```bash
$ singularity pull shub://hiaoxui/marcc-pytorch:latest
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
  PATH=/opt/conda/envs/pytorch-py3.6/bin:$PATH
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

%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command

%test
  # test that script is a success
```

## Collection

 - Name: [hiaoxui/marcc-pytorch](https://github.com/hiaoxui/marcc-pytorch)
 - License: None

