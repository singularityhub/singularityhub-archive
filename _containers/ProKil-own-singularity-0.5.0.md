---
id: 5590
name: "ProKil/own-singularity"
branch: "master"
tag: "0.5.0"
commit: "96b99cd8f10dba13f914a04d8f79a7350430fff2"
version: "d9d637116e3fd12e6b6747884dbbc8be"
build_date: "2019-10-20T04:18:46.125Z"
size_mb: 9635
size: 4391342111
sif: "https://datasets.datalad.org/shub/ProKil/own-singularity/0.5.0/2019-10-20-96b99cd8-d9d63711/d9d637116e3fd12e6b6747884dbbc8be.simg"
url: https://datasets.datalad.org/shub/ProKil/own-singularity/0.5.0/2019-10-20-96b99cd8-d9d63711/
recipe: https://datasets.datalad.org/shub/ProKil/own-singularity/0.5.0/2019-10-20-96b99cd8-d9d63711/Singularity
collection: ProKil/own-singularity
---

# ProKil/own-singularity:0.5.0

```bash
$ singularity pull shub://ProKil/own-singularity:0.5.0
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
  /opt/conda/bin/conda install -c conda-forge protobuf onnx
  
  # try a pip install
  /opt/conda/bin/pip install --upgrade pip
  /opt/conda/bin/pip install tensorflow
  /opt/conda/bin/pip install torchtext
  /opt/conda/bin/pip install bidict
  /opt/conda/bin/pip install networkx
  /opt/conda/bin/pip install pybind11
  /opt/conda/bin/pip install visdom
  git clone https://github.com/kitsing/openfst-wrapper.git
  cd openfst-wrapper
  /opt/conda/bin/python setup.py install
  cd ..
  git clone https://github.com/dmort27/panphon.git
  cd panphon
  /opt/conda/bin/python setup.py install
  cd ..

%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command

%test
  # test that script is a success
```

## Collection

 - Name: [ProKil/own-singularity](https://github.com/ProKil/own-singularity)
 - License: None

