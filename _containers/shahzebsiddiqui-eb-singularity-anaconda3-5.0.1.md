---
id: 1718
name: "shahzebsiddiqui/eb-singularity"
branch: "eb_images"
tag: "anaconda3-5.0.1"
commit: "6350854757f26b7b10339b18e17ea80cd9c64ad1"
version: "afbbb50a62b731cb30a9b0c82a5ec711"
build_date: "2020-06-02T22:11:36.772Z"
size_mb: 3488
size: 1474441247
sif: "https://datasets.datalad.org/shub/shahzebsiddiqui/eb-singularity/anaconda3-5.0.1/2020-06-02-63508547-afbbb50a/afbbb50a62b731cb30a9b0c82a5ec711.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/shahzebsiddiqui/eb-singularity/anaconda3-5.0.1/2020-06-02-63508547-afbbb50a/
recipe: https://datasets.datalad.org/shub/shahzebsiddiqui/eb-singularity/anaconda3-5.0.1/2020-06-02-63508547-afbbb50a/Singularity
collection: shahzebsiddiqui/eb-singularity
---

# shahzebsiddiqui/eb-singularity:anaconda3-5.0.1

```bash
$ singularity pull shub://shahzebsiddiqui/eb-singularity:anaconda3-5.0.1
```

## Singularity Recipe

```singularity
BootStrap: shub
From: shahzebsiddiqui/eb-singularity:centos-7.3.1611

%post
su - easybuild 
eb Anaconda3-5.0.1.eb --robot --installpath=/app/ --prefix=/scratch --tmpdir=/scratch/tmp  --module-naming-scheme=EasyBuildMNS
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
module load Anaconda3/5.0.1

%labels
```

## Collection

 - Name: [shahzebsiddiqui/eb-singularity](https://github.com/shahzebsiddiqui/eb-singularity)
 - License: None

