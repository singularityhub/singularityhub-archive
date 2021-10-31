---
id: 1785
name: "shahzebsiddiqui/eb-singularity"
branch: "eb_images"
tag: "cuda-9.0.176"
commit: "b34cf2d8d076bc6a628a79c91bed8eb9e22fcf4e"
version: "6fa47e771e5371b5be120227a5011f7d"
build_date: "2018-02-22T10:18:06.388Z"
size_mb: 3168
size: 1701122079
sif: "https://datasets.datalad.org/shub/shahzebsiddiqui/eb-singularity/cuda-9.0.176/2018-02-22-b34cf2d8-6fa47e77/6fa47e771e5371b5be120227a5011f7d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/shahzebsiddiqui/eb-singularity/cuda-9.0.176/2018-02-22-b34cf2d8-6fa47e77/
recipe: https://datasets.datalad.org/shub/shahzebsiddiqui/eb-singularity/cuda-9.0.176/2018-02-22-b34cf2d8-6fa47e77/Singularity
collection: shahzebsiddiqui/eb-singularity
---

# shahzebsiddiqui/eb-singularity:cuda-9.0.176

```bash
$ singularity pull shub://shahzebsiddiqui/eb-singularity:cuda-9.0.176
```

## Singularity Recipe

```singularity
BootStrap: shub
From: shahzebsiddiqui/eb-singularity:centos-7.3.1611

%post
pip install easybuild -U
su - easybuild 
eb CUDA-9.0.176.eb --robot --installpath=/app/ --prefix=/scratch --tmpdir=/scratch/tmp  --module-naming-scheme=EasyBuildMNS
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
module load CUDA/9.0.176

%labels
```

## Collection

 - Name: [shahzebsiddiqui/eb-singularity](https://github.com/shahzebsiddiqui/eb-singularity)
 - License: None

