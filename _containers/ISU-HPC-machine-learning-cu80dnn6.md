---
id: 2652
name: "ISU-HPC/machine-learning"
branch: "master"
tag: "cu80dnn6"
commit: "89c2aaa73b7fe47fb6643e5eb70544e04ffe6080"
version: "2d73d7a857afdd14084e2b37552dcbd0"
build_date: "2021-03-31T19:52:26.117Z"
size_mb: 7981
size: 3206357023
sif: "https://datasets.datalad.org/shub/ISU-HPC/machine-learning/cu80dnn6/2021-03-31-89c2aaa7-2d73d7a8/2d73d7a857afdd14084e2b37552dcbd0.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ISU-HPC/machine-learning/cu80dnn6/2021-03-31-89c2aaa7-2d73d7a8/
recipe: https://datasets.datalad.org/shub/ISU-HPC/machine-learning/cu80dnn6/2021-03-31-89c2aaa7-2d73d7a8/Singularity
collection: ISU-HPC/machine-learning
---

# ISU-HPC/machine-learning:cu80dnn6

```bash
$ singularity pull shub://ISU-HPC/machine-learning:cu80dnn6
```

## Singularity Recipe

```singularity
bootstrap:shub
From:ISU-HPC/ml-base:cu80dnn6

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

