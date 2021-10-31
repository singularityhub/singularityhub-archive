---
id: 9286
name: "dietrichliko/centos7"
branch: "master"
tag: "latest"
commit: "15114e578b30d76356ab62a178fda786395f11d9"
version: "58a8da56a02f00ddb96efbd37109db0c"
build_date: "2019-05-30T12:41:48.754Z"
size_mb: 1469
size: 484016159
sif: "https://datasets.datalad.org/shub/dietrichliko/centos7/latest/2019-05-30-15114e57-58a8da56/58a8da56a02f00ddb96efbd37109db0c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/dietrichliko/centos7/latest/2019-05-30-15114e57-58a8da56/
recipe: https://datasets.datalad.org/shub/dietrichliko/centos7/latest/2019-05-30-15114e57-58a8da56/Singularity
collection: dietrichliko/centos7
---

# dietrichliko/centos7:latest

```bash
$ singularity pull shub://dietrichliko/centos7:latest
```

## Singularity Recipe

```singularity
Bootstrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum

%help
    CentOS 7 for HEPHY analysis.
    * CVMFS
    * Grid UI
    * HEP_OSlibs

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

    libexec/cmsenv.sh                         /usr/local/libexec/
%post
    yum -y update
    yum -y install epel-release
    yum -y groupinstall "Development tools"
    yum -y install git-lfs

    yum -y install yum-priorities
    yum -y install HEP_OSlibs empty-ca-policy ui

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

