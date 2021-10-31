---
id: 8588
name: "Sylvia-Liang/torch8"
branch: "master"
tag: "latest"
commit: "c88d6deec50261d82707802c57076afb14623b30"
version: "1404f5844ec63b2c6612f151af28a6d0"
build_date: "2019-04-22T21:53:08.945Z"
size_mb: 11767
size: 6352420895
sif: "https://datasets.datalad.org/shub/Sylvia-Liang/torch8/latest/2019-04-22-c88d6dee-1404f584/1404f5844ec63b2c6612f151af28a6d0.simg"
url: https://datasets.datalad.org/shub/Sylvia-Liang/torch8/latest/2019-04-22-c88d6dee-1404f584/
recipe: https://datasets.datalad.org/shub/Sylvia-Liang/torch8/latest/2019-04-22-c88d6dee-1404f584/Singularity
collection: Sylvia-Liang/torch8
---

# Sylvia-Liang/torch8:latest

```bash
$ singularity pull shub://Sylvia-Liang/torch8:latest
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
  /opt/conda/bin/pip install --no-cache-dir -I stanfordnlp==0.1.2
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

 - Name: [Sylvia-Liang/torch8](https://github.com/Sylvia-Liang/torch8)
 - License: None

