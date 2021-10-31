---
id: 9894
name: "KatOfCats/vcftools"
branch: "master"
tag: "latest"
commit: "afe8590a6a6825eb07537521e707e123571867e7"
version: "5520807f12bdb01a7a89613fec9d9c2e"
build_date: "2019-06-19T16:10:43.545Z"
size_mb: 949
size: 316342303
sif: "https://datasets.datalad.org/shub/KatOfCats/vcftools/latest/2019-06-19-afe8590a-5520807f/5520807f12bdb01a7a89613fec9d9c2e.simg"
url: https://datasets.datalad.org/shub/KatOfCats/vcftools/latest/2019-06-19-afe8590a-5520807f/
recipe: https://datasets.datalad.org/shub/KatOfCats/vcftools/latest/2019-06-19-afe8590a-5520807f/Singularity
collection: KatOfCats/vcftools
---

# KatOfCats/vcftools:latest

```bash
$ singularity pull shub://KatOfCats/vcftools:latest
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
    PATH="/usr/local/vcftools/bin:$PATH"

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

# Install vcftools
git clone https://github.com/vcftools/vcftools.git
cd vcftools
./autogen.sh
./configure
make
make install

%labels
 edited from HPC UEA Team  hpc.admin@uea.ac.uk
```

## Collection

 - Name: [KatOfCats/vcftools](https://github.com/KatOfCats/vcftools)
 - License: [GNU Lesser General Public License v3.0](https://api.github.com/licenses/lgpl-3.0)

