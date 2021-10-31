---
id: 3124
name: "akashsingularityucr/caffe-cpu-faces"
branch: "master"
tag: "latest"
commit: "cded99d84e696440bf24ef934e9f5180290223b1"
version: "bbb32e2d36291850d48101731745de92"
build_date: "2020-06-19T06:38:23.816Z"
size_mb: 3941
size: 1554059295
sif: "https://datasets.datalad.org/shub/akashsingularityucr/caffe-cpu-faces/latest/2020-06-19-cded99d8-bbb32e2d/bbb32e2d36291850d48101731745de92.simg"
url: https://datasets.datalad.org/shub/akashsingularityucr/caffe-cpu-faces/latest/2020-06-19-cded99d8-bbb32e2d/
recipe: https://datasets.datalad.org/shub/akashsingularityucr/caffe-cpu-faces/latest/2020-06-19-cded99d8-bbb32e2d/Singularity
collection: akashsingularityucr/caffe-cpu-faces
---

# akashsingularityucr/caffe-cpu-faces:latest

```bash
$ singularity pull shub://akashsingularityucr/caffe-cpu-faces:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: bvlc/caffe:cpu

%environment

	#Environment variables

	#Use bash as default shell
	SHELL=/bin/bash


	#Add CUDA paths
	CPATH="/usr/local/cuda/include:$CPATH"
	PATH="/usr/local/cuda/bin:$PATH"
	LD_LIBRARY_PATH="/usr/local/cuda/lib64:$LD_LIBRARY_PATH"
	CUDA_HOME="/usr/local/cuda"

	#Add Caffe paths
	CAFFE_ROOT="/opt/caffe"
	PYCAFFE_ROOT="$CAFFE_ROOT/python"
	PYTHONPATH="$PYCAFFE_ROOT:$PYTHONPATH"
	PATH="$CAFFE_ROOT/build/tools:$PYCAFFE_ROOT:$PATH"

	export PATH LD_LIBRARY_PATH CPATH CUDA_HOME CAFFE_ROOT PYCAFFE_ROOT PYTHONPATH

%setup
	#Runs on host
	#The path to the image is $SINGULARITY_ROOTFS


%post
	#Post setup script

	#Load environment variables
	. /environment

	#Default mount paths
	mkdir /scratch /data /shared /fastdata
        
	# TensorFlow
        pip install --no-cache-dir tensorflow==1.12.0
        #pip install --no-cache-dir tensorflow-gpu==1.8
    
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
        #pip install keras
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
    
        # Installing dependencies for FACES project
        pip install --no-cache-dir imutils
        pip install --no-cache-dir dlib
        pip install --no-cache-dir progressbar2
        pip install --no-cache-dir flask
        pip install --no-cache-dir flask_cors
        pip install --no-cache-dir gunicorn
        pip install --no-cache-dir face_recognition
	
	# Update list of packages and install packages for ease of use.
	apt-get update
	apt-get install -y apt-utils
	apt-get install -y vim
	apt-get install -y tmux screen
	apt-get install -y xterm
	
	# Install for tkinter
	apt-get install -y python-tk
	#Instal dependencies for caffe
	apt-get install -y libxcb-xfixes0-dev

	
%runscript
	#Executes with the singularity run command
	#delete this section to use existing docker ENTRYPOINT command





%test
	#Test that script is a success
```

## Collection

 - Name: [akashsingularityucr/caffe-cpu-faces](https://github.com/akashsingularityucr/caffe-cpu-faces)
 - License: [BSD 3-Clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

