---
id: 9753
name: "Sylvia-Liang/torch31"
branch: "master"
tag: "latest"
commit: "6ea3057af51d8fc945eae04bfc067d1f233646a2"
version: "860e1da5de377548d48b447c1c777c0a"
build_date: "2019-06-12T11:53:04.562Z"
size_mb: 14562
size: 8743022623
sif: "https://datasets.datalad.org/shub/Sylvia-Liang/torch31/latest/2019-06-12-6ea3057a-860e1da5/860e1da5de377548d48b447c1c777c0a.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Sylvia-Liang/torch31/latest/2019-06-12-6ea3057a-860e1da5/
recipe: https://datasets.datalad.org/shub/Sylvia-Liang/torch31/latest/2019-06-12-6ea3057a-860e1da5/Singularity
collection: Sylvia-Liang/torch31
---

# Sylvia-Liang/torch31:latest

```bash
$ singularity pull shub://Sylvia-Liang/torch31:latest
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

%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command

%test
  # test that script is a success
```

## Collection

 - Name: [Sylvia-Liang/torch31](https://github.com/Sylvia-Liang/torch31)
 - License: None

