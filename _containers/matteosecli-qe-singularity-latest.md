---
id: 408
name: "matteosecli/qe-singularity"
branch: "master"
tag: "latest"
commit: "f0515b9a462de5b703c968d506a03246cd93a23c"
version: "3ead5e18e79d1b974c7da2beec2c16ab"
build_date: "2021-03-29T09:43:36.722Z"
size_mb: 528
size: 189165599
sif: "https://datasets.datalad.org/shub/matteosecli/qe-singularity/latest/2021-03-29-f0515b9a-3ead5e18/3ead5e18e79d1b974c7da2beec2c16ab.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/matteosecli/qe-singularity/latest/2021-03-29-f0515b9a-3ead5e18/
recipe: https://datasets.datalad.org/shub/matteosecli/qe-singularity/latest/2021-03-29-f0515b9a-3ead5e18/Singularity
collection: matteosecli/qe-singularity
---

# matteosecli/qe-singularity:latest

```bash
$ singularity pull shub://matteosecli/qe-singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

## Bootstrapping from Docker is faster, but if you want
## to install a vanilla Ubuntu decomment these lines
#    BootStrap: debootstrap
#    OSVersion: xenial
#    MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%labels
    MAINTAINER secli.matteo@gmail.com
    VERSION 0.2.1

%runscript
    exec runhelper "$@"

%setup
    # Copy into the container the runhelper script and the QE package 
        cp runhelper $SINGULARITY_ROOTFS/usr/bin/runhelper
        cp quantum-espresso* $SINGULARITY_ROOTFS/home/

%post
    # Turn off apt messages
        export DEBIAN_FRONTEND=noninteractive
    # Create a qe user
        echo "Creating qe user..."
        useradd -m -s /bin/bash qe
        passwd -d qe
    # Install QE dependencies and some utils
        echo "Installing Quantum ESPRESSO and dependencies..."
	echo "deb http://ppa.launchpad.net/ubuntu-toolchain-r/test/ubuntu xenial main" \
        > /etc/apt/sources.list.d/ubuntu-toolchain-r-ubuntu-test-xenial.list
        apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 1E9377A2BA9EF27F
        apt-get -y -qq update
        apt-get -y -qq install wget jq libgfortran3 liblapack3 libblas3 libfftw3-3 openmpi-bin
        apt-get -y -qq clean
    # Give the right permissions to the runhelper script
        chmod +x /usr/bin/runhelper
    # Install some examples (TODO: move to GitHub!)
        cd /home/qe
        wget -q http://people.sissa.it/~inno/qe/qe.tgz && tar xvzf qe.tgz && rm pw.x qe.tgz
    # Install the actual QE package
        dpkg -i /home/quantum-espresso*
        rm /home/quantum-espresso*
    # Fix possible problems
        apt-get -y -qq install -f
        apt-get -y -qq clean
    # Print a help message
        echo "To run, ./qe.img pw.x -in relax.in"

%test
    # Run the built-in test and remove the resulting files
        echo "Running a simple test..."
        cd /home/qe
        pw.x -in relax.in
        rm -r pwscf.save pwscf.wfc1
```

## Collection

 - Name: [matteosecli/qe-singularity](https://github.com/matteosecli/qe-singularity)
 - License: None

