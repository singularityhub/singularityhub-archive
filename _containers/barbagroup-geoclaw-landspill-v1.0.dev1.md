---
id: 15258
name: "barbagroup/geoclaw-landspill"
branch: "master"
tag: "v1.0.dev1"
commit: "032e86793becc959bbc65227a6d73cf89e250f86"
version: "d8ca5c73187d2ebe698eb059e26205fe51a48488008749e5359198bd7e68dbd0"
build_date: "2021-01-08T09:44:55.499Z"
size_mb: 151.5625
size: 158924800
sif: "https://datasets.datalad.org/shub/barbagroup/geoclaw-landspill/v1.0.dev1/2021-01-08-032e8679-d8ca5c73/d8ca5c73187d2ebe698eb059e26205fe51a48488008749e5359198bd7e68dbd0.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/barbagroup/geoclaw-landspill/v1.0.dev1/2021-01-08-032e8679-d8ca5c73/
recipe: https://datasets.datalad.org/shub/barbagroup/geoclaw-landspill/v1.0.dev1/2021-01-08-032e8679-d8ca5c73/Singularity
collection: barbagroup/geoclaw-landspill
---

# barbagroup/geoclaw-landspill:v1.0.dev1

```bash
$ singularity pull shub://barbagroup/geoclaw-landspill:v1.0.dev1
```

## Singularity Recipe

```singularity
# multi-stage build: builder
# ==========================
Bootstrap: docker
From: ubuntu:focal
Stage: builder

%environment
    export MPLBACKEND=agg

%post
    # prepare environment
    ln -snf /usr/share/zoneinfo/UTC /etc/localtime
    echo UTC > /etc/timezone
    apt update && apt -y full-upgrade
    apt install -y --no-install-recommends git ca-certificates gfortran python3 python3-pip

    # requires users to provide variable ${VER}
    git clone --branch v1.0.dev1 --recurse-submodules https://github.com/barbagroup/geoclaw-landspill.git

    # install dependencies
    cd /geoclaw-landspill && pip3 install -r requirements-build.txt

    # build binary wheel
    cd /geoclaw-landspill && python3 setup.py bdist_wheel --build-type RELEASE


# multi-stage build: production
# =============================
Bootstrap: docker
From: ubuntu:focal
Stage: production

%labels
    Author Pi-Yueh Chuang (pychuang@gwu.edu)
    Version v1.0.dev1

# copy data from builder
%files from builder
    /geoclaw-landspill/dist /root/dist
    /geoclaw-landspill/cases /root/cases

%post
    # move example to a proper location
    mv /root/cases /opt/geoclaw-landspill-cases 

    # create runtime environment
    ln -snf /usr/share/zoneinfo/UTC /etc/localtime && echo UTC > /etc/timezone
    apt update && apt -y full-upgrade
    apt install -y --no-install-recommends libgfortran5 libgomp1 python3 python3-pip
    rm -rf /var/lib/apt/lists/*

    # install geoclaw-landspill
    echo $(find /root -name "*.whl")
    pip3 install $(find /root -name "*.whl") && rm -rf /root/*

%runscript
    exec geoclaw-landspill $@

%help

    This help only covers the usage of this Singularity image. For the usage of
    geoclaw-landspill package, see https://github.com/barbagroup/geoclaw-landspill

    A Singularity image can be treated as an executable, which is equivalent to
    the executable `geoclaw-landspill` from geoclaw-landspill package. Assuming
    this Singularity image is called "landspill.sif", for example:

        * To run a simulation: `$ landspill.sif run <path to case>`
        * To create a NetCDF file: `$ landspill.sif createnc <path to case>`
        * To create quick depth plots: `$ landspill.sif plotdepth <path to case>`

    Alternatively, users can run these subcommands with, for example,

        * To run a simulation: `$ singularity run landspill.sif run <path to case>`
        * To create a NetCDF file: `$ singularity run landspill.sif createnc <path to case>`
        * To create quick depth plots: `$ singularity run landspill.sif plotdepth <path to case>`
```

## Collection

 - Name: [barbagroup/geoclaw-landspill](https://github.com/barbagroup/geoclaw-landspill)
 - License: [BSD 3-Clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

