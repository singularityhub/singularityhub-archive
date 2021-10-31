---
id: 545
name: "pegasus-isi/fedora-montage"
branch: "master"
tag: "latest"
commit: "bf336943b63825fc45cc445518f9c8e64062732e"
version: "413bec6436f37055f48fc7395a7b59b9"
build_date: "2018-03-06T21:27:45.503Z"
size_mb: 1730
size: 457228319
sif: "https://datasets.datalad.org/shub/pegasus-isi/fedora-montage/latest/2018-03-06-bf336943-413bec64/413bec6436f37055f48fc7395a7b59b9.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/pegasus-isi/fedora-montage/latest/2018-03-06-bf336943-413bec64/
recipe: https://datasets.datalad.org/shub/pegasus-isi/fedora-montage/latest/2018-03-06-bf336943-413bec64/Singularity
collection: pegasus-isi/fedora-montage
---

# pegasus-isi/fedora-montage:latest

```bash
$ singularity pull shub://pegasus-isi/fedora-montage:latest
```

## Singularity Recipe

```singularity
bootstrap: docker
From:      fedora:latest

%post

yum upgrade -y

yum groupinstall -y \
    "Development Tools" \
    "Development Libraries"

yum install -y \
    curl \
    gcc-gfortran \
    pkg-config \
    python2 \
    python2-astropy \
    python2-devel \
    unzip \
    vim \
    wget

yum clean all

cd /opt && \
    wget -nv https://github.com/Caltech-IPAC/Montage/archive/dev.zip && \
    unzip dev.zip && \
    rm -f dev.zip && \
    mv Montage-dev Montage && \
    cd Montage && \
    make
```

## Collection

 - Name: [pegasus-isi/fedora-montage](https://github.com/pegasus-isi/fedora-montage)
 - License: None

