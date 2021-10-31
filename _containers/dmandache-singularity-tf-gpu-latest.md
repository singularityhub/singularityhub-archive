---
id: 3184
name: "dmandache/singularity-tf-gpu"
branch: "master"
tag: "latest"
commit: "63fc669383fdfb0d6745abb5bc6805150a29e88d"
version: "71b0f8a283456b84ef57fa009896e9aa"
build_date: "2018-06-14T20:27:26.351Z"
size_mb: 3006
size: 1296752671
sif: "https://datasets.datalad.org/shub/dmandache/singularity-tf-gpu/latest/2018-06-14-63fc6693-71b0f8a2/71b0f8a283456b84ef57fa009896e9aa.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/dmandache/singularity-tf-gpu/latest/2018-06-14-63fc6693-71b0f8a2/
recipe: https://datasets.datalad.org/shub/dmandache/singularity-tf-gpu/latest/2018-06-14-63fc6693-71b0f8a2/Singularity
collection: dmandache/singularity-tf-gpu
---

# dmandache/singularity-tf-gpu:latest

```bash
$ singularity pull shub://dmandache/singularity-tf-gpu:latest
```

## Singularity Recipe

```singularity
# Defines a Singularity container with TensorFlow pre-installed
#

#
# Before bootstrapping this container, you must ensure that the following files
# are present in the current directory (alongside this definition file):
#
#   * cuda-linux64-rel-8.0.44-21122537.run  (* see below)
#   * NVIDIA-Linux-x86_64-375.20.run        (* see below)
#   * cudnn-8.0-linux-x64-v5.1.tgz          (https://developer.nvidia.com/cudnn)
#
# * The cuda-linux64 and NVIDIA-Linux files can be obtained by downloading the
# NVIDIA CUDA local runfile `cuda_8.0.44_linux.run` from:
#
#   https://developer.nvidia.com/cuda-downloads
#
# Then extract the necessary files by running:
#
#   sh cuda_8.0.44_linux.run --extract=<absolute/path/to/bootstrap/directory>
#
# IF YOUR HPC SYSTEM IS USING A DIFFERENT VERSION OF CUDA AND/OR NVIDIA DRIVERS
# YOU WILL NEED TO ADJUST THE ABOVE VERSION NUMBERS TO MATCH YOUR SYSTEM
#
# YOU WILL ALSO NEED TO DOWNLOAD THE APPROPRIATE DRIVER. For example,
# cuda_8.0.44_linux.run returns driver version 367.48.
#
# If you use this to create a container inside a virtual machine with no access to
# a GPU, comment out the final test.

BootStrap:docker
From:tensorflow/tensorflow:1.5.0-gpu-py3

%runscript
  exec python "$@" 

%post
  apt-get update -y
  apt-get install -y vim
  apt-get install -y git
  pip install -U numpy
  pip install dill h5py hyperopt keras pandas \
  	scikit-learn seaborn matplotlib 
  pip install jupyter
  pip install scikit-image
  
  # need to create mount point for home dir
  mkdir /scratch /share /local-scratch
  mkdir -p /pasteur/homes

%test
  # Sanity check that the container is operating

  # Test numpy 
  #/usr/bin/python -c "import numpy as np;np.__config__.show()"
  # Ensure that TensorFlow can be imported and session started (session start touches GPU)
  #/usr/bin/python -c "import tensorflow as tf;s = tf.Session()"

  # Runs in less than 30 minutes on low-end CPU; in less than 2 minutes on GPU
  # Comment the following line if building the container inside a VM with no access to a GPU
  # MC does not seem to be included with version 1.0.1
  #/usr/bin/python -m tensorflow.models.image.mnist.convolutional
  
  # Run with GPU
  #srun --gres=gpu:1 singularity run --nv ./containers/py3_tf15_gpu.img -c "import tensorflow as tf;s = tf.Session()"
```

## Collection

 - Name: [dmandache/singularity-tf-gpu](https://github.com/dmandache/singularity-tf-gpu)
 - License: None

