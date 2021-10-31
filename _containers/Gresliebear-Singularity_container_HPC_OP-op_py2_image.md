---
id: 15552
name: "Gresliebear/Singularity_container_HPC_OP"
branch: "main"
tag: "op_py2_image"
commit: "bb970c0ed187e1cfd174b347960be6fd038552f3"
version: "0fff2142cc29bd896e124c4e9adfa04e10c9c08aefbbf99dc89887435f49106c"
build_date: "2021-03-29T23:03:55.580Z"
size_mb: 536.84765625
size: 562925568
sif: "https://datasets.datalad.org/shub/Gresliebear/Singularity_container_HPC_OP/op_py2_image/2021-03-29-bb970c0e-0fff2142/0fff2142cc29bd896e124c4e9adfa04e10c9c08aefbbf99dc89887435f49106c.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/Gresliebear/Singularity_container_HPC_OP/op_py2_image/2021-03-29-bb970c0e-0fff2142/
recipe: https://datasets.datalad.org/shub/Gresliebear/Singularity_container_HPC_OP/op_py2_image/2021-03-29-bb970c0e-0fff2142/Singularity
collection: Gresliebear/Singularity_container_HPC_OP
---

# Gresliebear/Singularity_container_HPC_OP:op_py2_image

```bash
$ singularity pull shub://Gresliebear/Singularity_container_HPC_OP:op_py2_image
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:18.04

%labels
    Author: Leslie M. Wubbel
    Maintainer: Leslie M. Wubbel
    Version: v0.0.1
    
%post
    apt-get update -y
    apt-get install wget -y
    apt-get install git -y

       ## Basic installations 
    apt-get update -y
    apt install software-properties-common -y 
    apt-add-repository universe -y 

    ### ACI 
    #Set up the environment $ export PATH=/usr/local/cuda-9.1/bin:$PATH $ export LD_LIBRARY_PATH=/usr/local/cuda-9.1/lib64:$LD_LIBRARY_PATH $ export CPATH=/usr/local/cuda-9.1/samples/common/inc:$CPATH

    ## pip install requirements 
    ##
    ##
    # Initialize environment and update conda
    #export PATH=/usr/local/miniconda/bin:${PATH}
    #export LD_LIBRARY_PATH=/usr/local/miniconda/lib:${LD_LIBRARY_PATH}

    apt install python2.7 -y
    apt install python-pip -y
    pip install absl-py==0.11.0
    pip install astor==0.8.1
    pip install backports.weakref==1.0.post1
    pip install enum34==1.1.10
    pip install funcsigs==1.0.2
    pip install futures==3.3.0
    pip install gast==0.4.0
    pip install grpcio==1.34.0
    pip install Markdown==3.1.1
    pip install mock==3.0.5
    pip install numpy==1.16.6
    pip install protobuf==3.14.0
    pip install six==1.15.0
    pip install tensorboard==1.9.0
    pip install tensorflow==1.9.0
    pip install termcolor==1.1.0
    pip install Werkzeug==1.0.1
    pip install Pillow==6.2.2
    pip install scipy==1.2.3
    pip install absl-py==0.11.0
    pip install backports.functools-lru-cache==1.6.1
    pip install bz2file==0.98
    pip install cycler==0.10.0
    pip install imageio==2.6.0
    pip install kiwisolver==1.1.0
    pip install Markdown==3.1.1
    pip install matplotlib==2.2.5
    pip install nibabel==2.5.2
    pip install pandas==0.24.2
    pip install pyparsing==2.4.7
    pip install python-dateutil==2.8.1
    pip install pytz==2020.5

    
%test
    grep -q NAME=\"Ubuntu\" /etc/os-release
    if [ $? -eq 0 ]; then
        echo "Container base is Ubuntu as expected."
    else
        echo "Container base is not Ubuntu."
        exit 1
    fi
```

## Collection

 - Name: [Gresliebear/Singularity_container_HPC_OP](https://github.com/Gresliebear/Singularity_container_HPC_OP)
 - License: [MIT License](https://api.github.com/licenses/mit)

