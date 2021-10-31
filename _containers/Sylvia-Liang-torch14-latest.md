---
id: 8627
name: "Sylvia-Liang/torch14"
branch: "master"
tag: "latest"
commit: "b6e47404a36899e687a5ca346034c8f9c1efecf4"
version: "34c5c6fdc91e3bed3f887d7a9e7dc463"
build_date: "2019-04-24T14:27:19.290Z"
size_mb: 11523
size: 5916233759
sif: "https://datasets.datalad.org/shub/Sylvia-Liang/torch14/latest/2019-04-24-b6e47404-34c5c6fd/34c5c6fdc91e3bed3f887d7a9e7dc463.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Sylvia-Liang/torch14/latest/2019-04-24-b6e47404-34c5c6fd/
recipe: https://datasets.datalad.org/shub/Sylvia-Liang/torch14/latest/2019-04-24-b6e47404-34c5c6fd/Singularity
collection: Sylvia-Liang/torch14
---

# Sylvia-Liang/torch14:latest

```bash
$ singularity pull shub://Sylvia-Liang/torch14:latest
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
  /opt/conda/bin/pip install -U spacy
  /opt/conda/bin/pip install nltk
  /opt/conda/bin/pip install sparqlwrapper
  /opt/conda/bin/pip install tqdm
  /opt/conda/bin/conda install -c maciejkula -c pytorch spotlight=0.1.5
  /opt/conda/bin/pip install inflect
  /opt/conda/bin/pip install tagme
  /opt/conda/bin/pip install gensim
  /opt/conda/bin/pip install git+https://github.com/facebookresearch/fastText.git

%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command

%test
  # test that script is a success
```

## Collection

 - Name: [Sylvia-Liang/torch14](https://github.com/Sylvia-Liang/torch14)
 - License: None

