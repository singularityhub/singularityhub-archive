---
id: 4660
name: "GreenwoodLab/imputePrepSanger"
branch: "master"
tag: "imputeprepsanger"
commit: "2d68cff664bdc2ac06deb1840a464def0e2908f0"
version: "0c6a7e8610ae806463a965cf081dff01"
build_date: "2018-09-04T20:03:29.743Z"
size_mb: 517
size: 162566175
sif: "https://datasets.datalad.org/shub/GreenwoodLab/imputePrepSanger/imputeprepsanger/2018-09-04-2d68cff6-0c6a7e86/0c6a7e8610ae806463a965cf081dff01.simg"
url: https://datasets.datalad.org/shub/GreenwoodLab/imputePrepSanger/imputeprepsanger/2018-09-04-2d68cff6-0c6a7e86/
recipe: https://datasets.datalad.org/shub/GreenwoodLab/imputePrepSanger/imputeprepsanger/2018-09-04-2d68cff6-0c6a7e86/Singularity
collection: GreenwoodLab/imputePrepSanger
---

# GreenwoodLab/imputePrepSanger:imputeprepsanger

```bash
$ singularity pull shub://GreenwoodLab/imputePrepSanger:imputeprepsanger
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:6.9

%labels
  Maintainer Natacha Beck && Marie Forest

%files
  . imputePrepSanger

%post
  yum update -y
  yum install -y bzip2 \
                 gcc \
                 git \
                 make \
                 perl \
                 unzip \
                 wget \
                 zlib-devel \
                 which

  chmod 644 /imputePrepSanger/checkPositions.awk

  chmod 755 /imputePrepSanger/update_build.sh \
    && cp /imputePrepSanger/update_build.sh /bin/

  chmod 755 /imputePrepSanger/imputePrep_script.sh \
    && cp /imputePrepSanger/imputePrep_script.sh /bin/

  chmod 755 /imputePrepSanger/HRC-1000G-check-bim_v4.2.7.pl \
    && cp /imputePrepSanger/HRC-1000G-check-bim_v4.2.7.pl /bin/

  chmod 755 /imputePrepSanger/reportRedaction.sh \
    && cp /imputePrepSanger/reportRedaction.sh /bin/

  wget  https://github.com/samtools/bcftools/releases/download/1.3.1/bcftools-1.3.1.tar.bz2 \
 && bunzip2 -f bcftools-1.3.1.tar.bz2 \
 && tar -xvf bcftools-1.3.1.tar \
 && cd bcftools-1.3.1 \
 && make \
 && make install \
 && cp bcftools /bin/ \

  unzip /imputePrepSanger/plink_linux_x86_64.zip -d /imputePrepSanger/plink \
  && cp /imputePrepSanger/plink/plink /bin/

%runscript
  cd /imputePrepSanger/
```

## Collection

 - Name: [GreenwoodLab/imputePrepSanger](https://github.com/GreenwoodLab/imputePrepSanger)
 - License: None

