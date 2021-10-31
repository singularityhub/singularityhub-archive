---
id: 9207
name: "netcatninja/cookbook"
branch: "master"
tag: "test"
commit: "dbf77ee825bcd0c6d5f7d1ce70a5f44d9fba3d47"
version: "2bd9363486c5527ee66252cc4e93c8d2"
build_date: "2019-05-22T09:03:51.221Z"
size_mb: 785
size: 350232607
sif: "https://datasets.datalad.org/shub/netcatninja/cookbook/test/2019-05-22-dbf77ee8-2bd93634/2bd9363486c5527ee66252cc4e93c8d2.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/netcatninja/cookbook/test/2019-05-22-dbf77ee8-2bd93634/
recipe: https://datasets.datalad.org/shub/netcatninja/cookbook/test/2019-05-22-dbf77ee8-2bd93634/Singularity
collection: netcatninja/cookbook
---

# netcatninja/cookbook:test

```bash
$ singularity pull shub://netcatninja/cookbook:test
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: bionic
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%runscript
    echo "I am a test container."
    echo "Run singularity test -B /scratch image.sif for more."

%post
    sed -i 's/$/ universe/' /etc/apt/sources.list
    mkdir /projects /scratch
    apt-get -y update
    apt-get -y install curl emacs git htop less man python wget

%test
    echo "Testing Python..."  ## Test that Python exists on the $PATH
    python -V > /dev/null 2>&1
    if [ $? -eq 0 ]; then
        printf "\033[1;31mPython: OK\033[0m\n"
    else
        printf "\033[1;33mPython: ERROR\033[0m\n"
    fi

#    echo "Testing nvidia-smi..."  ## Test that nvidia-smi works on the $PATH
#    nvidia-smi > /dev/null 2>&1   
#    if [ $? -eq 0 ] ; then
#        printf "\033[1;31mRunning nvidia-smi: OK\033[0m\n"
#    else
#        printf "\033[1;33mRunning nvidia-smi: ERROR\033[0m\n"
#    fi

    echo "Testing /scratch..."
    fname=$(mktemp -p /scratch)  && date >> $fname  && rm $fname
    if [ $? -eq 0 ]; then
        printf "\033[1;31mWriting to /scratch: OK\033[0m\n"
    else
        printf "\033[1;33mWriting to /scratch: ERROR\033[0m\n"
        printf "\033[1;33m(Make sure you include '-B /scratch'\033[0m\n"
    fi

%labels
    Version v0.0.1

%help
    This is a test container used to confirm that Singularity installations are working properly.
```

## Collection

 - Name: [netcatninja/cookbook](https://github.com/netcatninja/cookbook)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

