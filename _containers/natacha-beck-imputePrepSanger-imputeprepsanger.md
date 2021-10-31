---
id: 3186
name: "natacha-beck/imputePrepSanger"
branch: "singularity"
tag: "imputeprepsanger"
commit: "e4f53832117838b47efd773f1f7a7ff49a0c62ef"
version: "e9ef13e69ac4ee3b1b3f997d8752f306"
build_date: "2018-07-10T20:27:34.590Z"
size_mb: 553
size: 172609567
sif: "https://datasets.datalad.org/shub/natacha-beck/imputePrepSanger/imputeprepsanger/2018-07-10-e4f53832-e9ef13e6/e9ef13e69ac4ee3b1b3f997d8752f306.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/natacha-beck/imputePrepSanger/imputeprepsanger/2018-07-10-e4f53832-e9ef13e6/
recipe: https://datasets.datalad.org/shub/natacha-beck/imputePrepSanger/imputeprepsanger/2018-07-10-e4f53832-e9ef13e6/Singularity
collection: natacha-beck/imputePrepSanger
---

# natacha-beck/imputePrepSanger:imputeprepsanger

```bash
$ singularity pull shub://natacha-beck/imputePrepSanger:imputeprepsanger
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

 - Name: [natacha-beck/imputePrepSanger](https://github.com/natacha-beck/imputePrepSanger)
 - License: None

