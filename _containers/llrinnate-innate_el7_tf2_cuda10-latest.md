---
id: 14062
name: "llrinnate/innate_el7_tf2_cuda10"
branch: "master"
tag: "latest"
commit: "fef1796a6ddf2064f73e24ff5dba9ccef7875ff2"
version: "3ebee37e4baeea39bdcc3add27a6e5c5"
build_date: "2020-09-23T15:41:21.850Z"
size_mb: 4815.0
size: 2813390879
sif: "https://datasets.datalad.org/shub/llrinnate/innate_el7_tf2_cuda10/latest/2020-09-23-fef1796a-3ebee37e/3ebee37e4baeea39bdcc3add27a6e5c5.sif"
url: https://datasets.datalad.org/shub/llrinnate/innate_el7_tf2_cuda10/latest/2020-09-23-fef1796a-3ebee37e/
recipe: https://datasets.datalad.org/shub/llrinnate/innate_el7_tf2_cuda10/latest/2020-09-23-fef1796a-3ebee37e/Singularity
collection: llrinnate/innate_el7_tf2_cuda10
---

# llrinnate/innate_el7_tf2_cuda10:latest

```bash
$ singularity pull shub://llrinnate/innate_el7_tf2_cuda10:latest
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
    export CUDA_VERSION="10.0.130"
    export CUDA_PKG_VERSION="10-0-10.0.130-1"

%files
    cuda.repo /etc/yum.repos.d
    runscript.sh /usr/sbin/

%post
    echo "  ==  CUDA Repo"
    NVIDIA_GPGKEY_SUM=d1be581509378368edeec8c1eb2958702feedf3bc3d17011adbf24efacce4ab5
    curl -fsSL https://developer.download.nvidia.com/compute/cuda/repos/rhel7/x86_64/7fa2af80.pub | sed '/^Version/d' > /etc/pki/rpm-gpg/RPM-GPG-KEY-NVIDIA
    echo "$NVIDIA_GPGKEY_SUM  /etc/pki/rpm-gpg/RPM-GPG-KEY-NVIDIA" | sha256sum -c --strict -
    echo "  ==  Installing CUDA"
    yum install -y cuda-cudart-10-0-10.0.130-1 cuda-compat-10-0 python36-pip git
    echo "  ==  Cleaning"
    rm -rf /var/cache/yum/*
    echo "  ==  Configuring CUDA"
    ln -s cuda-10.0 /usr/local/cuda
    echo "/usr/local/nvidia/lib" >> /etc/ld.so.conf.d/nvidia.conf
    echo "/usr/local/nvidia/lib64" >> /etc/ld.so.conf.d/nvidia.conf
    export PATH="/usr/local/nvidia/bin:/usr/local/cuda/bin:${PATH}"
    export LD_LIBRARY_PATH="/usr/local/nvidia/lib:/usr/local/nvidia/lib64"
    export CPATH="/usr/local/include"
    export NVIDIA_VISIBLE_DEVICES="all"
    export NVIDIA_DRIVER_CAPABILITIES="compute,utility"
    export NVIDIA_REQUIRE_CUDA="cuda>=10.0 brand=tesla,driver>=384,driver<385 brand=tesla,driver>=410,driver<411"
    echo "  ==  Installing pip packages"
    curl https://bootstrap.pypa.io/get-pip.py | python3
    python3 -m pip install --upgrade pip
    python3 -m pip install --upgrade setuptools
    python3 -m pip install 'tensorflow-gpu>=2' protobuf mlinnate keras scikit-learn torch xgboost
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

%runscript
    /usr/sbin/runscript.sh $@
```

## Collection

 - Name: [llrinnate/innate_el7_tf2_cuda10](https://github.com/llrinnate/innate_el7_tf2_cuda10)
 - License: [MIT License](https://api.github.com/licenses/mit)

