---
id: 7020
name: "murphygroup/singularity-matlabmcr2017a"
branch: "master"
tag: "latest"
commit: "8c346de1e0fa84d6b022e9df6b20d56e2b2b1bb6"
version: "58857c7dd7907db8625f2812c3078e50"
build_date: "2019-02-08T05:38:46.697Z"
size_mb: 3604
size: 1479090207
sif: "https://datasets.datalad.org/shub/murphygroup/singularity-matlabmcr2017a/latest/2019-02-08-8c346de1-58857c7d/58857c7dd7907db8625f2812c3078e50.simg"
url: https://datasets.datalad.org/shub/murphygroup/singularity-matlabmcr2017a/latest/2019-02-08-8c346de1-58857c7d/
recipe: https://datasets.datalad.org/shub/murphygroup/singularity-matlabmcr2017a/latest/2019-02-08-8c346de1-58857c7d/Singularity
collection: murphygroup/singularity-matlabmcr2017a
---

# murphygroup/singularity-matlabmcr2017a:latest

```bash
$ singularity pull shub://murphygroup/singularity-matlabmcr2017a:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

IncludeCmd: yes

%runscript
    exec /bin/bash "$@"

%post
    echo "Update aptitude"
    /usr/bin/apt-get update && apt-get install -y --no-install-recommends apt-utils
    /usr/bin/apt-get -y upgrade
    /usr/bin/apt-get update --fix-missing
    /usr/bin/apt-get --assume-yes install libxext-dev
    /usr/bin/apt-get install -y build-essential git \
        unzip \
		xorg \
		wget \
		tree \
		pandoc \
		curl \
		vim
	
    echo "Downloading Matlab MCR 2017a"
    mkdir /mcr-install && \
    mkdir /opt/mcr
    cd /mcr-install && \
    wget -nc http://ssd.mathworks.com/supportfiles/downloads/R2017a/deployment_files/R2017a/installers/glnxa64/MCR_R2017a_glnxa64_installer.zip && \
    cd /mcr-install && \
    echo "Unzipping container" && \
    unzip -q MCR_R2017a_glnxa64_installer.zip && \
    ./install -destinationFolder /opt/mcr -agreeToLicense yes -mode silent && \
    cd / && \
    echo "Removing temporary files" && \
    rm -rvf mcr-install
    
    echo "Configuring Environment for MCR"
    mv -v /opt/mcr/v92/sys/os/glnxa64/libstdc++.so.6 /opt/mcr/v92/sys/os/glnxa64/libstdc++.so.6.old
    echo 'export LD_LIBRARY_PATH=/opt/mcr/v92/runtime/glnxa64:/opt/mcr/v92/bin/glnxa64:/opt/mcr/v92/sys/os/glnxa64' >>$SINGULARITY_ENVIRONMENT
    echo 'export XAPPLRESDIR=/opt/mcr/v92/X11/app-defaults' >>$SINGULARITY_ENVIRONMENT
	
    echo "Configuring Environment for User" 
    USERNAME=murphylab
    UID=1000
    useradd -m -s /bin/bash -N -u $UID $USERNAME
    if [ ! -d /home/$USERNAME/ ]; then mkdir /home/$USERNAME/; fi
```

## Collection

 - Name: [murphygroup/singularity-matlabmcr2017a](https://github.com/murphygroup/singularity-matlabmcr2017a)
 - License: None

