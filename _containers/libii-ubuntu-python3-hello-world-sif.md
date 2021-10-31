---
id: 13887
name: "libii/ubuntu-python3-hello-world"
branch: "master"
tag: "sif"
commit: "78ddce0b07a4b97438db7131e2fe4a065593244f"
version: "None"
build_date: "2020-08-07T05:53:59.815Z"
size_mb: None
size: 83890176
sif: "https://datasets.datalad.org/shub/libii/ubuntu-python3-hello-world/sif/2020-08-07-78ddce0b-b2ada075/b2ada075ac72709233f724bb002b8759211ca33a01fe624ccd750b07006671d1.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/libii/ubuntu-python3-hello-world/sif/2020-08-07-78ddce0b-b2ada075/
recipe: https://github.com/libii/ubuntu-python3-hello-world/blob/master/Singularity
collection: libii/ubuntu-python3-hello-world
---

# libii/ubuntu-python3-hello-world:sif

```bash
$ singularity pull shub://libii/ubuntu-python3-hello-world:sif
```

## Singularity Recipe

```singularity
From: ubuntu

%help
    #comments/helpful hints
    Test Singularity Container with a Hello World Python Script

%labels
    #metadata within container
    Creator Liberty

%environment
    #export MY_VAR=’~~~~  This is my environment variable ~~~~’

%files
    #allows us to copy files into our container
    #FILE_NAME DIRECTOR
    helloWorld.py /
    #

    helloWorld.py ~/

%test
grep -q NAME=\"Ubuntu\" /etc/os-release
    if [ $? -eq 0 ]; then
        echo "Container base is Ubuntu as expected."
    else
        echo "Container base is not Ubuntu."
    fi

%post
    #add packages
    sed -i 's/security/old-releases/g' /etc/apt/sources.list && \
    sed -i 's/archive/old-releases/g' /etc/apt/sources.list && \
    sed -i 's/cosmic-old-releases/cosmic/g' /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -y vim && \
    apt-get install -y python3

%runscript
    #echo "Container was created $NOW"
    #cat /etc/lsb-release
    python ~/helloWorld.py
```
