---
id: 2654
name: "ISU-HPC/machine-learning"
branch: "master"
tag: "cu90"
commit: "e405b6c241bfc8d7f361f5acce4bea5881575a4b"
version: "52cbdcc7a25fa28ef1adbf162e7e047c"
build_date: "2020-12-29T03:19:13.325Z"
size_mb: 9537
size: 3664539679
sif: "https://datasets.datalad.org/shub/ISU-HPC/machine-learning/cu90/2020-12-29-e405b6c2-52cbdcc7/52cbdcc7a25fa28ef1adbf162e7e047c.simg"
url: https://datasets.datalad.org/shub/ISU-HPC/machine-learning/cu90/2020-12-29-e405b6c2-52cbdcc7/
recipe: https://datasets.datalad.org/shub/ISU-HPC/machine-learning/cu90/2020-12-29-e405b6c2-52cbdcc7/Singularity
collection: ISU-HPC/machine-learning
---

# ISU-HPC/machine-learning:cu90

```bash
$ singularity pull shub://ISU-HPC/machine-learning:cu90
```

## Singularity Recipe

```singularity
bootstrap:shub
From:ISU-HPC/ml-base:cu90

%labels

AUTHOR Yasasvy Nanyam ynanyam@iastate.edu

%post

    pip3 --no-cache-dir install \
            h5py \
            ipykernel \
            jupyter \
            matplotlib \
            numpy \
            pandas \
            Pillow \
            scipy \
            sklearn \
            opencv-python \
            mxnet-cu90 \
            common \
            python-utils \
            requests \
            future \
            hypothesis \
            scikit-learn

    python36 -m ipykernel.kernelspec

    echo "/usr/local/cuda-9.0/lib64/" >/etc/ld.so.conf.d/cuda.conf
    echo "/usr/local/cuda/extras/CUPTI/lib64/" >>/etc/ld.so.conf.d/cuda.conf

    # Install TensorFlow GPU version
    pip3 --no-cache-dir install --upgrade tensorflow-gpu==1.7

    # keras
    pip3 --no-cache-dir install --upgrade keras

    # Lasagne
    pip3 --no-cache-dir install git+git://github.com/Lasagne/Lasagne

    # dlib
    pip3 --no-cache-dir install dlib
    
    # pytorch
    pip3 --no-cache-dir install torch torchvision

    ############################
    # for pip2

    pip2 --no-cache-dir install --upgrade pip

    pip2 --no-cache-dir install \
            h5py \
            ipykernel \
            jupyter \
            matplotlib \
            numpy \
            pandas \
            Pillow \
            scipy \
            sklearn \
            opencv-python \
            mxnet-cu90 \
            common \
            requests \
            future \
            hypothesis \
            scikit-learn


    # Install TensorFlow GPU version
    pip2 --no-cache-dir install --upgrade tensorflow-gpu==1.7

    # keras
    pip2 --no-cache-dir install --upgrade keras

   
  # Lasagne
  pip2 --no-cache-dir install git+git://github.com/Lasagne/Lasagne

  # dlib
  pip2 --no-cache-dir install dlib
  
  #pytorch
  pip2 --no-cache-dir install torch torchvision
```

## Collection

 - Name: [ISU-HPC/machine-learning](https://github.com/ISU-HPC/machine-learning)
 - License: None

