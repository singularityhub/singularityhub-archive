---
id: 9891
name: "fredjaya/rec-bench"
branch: "feature/simg-hyphy"
tag: "hyphy"
commit: "76fb66f0c101e8d6d0a4e8b36bec58d468e380e5"
version: "ce1bea08e2c95b77633cae76454c5d6e"
build_date: "2019-06-27T08:32:44.511Z"
size_mb: 1636
size: 501895199
sif: "https://datasets.datalad.org/shub/fredjaya/rec-bench/hyphy/2019-06-27-76fb66f0-ce1bea08/ce1bea08e2c95b77633cae76454c5d6e.simg"
url: https://datasets.datalad.org/shub/fredjaya/rec-bench/hyphy/2019-06-27-76fb66f0-ce1bea08/
recipe: https://datasets.datalad.org/shub/fredjaya/rec-bench/hyphy/2019-06-27-76fb66f0-ce1bea08/Singularity
collection: fredjaya/rec-bench
---

# fredjaya/rec-bench:hyphy

```bash
$ singularity pull shub://fredjaya/rec-bench:hyphy
```

## Singularity Recipe

```singularity
BootStrap: shub
From: shub://fredjaya/rec-bench:base@digest

%post
    yum -y install scl-utils-build devtoolset-6 git
    scl enable devtoolset-6 bash
    cd /usr/src

    # Add cmake
    wget https://github.com/Kitware/CMake/releases/download/v3.15.0-rc1/cmake-3.15.0-rc1.tar.gz
    tar -zxvf cmake-3.15.0-rc1.tar.gz
    rm -rf cmake-3.15.0-rc1.tar.gz
    cd cmake-3.15.0-rc1
    ./bootstrap
    make
    make install

    # Add hyphy
    cd /usr/src
    git clone https://github.com/veg/hyphy.git
    cd hyphy
    cmake .
    # make executable
    make MP

%environment
    export PATH=/usr/src/hyphy/:$PATH

#%test
#    git --version
#    HYPHYMP
```

## Collection

 - Name: [fredjaya/rec-bench](https://github.com/fredjaya/rec-bench)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

