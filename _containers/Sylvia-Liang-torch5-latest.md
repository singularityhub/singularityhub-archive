---
id: 8585
name: "Sylvia-Liang/torch5"
branch: "master"
tag: "latest"
commit: "04185be1bca825b3d90484f08aaf2830bfec9a14"
version: "d5bf85409e7abb11f50562d9bdc25544"
build_date: "2019-04-22T21:53:08.923Z"
size_mb: 10957
size: 5749542943
sif: "https://datasets.datalad.org/shub/Sylvia-Liang/torch5/latest/2019-04-22-04185be1-d5bf8540/d5bf85409e7abb11f50562d9bdc25544.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Sylvia-Liang/torch5/latest/2019-04-22-04185be1-d5bf8540/
recipe: https://datasets.datalad.org/shub/Sylvia-Liang/torch5/latest/2019-04-22-04185be1-d5bf8540/Singularity
collection: Sylvia-Liang/torch5
---

# Sylvia-Liang/torch5:latest

```bash
$ singularity pull shub://Sylvia-Liang/torch5:latest
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
  /opt/conda/bin/pip install stanfordnlp==0.1.2
  /opt/conda/bin/pip install nltk
  /opt/conda/bin/pip install sparqlwrapper
  /opt/conda/bin/pip install tqdm
  /opt/conda/bin/conda install -c maciejkula -c pytorch spotlight=0.1.5
  /opt/conda/bin/pip install inflect
  /opt/conda/bin/pip install tagme
  /opt/conda/bin/pip install git+https://github.com/facebookresearch/fastText.git

%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command

%test
  # test that script is a success
```

## Collection

 - Name: [Sylvia-Liang/torch5](https://github.com/Sylvia-Liang/torch5)
 - License: None

