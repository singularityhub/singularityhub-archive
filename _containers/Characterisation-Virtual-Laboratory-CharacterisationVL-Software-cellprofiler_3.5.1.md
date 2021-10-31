---
id: 4619
name: "Characterisation-Virtual-Laboratory/CharacterisationVL-Software"
branch: "master"
tag: "cellprofiler_3.5.1"
commit: "09af1a485d808e449eee28c5aadb45d7d078b96b"
version: "c18a43b08daf857bb9bb6c9920289ffb"
build_date: "2020-09-16T23:29:50.742Z"
size_mb: 1721
size: 772349983
sif: "https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/cellprofiler_3.5.1/2020-09-16-09af1a48-c18a43b0/c18a43b08daf857bb9bb6c9920289ffb.simg"
url: https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/cellprofiler_3.5.1/2020-09-16-09af1a48-c18a43b0/
recipe: https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/cellprofiler_3.5.1/2020-09-16-09af1a48-c18a43b0/Singularity
collection: Characterisation-Virtual-Laboratory/CharacterisationVL-Software
---

# Characterisation-Virtual-Laboratory/CharacterisationVL-Software:cellprofiler_3.5.1

```bash
$ singularity pull shub://Characterisation-Virtual-Laboratory/CharacterisationVL-Software:cellprofiler_3.5.1
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
MirrorURL: http://us.archive.ubuntu.com/ubuntu/
OSVersion:  xenial
Include: apt wget sudo vim build-essential git sudo software-properties-common

%labels
MAINTAINER jafar.lie@monash.edu
HARDWARE gpu

%environment
 CELLPROFILERBIN=/opt/CellProfiler/bin
 export PATH=$CELLPROFILERBIN:$PATH

%post -c /bin/bash
 add-apt-repository main
 add-apt-repository universe
 add-apt-repository multiverse
 apt -y update
 apt -y upgrade
 apt -y install \
    build-essential    \
    cython             \
    git                \
    libmysqlclient-dev \
    libhdf5-dev        \
    libxml2-dev        \
    libxslt1-dev       \
    openjdk-8-jdk      \
    python-dev         \
    python-pip         \
    python-h5py        \
    python-matplotlib  \
    python-mysqldb     \
    python-scipy       \
    python-numpy       \
    python-vigra       \
    python-wxgtk3.0    \
    python-zmq
 echo "======================="
 echo "Installing CellProfiler"
 echo "======================="
 mkdir -p /opt/
 cd /opt/
 git clone https://github.com/CellProfiler/CellProfiler.git
 cd CellProfiler
 git checkout master
 sed -i -e 's/1.0.17/1.0.14/g' requirements.txt
 pip --disable-pip-version-check install --editable .
 pip install --upgrade pillow
 pip install javabridge==1.0.14
 
%runscript
    $*
```

## Collection

 - Name: [Characterisation-Virtual-Laboratory/CharacterisationVL-Software](https://github.com/Characterisation-Virtual-Laboratory/CharacterisationVL-Software)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

