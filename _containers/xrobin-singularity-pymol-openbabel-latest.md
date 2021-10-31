---
id: 1956
name: "xrobin/singularity-pymol-openbabel"
branch: "master"
tag: "latest"
commit: "40b7305a7f3011a0f49a1da8f321cc80bb137663"
version: "609b68b05f0faf1613f9848b0995c6be"
build_date: "2021-04-12T09:35:34.492Z"
size_mb: 2260
size: 998662175
sif: "https://datasets.datalad.org/shub/xrobin/singularity-pymol-openbabel/latest/2021-04-12-40b7305a-609b68b0/609b68b05f0faf1613f9848b0995c6be.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/xrobin/singularity-pymol-openbabel/latest/2021-04-12-40b7305a-609b68b0/
recipe: https://datasets.datalad.org/shub/xrobin/singularity-pymol-openbabel/latest/2021-04-12-40b7305a-609b68b0/Singularity
collection: xrobin/singularity-pymol-openbabel
---

# xrobin/singularity-pymol-openbabel:latest

```bash
$ singularity pull shub://xrobin/singularity-pymol-openbabel:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: centos:7

%runscript

   #"I can put here whatever I want to happen by default when the user runs the container"
   cat << EOF
This container includes the following apps:
PyMOL 2.0.7 - https://pymol.org
OpenBabel 2.4.1 - http://openbabel.org
To list them do "singularity apps pymol-openbabel.img"
EOF

%post
    # install some system deps
    #apt-get -y update
    #apt-get -y install locales curl bzip2
    #locale-gen en_US.UTF-8
    #apt-get clean
    yum install -y curl bzip2
    # System dependencies for PyMOL
    yum install -y libGL libGLU qt5-qtbase-gui

    # Openbabel from the system?
    # yum install openbabel

    # download and install miniconda2
    if [ ! -x "/opt/miniconda2/bin/conda" ]; then
      curl -sSL -O https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh
      bash Miniconda2-latest-Linux-x86_64.sh -p /opt/miniconda2 -b
      rm -fr Miniconda2-latest-Linux-x86_64.sh
    fi

    # use conda to install some bioinfo tools
    export PATH=/opt/miniconda2/bin:$PATH
    conda install --yes -c bioconda openbabel
    conda install --yes -c schrodinger pymol 

%environment
    export LANG=en_US.UTF-8
    export LANGUAGE=en_US:en
    export LC_ALL=en_US.UTF-8
    export PATH=/opt/miniconda2/bin:$PATH

%apphelp PyMOL
    "PyMOL version 2.0.7"

%apprun PyMOL
    /opt/miniconda2/bin/pymol

%apphelp OpenBabel
    "OpenBabel version 2.4.1"

%apprun OpenBabel
    /opt/miniconda2/bin/obabel
```

## Collection

 - Name: [xrobin/singularity-pymol-openbabel](https://github.com/xrobin/singularity-pymol-openbabel)
 - License: None

