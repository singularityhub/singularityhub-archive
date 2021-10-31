---
id: 6873
name: "koray6/machine-learning"
branch: "master"
tag: "cu90"
commit: "e405b6c241bfc8d7f361f5acce4bea5881575a4b"
version: "25024647ed04f58e0f4559413c661a61"
build_date: "2019-02-05T05:54:32.655Z"
size_mb: 9654
size: 3908108319
sif: "https://datasets.datalad.org/shub/koray6/machine-learning/cu90/2019-02-05-e405b6c2-25024647/25024647ed04f58e0f4559413c661a61.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/koray6/machine-learning/cu90/2019-02-05-e405b6c2-25024647/
recipe: https://datasets.datalad.org/shub/koray6/machine-learning/cu90/2019-02-05-e405b6c2-25024647/Singularity
collection: koray6/machine-learning
---

# koray6/machine-learning:cu90

```bash
$ singularity pull shub://koray6/machine-learning:cu90
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

 - Name: [koray6/machine-learning](https://github.com/koray6/machine-learning)
 - License: None

