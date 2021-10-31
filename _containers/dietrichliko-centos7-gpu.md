---
id: 9320
name: "dietrichliko/centos7"
branch: "master"
tag: "gpu"
commit: "15114e578b30d76356ab62a178fda786395f11d9"
version: "201facf6bb4c1a0688ce7675f345658f"
build_date: "2019-05-30T14:54:27.662Z"
size_mb: 4377
size: 2182148127
sif: "https://datasets.datalad.org/shub/dietrichliko/centos7/gpu/2019-05-30-15114e57-201facf6/201facf6bb4c1a0688ce7675f345658f.simg"
url: https://datasets.datalad.org/shub/dietrichliko/centos7/gpu/2019-05-30-15114e57-201facf6/
recipe: https://datasets.datalad.org/shub/dietrichliko/centos7/gpu/2019-05-30-15114e57-201facf6/Singularity
collection: dietrichliko/centos7
---

# dietrichliko/centos7:gpu

```bash
$ singularity pull shub://dietrichliko/centos7:gpu
```

## Singularity Recipe

```singularity
Bootstrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum

%help
    CentOS 7 for HEPHY analysis with GPU
    * CVMFS
    * Grid UI
    * HEP_OSlibs
    * CUDA 9.2 / CUDNN7

%labels
    Maintainer Dietrich Liko <Dietrich.Liko@oeaw.ac.at>
    Version  v0.1.0


%setup
    mkdir    ${SINGULARITY_ROOTFS}/etc/grid-security
    mkdir    ${SINGULARITY_ROOTFS}/etc/grid-security/vomsdir
    mkdir    ${SINGULARITY_ROOTFS}/etc/vomses

    cp -r vomsdir/ ${SINGULARITY_ROOTFS}/etc/grid-security/vomsdir/
    cp -r vomses/  ${SINGULARITY_ROOTFS}/etc/vomses/

%files
    repos/wlcg-centos7.repo                   /etc/yum.repos.d/
    repos/UMD-4-base.repo                     /etc/yum.repos.d/
    repos/UMD-4-updates.repo                  /etc/yum.repos.d/
    repos/dliko-empty-ca-policy-epel-7.repo   /etc/yum.repos.d/
    repos/cuda.repo                           /etc/yum.repos.d/
    repos/nvidia-ml.repo                      /etc/yum.repos.d/

    libexec/cmsenv.sh                         /usr/local/libexec/
%post
    yum -y update
    yum -y install epel-release
    yum -y groupinstall "Development tools"
    yum -y install git-lfs

    yum -y install yum-priorities
    yum -y install HEP_OSlibs empty-ca-policy ui

    yum -y install cuda-cudart-9-2 \
                   cuda-libraries-9-2 \
                   cuda-libraries-dev-9-2 \
                   libnccl-*+cuda9.2 \
                   libnccl-devel-*+cuda9.2\
                   cuda-nvml-dev-9-2 \
                   cuda-minimal-build-9-2 \
                   cuda-command-line-tools-9-2 \
                   libcudnn7-*.cuda9.2 \
                   libcudnn7-devel-*.cuda9.2 \
                   nvidia-driver-cuda \
                   nvidia-driver-devel

    yum clean all
    rm -rf /var/cache/yum

    ln -s /cvmfs/grid.cern.ch/etc/grid-security/certificates /etc/grid-security/certificates

    mkdir /cvmfs /afs /scratch

%environment
    export LCG_GFAL_INFOSYS=egee-bdii.cnaf.infn.it:2170
    export MYPROXY_SERVER=myproxy.cern.ch
    export DPNS_HOST=hephyse.oeaw.ac.at
    export DPM_HOST=hephyse.oeaw.ac.at

%apprun cms
    if [ $# -gt 0 ]
    then
      exec /bin/bash --init-file=/usr/local/libexec/cmsenv.sh -c "$@"
    else
      exec /bin/bash --init-file=/usr/local/libexec/cmsenv.sh
    fi
%appenv cms
    unset SCRAM_ARCH

%apphelp cms
    CentOS 7 for HEPHY analysis with CMS environment.
    * CVMFS
    * Grid UI
    * HEP_OSlibs
```

## Collection

 - Name: [dietrichliko/centos7](https://github.com/dietrichliko/centos7)
 - License: [MIT License](https://api.github.com/licenses/mit)

