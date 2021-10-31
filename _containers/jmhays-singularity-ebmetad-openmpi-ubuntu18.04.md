---
id: 5832
name: "jmhays/singularity-ebmetad"
branch: "master"
tag: "openmpi-ubuntu18.04"
commit: "6705324b4bcae42181931eeb5d94973f767c0b45"
version: "8bc3c010657abc1d4e8f1974a890031d"
build_date: "2018-12-09T13:14:42.970Z"
size_mb: 971
size: 267091999
sif: "https://datasets.datalad.org/shub/jmhays/singularity-ebmetad/openmpi-ubuntu18.04/2018-12-09-6705324b-8bc3c010/8bc3c010657abc1d4e8f1974a890031d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jmhays/singularity-ebmetad/openmpi-ubuntu18.04/2018-12-09-6705324b-8bc3c010/
recipe: https://datasets.datalad.org/shub/jmhays/singularity-ebmetad/openmpi-ubuntu18.04/2018-12-09-6705324b-8bc3c010/Singularity
collection: jmhays/singularity-ebmetad
---

# jmhays/singularity-ebmetad:openmpi-ubuntu18.04

```bash
$ singularity pull shub://jmhays/singularity-ebmetad:openmpi-ubuntu18.04
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04


%files

    md_meta_EBMetaD/ 	/opt


%environment

    plumedir=/builds/md_meta_EBMetaD
    PATH=/usr/local/gromacs/bin:${PATH}

    export plumedir PATH


%labels

   AUTHOR jmh5sf@virginia.edu


%post

    apt-get update && apt-get -y install wget libopenmpi-dev gcc g++ libfftw3-dev make patch

    mkdir /builds
    cd /builds
    mv /opt/md_meta_EBMetaD /builds

    # Get gromacs 4.5.1
    wget ftp://ftp.gromacs.org/pub/gromacs/gromacs-4.5.1.tar.gz
    tar xf gromacs-4.5.1.tar.gz
    cd gromacs-4.5.1
    ./configure --enable-mpi

    # Patch with plumed
    export plumedir=/builds/md_meta_EBMetaD
    cp ${plumedir}/patches/plumedpatch_gromacs_4.5.1.sh .
    bash plumedpatch_gromacs_4.5.1.sh -patch

    # Now make
    make -j8; make install
```

## Collection

 - Name: [jmhays/singularity-ebmetad](https://github.com/jmhays/singularity-ebmetad)
 - License: [BSD 3-Clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

