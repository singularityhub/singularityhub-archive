---
id: 4694
name: "natacha-beck/imputePrepSanger"
branch: "singularity"
tag: "imputeprepsanger_v1.0"
commit: "324dd1400cd9d878b1d226d21b8f0a4f95b05c6c"
version: "1da154954736d19a3d8bde25ce9dc869"
build_date: "2018-09-10T04:18:51.816Z"
size_mb: 6137
size: 1699794975
sif: "https://datasets.datalad.org/shub/natacha-beck/imputePrepSanger/imputeprepsanger_v1.0/2018-09-10-324dd140-1da15495/1da154954736d19a3d8bde25ce9dc869.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/natacha-beck/imputePrepSanger/imputeprepsanger_v1.0/2018-09-10-324dd140-1da15495/
recipe: https://datasets.datalad.org/shub/natacha-beck/imputePrepSanger/imputeprepsanger_v1.0/2018-09-10-324dd140-1da15495/Singularity
collection: natacha-beck/imputePrepSanger
---

# natacha-beck/imputePrepSanger:imputeprepsanger_v1.0

```bash
$ singularity pull shub://natacha-beck/imputePrepSanger:imputeprepsanger_v1.0
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
# Standard installation
cd /
yum update -y
yum install -y bzip2      \
               gcc        \
               git        \
               make       \
               perl       \
               unzip      \
               wget       \
               zlib-devel \
               which

# Bunch of chmod
chmod 755 /imputePrepSanger
chmod 755 /imputePrepSanger/*.awk
chmod 755 /imputePrepSanger/update_build.sh
chmod 755 /imputePrepSanger/imputePrep_script.sh
chmod 755 /imputePrepSanger/HRC-1000G-check-bim_v4.2.7.pl
chmod 755 /imputePrepSanger/reportRedaction.sh

# Install bcftools
cd /
wget  https://github.com/samtools/bcftools/releases/download/1.3.1/bcftools-1.3.1.tar.bz2 \
&& bunzip2 -f bcftools-1.3.1.tar.bz2                                                      \
&& tar -xvf bcftools-1.3.1.tar                                                            \
&& cd bcftools-1.3.1                                                                      \
&& make                                                                                   \
&& make install 

# Install plink
cd    /imputePrepSanger
unzip /imputePrepSanger/plink_linux_x86_64.zip -d /imputePrepSanger/plink

# Copy fix_data
mkdir   /fix_data                                                                            \
&&   cd /fix_data                                                                            \
&& wget ftp://ngs.sanger.ac.uk/production/hrc/HRC.r1-1/HRC.r1-1.GRCh37.wgs.mac5.sites.tab.gz \
&& gunzip HRC.r1-1.GRCh37.wgs.mac5.sites.tab.gz                                              \
&& wget ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/human_g1k_v37.fasta.gz  \
&& gunzip human_g1k_v37.fasta.gz || true                                                     \
&& wget https://imputation.sanger.ac.uk/www/plink2ensembl.txt

%environment
  PATH=$PATH:/imputePrepSanger:/imputePrepSanger/plink

%runscript
  cd /imputePrepSanger/
```

## Collection

 - Name: [natacha-beck/imputePrepSanger](https://github.com/natacha-beck/imputePrepSanger)
 - License: None

