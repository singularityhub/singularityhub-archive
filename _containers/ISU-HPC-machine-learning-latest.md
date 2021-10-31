---
id: 2445
name: "ISU-HPC/machine-learning"
branch: "master"
tag: "latest"
commit: "3769a5abaaa5c834c874fa2564069e80badf0531"
version: "bd5df09db9218b4e12c20ddda7a863aa"
build_date: "2021-03-31T20:01:29.274Z"
size_mb: 9630
size: 3966701599
sif: "https://datasets.datalad.org/shub/ISU-HPC/machine-learning/latest/2021-03-31-3769a5ab-bd5df09d/bd5df09db9218b4e12c20ddda7a863aa.simg"
url: https://datasets.datalad.org/shub/ISU-HPC/machine-learning/latest/2021-03-31-3769a5ab-bd5df09d/
recipe: https://datasets.datalad.org/shub/ISU-HPC/machine-learning/latest/2021-03-31-3769a5ab-bd5df09d/Singularity
collection: ISU-HPC/machine-learning
---

# ISU-HPC/machine-learning:latest

```bash
$ singularity pull shub://ISU-HPC/machine-learning:latest
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
    pip3 --no-cache-dir install --upgrade tensorflow-gpu

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
    pip2 --no-cache-dir install --upgrade tensorflow-gpu

    # keras
    pip2 --no-cache-dir install --upgrade keras

   
  # Lasagne
  pip2 --no-cache-dir install git+git://github.com/Lasagne/Lasagne

  # dlib
  pip2 --no-cache-dir install dlib
  
  #pytorch
  pip2 --no-cache-dir install torch torchvision
  
  # Upgrade pytorch for python2 and python3
  
  pip2 --no-cache-dir install --upgrade torch torchvision
  
  pip3 --no-cache-dir install --upgrade torch torchvision
```

## Collection

 - Name: [ISU-HPC/machine-learning](https://github.com/ISU-HPC/machine-learning)
 - License: None

