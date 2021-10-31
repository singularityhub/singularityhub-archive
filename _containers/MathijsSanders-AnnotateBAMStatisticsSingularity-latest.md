---
id: 11816
name: "MathijsSanders/AnnotateBAMStatisticsSingularity"
branch: "master"
tag: "latest"
commit: "361edda1c3fe75983ea36e2438a0851983e2a587"
version: "6a8e4b5142a7ff30cb99be736064b94b"
build_date: "2021-04-06T14:47:09.882Z"
size_mb: 424.0
size: 146042911
sif: "https://datasets.datalad.org/shub/MathijsSanders/AnnotateBAMStatisticsSingularity/latest/2021-04-06-361edda1-6a8e4b51/6a8e4b5142a7ff30cb99be736064b94b.sif"
url: https://datasets.datalad.org/shub/MathijsSanders/AnnotateBAMStatisticsSingularity/latest/2021-04-06-361edda1-6a8e4b51/
recipe: https://datasets.datalad.org/shub/MathijsSanders/AnnotateBAMStatisticsSingularity/latest/2021-04-06-361edda1-6a8e4b51/Singularity
collection: MathijsSanders/AnnotateBAMStatisticsSingularity
---

# MathijsSanders/AnnotateBAMStatisticsSingularity:latest

```bash
$ singularity pull shub://MathijsSanders/AnnotateBAMStatisticsSingularity:latest
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: xenial
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%labels
MAINTAINER MathijsSanders

%runscript

exec /bin/bash /code/runScript.sh "$@"

%post
sed -i 's/$/ universe/' /etc/apt/sources.list
apt-get update
apt-get -y install build-essential git zlib1g-dev
apt-get clean
cd /tmp/
git clone https://github.com/MathijsSanders/AnnotateBAMStatistics.git
cd AnnotateBAMStatistics
make all
cp /tmp/AnnotateBAMStatistics/dist/Release/GNU-Linux/AnnotateBAMStatistics /usr/bin/
mkdir /code
cp /tmp/AnnotateBAMStatistics/runScript.sh /code/
chmod u+x /code/runScript.sh
rm -rf /tmp/AnnotateBAMStatistics	

%environment
export PATH=$PATH:/usr/games
export LC_ALL=C
```

## Collection

 - Name: [MathijsSanders/AnnotateBAMStatisticsSingularity](https://github.com/MathijsSanders/AnnotateBAMStatisticsSingularity)
 - License: None

