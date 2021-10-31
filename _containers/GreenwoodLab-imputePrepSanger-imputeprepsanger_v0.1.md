---
id: 4805
name: "GreenwoodLab/imputePrepSanger"
branch: "master"
tag: "imputeprepsanger_v0.1"
commit: "1cc66016e576e30ea3f0edcb5adb790a1ba2b9d0"
version: "e5ec0e5a177ac01303280a40c306cb3e"
build_date: "2018-09-13T21:15:41.965Z"
size_mb: 517
size: 162578463
sif: "https://datasets.datalad.org/shub/GreenwoodLab/imputePrepSanger/imputeprepsanger_v0.1/2018-09-13-1cc66016-e5ec0e5a/e5ec0e5a177ac01303280a40c306cb3e.simg"
url: https://datasets.datalad.org/shub/GreenwoodLab/imputePrepSanger/imputeprepsanger_v0.1/2018-09-13-1cc66016-e5ec0e5a/
recipe: https://datasets.datalad.org/shub/GreenwoodLab/imputePrepSanger/imputeprepsanger_v0.1/2018-09-13-1cc66016-e5ec0e5a/Singularity
collection: GreenwoodLab/imputePrepSanger
---

# GreenwoodLab/imputePrepSanger:imputeprepsanger_v0.1

```bash
$ singularity pull shub://GreenwoodLab/imputePrepSanger:imputeprepsanger_v0.1
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

 - Name: [GreenwoodLab/imputePrepSanger](https://github.com/GreenwoodLab/imputePrepSanger)
 - License: None

