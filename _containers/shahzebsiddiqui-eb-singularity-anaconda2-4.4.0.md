---
id: 1717
name: "shahzebsiddiqui/eb-singularity"
branch: "eb_images"
tag: "anaconda2-4.4.0"
commit: "1014270887f18faf75574eda57369b91a7b97a3a"
version: "67d6cfee30e89c478c0f740322e5ce08"
build_date: "2018-02-15T11:57:05.773Z"
size_mb: 2765
size: 829857823
sif: "https://datasets.datalad.org/shub/shahzebsiddiqui/eb-singularity/anaconda2-4.4.0/2018-02-15-10142708-67d6cfee/67d6cfee30e89c478c0f740322e5ce08.simg"
url: https://datasets.datalad.org/shub/shahzebsiddiqui/eb-singularity/anaconda2-4.4.0/2018-02-15-10142708-67d6cfee/
recipe: https://datasets.datalad.org/shub/shahzebsiddiqui/eb-singularity/anaconda2-4.4.0/2018-02-15-10142708-67d6cfee/Singularity
collection: shahzebsiddiqui/eb-singularity
---

# shahzebsiddiqui/eb-singularity:anaconda2-4.4.0

```bash
$ singularity pull shub://shahzebsiddiqui/eb-singularity:anaconda2-4.4.0
```

## Singularity Recipe

```singularity
BootStrap: shub
From: shahzebsiddiqui/eb-singularity:centos-7.3.1611

%post
su - easybuild 
eb Anaconda2-4.4.0.eb --robot --installpath=/app/ --prefix=/scratch --tmpdir=/scratch/tmp  --module-naming-scheme=EasyBuildMNS
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
module load Anaconda2/4.4.0

%labels
```

## Collection

 - Name: [shahzebsiddiqui/eb-singularity](https://github.com/shahzebsiddiqui/eb-singularity)
 - License: None

