---
id: 11914
name: "MathijsSanders/AdditionalBAMStatisticsSingularity"
branch: "master"
tag: "latest"
commit: "e556bb0e53948f7709433ad9fb8abbcee5152877"
version: "c6922e253e99aa1f1968bb7ddc54dd1c"
build_date: "2019-12-24T14:22:45.021Z"
size_mb: 770.0
size: 253345823
sif: "https://datasets.datalad.org/shub/MathijsSanders/AdditionalBAMStatisticsSingularity/latest/2019-12-24-e556bb0e-c6922e25/c6922e253e99aa1f1968bb7ddc54dd1c.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/MathijsSanders/AdditionalBAMStatisticsSingularity/latest/2019-12-24-e556bb0e-c6922e25/
recipe: https://datasets.datalad.org/shub/MathijsSanders/AdditionalBAMStatisticsSingularity/latest/2019-12-24-e556bb0e-c6922e25/Singularity
collection: MathijsSanders/AdditionalBAMStatisticsSingularity
---

# MathijsSanders/AdditionalBAMStatisticsSingularity:latest

```bash
$ singularity pull shub://MathijsSanders/AdditionalBAMStatisticsSingularity:latest
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: disco
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%labels
MAINTAINER MathijsSanders

%runscript
exec /bin/bash /code/runScript.sh "$@"

%post
sed -i 's/$/ universe/' /etc/apt/sources.list
apt-get update
apt-get -y install openjdk-12-jre git samtools
cd /tmp/
git clone https://github.com/MathijsSanders/AdditionalBAMStatistics.git
cd AdditionalBAMStatistics/
mkdir /code
mv additionalBamStatistics.jar runScript.sh /code/
chmod u+x /code/runScript.sh
rm -rf /tmp/AdditionalBAMStatistics
apt-get clean

%environment
export LC_ALL=C
```

## Collection

 - Name: [MathijsSanders/AdditionalBAMStatisticsSingularity](https://github.com/MathijsSanders/AdditionalBAMStatisticsSingularity)
 - License: None

