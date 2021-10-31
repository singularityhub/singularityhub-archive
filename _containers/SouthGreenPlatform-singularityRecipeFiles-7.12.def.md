---
id: 12114
name: "SouthGreenPlatform/singularityRecipeFiles"
branch: "master"
tag: "7.12.def"
commit: "2a9b759923502166114d4ce80a70362bd0087251"
version: "b5a18d2dbae31771957b707d4b846c4c54c47046c4761e71677d4d0b327791ce"
build_date: "2021-04-04T09:13:23.440Z"
size_mb: 109.5703125
size: 114892800
sif: "https://datasets.datalad.org/shub/SouthGreenPlatform/singularityRecipeFiles/7.12.def/2021-04-04-2a9b7599-b5a18d2d/b5a18d2dbae31771957b707d4b846c4c54c47046c4761e71677d4d0b327791ce.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/SouthGreenPlatform/singularityRecipeFiles/7.12.def/2021-04-04-2a9b7599-b5a18d2d/
recipe: https://datasets.datalad.org/shub/SouthGreenPlatform/singularityRecipeFiles/7.12.def/2021-04-04-2a9b7599-b5a18d2d/Singularity
collection: SouthGreenPlatform/singularityRecipeFiles
---

# SouthGreenPlatform/singularityRecipeFiles:7.12.def

```bash
$ singularity pull shub://SouthGreenPlatform/singularityRecipeFiles:7.12.def
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:18.04

%labels
Maintainer tando
base.image="ubuntu:18.04"
version="1"
software="bwa"
software.version="0.7.12"

%help
Being in the folder of the container
Launch the command: singularity run bwa-0.7.12.simg + arguments to use bwa 


%post
apt-get update
apt-get install -y build-essential wget gcc zlib1g-dev
mkdir -p /opt/sources/
cd /opt/sources/
wget https://github.com/lh3/bwa/archive/0.7.12.tar.gz
tar xvfz 0.7.12.tar.gz
cd bwa-0.7.12
make
cp -r /opt/sources/bwa-0.7.12 /usr/local/bwa-0.7.12
chmod +x -R /usr/local/bwa-0.7.12

%runscript
exec /usr/local/bwa-0.7.12/bwa "$@"
```

## Collection

 - Name: [SouthGreenPlatform/singularityRecipeFiles](https://github.com/SouthGreenPlatform/singularityRecipeFiles)
 - License: None

