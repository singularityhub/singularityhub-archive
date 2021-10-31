---
id: 14203
name: "andreiprodan/singularity"
branch: "master"
tag: "latest"
commit: "6995670de0edaa341fea5d000f3ad0d12c3117f1"
version: "d9e9a0a71f0853002909cdb09888bb0386ff1bf3765b8ba7b0949fb1b4ea2609"
build_date: "2021-04-16T13:42:10.171Z"
size_mb: 221.04296875
size: 231780352
sif: "https://datasets.datalad.org/shub/andreiprodan/singularity/latest/2021-04-16-6995670d-d9e9a0a7/d9e9a0a71f0853002909cdb09888bb0386ff1bf3765b8ba7b0949fb1b4ea2609.sif"
url: https://datasets.datalad.org/shub/andreiprodan/singularity/latest/2021-04-16-6995670d-d9e9a0a7/
recipe: https://datasets.datalad.org/shub/andreiprodan/singularity/latest/2021-04-16-6995670d-d9e9a0a7/Singularity
collection: andreiprodan/singularity
---

# andreiprodan/singularity:latest

```bash
$ singularity pull shub://andreiprodan/singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu@sha256:fff16eea1a8ae92867721d90c59a75652ea66d29c05294e6e2f898704bdb8cf1

%runscript
    exec echo "This is an Ubuntu 20.04 LTS Container with Miniconda v4.8.3!!"

%files
   
%environment
   CONDA_INSTALL_PATH="/usr/local/miniconda3"
   CONDA_BIN_PATH="/usr/local/miniconda3/bin"
   export PATH="$CONDA_BIN_PATH:$PATH"
   export LC_ALL=C.UTF-8
   export LANG=C.UTF-8

%labels
   OWNER andreiprodan

%post
   echo "The post section is where you can install, and configure your container."  
   apt-get update && apt-get -y install wget     # Installing commonly used apps
   wget https://repo.anaconda.com/miniconda/Miniconda3-py38_4.8.3-Linux-x86_64.sh    # download and install Anaconda (miniconda, conda v.4.8.3)
   chmod +x Miniconda3-py38_4.8.3-Linux-x86_64.sh
   CONDA_INSTALL_PATH="/usr/local/miniconda3"
   ./Miniconda3-py38_4.8.3-Linux-x86_64.sh -b -p $CONDA_INSTALL_PATH
   rm Miniconda3-py38_4.8.3-Linux-x86_64.sh
   export PATH="/usr/local/miniconda3/bin:$PATH"      # cant create environments without this
```

## Collection

 - Name: [andreiprodan/singularity](https://github.com/andreiprodan/singularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

