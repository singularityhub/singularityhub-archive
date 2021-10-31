---
id: 1716
name: "shahzebsiddiqui/eb-singularity"
branch: "eb_images"
tag: "m4-1.4.18"
commit: "1014270887f18faf75574eda57369b91a7b97a3a"
version: "f07c3c289a53bc36dd1b6903fe589724"
build_date: "2018-02-15T11:57:05.783Z"
size_mb: 717
size: 225517599
sif: "https://datasets.datalad.org/shub/shahzebsiddiqui/eb-singularity/m4-1.4.18/2018-02-15-10142708-f07c3c28/f07c3c289a53bc36dd1b6903fe589724.simg"
url: https://datasets.datalad.org/shub/shahzebsiddiqui/eb-singularity/m4-1.4.18/2018-02-15-10142708-f07c3c28/
recipe: https://datasets.datalad.org/shub/shahzebsiddiqui/eb-singularity/m4-1.4.18/2018-02-15-10142708-f07c3c28/Singularity
collection: shahzebsiddiqui/eb-singularity
---

# shahzebsiddiqui/eb-singularity:m4-1.4.18

```bash
$ singularity pull shub://shahzebsiddiqui/eb-singularity:m4-1.4.18
```

## Singularity Recipe

```singularity
BootStrap: shub
From: shahzebsiddiqui/eb-singularity:centos-7.3.1611

%post
su - easybuild 
eb M4-1.4.18.eb --robot --installpath=/app/ --prefix=/scratch --tmpdir=/scratch/tmp  --module-naming-scheme=EasyBuildMNS
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
module load M4/1.4.18

%labels
```

## Collection

 - Name: [shahzebsiddiqui/eb-singularity](https://github.com/shahzebsiddiqui/eb-singularity)
 - License: None

