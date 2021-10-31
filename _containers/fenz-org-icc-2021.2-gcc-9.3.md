---
id: 15889
name: "fenz-org/icc"
branch: "master"
tag: "2021.2-gcc-9.3"
commit: "cc43d5bb376c09536deb0319baa83e289a005151"
version: "e1190fab455f9ee2905320a30458f4dc0edeb31bff17eae3121613ebe4dcaf73"
build_date: "2021-04-11T23:15:02.723Z"
size_mb: 1214.93359375
size: 1273950208
sif: "https://datasets.datalad.org/shub/fenz-org/icc/2021.2-gcc-9.3/2021-04-11-cc43d5bb-e1190fab/e1190fab455f9ee2905320a30458f4dc0edeb31bff17eae3121613ebe4dcaf73.sif"
url: https://datasets.datalad.org/shub/fenz-org/icc/2021.2-gcc-9.3/2021-04-11-cc43d5bb-e1190fab/
recipe: https://datasets.datalad.org/shub/fenz-org/icc/2021.2-gcc-9.3/2021-04-11-cc43d5bb-e1190fab/Singularity
collection: fenz-org/icc
---

# fenz-org/icc:2021.2-gcc-9.3

```bash
$ singularity pull shub://fenz-org/icc:2021.2-gcc-9.3
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:20.04

%post
    export DEBIAN_FRONTEND=noninteractive
    export APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE=1
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
    export LANGUAGE=C.UTF-8

    # install OS tools
    apt-get update -y && \
    apt-get install -y --no-install-recommends -o=Dpkg::Use-Pty=0 \
        build-essential \
        pkg-config \
        ca-certificates \
        gnupg \
        curl \
        libarchive13

    export cmake_url=https://github.com/Kitware/CMake/releases/download/v3.20.0/cmake-3.20.0-linux-x86_64.sh
    cd / && curl -LO $cmake_url
    file=$(basename "$cmake_url")
    bash $file --prefix=/usr --skip-license
    rm $file

    # add apt repo public key
    export url=https://apt.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS-2023.PUB
    cd / && curl -LO $url
    file=$(basename "$url")
    apt-key add "$file"
    rm "$file"

    # configure the repository
    export repo=https://apt.repos.intel.com/oneapi
    echo "deb $repo all main" > /etc/apt/sources.list.d/oneAPI.list

    apt-get update -y && \
    apt-get install -y --no-install-recommends -o=Dpkg::Use-Pty=0 \
        intel-oneapi-compiler-dpcpp-cpp-and-cpp-classic
    apt-get clean
    rm -rf /var/lib/apt/lists/*

%environment
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
    export LANGUAGE=C.UTF-8
    # setvars.sh environment variables
    export CMAKE_PREFIX_PATH='/opt/intel/oneapi/tbb/2021.2.0/env/..:'
    export CPATH='/opt/intel/oneapi/tbb/2021.2.0/env/../include:/opt/intel/oneapi/dev-utilities/2021.2.0/include:/opt/intel/oneapi/compiler/2021.2.0/linux/include'
    export INFOPATH='/opt/intel/oneapi/debugger/10.1.1/documentation/info/'
    export INTELFPGAOCLSDKROOT='/opt/intel/oneapi/compiler/2021.2.0/linux/lib/oclfpga'
    export INTEL_PYTHONHOME='/opt/intel/oneapi/debugger/10.1.1/dep'
    export LD_LIBRARY_PATH='/opt/intel/oneapi/tbb/2021.2.0/env/../lib/intel64/gcc4.8:/opt/intel/oneapi/debugger/10.1.1/dep/lib:/opt/intel/oneapi/debugger/10.1.1/libipt/intel64/lib:/opt/intel/oneapi/debugger/10.1.1/gdb/intel64/lib:/opt/intel/oneapi/compiler/2021.2.0/linux/lib:/opt/intel/oneapi/compiler/2021.2.0/linux/lib/x64:/opt/intel/oneapi/compiler/2021.2.0/linux/lib/emu:/opt/intel/oneapi/compiler/2021.2.0/linux/lib/oclfpga/host/linux64/lib:/opt/intel/oneapi/compiler/2021.2.0/linux/lib/oclfpga/linux64/lib:/opt/intel/oneapi/compiler/2021.2.0/linux/compiler/lib/intel64_lin:/opt/intel/oneapi/compiler/2021.2.0/linux/compiler/lib'
    export LIBRARY_PATH='/opt/intel/oneapi/tbb/2021.2.0/env/../lib/intel64/gcc4.8:/opt/intel/oneapi/compiler/2021.2.0/linux/compiler/lib/intel64_lin:/opt/intel/oneapi/compiler/2021.2.0/linux/lib'
    export MANPATH='/opt/intel/oneapi/debugger/10.1.1/documentation/man:/opt/intel/oneapi/compiler/2021.2.0/documentation/en/man/common'
    export OCL_ICD_FILENAMES='libintelocl_emu.so:libalteracl.so:/opt/intel/oneapi/compiler/2021.2.0/linux/lib/x64/libintelocl.so'
    export ONEAPI_ROOT='/opt/intel/oneapi'
    export PATH=/opt/intel/oneapi/dev-utilities/2021.2.0/bin:/opt/intel/oneapi/debugger/10.1.1/gdb/intel64/bin:/opt/intel/oneapi/compiler/2021.2.0/linux/lib/oclfpga/llvm/aocl-bin:/opt/intel/oneapi/compiler/2021.2.0/linux/lib/oclfpga/bin:/opt/intel/oneapi/compiler/2021.2.0/linux/bin/intel64:/opt/intel/oneapi/compiler/2021.2.0/linux/bin:/opt/intel/oneapi/compiler/2021.2.0/linux/ioc/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
    export SETVARS_COMPLETED='1'
    export SETVARS_VARS_PATH='/opt/intel/oneapi/tbb/latest/env/vars.sh'
    export TBBROOT='/opt/intel/oneapi/tbb/2021.2.0/env/..'
```

## Collection

 - Name: [fenz-org/icc](https://github.com/fenz-org/icc)
 - License: None

