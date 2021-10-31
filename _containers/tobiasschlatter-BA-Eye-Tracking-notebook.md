---
id: 7650
name: "tobiasschlatter/BA-Eye-Tracking"
branch: "master"
tag: "notebook"
commit: "2b6be267904ef1578fd6673ceb1e2ab4fbfbe970"
version: "b0bc99e1da8978bc19bf70283e6ed8af"
build_date: "2019-03-12T08:04:35.418Z"
size_mb: 1613
size: 516030495
sif: "https://datasets.datalad.org/shub/tobiasschlatter/BA-Eye-Tracking/notebook/2019-03-12-2b6be267-b0bc99e1/b0bc99e1da8978bc19bf70283e6ed8af.simg"
url: https://datasets.datalad.org/shub/tobiasschlatter/BA-Eye-Tracking/notebook/2019-03-12-2b6be267-b0bc99e1/
recipe: https://datasets.datalad.org/shub/tobiasschlatter/BA-Eye-Tracking/notebook/2019-03-12-2b6be267-b0bc99e1/Singularity
collection: tobiasschlatter/BA-Eye-Tracking
---

# tobiasschlatter/BA-Eye-Tracking:notebook

```bash
$ singularity pull shub://tobiasschlatter/BA-Eye-Tracking:notebook
```

## Singularity Recipe

```singularity
BootStrap: docker
From: continuumio/miniconda3

%help
    The miniconda3 image is based on Debian GNU/Linux 9.5 (stretch)

%post
    apt update
    apt install -y software-properties-common git wget
    
    # Needed for OpenCV
    apt install -y libsm6 libxext6 libxrender1 libfontconfig1
    
    # Install caffe CUDA 
    #echo "deb http://ftp2.cn.debian.org/debian sid main contrib non-free" >> /etc/apt/sources.list
    #apt update
    #apt install -y cuda
    #apt install -y caffe-cuda
    
    #apt-add-repository universe
    #apt update
    #apt install -y git wget build-essential
    
    # Fix some super annoying locale issues
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
    echo 'export LC_ALL=C.UTF-8' >> "$SINGULARITY_ENVIRONMENT"
    echo 'export LANG=C.UTF-8' >> "$SINGULARITY_ENVIRONMENT"
    echo "export PATH=/usr/local:/usr/local/bin:$PATH" >> "$SINGULARITY_ENVIRONMENT"

    # Update conda packages
    /opt/conda/bin/conda update --all -y --quiet
    # Install basic packages
    /opt/conda/bin/conda install -c conda-forge -y -q pip matplotlib tqdm jupyter cython scipy numpy pandas
    # Update pip
    /opt/conda/bin/pip install -U pip -q
    # Clean up
    /opt/conda/bin/conda clean --all -y --quiet
    apt-get autoremove -y
    apt-get clean
   
%environment
    conda=/opt/conda/bin/conda
    pip=/opt/conda/bin/pip
    python3=/opt/conda/bin/python
    export conda pip python3
     
%runscript
     echo "Starting the image..."
     echo "Re-Creating conda environment..."
     conda remove -n notebook --all -y
     conda create -y -q -n notebook python=3.6
     echo "Switching to the new env..."
     source activate notebook
     echo "Please use below command to start the notebook:"
     echo "/opt/conda/bin/jupyter notebook --notebook-dir=<path-to-notebook-directory> --allow-root --ip=0.0.0.0 --port=<port> --no-browser"
     #exec /opt/conda/bin/jupyter notebook --notebook-dir=/projects --allow-root --port=8888 --no-browser

%test  
     echo "Testing python..."
     /opt/conda/bin/python -V
```

## Collection

 - Name: [tobiasschlatter/BA-Eye-Tracking](https://github.com/tobiasschlatter/BA-Eye-Tracking)
 - License: None

