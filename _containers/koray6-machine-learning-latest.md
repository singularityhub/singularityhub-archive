---
id: 6872
name: "koray6/machine-learning"
branch: "master"
tag: "latest"
commit: "f774d5db4f8b8a12b11cf50ff441aece8fdced52"
version: "36ac8a39a47b3e9655f2816108029b1d"
build_date: "2019-02-05T05:54:32.661Z"
size_mb: 9688
size: 3985616927
sif: "https://datasets.datalad.org/shub/koray6/machine-learning/latest/2019-02-05-f774d5db-36ac8a39/36ac8a39a47b3e9655f2816108029b1d.simg"
url: https://datasets.datalad.org/shub/koray6/machine-learning/latest/2019-02-05-f774d5db-36ac8a39/
recipe: https://datasets.datalad.org/shub/koray6/machine-learning/latest/2019-02-05-f774d5db-36ac8a39/Singularity
collection: koray6/machine-learning
---

# koray6/machine-learning:latest

```bash
$ singularity pull shub://koray6/machine-learning:latest
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
```

## Collection

 - Name: [koray6/machine-learning](https://github.com/koray6/machine-learning)
 - License: None

