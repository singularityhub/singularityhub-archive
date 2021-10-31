---
id: 6875
name: "koray6/machine-learning"
branch: "master"
tag: "cu80dnn6"
commit: "89c2aaa73b7fe47fb6643e5eb70544e04ffe6080"
version: "18d930a75b817f471b003f9dd3c5cb20"
build_date: "2019-02-05T05:54:32.643Z"
size_mb: 8068
size: 3431776287
sif: "https://datasets.datalad.org/shub/koray6/machine-learning/cu80dnn6/2019-02-05-89c2aaa7-18d930a7/18d930a75b817f471b003f9dd3c5cb20.simg"
url: https://datasets.datalad.org/shub/koray6/machine-learning/cu80dnn6/2019-02-05-89c2aaa7-18d930a7/
recipe: https://datasets.datalad.org/shub/koray6/machine-learning/cu80dnn6/2019-02-05-89c2aaa7-18d930a7/Singularity
collection: koray6/machine-learning
---

# koray6/machine-learning:cu80dnn6

```bash
$ singularity pull shub://koray6/machine-learning:cu80dnn6
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

 - Name: [koray6/machine-learning](https://github.com/koray6/machine-learning)
 - License: None

