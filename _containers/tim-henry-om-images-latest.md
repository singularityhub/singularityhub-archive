---
id: 7212
name: "tim-henry/om-images"
branch: "master"
tag: "latest"
commit: "9399302365e1f117b795ab481a57104b187ed412"
version: "83b1e335d7b62d3c3394954a1750d14b"
build_date: "2019-02-14T08:45:05.082Z"
size_mb: 9006
size: 4230393887
sif: "https://datasets.datalad.org/shub/tim-henry/om-images/latest/2019-02-14-93993023-83b1e335/83b1e335d7b62d3c3394954a1750d14b.simg"
url: https://datasets.datalad.org/shub/tim-henry/om-images/latest/2019-02-14-93993023-83b1e335/
recipe: https://datasets.datalad.org/shub/tim-henry/om-images/latest/2019-02-14-93993023-83b1e335/Singularity
collection: tim-henry/om-images
---

# tim-henry/om-images:latest

```bash
$ singularity pull shub://tim-henry/om-images:latest
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

 - Name: [tim-henry/om-images](https://github.com/tim-henry/om-images)
 - License: None

