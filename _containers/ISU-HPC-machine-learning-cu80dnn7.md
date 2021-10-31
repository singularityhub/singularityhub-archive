---
id: 2653
name: "ISU-HPC/machine-learning"
branch: "master"
tag: "cu80dnn7"
commit: "399ce915ab6cd09cc1451fc38508f9ab6e2994f2"
version: "9a7039b28d9a52a2dcf6e85c350c12be"
build_date: "2020-03-14T03:19:39.957Z"
size_mb: 8083
size: 3263725599
sif: "https://datasets.datalad.org/shub/ISU-HPC/machine-learning/cu80dnn7/2020-03-14-399ce915-9a7039b2/9a7039b28d9a52a2dcf6e85c350c12be.simg"
url: https://datasets.datalad.org/shub/ISU-HPC/machine-learning/cu80dnn7/2020-03-14-399ce915-9a7039b2/
recipe: https://datasets.datalad.org/shub/ISU-HPC/machine-learning/cu80dnn7/2020-03-14-399ce915-9a7039b2/Singularity
collection: ISU-HPC/machine-learning
---

# ISU-HPC/machine-learning:cu80dnn7

```bash
$ singularity pull shub://ISU-HPC/machine-learning:cu80dnn7
```

## Singularity Recipe

```singularity
bootstrap:shub
From:ISU-HPC/ml-base:cu80dnn7

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
            mxnet-cu80 \
            common \
            python-utils \
            requests \
            future \
            hypothesis \
            scikit-learn

    python36 -m ipykernel.kernelspec

    echo "/usr/local/cuda-8.0/lib64/" >/etc/ld.so.conf.d/cuda.conf
    echo "/usr/local/cuda/extras/CUPTI/lib64/" >>/etc/ld.so.conf.d/cuda.conf

    # Install TensorFlow GPU version
    pip3 --no-cache-dir install --upgrade tensorflow-gpu==1.4

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
            mxnet-cu80 \
            common \
            requests \
            future \
            hypothesis \
            scikit-learn


    # Install TensorFlow GPU version
    pip2 --no-cache-dir install --upgrade tensorflow-gpu==1.4

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

