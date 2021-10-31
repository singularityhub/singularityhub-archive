---
id: 8420
name: "Amjadhpc/w2rap-contigger"
branch: "master"
tag: "latest"
commit: "221f6cabedd19743046ee5dec18e6feb85130218"
version: "2d50d4e47f3b2744b7c24711906c07f9"
build_date: "2019-07-01T20:21:49.640Z"
size_mb: 2855
size: 681750559
sif: "https://datasets.datalad.org/shub/Amjadhpc/w2rap-contigger/latest/2019-07-01-221f6cab-2d50d4e4/2d50d4e47f3b2744b7c24711906c07f9.simg"
url: https://datasets.datalad.org/shub/Amjadhpc/w2rap-contigger/latest/2019-07-01-221f6cab-2d50d4e4/
recipe: https://datasets.datalad.org/shub/Amjadhpc/w2rap-contigger/latest/2019-07-01-221f6cab-2d50d4e4/Singularity
collection: Amjadhpc/w2rap-contigger
---

# Amjadhpc/w2rap-contigger:latest

```bash
$ singularity pull shub://Amjadhpc/w2rap-contigger:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: gcc:5.5.0
IncludeCmd: yes

%setup
# Copy any necessary files

%environment

    # Use bash as default shell
    SHELL=/bin/bash

    # Add paths
    PATH="/usr/local/w2rap-contigger/bin:$PATH"

    # Export paths
    export PATH


%post
    # Make gpfs folder to hold mount
    mkdir /gpfs
    mkdir /shared
    mkdir /local
    mkdir /scratch
    # Create and move to build directory
    mkdir /root/build && cd /root/build

# run OS updates
apt-get update -y  && apt-get upgrade -y

# Install cmake
cd /usr/local/
wget https://cmake.org/files/v3.4/cmake-3.4.1-Linux-x86_64.tar.gz
tar xvf cmake-3.4.1-Linux-x86_64.tar.gz
export PATH="`pwd`/cmake-3.4.1-Linux-x86_64/bin:$PATH"
rm -rf cmake-3.4.1-Linux-x86_64.tar.gz

# Install w2rap-contigger
git clone https://github.com/gonzalogacc/w2rap-contigger.git
cd w2rap-contigger/
cmake -DCMAKE_CXX_COMPILER=g++ .
make -j 4
%labels
 HPC UEA Team  hpc.admin@uea.ac.uk
%help
We are testing again again and again
```

## Collection

 - Name: [Amjadhpc/w2rap-contigger](https://github.com/Amjadhpc/w2rap-contigger)
 - License: [MIT License](https://api.github.com/licenses/mit)

