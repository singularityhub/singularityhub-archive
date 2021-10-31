---
id: 2334
name: "ucr-singularity/ml-software"
branch: "master"
tag: "pip-cv2"
commit: "5fabfe72e1a52e929554148457b8bcd7bd9d5395"
version: "0ecbb4d06e075825e7c8d5f446735685"
build_date: "2018-04-02T06:51:03.440Z"
size_mb: 8848
size: 4204441631
sif: "https://datasets.datalad.org/shub/ucr-singularity/ml-software/pip-cv2/2018-04-02-5fabfe72-0ecbb4d0/0ecbb4d06e075825e7c8d5f446735685.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ucr-singularity/ml-software/pip-cv2/2018-04-02-5fabfe72-0ecbb4d0/
recipe: https://datasets.datalad.org/shub/ucr-singularity/ml-software/pip-cv2/2018-04-02-5fabfe72-0ecbb4d0/Singularity
collection: ucr-singularity/ml-software
---

# ucr-singularity/ml-software:pip-cv2

```bash
$ singularity pull shub://ucr-singularity/ml-software:pip-cv2
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: ucr-singularity/cuda-9.0-base

%post

    # TensorFlow
    pip install --no-cache-dir tensorflow-gpu==1.5.0
    
    # Deep Mind Sonnet
    pip install --no-cache-dir dm-sonnet-gpu==1.17

    # Theano
    pip install --no-cache-dir Theano==1.0.1

    # Keras
    pip install --no-cache-dir keras==2.1.5

    # Pytorch, per pytorch.org recommendation
    pip install --no-cache-dir https://download.pytorch.org/whl/cu90/torch-0.3.1-cp27-cp27mu-linux_x86_64.whl
    pip install --no-cache-dir torchvision==0.2.0

    # OpenCV from pip, including contrib.  This makes the install MUCH faster.
    # See https://pypi.python.org/pypi/opencv-contrib-python for capabilities 
    # and limitations.  
    pip install --no-cache-dir opencv-contrib-python    
    
    # Install Pydensecrf
    pip install git+https://github.com/lucasb-eyer/pydensecrf.git
```

## Collection

 - Name: [ucr-singularity/ml-software](https://github.com/ucr-singularity/ml-software)
 - License: None

