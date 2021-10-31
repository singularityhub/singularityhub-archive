---
id: 8094
name: "ebothmann/sherpa-singularity"
branch: "master"
tag: "rivet"
commit: "976252395901707b856624d26c11384f50197918"
version: "6e083f260d6bb060871a25eb64ccb1e2"
build_date: "2019-04-03T14:45:49.561Z"
size_mb: 731
size: 214630431
sif: "https://datasets.datalad.org/shub/ebothmann/sherpa-singularity/rivet/2019-04-03-97625239-6e083f26/6e083f260d6bb060871a25eb64ccb1e2.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ebothmann/sherpa-singularity/rivet/2019-04-03-97625239-6e083f26/
recipe: https://datasets.datalad.org/shub/ebothmann/sherpa-singularity/rivet/2019-04-03-97625239-6e083f26/Singularity
collection: ebothmann/sherpa-singularity
---

# ebothmann/sherpa-singularity:rivet

```bash
$ singularity pull shub://ebothmann/sherpa-singularity:rivet
```

## Singularity Recipe

```singularity
# The following header has been based on instructions in
# https://singularity.lbl.gov/build-docker-module
Bootstrap: docker
From: centos:7

%help
A Singularity recipe based on CentOS 7 to define an image that includes
FastJet, HepMC2, YODA and Rivet. This serves as a base image for both the
Sherpa images and the Plotting image in this repo, since they both depend on
Rivet.


%labels
    Maintainer Enrico Bothmann
    Version v1.0


%environment
    . /usr/local/rivetenv.sh


%runscript
    rivet "$@"


%files
    rivet-bootstrap
    install_Rivet


%post
    echo Installing yum dependencies ...
    yum -y groupinstall "Development Tools"
    yum -y install \
        gsl-devel \
        make \
        openssl-devel \
        python-devel \
        wget \
        which \
        zlib-devel

    echo Bootstrapping Rivet, FastJet, YODA and HepMC
    mkdir -p /scratch/rivet
    cd /scratch/rivet
    mv /rivet-bootstrap .
    chmod +x /install_Rivet
    /install_Rivet
    cd /
    rm -rf /scratch

    echo Clean up
    ldconfig
    yum clean all
```

## Collection

 - Name: [ebothmann/sherpa-singularity](https://github.com/ebothmann/sherpa-singularity)
 - License: None

