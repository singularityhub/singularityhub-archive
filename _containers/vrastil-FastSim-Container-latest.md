---
id: 4907
name: "vrastil/FastSim-Container"
branch: "master"
tag: "latest"
commit: "11863d88e12a65a5c343a738ffac269e2f6e1cf7"
version: "f27829570b8549ccf219c57efd27e5da"
build_date: "2019-07-20T11:58:39.597Z"
size_mb: 1575
size: 688336927
sif: "https://datasets.datalad.org/shub/vrastil/FastSim-Container/latest/2019-07-20-11863d88-f2782957/f27829570b8549ccf219c57efd27e5da.simg"
url: https://datasets.datalad.org/shub/vrastil/FastSim-Container/latest/2019-07-20-11863d88-f2782957/
recipe: https://datasets.datalad.org/shub/vrastil/FastSim-Container/latest/2019-07-20-11863d88-f2782957/Singularity
collection: vrastil/FastSim-Container
---

# vrastil/FastSim-Container:latest

```bash
$ singularity pull shub://vrastil/FastSim-Container:latest
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: vrastil/FastSim-Container-Base

%help
    Contains necessary packages and libraries to build and run FastSim (https://github.com/vrastil/FastSim).

%post
    ###########
    # FastSim #
    ###########
    mkdir /data && cd /data
    git clone https://github.com/vrastil/FastSim.git && cd FastSim
    git submodule update --init --recursive
    mkdir build && cd build
    cmake ..
    make install

    ############
    # Clean-up #
    ############
    ldconfig
    cd /data
    rm -rf *
    apt-get clean
```

## Collection

 - Name: [vrastil/FastSim-Container](https://github.com/vrastil/FastSim-Container)
 - License: None

