---
id: 1444
name: "shahzebsiddiqui/eb-singularity"
branch: "eb_images"
tag: "git-lfs-1.1.1"
commit: "1b720948d4222b590256436b9af9ddb96cc4cdb0"
version: "ff43020d51b85e8e40c9c672f70844ce"
build_date: "2021-03-02T20:03:29.231Z"
size_mb: 721
size: 226234399
sif: "https://datasets.datalad.org/shub/shahzebsiddiqui/eb-singularity/git-lfs-1.1.1/2021-03-02-1b720948-ff43020d/ff43020d51b85e8e40c9c672f70844ce.simg"
url: https://datasets.datalad.org/shub/shahzebsiddiqui/eb-singularity/git-lfs-1.1.1/2021-03-02-1b720948-ff43020d/
recipe: https://datasets.datalad.org/shub/shahzebsiddiqui/eb-singularity/git-lfs-1.1.1/2021-03-02-1b720948-ff43020d/Singularity
collection: shahzebsiddiqui/eb-singularity
---

# shahzebsiddiqui/eb-singularity:git-lfs-1.1.1

```bash
$ singularity pull shub://shahzebsiddiqui/eb-singularity:git-lfs-1.1.1
```

## Singularity Recipe

```singularity
BootStrap: shub
From: shahzebsiddiqui/eb-singularity:centos-7.3.1611

%post
su - easybuild 
eb git-lfs-1.1.1.eb --robot --installpath=/app/ --prefix=/scratch --tmpdir=/scratch/tmp  --module-naming-scheme=EasyBuildMNS
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
module load git-lfs/1.1.1

%labels
```

## Collection

 - Name: [shahzebsiddiqui/eb-singularity](https://github.com/shahzebsiddiqui/eb-singularity)
 - License: None

