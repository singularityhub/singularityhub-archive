---
id: 6874
name: "koray6/machine-learning"
branch: "master"
tag: "cu80dnn7"
commit: "50a1fc4f7464bda414c19c273d509dba2c9a8cd2"
version: "e58a82955d00d8fb4b218c760165a36b"
build_date: "2019-02-05T05:54:32.649Z"
size_mb: 8782
size: 3799810079
sif: "https://datasets.datalad.org/shub/koray6/machine-learning/cu80dnn7/2019-02-05-50a1fc4f-e58a8295/e58a82955d00d8fb4b218c760165a36b.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/koray6/machine-learning/cu80dnn7/2019-02-05-50a1fc4f-e58a8295/
recipe: https://datasets.datalad.org/shub/koray6/machine-learning/cu80dnn7/2019-02-05-50a1fc4f-e58a8295/Singularity
collection: koray6/machine-learning
---

# koray6/machine-learning:cu80dnn7

```bash
$ singularity pull shub://koray6/machine-learning:cu80dnn7
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
            mxnet-cu80==0.11.0 \
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

