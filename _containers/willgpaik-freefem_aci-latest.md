---
id: 7710
name: "willgpaik/freefem_aci"
branch: "master"
tag: "latest"
commit: "160f9d37c54bae5bc8a5a3f933917f176fdc3177"
version: "0fc725b80dc7536b3f45916140b3b92b"
build_date: "2020-06-29T20:02:21.190Z"
size_mb: 3350
size: 1090895903
sif: "https://datasets.datalad.org/shub/willgpaik/freefem_aci/latest/2020-06-29-160f9d37-0fc725b8/0fc725b80dc7536b3f45916140b3b92b.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/willgpaik/freefem_aci/latest/2020-06-29-160f9d37-0fc725b8/
recipe: https://datasets.datalad.org/shub/willgpaik/freefem_aci/latest/2020-06-29-160f9d37-0fc725b8/Singularity
collection: willgpaik/freefem_aci
---

# willgpaik/freefem_aci:latest

```bash
$ singularity pull shub://willgpaik/freefem_aci:latest
```

## Singularity Recipe

```singularity
BootStrap: shub
From: shub://willgpaik/centos7_aci:latest
%setup

%files

%environment 
    PATH="$PATH:/usr/lib64/openmpi/bin/:/opt/sw/freefem/bin/"
    export PATH
    LD_PRELOAD="/opt/eod/lib/libopentextdlfaker.so.3:/opt/eod/lib/libopentextglfaker.so.3 \
        :/opt/eod/lib64/libopentextdlfaker.so.3:/opt/eod/lib64/libopentextglfaker.so.3"
    export LD_PRELOAD

%runscript


%post
    yum -y install m4-devel \
      bison-devel \
      flex-devel \
      patch \
      openmpi-devel \
      fftw-devel \
      openblas-devel \
      lapack-devel \
      freeglut-devel \
      scotch-devel \
      arpack-devel \
      suitesparse-devel \
      MUMPS-devel \
      NLopt-devel \
      coin-or-Ipopt-devel \
      gnuplot \
      superLU-devel \
      hypre \
      perl-Digest-MD5
    yum -y update

    source /opt/rh/devtoolset-8/enable

    # Install FreeFem++
    mkdir -p /opt/sw/
    cd /opt/
    wget https://raw.githubusercontent.com/willgpaik/freefem_aci/master/freefem_install.sh
    chmod +x freefem_install.sh
    ./freefem_install.sh
    
    rm freefem_install.sh
    
    # Download requires libraries for EoD:
    cd /opt/
    svn export https://github.com/willgpaik/MorphoGraphX_aci.git/trunk/eod_graphics_libraries
    mv eod_graphics_libraries eod
```

## Collection

 - Name: [willgpaik/freefem_aci](https://github.com/willgpaik/freefem_aci)
 - License: None

