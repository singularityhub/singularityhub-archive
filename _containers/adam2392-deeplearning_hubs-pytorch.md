---
id: 3173
name: "adam2392/deeplearning_hubs"
branch: "master"
tag: "pytorch"
commit: "55919c93c7722dabbcf7b22c4daabda2c3f51afa"
version: "c2402cb62a2bff6fdc53763e6b9100fe"
build_date: "2018-06-13T15:01:49.016Z"
size_mb: 8601
size: 4049891359
sif: "https://datasets.datalad.org/shub/adam2392/deeplearning_hubs/pytorch/2018-06-13-55919c93-c2402cb6/c2402cb62a2bff6fdc53763e6b9100fe.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/adam2392/deeplearning_hubs/pytorch/2018-06-13-55919c93-c2402cb6/
recipe: https://datasets.datalad.org/shub/adam2392/deeplearning_hubs/pytorch/2018-06-13-55919c93-c2402cb6/Singularity
collection: adam2392/deeplearning_hubs
---

# adam2392/deeplearning_hubs:pytorch

```bash
$ singularity pull shub://adam2392/deeplearning_hubs:pytorch
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
  /opt/conda/bin/conda install -c anaconda numpy pytest flake8 tensorboard
  /opt/conda/bin/conda install -c conda-forge tensorboardx tqdm protobuf onnx spectrum nibabel

%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command

%test
  # test that script is a success
```

## Collection

 - Name: [adam2392/deeplearning_hubs](https://github.com/adam2392/deeplearning_hubs)
 - License: [Other](None)

