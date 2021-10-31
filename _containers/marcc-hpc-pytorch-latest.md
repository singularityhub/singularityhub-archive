---
id: 3952
name: "marcc-hpc/pytorch"
branch: "0.5.0"
tag: "latest"
commit: "902a887b1ac715cbac1d11debf8cd82984d73a6a"
version: "4015e08c7c652c85c811f40024548087"
build_date: "2020-05-21T09:44:18.123Z"
size_mb: 9028
size: 4229750815
sif: "https://datasets.datalad.org/shub/marcc-hpc/pytorch/latest/2020-05-21-902a887b-4015e08c/4015e08c7c652c85c811f40024548087.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/marcc-hpc/pytorch/latest/2020-05-21-902a887b-4015e08c/
recipe: https://datasets.datalad.org/shub/marcc-hpc/pytorch/latest/2020-05-21-902a887b-4015e08c/Singularity
collection: marcc-hpc/pytorch
---

# marcc-hpc/pytorch:latest

```bash
$ singularity pull shub://marcc-hpc/pytorch:latest
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
  
  # try a pip install
  /opt/conda/bin/pip install torchtext
  /opt/conda/bin/pip install pretrainedmodels

%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command

%test
  # test that script is a success
```

## Collection

 - Name: [marcc-hpc/pytorch](https://github.com/marcc-hpc/pytorch)
 - License: [MIT License](https://api.github.com/licenses/mit)

