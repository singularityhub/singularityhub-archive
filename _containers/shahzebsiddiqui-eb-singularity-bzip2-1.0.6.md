---
id: 1443
name: "shahzebsiddiqui/eb-singularity"
branch: "eb_images"
tag: "bzip2-1.0.6"
commit: "1b720948d4222b590256436b9af9ddb96cc4cdb0"
version: "024c6685d6fa78537762fb8e0589ee6f"
build_date: "2018-01-24T08:43:02.358Z"
size_mb: 712
size: 223412255
sif: "https://datasets.datalad.org/shub/shahzebsiddiqui/eb-singularity/bzip2-1.0.6/2018-01-24-1b720948-024c6685/024c6685d6fa78537762fb8e0589ee6f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/shahzebsiddiqui/eb-singularity/bzip2-1.0.6/2018-01-24-1b720948-024c6685/
recipe: https://datasets.datalad.org/shub/shahzebsiddiqui/eb-singularity/bzip2-1.0.6/2018-01-24-1b720948-024c6685/Singularity
collection: shahzebsiddiqui/eb-singularity
---

# shahzebsiddiqui/eb-singularity:bzip2-1.0.6

```bash
$ singularity pull shub://shahzebsiddiqui/eb-singularity:bzip2-1.0.6
```

## Singularity Recipe

```singularity
BootStrap: shub
From: shahzebsiddiqui/eb-singularity:centos-7.3.1611

%post
su - easybuild 
eb bzip2-1.0.6.eb --robot --installpath=/app/ --prefix=/scratch --tmpdir=/scratch/tmp  --module-naming-scheme=EasyBuildMNS
exit
rm -rf /scratch/tmp/*
rm -rf /scratch/build
rm -rf /scratch/sources
rm -rf /scratch/ebfiles_repo

%runscript
eval "$@"

%environment
source /etc/profile
module use /app/modules/all/
module load bzip2/1.0.6

%labels
```

## Collection

 - Name: [shahzebsiddiqui/eb-singularity](https://github.com/shahzebsiddiqui/eb-singularity)
 - License: None

