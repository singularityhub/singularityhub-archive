---
id: 8416
name: "nysbc/topaz"
branch: "master"
tag: "latest"
commit: "633188fc0140f6a5819f98070102ed8876a39e93"
version: "33d509d0e4ad1991c7b2f47c4092e22a"
build_date: "2021-04-19T17:33:13.158Z"
size_mb: 5278.0
size: 2927902751
sif: "https://datasets.datalad.org/shub/nysbc/topaz/latest/2021-04-19-633188fc-33d509d0/33d509d0e4ad1991c7b2f47c4092e22a.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/nysbc/topaz/latest/2021-04-19-633188fc-33d509d0/
recipe: https://datasets.datalad.org/shub/nysbc/topaz/latest/2021-04-19-633188fc-33d509d0/Singularity
collection: nysbc/topaz
---

# nysbc/topaz:latest

```bash
$ singularity pull shub://nysbc/topaz:latest
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
    yum -y install https://repo.ius.io/ius-release-el7.rpm
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

 - Name: [nysbc/topaz](https://github.com/nysbc/topaz)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

