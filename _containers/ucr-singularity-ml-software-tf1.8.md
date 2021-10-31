---
id: 5574
name: "ucr-singularity/ml-software"
branch: "master"
tag: "tf1.8"
commit: "40619b0a951aa23e25d934a968fa6f30cf20fb76"
version: "1db56531d9e2da915b31c0ce9ff1b080"
build_date: "2018-11-12T16:21:13.702Z"
size_mb: 8924
size: 4198739999
sif: "https://datasets.datalad.org/shub/ucr-singularity/ml-software/tf1.8/2018-11-12-40619b0a-1db56531/1db56531d9e2da915b31c0ce9ff1b080.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ucr-singularity/ml-software/tf1.8/2018-11-12-40619b0a-1db56531/
recipe: https://datasets.datalad.org/shub/ucr-singularity/ml-software/tf1.8/2018-11-12-40619b0a-1db56531/Singularity
collection: ucr-singularity/ml-software
---

# ucr-singularity/ml-software:tf1.8

```bash
$ singularity pull shub://ucr-singularity/ml-software:tf1.8
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: ucr-singularity/cuda-9.0-base

%post

    # TensorFlow
    pip install --no-cache-dir tensorflow-gpu==1.8
    
    # Deep Mind Sonnet
    pip install --no-cache-dir dm-sonnet-gpu==1.17

    # Theano
    pip install --no-cache-dir Theano==1.0.1

    # Keras
    #pip install --no-cache-dir keras==2.1.5
    pip install --no-cache-dir keras==2.2.1
    
    # Pytorch, per pytorch.org recommendation
    pip install --no-cache-dir https://download.pytorch.org/whl/cu90/torch-0.3.1-cp27-cp27mu-linux_x86_64.whl
    pip install --no-cache-dir torchvision==0.2.0

    # OpenCV from pip, including contrib.  This makes the install MUCH faster.
    # See https://pypi.python.org/pypi/opencv-contrib-python for capabilities 
    # and limitations.  
    pip install --no-cache-dir opencv-contrib-python    

    # Install Pydensecrf
    pip install git+https://github.com/lucasb-eyer/pydensecrf.git

    # Set locale in environment
    echo 'export LC_ALL=C' >>$SINGULARITY_ENVIRONMENT
    
    #Keras ml package
    pip install --no-cache-dir keras_vggface
    
    #For keras generator
    pip install --no-cache-dir bcolz
    
    #Neuro-Imaging package
    pip install --no-cache-dir nibabel
    pip install --no-cache-dir niftynet
    pip install --no-cache-dir SimpleITK
    
    #Parallel Processing
    pip install --no-cache-dir joblib
    
    #Progess
    pip install --no-cache-dir tqdm
    
    #Sklearn update
    pip install --no-cache-dir scikit-learn==0.19.2
    
    #Biomedical Denoising library
    pip install --no-cache-dir csbdeep
    #Dependencies for CSBDeep
    pip install --no-cache-dir tifffile
    
    #Uncompress package 7z
    apt-get update && apt-get -y install p7zip-full p7zip-rar
    apt-get -y install dtrx
    
    #Cluster Analysis
    pip install --no-cache-dir yellowbrick

    # Deepdish
    pip install --no-cache-dir deepdish
```

## Collection

 - Name: [ucr-singularity/ml-software](https://github.com/ucr-singularity/ml-software)
 - License: None

