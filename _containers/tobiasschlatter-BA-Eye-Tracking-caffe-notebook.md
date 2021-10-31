---
id: 7704
name: "tobiasschlatter/BA-Eye-Tracking"
branch: "master"
tag: "caffe-notebook"
commit: "899f63e4fdca74e8b75210530be67e84b83d37f5"
version: "761d2367442dc668e25ad229527ae327"
build_date: "2019-07-02T13:59:55.302Z"
size_mb: 9383
size: 3511332895
sif: "https://datasets.datalad.org/shub/tobiasschlatter/BA-Eye-Tracking/caffe-notebook/2019-07-02-899f63e4-761d2367/761d2367442dc668e25ad229527ae327.simg"
url: https://datasets.datalad.org/shub/tobiasschlatter/BA-Eye-Tracking/caffe-notebook/2019-07-02-899f63e4-761d2367/
recipe: https://datasets.datalad.org/shub/tobiasschlatter/BA-Eye-Tracking/caffe-notebook/2019-07-02-899f63e4-761d2367/Singularity
collection: tobiasschlatter/BA-Eye-Tracking
---

# tobiasschlatter/BA-Eye-Tracking:caffe-notebook

```bash
$ singularity pull shub://tobiasschlatter/BA-Eye-Tracking:caffe-notebook
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:10.0-cudnn7-devel-ubuntu18.04

%help
    Help

%environment
    # Bash shell should be the default
    SHELL=/bin/bash
    
    # Update the Path
    PATH="/opt/conda/bin:$PATH"
    export PATH
    
    PYTHONPATH="/opt/caffe/python:$PYTHONPATH"
    export PYTHONPATH

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
    /opt/conda/bin/conda install -c conda-forge -y -q ipywebrtc
    # Update pip
    /opt/conda/bin/pip install -U pip -q
    # Clean up
    /opt/conda/bin/conda clean --all -y --quiet
    apt-get autoremove -y
    apt-get clean
    
    # Update the PATH
    #echo "export PATH=/opt/conda/bin:/usr/local:/usr/local/bin:$PATH" >> "$SINGULARITY_ENVIRONMENT"
    #echo "export PATH=/opt/conda/bin:/usr/local:/usr/local/bin:$PATH" >> /root/.bashrc
    #echo "export PATH=/opt/conda/bin:/usr/local:/usr/local/bin:$PATH" >> /root/.profile
    export PATH=/opt/conda/bin:/usr/local:/usr/local/bin:$PATH
    
    # Setup a new anaconda env and activate it
    #/opt/conda/bin/conda remove -n notebook --all -y
    #/opt/conda/bin/conda create -y -n notebook python=3.7
    #echo "Listing the env info..."
    #/opt/conda/bin/conda list -n notebook
    # Setup the shell for conda
    #/opt/conda/bin/conda init
    #echo ". /opt/conda/etc/profile.d/conda.sh" >> /root/.bashrc
    #echo ". /opt/conda/etc/profile.d/conda.sh" >> /environment
    #echo "What does this do?"
    #. /opt/conda/etc/profile.d/conda.sh
    #echo "Switching to the new env..."
    #. activate notebook
    #/opt/conda/bin/conda activate notebook
    
    # Remove all the numpy installations and reinstall it properly
    # (Otherwise python complains about multiple installation)
    /opt/conda/bin/pip uninstall -y numpy 2>/dev/null
    /opt/conda/bin/pip uninstall -y numpy 2>/dev/null
    /opt/conda/bin/pip uninstall -y numpy 2>/dev/null
    /opt/conda/bin/pip uninstall -y numpy 2>/dev/null
    /opt/conda/bin/pip install numpy
    
    # Make sure we are not presented a prompt during the non-interactive build
    ln -fs /usr/share/zoneinfo/Europe/Berlin /etc/localtime
    DEBIAN_FRONTEND=noninteractive
    echo 'Europe/Berlin' > /etc/timezone
    
    # OpenCV & dependencies
    apt-get install -y libopencv-dev
    apt-get install -y libsm6 libxext6 libxrender1 libfontconfig1
    
    # Caffe dependencies
    apt-get -qq install -y build-essential git pkg-config
    apt-get -qq install -y libgflags-dev
    apt-get -qq install -y libprotobuf-dev libleveldb-dev libsnappy-dev libhdf5-serial-dev protobuf-compiler
    apt-get -qq install -y libatlas-base-dev
    apt-get -qq install -y --no-install-recommends libboost-all-dev
    apt-get -qq install -y libhdf5-dev
    apt-get -qq install -y libgflags-dev libgoogle-glog-dev liblmdb-dev
    
    # We need to find the conda libs as well
    echo 'export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/opt/conda/lib"' >> /environment
    echo 'export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/opt/conda/lib"' >> "$SINGULARITY_ENVIRONMENT"
    
    # Fixing a couple of problems with libhdf5
    export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/opt/conda/lib"
    ln -s /opt/conda/lib/libhdf5_hl.so.100 /usr/lib/libhdf5_hl.so.100
    ln -s /opt/conda/lib/libhdf5.so.103 /usr/lib/libhdf5.so.103
    
    # For some reason these interfere with the build of caffe - make them go away...
    /opt/conda/bin/conda uninstall -y -q libtiff
    /opt/conda/bin/conda uninstall -y -q libuuid
 
    # Build Caffe
    git clone https://github.com/BVLC/caffe /opt/caffe/
    cd /opt/caffe/
    wget -L -O Makefile.config https://gist.githubusercontent.com/tobiasschlatter/fe1b65a98964cbd06c1054df0e95cffb/raw/Makefile.config
    
    make clean
    make all
    make test
    
    make pycaffe
    
    cd python
    
    # Installing the caffe python requirements
    for req in $(cat requirements.txt); do /opt/conda/bin/pip install $req; done
    
    # Date util is too old to be used with python 3 -> replace it!
    /opt/conda/bin/pip install 'python-dateutil>=2.0' --force-reinstall
    
    # Fix some super annoying locale issues
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
    echo 'export LC_ALL=C.UTF-8' >> "$SINGULARITY_ENVIRONMENT"
    echo 'export LANG=C.UTF-8' >> "$SINGULARITY_ENVIRONMENT"
    
    # Update the PATH
    echo "export PATH=/opt/caffe/python:/opt/conda/bin:/usr/local:/usr/local/bin:$PATH" >> "$SINGULARITY_ENVIRONMENT"
    export PATH=/opt/caffe/python:/opt/conda/bin:/usr/local:/usr/local/bin:$PATH
    
    # Update the PYTHONPATH
    echo "export PYTHONPATH=/opt/caffe/python:$PYTHONPATH" >> "$SINGULARITY_ENVIRONMENT"
    export "PYTHONPATH=/opt/caffe/python:$PYTHONPATH"
    
    python -c "import caffe; print(caffe.__version__)"
    
    # For webcam usage
    /opt/conda/bin/jupyter labextension install -y jupyter-webrtc

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

