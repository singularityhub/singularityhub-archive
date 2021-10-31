---
id: 4393
name: "kkleinoros/imputePrepSanger"
branch: "master"
tag: "imputeprepsanger_v1.0"
commit: "8b90c844d7c6e54f76cf0c4eb981ffbfdcdc20b3"
version: "f94e5ced2d72d2d1c4287e2e5ff3d48c"
build_date: "2018-08-30T10:21:13.089Z"
size_mb: 6147
size: 1699786783
sif: "https://datasets.datalad.org/shub/kkleinoros/imputePrepSanger/imputeprepsanger_v1.0/2018-08-30-8b90c844-f94e5ced/f94e5ced2d72d2d1c4287e2e5ff3d48c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/kkleinoros/imputePrepSanger/imputeprepsanger_v1.0/2018-08-30-8b90c844-f94e5ced/
recipe: https://datasets.datalad.org/shub/kkleinoros/imputePrepSanger/imputeprepsanger_v1.0/2018-08-30-8b90c844-f94e5ced/Singularity
collection: kkleinoros/imputePrepSanger
---

# kkleinoros/imputePrepSanger:imputeprepsanger_v1.0

```bash
$ singularity pull shub://kkleinoros/imputePrepSanger:imputeprepsanger_v1.0
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

  mkdir   /fix_data \
    && cd /fix_data \
    && wget ftp://ngs.sanger.ac.uk/production/hrc/HRC.r1-1/HRC.r1-1.GRCh37.wgs.mac5.sites.tab.gz \
    && gunzip HRC.r1-1.GRCh37.wgs.mac5.sites.tab.gz                                           \
    && wget ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/human_g1k_v37.fasta.gz  \
    && gunzip human_g1k_v37.fasta.gz || true                                                     \
    && wget https://imputation.sanger.ac.uk/www/plink2ensembl.txt

%runscript
  cd /imputePrepSanger/
```

## Collection

 - Name: [kkleinoros/imputePrepSanger](https://github.com/kkleinoros/imputePrepSanger)
 - License: None

