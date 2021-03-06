---
id: 7802
name: "tobiasschlatter/BA-Eye-Tracking"
branch: "master"
tag: "playground"
commit: "bda47e30e39e8e850a718addd5672c5f0298ef04"
version: "3ac88c674d40c0894142101401fd4742"
build_date: "2019-03-30T02:29:55.838Z"
size_mb: 10619
size: 4328607775
sif: "https://datasets.datalad.org/shub/tobiasschlatter/BA-Eye-Tracking/playground/2019-03-30-bda47e30-3ac88c67/3ac88c674d40c0894142101401fd4742.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/tobiasschlatter/BA-Eye-Tracking/playground/2019-03-30-bda47e30-3ac88c67/
recipe: https://datasets.datalad.org/shub/tobiasschlatter/BA-Eye-Tracking/playground/2019-03-30-bda47e30-3ac88c67/Singularity
collection: tobiasschlatter/BA-Eye-Tracking
---

# tobiasschlatter/BA-Eye-Tracking:playground

```bash
$ singularity pull shub://tobiasschlatter/BA-Eye-Tracking:playground
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:10.0-cudnn7-devel-ubuntu18.04

%help
    Helpp

%environment
    # Bash shell should be the default
    SHELL=/bin/bash
    
    # Update the Path
    PATH="/opt/conda/bin:$PATH"
    export PATH
    
    #PYTHONPATH="/opt/caffe/python:$PYTHONPATH"
    #export PYTHONPATH

    conda="/opt/conda/bin/conda"
    pip="/opt/conda/bin/pip"
    python3="/opt/conda/bin/python"
    jupyter="/opt/conda/bin/jupyter"
    export conda pip python3 jupyter

%post
    # load environment variables
    . /environment

    # use bash as default shell
    echo "\n #Using bash as default shell \n" >> /environment
    echo 'SHELL=/bin/bash' >> /environment
    echo "\n #Adding conda path \n" >> /environment
    echo 'export PATH="/opt/conda/bin:$PATH"' >> /environment

    # make environment file executable
    chmod +x /environment

    apt update
    apt-get -qq install -y software-properties-common git wget
    apt-get -qq install -y doxygen
    
    # Installing conda
    wget https://repo.anaconda.com/archive/Anaconda3-5.3.1-Linux-x86_64.sh -O /tmp/anaconda.sh
    bash /tmp/anaconda.sh -b -p /opt/conda
    
    # Update conda packages
    /opt/conda/bin/conda update --all -y --quiet
    # Install basic packages
    /opt/conda/bin/conda install -c conda-forge -y -q pip matplotlib tqdm jupyter cython scipy numpy pandas nodejs tensorflow
    #/opt/conda/bin/conda install -c conda-forge -y -q opencv

    /opt/conda/bin/conda install -c pytorch -y -q pytorch torchvision cudatoolkit=10.0
    /opt/conda/bin/conda install -c conda-forge torchfile
    /opt/conda/bin/conda install -c conda-forge -y -q ipywebrtc
    /opt/conda/bin/jupyter labextension install -y jupyter-webrtc
    
    # Update pip
    /opt/conda/bin/pip install -U pip -q
    
    # Clean up
    /opt/conda/bin/conda clean --all -y --quiet
    apt-get autoremove -y
    apt-get clean
    
    # Update the PATH
    export PATH=/opt/conda/bin:/usr/local:/usr/local/bin:$PATH
    
    # Remove all the numpy installations and reinstall it properly
    # (Otherwise python complains about multiple installation)
    /opt/conda/bin/pip uninstall -y numpy 2>/dev/null
    /opt/conda/bin/pip uninstall -y numpy 2>/dev/null
    /opt/conda/bin/pip uninstall -y numpy 2>/dev/null
    /opt/conda/bin/pip uninstall -y numpy 2>/dev/null
    /opt/conda/bin/pip install numpy
    
    # OpenCV & dependencies
    apt-get install -y libopencv-dev
    apt-get install -y libsm6 libxext6 libxrender1 libfontconfig1
    /opt/conda/bin/conda install -c menpo -y -q opencv
    
    # We need to find the conda libs as well
    echo 'export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/opt/conda/lib"' >> /environment
    echo 'export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/opt/conda/lib"' >> "$SINGULARITY_ENVIRONMENT"

    # Fixing a couple of problems with libhdf5
    export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/opt/conda/lib"
    
    #/opt/conda/bin/conda install -c conda-forge -y -q Pillow
    
    # Make sure we are not presented a prompt during the non-interactive build
    ln -fs /usr/share/zoneinfo/Europe/Berlin /etc/localtime
    DEBIAN_FRONTEND=noninteractive
    echo 'Europe/Berlin' > /etc/timezone
    
    # Fix some super annoying locale issues
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
    echo 'export LC_ALL=C.UTF-8' >> "$SINGULARITY_ENVIRONMENT"
    echo 'export LANG=C.UTF-8' >> "$SINGULARITY_ENVIRONMENT"
    
    # Update the PATH
    echo "export PATH=/opt/conda/bin:/usr/local:/usr/local/bin:$PATH" >> "$SINGULARITY_ENVIRONMENT"
    export PATH=/opt/conda/bin:/usr/local:/usr/local/bin:$PATH
    
    # Update the PYTHONPATH
    #echo "export PYTHONPATH=/opt/caffe/python:$PYTHONPATH" >> "$SINGULARITY_ENVIRONMENT"
    #export "PYTHONPATH=/opt/caffe/python:$PYTHONPATH"

%runscript
     echo "Starting the image..."
     echo "Re-Creating conda environment..."
     conda init bash
     echo "Starting notebook..."
     echo "--> The notebook will be reachable at: https://${HOSTNAME}.cloudlab.zhaw.ch:8935 + (token query string)"
     /opt/conda/bin/jupyter notebook --notebook-dir=/cluster/home/schlato1/workspace --allow-root --ip=0.0.0.0 --port=8935 --no-browser --certfile=certs/selfsigned.pem --keyfile certs/selfsigned.key

%test  
     echo "Testing python..."
     python3 -V
```

## Collection

 - Name: [tobiasschlatter/BA-Eye-Tracking](https://github.com/tobiasschlatter/BA-Eye-Tracking)
 - License: None

