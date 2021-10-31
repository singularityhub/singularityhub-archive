---
id: 7043
name: "murphygroup/singularity-cellorganizer"
branch: "master"
tag: "latest"
commit: "1eff0e0b20eb2a35b5b074bc77a64066c7453fe7"
version: "15b59914e7635aafe916142a8b2a9224"
build_date: "2019-06-18T22:56:15.755Z"
size_mb: 5677
size: 2766250015
sif: "https://datasets.datalad.org/shub/murphygroup/singularity-cellorganizer/latest/2019-06-18-1eff0e0b-15b59914/15b59914e7635aafe916142a8b2a9224.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/murphygroup/singularity-cellorganizer/latest/2019-06-18-1eff0e0b-15b59914/
recipe: https://datasets.datalad.org/shub/murphygroup/singularity-cellorganizer/latest/2019-06-18-1eff0e0b-15b59914/Singularity
collection: murphygroup/singularity-cellorganizer
---

# murphygroup/singularity-cellorganizer:latest

```bash
$ singularity pull shub://murphygroup/singularity-cellorganizer:latest
```

## Singularity Recipe

```singularity
Bootstrap:shub
From:murphygroup/singularity-matlabmcr2018b

IncludeCmd: yes

%runscript
    exec /bin/bash "$@"
%post
    echo "Configuring Environment for User" 

    echo "Create folders"
    # Make folders for CBD HPC cluster
    if [ ! -d /images ]; then mkdir /images; fi
    if [ ! -d /projects ]; then mkdir /projects; fi
    if [ ! -d /share ]; then mkdir /share; fi
    if [ ! -d /scratch ]; then mkdir /scratch; fi
 
    echo "Download binaries"
    cd /home/murphylab && \
    wget -nc --quiet http://www.cellorganizer.org/Downloads/v2.8.1/docker/cellorganizer-binaries-matlabmcr2018b.tgz && \
    tar -xvf cellorganizer-binaries-matlabmcr2018b.tgz && \
    rm cellorganizer-binaries-matlabmcr2018b.tgz   
 
    mv cellorganizer-binaries/ /opt/ && \
    chmod +x /opt/cellorganizer-binaries/img2slml && \
    chmod +x /opt/cellorganizer-binaries/slml2img && \
    chmod +x /opt/cellorganizer-binaries/slml2report && \
    chmod +x /opt/cellorganizer-binaries/slml2info && \
    chmod +x /opt/cellorganizer-binaries/slml2slml && \

    ln -s /opt/cellorganizer-binaries/img2slml /usr/local/bin/img2slml && \
    ln -s /opt/cellorganizer-binaries/slml2img /usr/local/bin/slml2img && \
    ln -s /opt/cellorganizer-binaries/slml2report /usr/local/bin/slml2report && \
    ln -s /opt/cellorganizer-binaries/slml2info /usr/local/bin/slml2info && \
    ln -s /opt/cellorganizer-binaries/slml2slml /usr/local/bin/slml2slml

    mv /opt/mcr/v95/bin/glnxa64/libexpat.so.1 /opt/mcr/v95/bin/glnxa64/libexpat.so.1.backup
    mv /opt/mcr/v95/bin/glnxa64/libexpat.so.1.5.0 /opt/mcr/v95/bin/glnxa64/libexpat.so.1.5.0.backup
    mv /opt/mcr/v95/bin/glnxa64/libcrypto.so.1.0.0 /opt/mcr/v95/bin/glnxa64/libcrypto.so.1.0.0.backup
    mv /opt/mcr/v95/bin/glnxa64/libssl.so.1.0.0 /opt/mcr/v95/bin/glnxa64/libssl.so.1.0.0.backup

    echo "Installing Update Notebook Script"
    mkdir /opt/cellorganizer-scripts
    cat >> /opt/cellorganizer-scripts/update.sh <<- EOF
	#!/bin/bash
	url='http://www.cellorganizer.org/Downloads/v2.8.0/singularity/scripts.tgz'
	wget -nc --quiet -O scripts.tgz \$url
	tar -xvkf scripts.tgz
	rm -rf scripts.tgz
	EOF

    cat >> /opt/cellorganizer-scripts/get_images.sh <<- EOF
	#!/bin/bash
	FILE='.succesfully_downloaded_images'
	if [ ! -f "\$FILE" ]; then
		url='http://murphylab.web.cmu.edu/data/Hela/3D/multitiff/cellorganizer_full_image_collection.zip'
		DIRECTORY='images'
	    if [ ! -d "\$DIRECTORY" ]; then
	        mkdir images && cd images
	    else
	        cd images
	    fi
	    wget -O image_set.zip \$url
	    unzip image_set.zip
	    rm -rf image_set.zip
	    touch ../.succesfully_downloaded_images
	else
	    echo 'Images already downloaded.'
	fi
	EOF
	

    echo "Installing Download Demos Scripts"
	cd /home/murphylab
    mkdir /opt/cellorganizer-demos
	url='http://www.cellorganizer.org/Downloads/v2.8.0/singularity/demos.tgz'
	wget -O demo_set.tgz $url && tar xvf demo_set.tgz -C /opt/cellorganizer-demos 
	rm -rf demo_set.tgz
	

######img2slml############
%appenv img2slml
    cell_app=/opt/cellorganizer-binaries/img2slml/
    export cell_app

%apphelp img2slml
    exec echo "Running app img2slml"

%apprun img2slml
    exec /bin/bash "$@"

######slml2img############
%appenv slml2img
    cell_app=/opt/cellorganizer-binaries/slml2img
    export cell_app

%apphelp slml2img
    exec echo "Running app slml2img"

%apprun slml2img
    exec /bin/bash "$@"

######slml2report############
%appenv slml2report
    cell_app=/opt/cellorganizer-binaries/slml2report
    export cell_app

%apphelp slml2report
    exec echo "Running app slml2report"

%apprun slml2report
    exec /bin/bash "$@"

######slml2info############
%appenv slml2info
    cell_app=s/opt/cellorganizer-binaries/lml2info
    export cell_app

%apphelp slml2info
    exec echo "Running app slml2info"

%apprun slml2info
    exec /bin/bash "$@"

######slml2slml############
%appenv slml2slml
    cell_app=/opt/cellorganizer-binaries/slml2slml
    export cell_app

%apphelp slml2slml
    exec echo "Running app slml2slml"

%apprun slml2slml
    exec /bin/bash "$@"
```

## Collection

 - Name: [murphygroup/singularity-cellorganizer](https://github.com/murphygroup/singularity-cellorganizer)
 - License: [GNU Lesser General Public License v3.0](https://api.github.com/licenses/lgpl-3.0)

