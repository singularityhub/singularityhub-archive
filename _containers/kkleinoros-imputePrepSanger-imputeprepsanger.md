---
id: 4394
name: "kkleinoros/imputePrepSanger"
branch: "master"
tag: "imputeprepsanger"
commit: "2d68cff664bdc2ac06deb1840a464def0e2908f0"
version: "bdb1e3faa641005807e1a7674fae5d36"
build_date: "2018-08-30T10:21:13.082Z"
size_mb: 517
size: 162557983
sif: "https://datasets.datalad.org/shub/kkleinoros/imputePrepSanger/imputeprepsanger/2018-08-30-2d68cff6-bdb1e3fa/bdb1e3faa641005807e1a7674fae5d36.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/kkleinoros/imputePrepSanger/imputeprepsanger/2018-08-30-2d68cff6-bdb1e3fa/
recipe: https://datasets.datalad.org/shub/kkleinoros/imputePrepSanger/imputeprepsanger/2018-08-30-2d68cff6-bdb1e3fa/Singularity
collection: kkleinoros/imputePrepSanger
---

# kkleinoros/imputePrepSanger:imputeprepsanger

```bash
$ singularity pull shub://kkleinoros/imputePrepSanger:imputeprepsanger
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

 - Name: [kkleinoros/imputePrepSanger](https://github.com/kkleinoros/imputePrepSanger)
 - License: None

