---
id: 1715
name: "shahzebsiddiqui/eb-singularity"
branch: "eb_images"
tag: "bison-3.0.4"
commit: "1014270887f18faf75574eda57369b91a7b97a3a"
version: "965c38bc5eb307a414f107bc2c8cada1"
build_date: "2018-02-15T11:57:05.794Z"
size_mb: 721
size: 226566175
sif: "https://datasets.datalad.org/shub/shahzebsiddiqui/eb-singularity/bison-3.0.4/2018-02-15-10142708-965c38bc/965c38bc5eb307a414f107bc2c8cada1.simg"
url: https://datasets.datalad.org/shub/shahzebsiddiqui/eb-singularity/bison-3.0.4/2018-02-15-10142708-965c38bc/
recipe: https://datasets.datalad.org/shub/shahzebsiddiqui/eb-singularity/bison-3.0.4/2018-02-15-10142708-965c38bc/Singularity
collection: shahzebsiddiqui/eb-singularity
---

# shahzebsiddiqui/eb-singularity:bison-3.0.4

```bash
$ singularity pull shub://shahzebsiddiqui/eb-singularity:bison-3.0.4
```

## Singularity Recipe

```singularity
BootStrap: shub
From: shahzebsiddiqui/eb-singularity:centos-7.3.1611

%post
su - easybuild 
eb Bison-3.0.4.eb --robot --installpath=/app/ --prefix=/scratch --tmpdir=/scratch/tmp  --module-naming-scheme=EasyBuildMNS
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
module load Bison/3.0.4

%labels
```

## Collection

 - Name: [shahzebsiddiqui/eb-singularity](https://github.com/shahzebsiddiqui/eb-singularity)
 - License: None

