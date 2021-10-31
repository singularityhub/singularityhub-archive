---
id: 9833
name: "Sylvia-Liang/torch34"
branch: "master"
tag: "latest"
commit: "989d40e628d98d9eefb892537aef2f2afbfcc770"
version: "8c55e694be8bdeb4ef63d96118c25d73"
build_date: "2019-06-17T19:35:32.454Z"
size_mb: 14637
size: 8774406175
sif: "https://datasets.datalad.org/shub/Sylvia-Liang/torch34/latest/2019-06-17-989d40e6-8c55e694/8c55e694be8bdeb4ef63d96118c25d73.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Sylvia-Liang/torch34/latest/2019-06-17-989d40e6-8c55e694/
recipe: https://datasets.datalad.org/shub/Sylvia-Liang/torch34/latest/2019-06-17-989d40e6-8c55e694/Singularity
collection: Sylvia-Liang/torch34
---

# Sylvia-Liang/torch34:latest

```bash
$ singularity pull shub://Sylvia-Liang/torch34:latest
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
  /opt/conda/bin/pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.1.0/en_core_web_sm-2.1.0.tar.gz
  /opt/conda/bin/pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_md-2.1.0/en_core_web_md-2.1.0.tar.gz
  /opt/conda/bin/pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_lg-2.1.0/en_core_web_lg-2.1.0.tar.gz
  /opt/conda/bin/pip install nltk
  /opt/conda/bin/pip install sparqlwrapper
  /opt/conda/bin/pip install tqdm
  /opt/conda/bin/conda install -c maciejkula -c pytorch spotlight=0.1.5
  /opt/conda/bin/pip install inflect
  /opt/conda/bin/pip install tagme
  /opt/conda/bin/pip install gensim
  /opt/conda/bin/pip install seaborn
  /opt/conda/bin/pip install git+https://github.com/facebookresearch/fastText.git
  /opt/conda/bin/pip install Cython
  /opt/conda/bin/pip install click
  /opt/conda/bin/pip install dominate
  /opt/conda/bin/pip install Flask
  /opt/conda/bin/pip install Flask-Bootstrap
  /opt/conda/bin/pip install Flask-Classful
  /opt/conda/bin/pip install Flask-Login
  /opt/conda/bin/pip install Flask-SQLAlchemy
  /opt/conda/bin/pip install Flask-WTF
  /opt/conda/bin/pip install itsdangerous
  /opt/conda/bin/pip install Jinja2
  /opt/conda/bin/pip install MarkupSafe
  /opt/conda/bin/pip install singledispatch
  /opt/conda/bin/pip install SQLAlchemy
  /opt/conda/bin/pip install visitor
  /opt/conda/bin/pip install Werkzeug
  /opt/conda/bin/pip install WTForms
  /opt/conda/bin/pip install gevent
  /opt/conda/bin/pip install pybloomfiltermmap3
  /opt/conda/bin/pip install pybloom_live
  /opt/conda/bin/pip install anytree
  /opt/conda/bin/pip install ujson
  /opt/conda/bin/pip install timeout
  /opt/conda/bin/pip install interruptingcow
  /opt/conda/bin/pip install joblib
  /opt/conda/bin/pip install backports.functools-lru-cache
  /opt/conda/bin/pip install subprocess32
  /opt/conda/bin/pip install wheel

%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command

%test
  # test that script is a success
```

## Collection

 - Name: [Sylvia-Liang/torch34](https://github.com/Sylvia-Liang/torch34)
 - License: None

