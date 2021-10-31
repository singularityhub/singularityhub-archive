---
id: 12470
name: "daverblair/singularity_vlpi"
branch: "master"
tag: "latest"
commit: "80861c6261378e595db9f5a1df6bf250f207906d"
version: "cd8dc7f6c459a092a02575de504788d6"
build_date: "2021-03-05T21:51:53.806Z"
size_mb: 8435.0
size: 4636631071
sif: "https://datasets.datalad.org/shub/daverblair/singularity_vlpi/latest/2021-03-05-80861c62-cd8dc7f6/cd8dc7f6c459a092a02575de504788d6.sif"
url: https://datasets.datalad.org/shub/daverblair/singularity_vlpi/latest/2021-03-05-80861c62-cd8dc7f6/
recipe: https://datasets.datalad.org/shub/daverblair/singularity_vlpi/latest/2021-03-05-80861c62-cd8dc7f6/Singularity
collection: daverblair/singularity_vlpi
---

# daverblair/singularity_vlpi:latest

```bash
$ singularity pull shub://daverblair/singularity_vlpi:latest
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

  #conda installs
  /opt/conda/bin/conda install libgcc opencv 
  

  #pip installs 
  #pytorch fixed to 1.5.1
  /opt/conda/bin/pip install scikit-learn==0.22.1
  /opt/conda/bin/pip install vlpi==0.1.5
  /opt/conda/bin/pip install QRankGWAS
  /opt/conda/bin/pip install CrypticPhenoImpute
		
  
  

%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command

%test
  # test that script is a success
```

## Collection

 - Name: [daverblair/singularity_vlpi](https://github.com/daverblair/singularity_vlpi)
 - License: None

