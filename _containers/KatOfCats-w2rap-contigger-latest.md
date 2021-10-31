---
id: 8485
name: "KatOfCats/w2rap-contigger"
branch: "master"
tag: "latest"
commit: "5c9df00fd133b31edf391a162a8c76582796d3b5"
version: "d31cd6065413bef73082c44c988b8808"
build_date: "2020-09-01T09:40:36.061Z"
size_mb: 2856.0
size: 682663967
sif: "https://datasets.datalad.org/shub/KatOfCats/w2rap-contigger/latest/2020-09-01-5c9df00f-d31cd606/d31cd6065413bef73082c44c988b8808.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/KatOfCats/w2rap-contigger/latest/2020-09-01-5c9df00f-d31cd606/
recipe: https://datasets.datalad.org/shub/KatOfCats/w2rap-contigger/latest/2020-09-01-5c9df00f-d31cd606/Singularity
collection: KatOfCats/w2rap-contigger
---

# KatOfCats/w2rap-contigger:latest

```bash
$ singularity pull shub://KatOfCats/w2rap-contigger:latest
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
git clone https://github.com/bioinfologics/w2rap-contigger.git
cd w2rap-contigger/
#git checkout bj
cmake -DCMAKE_CXX_COMPILER=g++ .
make -j 4

%labels
 edited from HPC UEA Team  hpc.admin@uea.ac.uk
```

## Collection

 - Name: [KatOfCats/w2rap-contigger](https://github.com/KatOfCats/w2rap-contigger)
 - License: [MIT License](https://api.github.com/licenses/mit)

