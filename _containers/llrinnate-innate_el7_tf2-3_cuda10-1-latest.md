---
id: 14452
name: "llrinnate/innate_el7_tf2-3_cuda10-1"
branch: "master"
tag: "latest"
commit: "efc940947525e8441fea0ba4cb712ec0113ee62a"
version: "91ceb2950257501af4746c9362b33be5"
build_date: "2020-11-19T14:35:49.722Z"
size_mb: 9575.0
size: 5222928415
sif: "https://datasets.datalad.org/shub/llrinnate/innate_el7_tf2-3_cuda10-1/latest/2020-11-19-efc94094-91ceb295/91ceb2950257501af4746c9362b33be5.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/llrinnate/innate_el7_tf2-3_cuda10-1/latest/2020-11-19-efc94094-91ceb295/
recipe: https://datasets.datalad.org/shub/llrinnate/innate_el7_tf2-3_cuda10-1/latest/2020-11-19-efc94094-91ceb295/Singularity
collection: llrinnate/innate_el7_tf2-3_cuda10-1
---

# llrinnate/innate_el7_tf2-3_cuda10-1:latest

```bash
$ singularity pull shub://llrinnate/innate_el7_tf2-3_cuda10-1:latest
```

## Singularity Recipe

```singularity
Bootstrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/x86_64/
Include: yum

%help
    Singularity container to exec innate tasks.
    CUDA version : 10.0.130
    CentOS 7

%labels
    Author LLR
    Version 1.1

%environment
    export CUDA_VERSION="10.1.105"
    export CUDA_PKG_VERSION="10.1.105-418.39"

%files
    runscript.sh /usr/sbin/

%post
    echo "  ==  Installing requirements"
    yum install -y epel-release python36-pip git vim gcc wget bzip2

    echo "  ==  Installing CUDA"
    wget -O $SINGULARITY_CONTAINER/tmp/cuda_10.1.105_418.39_linux.run https://developer.nvidia.com/compute/cuda/10.1/Prod/local_installers/cuda_10.1.105_418.39_linux.run
    wget -O $SINGULARITY_CONTAINER/tmp/cudnn-7.6.5-cuda10.1_0.tar.bz2 https://anaconda.org/anaconda/cudnn/7.6.5/download/linux-64/cudnn-7.6.5-cuda10.1_0.tar.bz2
    cd $SINGULARITY_CONTAINER/tmp/
    mkdir ./cuda_10.1.105_418.39_linux
    mkdir ./cudnn-7.6.5-cuda10.1_0
    tail -n +521 cuda_10.1.105_418.39_linux.run > cuda_10.1.105_418.39_linux.tar.gz
    tar zxf cuda_10.1.105_418.39_linux.tar.gz -C ./cuda_10.1.105_418.39_linux
    tar jxf cudnn-7.6.5-cuda10.1_0.tar.bz2 -C ./cudnn-7.6.5-cuda10.1_0
    sh ./cuda_10.1.105_418.39_linux.run --silent
    sh ./cuda_10.1.105_418.39_linux.run --silent --driver
    sh ./cuda_10.1.105_418.39_linux.run --silent --toolkit
    cp ./cuda_10.1.105_418.39_linux/builds/cuda-toolkit/targets/x86_64-linux/lib/*.so.10 /usr/local/cuda-10.1/targets/x86_64-linux/lib/
    cd ./cuda_10.1.105_418.39_linux/builds
    ./NVIDIA-Linux-x86_64-418.39.run --extract-only
    cp ./NVIDIA-Linux-x86_64-418.39/*.so.418.39 /usr/local/cuda-10.1/targets/x86_64-linux/lib/
    cp $SINGULARITY_CONTAINER/tmp/cudnn-7.6.5-cuda10.1_0/lib/libcudnn.so.7 /usr/local/cuda-10.1/targets/x86_64-linux/lib/

    for myfile in /usr/local/cuda-10.1/targets/x86_64-linux/lib/*418.39; do target=$(echo $myfile | sed -e 's/418\.39/1/g'); ln -s $myfile $target; done
    ln -s cuda-10.1 /usr/local/cuda
    echo "/usr/local/nvidia/lib" >> /etc/ld.so.conf.d/nvidia.conf
    echo "/usr/local/nvidia/lib64" >> /etc/ld.so.conf.d/nvidia.conf
    echo 'export PATH="/usr/local/nvidia/bin:/usr/local/cuda/bin:${PATH}"' >> /environment
    echo 'export LD_LIBRARY_PATH="/usr/local/cuda-10.1/targets/x86_64-linux/lib/:/usr/local/nvidia/lib:/usr/local/nvidia/lib64"' >> /environment
    echo 'export CPATH="/usr/local/include"' >> /environment
    echo 'export NVIDIA_VISIBLE_DEVICES="all"' >> /environment
    echo 'export NVIDIA_DRIVER_CAPABILITIES="compute,utility"' >> /environment

    echo "  ==  Installing pip packages"
    curl https://bootstrap.pypa.io/get-pip.py | python3
    python3 -m pip install --upgrade pip
    python3 -m pip install --upgrade setuptools
    python3 -m pip install 'tensorflow-gpu==2.3.0' protobuf mlinnate keras scikit-learn torch xgboost

    echo "  ==  Configuring"
    chmod 755 /usr/sbin/runscript.sh
    mkdir -p /opt/exp_soft
    pck_dir=$(python3 -m pip show mlinnate | grep Location | cut -f2 -d' ')
    ln -s ${pck_dir}/mlinnate/innate.py ${pck_dir}/innate.py
    ln -s ${pck_dir}/mlinnate/innate_keras_callback.py ${pck_dir}/innate_keras_callback.py

    echo "  ==  Installing qkeras"
    cd /tmp
    git clone https://github.com/google/qkeras.git
    cd qkeras
    python3 setup.py build
    python3 setup.py install

    echo "  ==  Cleaning"
    yum clean all
    rm -rf $SINGULARITY_CONTAINER/var/cache/yum/*
    rm -rf /tmp/qkeras
    rm -rf $SINGULARITY_CONTAINER/tmp/cuda_10.1.105_418.39_linux.run
    rm -rf $SINGULARITY_CONTAINER/tmp/cuda_10.1.105_418.39_linux.tar.gz
    rm -rf $SINGULARITY_CONTAINER/tmp/cuda_10.1.105_418.39_linux
    rm -rf $SINGULARITY_CONTAINER/tmp/cudnn-7.6.5-cuda10.1_0.tar.bz2
    rm -rf $SINGULARITY_CONTAINER/tmp/cudnn-7.6.5-cuda10.1_0

%runscript
    /usr/sbin/runscript.sh $@
```

## Collection

 - Name: [llrinnate/innate_el7_tf2-3_cuda10-1](https://github.com/llrinnate/innate_el7_tf2-3_cuda10-1)
 - License: [MIT License](https://api.github.com/licenses/mit)

