---
id: 3469
name: "natacha-beck/imputePrepSanger"
branch: "singularity"
tag: "imputeprepsanger_v0.1"
commit: "492b166749b86dafea8d39d27ecab8d60a732b16"
version: "69611f4a4e926aaa88ffaec44083df44"
build_date: "2018-09-07T01:41:55.857Z"
size_mb: 514
size: 161779743
sif: "https://datasets.datalad.org/shub/natacha-beck/imputePrepSanger/imputeprepsanger_v0.1/2018-09-07-492b1667-69611f4a/69611f4a4e926aaa88ffaec44083df44.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/natacha-beck/imputePrepSanger/imputeprepsanger_v0.1/2018-09-07-492b1667-69611f4a/
recipe: https://datasets.datalad.org/shub/natacha-beck/imputePrepSanger/imputeprepsanger_v0.1/2018-09-07-492b1667-69611f4a/Singularity
collection: natacha-beck/imputePrepSanger
---

# natacha-beck/imputePrepSanger:imputeprepsanger_v0.1

```bash
$ singularity pull shub://natacha-beck/imputePrepSanger:imputeprepsanger_v0.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:6.9

%labels
  Maintainer Natacha Beck && Marie Forest

%files
  . /imputePrepSanger

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

  chmod 755 /imputePrepSanger

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

 - Name: [natacha-beck/imputePrepSanger](https://github.com/natacha-beck/imputePrepSanger)
 - License: None

