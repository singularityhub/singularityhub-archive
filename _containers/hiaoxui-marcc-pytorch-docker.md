---
id: 4105
name: "hiaoxui/marcc-pytorch"
branch: "master"
tag: "docker"
commit: "099ddb47252b9bad73f71ac6315286407d5d3fa8"
version: "970d28b0f4957fa50f8b1c0d2bbcbd5a"
build_date: "2018-08-21T21:25:53.538Z"
size_mb: 8619
size: 4057042975
sif: "https://datasets.datalad.org/shub/hiaoxui/marcc-pytorch/docker/2018-08-21-099ddb47-970d28b0/970d28b0f4957fa50f8b1c0d2bbcbd5a.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/hiaoxui/marcc-pytorch/docker/2018-08-21-099ddb47-970d28b0/
recipe: https://datasets.datalad.org/shub/hiaoxui/marcc-pytorch/docker/2018-08-21-099ddb47-970d28b0/Singularity
collection: hiaoxui/marcc-pytorch
---

# hiaoxui/marcc-pytorch:docker

```bash
$ singularity pull shub://hiaoxui/marcc-pytorch:docker
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

  chmod -R +w /opt/conda

%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command

%test
  # test that script is a success
```

## Collection

 - Name: [hiaoxui/marcc-pytorch](https://github.com/hiaoxui/marcc-pytorch)
 - License: None

