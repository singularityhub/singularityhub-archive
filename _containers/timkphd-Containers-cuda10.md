---
id: 12745
name: "timkphd/Containers"
branch: "master"
tag: "cuda10"
commit: "27334d1edff5916fd2fde00ee16c0cccb17693e0"
version: "0ee3492df2b7f23132fc7aa0409c2c963e82b18bcdd1f18f7d5e2702f1d4c0f9"
build_date: "2020-06-05T21:14:28.429Z"
size_mb: 3375.59375
size: 3539566592
sif: "https://datasets.datalad.org/shub/timkphd/Containers/cuda10/2020-06-05-27334d1e-0ee3492d/0ee3492df2b7f23132fc7aa0409c2c963e82b18bcdd1f18f7d5e2702f1d4c0f9.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/timkphd/Containers/cuda10/2020-06-05-27334d1e-0ee3492d/
recipe: https://datasets.datalad.org/shub/timkphd/Containers/cuda10/2020-06-05-27334d1e-0ee3492d/Singularity
collection: timkphd/stuff
---

# timkphd/Containers:cuda10

```bash
$ singularity pull shub://timkphd/Containers:cuda10
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%setup
    #touch /file1
    #touch ${SINGULARITY_ROOTFS}/file2

%files
    #/file1
    #/file1 /opt

%environment
    export LISTEN_PORT=12345
    export LC_ALL=C
    #export TMPDIR=/bin/mytmp

%post

   apt-get update && apt-get install -y netcat
   apt-get install -y wget 
   apt-get install -y gnupg
  

# cd to /tmp where this shell has write permission
cd /tmp
# now get the key:
wget https://apt.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS-2019.PUB
# now install that key
apt-key add GPG-PUB-KEY-INTEL-SW-PRODUCTS-2019.PUB
# now remove the public key file exit the root shell
rm GPG-PUB-KEY-INTEL-SW-PRODUCTS-2019.PUB

echo "deb https://apt.repos.intel.com/mkl all main
deb https://apt.repos.intel.com/2019 intel-psxe-runtime main
deb https://apt.repos.intel.com/ipp all main
deb https://apt.repos.intel.com/tbb all main
deb https://apt.repos.intel.com/daal all main
deb https://apt.repos.intel.com/mpi all main" > /etc/apt/sources.list.d/intelproducts.list


#wget https://apt.repos.intel.com/setup/intelproducts.list -O /etc/apt/sources.list.d/intelproducts.list

apt-get --allow-unauthenticated -y update

#apt search cuda
#bonk

    apt install -y gcc
    apt install -y gfortran
    apt install -y make
    export DEBIAN_FRONTEND=noninteractive
    apt-get -y install git-gui
#  intel-mkl-64bit-2020.1-102 2020.1-102
#  intel-mkl-64bit-2020.0-088 2020.0-088
#  intel-mkl-64bit-2019.5-075 2019.5-075
#  intel-mkl-64bit-2019.4-070 2019.4-070
#  intel-mkl-64bit-2019.3-062 2019.3-062
#  intel-mkl-64bit-2019.2-057 2019.2-057
#  intel-mkl-64bit-2019.1-053 2019.1-053
#  intel-mkl-64bit-2019.0-045 2019.0-045
#  intel-mkl-64bit-2018.4-057 2018.4-057
#  intel-mkl-64bit-2018.3-051 2018.3-051
#  intel-mkl-64bit-2018.2-046 2018.2-046
#  intel-mkl-64bit-2018.1-038 2018.1-038
#  intel-mkl-64bit-2018.0-033 2018.0-033


#    apt-get -y install intel-mkl-64bit-2018.4-057
     apt-get -y install intel-psxe-runtime
#    apt-get install -y dialog

if true ; then
    apt-get install -y software-properties-common
    apt-get update
 #   add-apt-repository ppa:graphics-drivers/ppa
    apt update
 #   apt-get install -y ubuntu-drivers-common
fi
    #ubuntu-drivers devices
    #ubuntu-drivers autoinstall
    
if true ; then
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-ubuntu1804.pin
mv cuda-ubuntu1804.pin /etc/apt/preferences.d/cuda-repository-pin-600
apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub
add-apt-repository "deb http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/ /"
apt-get update
apt-get -y install cuda



#wget http://developer.download.nvidia.com/compute/cuda/10.2/Prod/local_installers/cuda_10.2.89_440.33.01_linux.run
#sh cuda_10.2.89_440.33.01_linux.run  --silent  --no-opengl-libs --toolkit
#sh cuda_10.2.89_440.33.01_linux.run  --silent  --no-opengl-libs
#cat /var/log/cuda-installer.log 
else
    apt install -y nvidia-utils-440
    apt-get install -y nvidia-cuda-toolkit
fi
    NOW=`date`
    echo "export NOW=\"${NOW}\"" >> $SINGULARITY_ENVIRONMENT

    cd /opt
    git clone https://github.com/timkphd/examples.git
    cd examples
    export PATH=/usr/local/cuda/bin:$PATH
    export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
    cd gpu_parallel 
    nvcc sermain.c hysub.cu -o testgpu
    nvcc gpucount.c -o gpucount
    

%runscript

    echo "Container was created $NOW"
    echo "Arguments received: $*"
    exec echo "$@"

%environment 
    export PATH=/usr/local/cuda/bin:$PATH
    export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH

%startscript
    nc -lp $LISTEN_PORT

%test
    grep -q NAME=\"Ubuntu\" /etc/os-release
    if [ $? -eq 0 ]; then
        echo "Container base is Ubuntu as expected."
    else
        echo "Container base is not Ubuntu."
    fi

%labels
    Author d@sylabs.io
    Version v0.0.1

%help
    This is a demo container used to illustrate a def file that uses all
    supported sections.
```

## Collection

 - Name: [timkphd/Containers](https://github.com/timkphd/Containers)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

