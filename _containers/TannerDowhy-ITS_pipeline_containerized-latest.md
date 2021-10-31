---
id: 3843
name: "TannerDowhy/ITS_pipeline_containerized"
branch: "master"
tag: "latest"
commit: "f82d0321e74d6b57715a31b40ed7bfa3f59222ef"
version: "ec47267665e575e5333327dcdfb484df"
build_date: "2018-08-03T18:41:28.464Z"
size_mb: 967
size: 306778143
sif: "https://datasets.datalad.org/shub/TannerDowhy/ITS_pipeline_containerized/latest/2018-08-03-f82d0321-ec472676/ec47267665e575e5333327dcdfb484df.simg"
url: https://datasets.datalad.org/shub/TannerDowhy/ITS_pipeline_containerized/latest/2018-08-03-f82d0321-ec472676/
recipe: https://datasets.datalad.org/shub/TannerDowhy/ITS_pipeline_containerized/latest/2018-08-03-f82d0321-ec472676/Singularity
collection: TannerDowhy/ITS_pipeline_containerized
---

# TannerDowhy/ITS_pipeline_containerized:latest

```bash
$ singularity pull shub://TannerDowhy/ITS_pipeline_containerized:latest
```

## Singularity Recipe

```singularity
BootStrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum

%setup
    mkdir ${SINGULARITY_ROOTFS}/primer_removal ${SINGULARITY_ROOTFS}/primer_removal/output ${SINGULARITY_ROOTFS}/primer_removal/reports

%files
    ../software/primer_removal.py /primer_removal/primer_removal.py
    ../software/touch.sh /primer_removal/touch.sh
    ../software/run_primer.sh /primer_removal/run_primer.sh
    ../software/submit.sh /primer_removal/submit.sh

%post
    yum -y groupinstall "Development Tools"
    yum -y install zlib-devel
    yum -y install https://centos7.iuscommunity.org/ius-release.rpm
    yum -y update
    yum -y install python36u python36u-libs python36u-devel python36u-pip

    pip3.6 install cutadapt
```

## Collection

 - Name: [TannerDowhy/ITS_pipeline_containerized](https://github.com/TannerDowhy/ITS_pipeline_containerized)
 - License: None

