---
id: 10218
name: "ThomasDougherty/ml-software"
branch: "master"
tag: "pip-cv2"
commit: "5fabfe72e1a52e929554148457b8bcd7bd9d5395"
version: "de0d1fb68e34617a19587879e337070b"
build_date: "2019-07-03T23:18:01.339Z"
size_mb: 8780
size: 4188065823
sif: "https://datasets.datalad.org/shub/ThomasDougherty/ml-software/pip-cv2/2019-07-03-5fabfe72-de0d1fb6/de0d1fb68e34617a19587879e337070b.simg"
url: https://datasets.datalad.org/shub/ThomasDougherty/ml-software/pip-cv2/2019-07-03-5fabfe72-de0d1fb6/
recipe: https://datasets.datalad.org/shub/ThomasDougherty/ml-software/pip-cv2/2019-07-03-5fabfe72-de0d1fb6/Singularity
collection: ThomasDougherty/ml-software
---

# ThomasDougherty/ml-software:pip-cv2

```bash
$ singularity pull shub://ThomasDougherty/ml-software:pip-cv2
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

 - Name: [ThomasDougherty/ml-software](https://github.com/ThomasDougherty/ml-software)
 - License: None

