---
id: 8757
name: "Characterisation-Virtual-Laboratory/CharacterisationVL-Software"
branch: "master"
tag: "eman_2.3"
commit: "7ba5eb8465ec3b5e7dd6f4e2e1d149f5570ba385"
version: "88afa06c6a7c9064d5af8c367a51f916"
build_date: "2020-09-16T23:50:29.081Z"
size_mb: 11640
size: 5739835423
sif: "https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/eman_2.3/2020-09-16-7ba5eb84-88afa06c/88afa06c6a7c9064d5af8c367a51f916.simg"
url: https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/eman_2.3/2020-09-16-7ba5eb84-88afa06c/
recipe: https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/eman_2.3/2020-09-16-7ba5eb84-88afa06c/Singularity
collection: Characterisation-Virtual-Laboratory/CharacterisationVL-Software
---

# Characterisation-Virtual-Laboratory/CharacterisationVL-Software:eman_2.3

```bash
$ singularity pull shub://Characterisation-Virtual-Laboratory/CharacterisationVL-Software:eman_2.3
```

## Singularity Recipe

```singularity
Bootstrap: shub
From:      Characterisation-Virtual-Laboratory/CharacterisationVL-Software:1804-cuda9

%labels
    MAINTAINER_NAME  Jay van Schyndel
    MAINTAINER_EMAIL jay.vanschyndel@monash.edu

    APPLICATION_NAME ubuntu
    APPLICATION_VERSION 18.04

    HARDWARE GPU

    LAST_UPDATED 01-MAY-2019

%files
    #eman2Install.exp /tmp/
    input.txt /tmp/

%environment
    export PATH=/opt/eman/bin:$PATH
    export CONDA_SHLVL=1
    export CONDA_EXE=/opt/eman/bin/conda
    export CONDA_PREFIX=/opt/eman
    export CONDA_PYTHON_EXE=/opt/eman/bin/python
    #export CONDA_PROMPT_MODIFIER=(base)
    export CONDA_DEFAULT_ENV=base
 
%post
    echo "*********************************************************"
    echo "Setup and display environment"
    echo "*********************************************************"
    export LC_ALL=en_AU.UTF-8
    export LANGUAGE=en_AU.UTF-8
    export DEBIAN_FRONTEND=noninteractive
    echo $LC_ALL
    echo $LANGUAGE
    echo $DEBIAN_FRONTEND
    echo "*********************************************************"
    echo "Install repositories"
    echo "*********************************************************"
    apt-get install -y software-properties-common
    apt-add-repository -y 'deb http://us.archive.ubuntu.com/ubuntu/ bionic main restricted'
    apt-add-repository -y 'deb http://us.archive.ubuntu.com/ubuntu/ bionic-updates main restricted'
    apt-add-repository -y 'deb http://us.archive.ubuntu.com/ubuntu/ bionic universe'
    apt-add-repository -y 'deb http://us.archive.ubuntu.com/ubuntu/ bionic-updates universe'
    echo "*********************************************************"
    echo "Update repositories and install desktop"
    echo "*********************************************************"
    apt update
    apt upgrade -y
    apt install -y locales
    locale-gen en_AU.UTF-8

    echo "================================"
    echo "Downloading EMAN 2.3            "
    echo "================================"
    cd /tmp
    wget https://cryoem.bcm.edu/cryoem/static/software/release-2.3/eman2.3.linux64.sh
    chmod u+x eman2.3.linux64.sh

    echo "================================"
    echo "Installing EMAN 2.3             "
    echo "================================"
    export PATH=/opt/eman/bin:$PATH
    #expect eman2Install.exp
    cat input.txt | bash eman2.3.linux64.sh    

%runscript
    $*
```

## Collection

 - Name: [Characterisation-Virtual-Laboratory/CharacterisationVL-Software](https://github.com/Characterisation-Virtual-Laboratory/CharacterisationVL-Software)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

