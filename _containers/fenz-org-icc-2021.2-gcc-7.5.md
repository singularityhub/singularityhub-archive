---
id: 15888
name: "fenz-org/icc"
branch: "master"
tag: "2021.2-gcc-7.5"
commit: "205f3f7df9845a4b1f4c9f390d72ec71de12c653"
version: "71648d8b1ec4503cecdbd0d5b58e33db5306e986fb2569a68f6dc08f26ca6df6"
build_date: "2021-04-12T20:02:15.683Z"
size_mb: 1240.5234375
size: 1300783104
sif: "https://datasets.datalad.org/shub/fenz-org/icc/2021.2-gcc-7.5/2021-04-12-205f3f7d-71648d8b/71648d8b1ec4503cecdbd0d5b58e33db5306e986fb2569a68f6dc08f26ca6df6.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/fenz-org/icc/2021.2-gcc-7.5/2021-04-12-205f3f7d-71648d8b/
recipe: https://datasets.datalad.org/shub/fenz-org/icc/2021.2-gcc-7.5/2021-04-12-205f3f7d-71648d8b/Singularity
collection: fenz-org/icc
---

# fenz-org/icc:2021.2-gcc-7.5

```bash
$ singularity pull shub://fenz-org/icc:2021.2-gcc-7.5
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: intel/oneapi:os-tools-ubuntu18.04

%post
    export DEBIAN_FRONTEND=noninteractive
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
    export LANGUAGE=C.UTF-8

    apt-get update -y && \
    apt-get install -y --no-install-recommends -o=Dpkg::Use-Pty=0 \
        intel-oneapi-compiler-dpcpp-cpp-and-cpp-classic

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

