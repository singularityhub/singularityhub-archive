---
id: 9093
name: "HenryDayHall/HiggsPhenoSingularity"
branch: "master"
tag: "higgspheno"
commit: "ebeb66a3389e37e3c2f631346a1a124633035f21"
version: "b3a2fd71b9b2dae098967b40079fe7fe"
build_date: "2019-05-23T03:52:52.876Z"
size_mb: 393
size: 139497503
sif: "https://datasets.datalad.org/shub/HenryDayHall/HiggsPhenoSingularity/higgspheno/2019-05-23-ebeb66a3-b3a2fd71/b3a2fd71b9b2dae098967b40079fe7fe.simg"
url: https://datasets.datalad.org/shub/HenryDayHall/HiggsPhenoSingularity/higgspheno/2019-05-23-ebeb66a3-b3a2fd71/
recipe: https://datasets.datalad.org/shub/HenryDayHall/HiggsPhenoSingularity/higgspheno/2019-05-23-ebeb66a3-b3a2fd71/Singularity
collection: HenryDayHall/HiggsPhenoSingularity
---

# HenryDayHall/HiggsPhenoSingularity:higgspheno

```bash
$ singularity pull shub://HenryDayHall/HiggsPhenoSingularity:higgspheno
```

## Singularity Recipe

```singularity
####
# to build me
# sudo singularity build higgsPheno.sif higgsPheno.def
####
# to run me do
# singularity run --containall --bind /my/out/dir/ higgsPheno.sif
#     the "--containall" flag prevents interactions with your system
#     the "--bind /my/out/dir/" mounts a directory in your system
#     this allows scripts in that directory to be accessed from the image
#     and results from the image to persist in the directory
#     It also allows the run script to call .bashrc

BootStrap: docker
From: ubuntu:18.04
    
# commands on the host system
%setup
    # make print colour #
    GREEN='\033[0;32m'
    NOCOLOUR='\033[0m'
    echo "${GREEN}~~~ Getting modified packages from github ~~~ ${NOCOLOUR}"
    export PACKAGES_TMP=/tmp/packages
    rm -fr $PACKAGES_TMP
    mkdir -p $PACKAGES_TMP
    git clone https://github.com/HenryDayHall/higgsPhenoPackages.git $PACKAGES_TMP
    cp -R ${PACKAGES_TMP} ${SINGULARITY_ROOTFS}

# get files from the host (but we dont need any)
%files
    /home/henry/Programs/singularity_conts/higgsPheno/host_test a
    /home/henry/Programs/singularity_conts/higgsPheno/host_test_file b

# what is done when the container is built
%post
    # make print colour #
    GREEN='\033[0;32m'
    NOCOLOUR='\033[0m'
    # start
    echo "${GREEN}~~~ install apt packages ~~~ ${NOCOLOUR}"
    apt -y update
    # for scripts
    apt -y install python2.7
    # for fetching from repos if needed
    apt -y install git
    # for getting anything else from the net
    apt -y install wget
    # text editors
    apt -y install vim-tiny
    apt -y install nano
    # for making downloaded packages
    apt -y install make
    # for compiling 2HDMC
    apt -y install libgsl-dev
    apt -y install g++

    echo "${GREEN}~~~ Set up a .bashrc ~~~ ${NOCOLOUR}"
    BASHRC=/home/.bashrc
    touch $BASHRC
    echo "alias vim=vim.tiny\n" >> $BASHRC
    echo "alias python=python2.7\n" >> $BASHRC
    # will be called in run

    ## Not working???
    ## the /home/ directory appears empty
    # echo "${GREEN}~~~ Move packages to home dir ~~~ ${NOCOLOUR}"
    MY_HOME=$(ls -l /home/)
    echo in post home is $MY_HOME
    echo $USER
    # PACKAGES=$MY_HOME/packages/
    # mv /packages $PACKAGES
    
    #echo "${GREEN}~~~ Give the user permission and control ~~~ ${NOCOLOUR}"
    PACKAGES=/packages
    #chown -R $USER $PACKAGES
    #chmod -R 766 $PACKAGES
    echo "${GREEN}~~~ Making the packages ~~~ ${NOCOLOUR}"
    echo "${GREEN}~~~ 2HDMC ~~~ ${NOCOLOUR}"
    cd $PACKAGES/2HDMC
    # for some reason the lib dir is not automaticaly constructed
    mkdir lib
    make


# enviroment variabels instide the container
# sourced at run time not build time
%environment
    export PACKAGES=/packages/
    export BASHRC=/home/.bashrc


# this is executed when the contain is launched with
# singularity run higgsPheno.sif
%runscript
    # make print colour #
    GREEN='\033[0;32m'
    NOCOLOUR='\033[0m'
    cp -r /packages/* ~/
    echo "${GREEN}Test me with" 
    echo "\$ cd 2HDMC"
    echo "\$ make test2HDMC"
    echo "\$ ./test2HDMC ${NOCOLOUR}"
    /bin/bash --rcfile $BASHRC
    

# this would be executed just after build
%test
    echo I havent written any tests
    MY_HOME=$(ls -l /home/)
    echo in test home is $MY_HOME
    echo $USER

# metadata
%labels
    Author HenryDayHall
    Version v1.0

%help
    to build me
    > sudo singularity build higgsPheno.sif higgsPheno.def
    to run me do
    > singularity run --containall --bind /my/out/dir/ higgsPheno.sif
        the "--containall" flag prevents interactions with your system
        the "--bind /my/out/dir/" mounts a directory in your system
        this allows scripts in that directory to be accessed from the image
        and results from the image to persist in the directory
        It also allows the run script to call .bashrc
```

## Collection

 - Name: [HenryDayHall/HiggsPhenoSingularity](https://github.com/HenryDayHall/HiggsPhenoSingularity)
 - License: None

