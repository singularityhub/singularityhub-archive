---
id: 3943
name: "marcc-hpc/pytorch"
branch: "0.5.0"
tag: "0.5.0"
commit: "9a13601bad8d15004119e68aea1c412cfc8af347"
version: "9a13bde09e3f45a11750b1da7ccbaa88"
build_date: "2018-08-13T01:36:21.039Z"
size_mb: 8208
size: 3855593503
sif: "https://datasets.datalad.org/shub/marcc-hpc/pytorch/0.5.0/2018-08-13-9a13601b-9a13bde0/9a13bde09e3f45a11750b1da7ccbaa88.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/marcc-hpc/pytorch/0.5.0/2018-08-13-9a13601b-9a13bde0/
recipe: https://datasets.datalad.org/shub/marcc-hpc/pytorch/0.5.0/2018-08-13-9a13601b-9a13bde0/Singularity
collection: marcc-hpc/pytorch
---

# marcc-hpc/pytorch:0.5.0

```bash
$ singularity pull shub://marcc-hpc/pytorch:0.5.0
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

%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command

%test
  # test that script is a success
```

## Collection

 - Name: [marcc-hpc/pytorch](https://github.com/marcc-hpc/pytorch)
 - License: [MIT License](https://api.github.com/licenses/mit)

