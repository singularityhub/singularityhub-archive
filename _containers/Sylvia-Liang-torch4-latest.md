---
id: 8582
name: "Sylvia-Liang/torch4"
branch: "master"
tag: "latest"
commit: "0a442dac50ea1a115e63a6b0a70f56a33a4e63f3"
version: "ee525e389526cc0a9fa44ebeaf785c95"
build_date: "2019-04-22T21:53:08.905Z"
size_mb: 11404
size: 5848203295
sif: "https://datasets.datalad.org/shub/Sylvia-Liang/torch4/latest/2019-04-22-0a442dac-ee525e38/ee525e389526cc0a9fa44ebeaf785c95.simg"
url: https://datasets.datalad.org/shub/Sylvia-Liang/torch4/latest/2019-04-22-0a442dac-ee525e38/
recipe: https://datasets.datalad.org/shub/Sylvia-Liang/torch4/latest/2019-04-22-0a442dac-ee525e38/Singularity
collection: Sylvia-Liang/torch4
---

# Sylvia-Liang/torch4:latest

```bash
$ singularity pull shub://Sylvia-Liang/torch4:latest
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
  /opt/conda/bin/pip install spacy
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

 - Name: [Sylvia-Liang/torch4](https://github.com/Sylvia-Liang/torch4)
 - License: None

