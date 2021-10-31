---
id: 7712
name: "dallakyan/topaz_singularity"
branch: "master"
tag: "latest"
commit: "999f3b8270b329e7678121c43066a65275cc52d0"
version: "02ac7a823ee207c4fe0f08ebc22f335b"
build_date: "2019-03-12T08:04:35.745Z"
size_mb: 6210
size: 3323482143
sif: "https://datasets.datalad.org/shub/dallakyan/topaz_singularity/latest/2019-03-12-999f3b82-02ac7a82/02ac7a823ee207c4fe0f08ebc22f335b.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/dallakyan/topaz_singularity/latest/2019-03-12-999f3b82-02ac7a82/
recipe: https://datasets.datalad.org/shub/dallakyan/topaz_singularity/latest/2019-03-12-999f3b82-02ac7a82/Singularity
collection: dallakyan/topaz_singularity
---

# dallakyan/topaz_singularity:latest

```bash
$ singularity pull shub://dallakyan/topaz_singularity:latest
```

## Singularity Recipe

```singularity
BootStrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum wget
%setup
    # commands to be executed on host outside container during bootstrap
%test
    # commands to be executed within container at close of bootstrap process
    exec /usr/bin/python3.5 --version
%environment
    export CUDA_HOME=/usr/local/cuda
    CUDA_LIB=$CUDA_HOME/lib64
    CUDA_INCLUDE=$CUDA_HOME/include
    CUDA_BIN=$CUDA_HOME/bin
    export LD_LIBRARY_PATH=$CUDA_LIB
    export PATH=$CUDA_BIN:$PATH
%runscript
    # commands to be executed when the container runs
    echo "LD_LIBRARY_PATH: $LD_LIBRARY_PATH"
    echo "PATH: $PATH"
    echo "Arguments received: $*"
    exec /usr/local/conda/bin/topaz "$@"
%post
    # commands to be executed inside container during bootstrap
    yum -y install epel-release
    yum -y install https://centos7.iuscommunity.org/ius-release.rpm
    yum -y install http://developer.download.nvidia.com/compute/cuda/repos/rhel7/x86_64/cuda-repo-rhel7-8.0.61-1.x86_64.rpm
    yum clean all && yum makecache
    yum -y install wget python35u python35u-pip libgomp cuda-runtime-8-0 bzip2
    ln -s /usr/local/cuda-8.0 /usr/local/cuda
    # install conda
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh
    bash ~/miniconda.sh -b -p /usr/local/conda
    /usr/local/conda/bin/conda install -y numpy pandas scikit-learn
    # install topaz
    /usr/local/conda/bin/conda install  -y topaz cuda80 -c tbepler -c soumith
    # in-container bind points for shared filesystems
    mkdir -p /gpfs
```

## Collection

 - Name: [dallakyan/topaz_singularity](https://github.com/dallakyan/topaz_singularity)
 - License: None

