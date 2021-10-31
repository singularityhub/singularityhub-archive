---
id: 1100
name: "tin6150/knime"
branch: "withFullExtension"
tag: "latest"
commit: "caca6d9e400e7bf86b8d6d2190a9fd1410c4c552"
version: "1b27206ffa391cc92e8620c194980cdf"
build_date: "2017-12-11T03:00:01.201Z"
size_mb: 5288
size: 4400566303
sif: "https://datasets.datalad.org/shub/tin6150/knime/latest/2017-12-11-caca6d9e-1b27206f/1b27206ffa391cc92e8620c194980cdf.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/tin6150/knime/latest/2017-12-11-caca6d9e-1b27206f/
recipe: https://datasets.datalad.org/shub/tin6150/knime/latest/2017-12-11-caca6d9e-1b27206f/Singularity
collection: tin6150/knime
---

# tin6150/knime:latest

```bash
$ singularity pull shub://tin6150/knime:latest
```

## Singularity Recipe

```singularity
# singularity container definition for
# Knime hosted on ubuntu 

# Knime download require registration and agreement to to EULA.
# This singularity container is for POC.  
# If you use this, please register your at knime.com

# container size is about 1.8 GB
# Knime workspace will default to $HOME, 
# so that need to be bind mounted to writable location.

# the master branch uses the core Knime Analytics Platform
# without the extensions
# the branch "withFullExtension" would have that extension
# and ballon the container to 5308 MB

#BootStrap: debootstrap
#OSVersion: trusty
#MirrorURL: http://us.archive.ubuntu.com/ubuntu/

BootStrap: docker
From: ubuntu:14.04

%runscript
    echo ''
    echo 'To run Knime from a Singularity container, running'
    echo './tin6150-knime-master.img'
    echo 'But if that does not, try:'
    echo 'singularity run -B /run tin6150-knime-master.img'
    echo ''
    echo 'Please go to http://www.knime.com/downloads and complete the registration/EULA when using knime from this Proof of Concept Container. ' 
    echo 'Knime Will start after a brief pause...'
    sleep 3
    echo 'Starting...'
    /opt/knime/knime "$@"
    

%post
    echo "Hello from inside the container"
    #sed -i 's/$/ universe/' /etc/apt/sources.list	## dont remember what this was for
    apt-key update
    apt-get update
    #apt-get -f -y --force-yes install vim ncurses-term less wget curl tar bzip2 coreutils python zlib1g-dev zlib1g libgtk-3-0 libgtk2.0-0 firefox xul-ext-ubufox  libwebkitgtk-3.0-0
    apt-get -f -y --force-yes install vim ncurses-term less wget curl tar bzip2 coreutils python zlib1g-dev zlib1g libgtk-3-0 firefox xul-ext-ubufox  libwebkitgtk-3.0-0
    # https://www.knime.com/faq#q6 about webkit requirements
    # xul-ext-ubufox don't seems to do anything to help
    # gtk-2 was used up to knime 2.9, so should only need gtk-3 for knime 3.x and above
    touch /THIS_IS_INSIDE_SINGULARITY
    cd /opt
    # download knime from a temporary location.
    # after POC, need to work out with Greg Landrum et co on way to download from knime.com and get user registration and agreement.
    #KNIME_VER="knime_3.4.0"
    KNIME_VER="knime-full-latest"
    KNIME_PLAT="linux.gtk.x86_64"
    export KNIME_VER KNIME_PLAT
    KNIME_GZ=tmp.${KNIME_VER}.${KNIME_PLAT}.tar.gz 
    export KNIME_GZ
    # wget -q would be completely quiet.  
    # but -nv reduces output to sing hub enough.
    #test -f $KNIME_GZ || wget --no-verbose https://www.dropbox.com/s/lyzmfu3y6q1x06k/knime_3.4.0.linux.gtk.x86_64.tar.gz?dl=0 -O $KNIME_GZ 
    ## there maybe a docker-ized version of knime.  see 
    ## https://www.knime.com/forum/knime-general/knime-in-docker
    #test -f $KNIME_GZ || wget --no-verbose https://www.knime.com/knime_downloads/linux/knime-full-latest-linux.gtk.x86_64.tar.gz -O $KNIME_GZ 
    # note that full Extension version use -linux, whereas the basic platform w/o extension use .linux in the filename :(
    test -f $KNIME_GZ || wget --no-verbose https://www.knime.com/knime_downloads/linux/${KNIME_VER}-${KNIME_PLAT}.tar.gz -O $KNIME_GZ 
    # 
    tar xzf $KNIME_GZ
    #rm $KNIME_GZ  # 400 MB for version without "all free extension"
    #rm $KNIME_GZ  #   2 GB for full version ie include "all free extension"
    #ln -s $KNIME_VER knime
    ln -s knime[_-]* knime     # hopefully with the renamed KNIME_GZ would work have multiple source matching now
    echo "Goodbye from inside the container"
```

## Collection

 - Name: [tin6150/knime](https://github.com/tin6150/knime)
 - License: None

