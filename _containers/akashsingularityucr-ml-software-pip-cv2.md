---
id: 6053
name: "akashsingularityucr/ml-software"
branch: "master"
tag: "pip-cv2"
commit: "5fabfe72e1a52e929554148457b8bcd7bd9d5395"
version: "487454ef66eec6c29e18991b56767c22"
build_date: "2018-12-24T04:53:14.105Z"
size_mb: 8765
size: 4183146527
sif: "https://datasets.datalad.org/shub/akashsingularityucr/ml-software/pip-cv2/2018-12-24-5fabfe72-487454ef/487454ef66eec6c29e18991b56767c22.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/akashsingularityucr/ml-software/pip-cv2/2018-12-24-5fabfe72-487454ef/
recipe: https://datasets.datalad.org/shub/akashsingularityucr/ml-software/pip-cv2/2018-12-24-5fabfe72-487454ef/Singularity
collection: akashsingularityucr/ml-software
---

# akashsingularityucr/ml-software:pip-cv2

```bash
$ singularity pull shub://akashsingularityucr/ml-software:pip-cv2
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

 - Name: [akashsingularityucr/ml-software](https://github.com/akashsingularityucr/ml-software)
 - License: None

