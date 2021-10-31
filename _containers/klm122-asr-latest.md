---
id: 10782
name: "klm122/asr"
branch: "master"
tag: "latest"
commit: "96060b3f17b0692cc16d4363b6ce3a5bff35baa4"
version: "d3ced363efc5f48878600630232ce036"
build_date: "2019-09-01T10:58:42.025Z"
size_mb: 70.0
size: 25849887
sif: "https://datasets.datalad.org/shub/klm122/asr/latest/2019-09-01-96060b3f-d3ced363/d3ced363efc5f48878600630232ce036.sif"
url: https://datasets.datalad.org/shub/klm122/asr/latest/2019-09-01-96060b3f-d3ced363/
recipe: https://datasets.datalad.org/shub/klm122/asr/latest/2019-09-01-96060b3f-d3ced363/Singularity
collection: klm122/asr
---

# klm122/asr:latest

```bash
$ singularity pull shub://klm122/asr:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04
%environment
export APT_INSTALL="apt-get install -y --no-install-recommends"
export DEBIAN_FRONTEND=noninteractive
export PIP_INSTALL="python3 -m pip --no-cache-dir install --upgrade"
export MKLROOT=/opt/intel/mkl

%post
%%%%%
export APT_INSTALL="apt-get install -y --no-install-recommends"
export DEBIAN_FRONTEND=noninteractive
export PIP_INSTALL="python3 -m pip --no-cache-dir install --upgrade"
export MKLROOT=/opt/intel/mkl

apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y install gcc g++ gfortran wget cpio && \
  cd /tmp && \
  wget -q http://registrationcenter-download.intel.com/akdlm/irc_nas/tec/15275/l_mkl_2019.3.199.tgz && \
  tar -xzf l_mkl_2019.3.199.tgz && \
  cd l_mkl_2019.3.199 && \
  sed -i 's/ACCEPT_EULA=decline/ACCEPT_EULA=accept/g' silent.cfg && \
  sed -i 's/ARCH_SELECTED=ALL/ARCH_SELECTED=INTEL64/g' silent.cfg && \
#  sed -i 's/COMPONENTS=DEFAULTS/COMPONENTS=;intel-comp-l-all-vars__noarch;intel-openmp-l-all__x86_64;intel-openmp-l-ps-libs__x86_64;intel-openmp-l-ps-libs-jp__x86_64;intel-tbb-libs__noarch;intel-mkl-common__noarch;intel-mkl-sta-common__noarch;intel-mkl__x86_64;intel-mkl-rt__x86_64;intel-mkl-ps-rt-jp__x86_64;intel-mkl-doc__noarch;intel-mkl-ps-doc__noarch;intel-mkl-ps-doc-jp__noarch;intel-mkl-gnu__x86_64;intel-mkl-gnu-rt__x86_64;intel-mkl-ps-common__noarch;intel-mkl-ps-common-jp__noarch;intel-mkl-ps-common-64bit__x86_64;intel-mkl-common-c__noarch;intel-mkl-common-c-64bit__x86_64;intel-mkl-ps-common-c__noarch;intel-mkl-doc-c__noarch;intel-mkl-ps-doc-c-jp__noarch;intel-mkl-ps-ss-tbb__x86_64;intel-mkl-ps-ss-tbb-rt__x86_64;intel-mkl-gnu-c__x86_64;intel-mkl-ps-common-f__noarch;intel-mkl-ps-common-f-64bit__x86_64;intel-mkl-ps-doc-f__noarch;intel-mkl-ps-doc-f-jp__noarch;intel-mkl-ps-gnu-f-rt__x86_64;intel-mkl-ps-gnu-f__x86_64;intel-mkl-ps-f95-common__noarch;intel-mkl-ps-f__x86_64;intel-mkl-psxe__noarch;intel-psxe-common__noarch;intel-psxe-common-doc__noarch;intel-compxe-pset/g' silent.cfg && \
  sed -i 's/COMPONENTS=DEFAULTS/COMPONENTS=;intel-comp-l-all-vars__noarch;intel-comp-nomcu-vars__noarch;intel-openmp__x86_64;intel-tbb-libs__x86_64;intel-mkl-common__noarch;intel-mkl-installer-license__noarch;intel-mkl-core__x86_64;intel-mkl-core-rt__x86_64;intel-mkl-doc__noarch;intel-mkl-doc-ps__noarch;intel-mkl-gnu__x86_64;intel-mkl-gnu-rt__x86_64;intel-mkl-common-ps__noarch;intel-mkl-core-ps__x86_64;intel-mkl-common-c__noarch;intel-mkl-core-c__x86_64;intel-mkl-common-c-ps__noarch;intel-mkl-tbb__x86_64;intel-mkl-tbb-rt__x86_64;intel-mkl-gnu-c__x86_64;intel-mkl-common-f__noarch;intel-mkl-core-f__x86_64;intel-mkl-gnu-f-rt__x86_64;intel-mkl-gnu-f__x86_64;intel-mkl-f95-common__noarch;intel-mkl-f__x86_64;intel-mkl-psxe__noarch;intel-psxe-common__noarch;intel-psxe-common-doc__noarch;intel-compxe-pset/g' silent.cfg && \
  ./install.sh -s silent.cfg && \
  cd .. && rm -rf * && \
  rm -rf /opt/intel/.*.log /opt/intel/compilers_and_libraries_2019.3.199/licensing && \
  echo "/opt/intel/mkl/lib/intel64" >> /etc/ld.so.conf.d/intel.conf && \
  ldconfig && \
  echo "source /opt/intel/mkl/bin/mklvars.sh intel64" >> /etc/bash.bashrc
  
apt-get install xmlstarlet

%runscript
exec /bin/bash "$@"
```

## Collection

 - Name: [klm122/asr](https://github.com/klm122/asr)
 - License: None

