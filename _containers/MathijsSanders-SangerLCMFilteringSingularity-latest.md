---
id: 11927
name: "MathijsSanders/SangerLCMFilteringSingularity"
branch: "master"
tag: "latest"
commit: "b4a65d4d6258c1839a8f959c5b8c5e692f4548de"
version: "2ca3c98169b075f9a94657d62735dc9f146b32df0ff1fd84a76ee33f6be3c3e3"
build_date: "2021-04-06T15:31:09.420Z"
size_mb: 252.859375
size: 265142272
sif: "https://datasets.datalad.org/shub/MathijsSanders/SangerLCMFilteringSingularity/latest/2021-04-06-b4a65d4d-2ca3c981/2ca3c98169b075f9a94657d62735dc9f146b32df0ff1fd84a76ee33f6be3c3e3.sif"
url: https://datasets.datalad.org/shub/MathijsSanders/SangerLCMFilteringSingularity/latest/2021-04-06-b4a65d4d-2ca3c981/
recipe: https://datasets.datalad.org/shub/MathijsSanders/SangerLCMFilteringSingularity/latest/2021-04-06-b4a65d4d-2ca3c981/Singularity
collection: MathijsSanders/SangerLCMFilteringSingularity
---

# MathijsSanders/SangerLCMFilteringSingularity:latest

```bash
$ singularity pull shub://MathijsSanders/SangerLCMFilteringSingularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%labels
Maintainer MathijsSanders
Version v1.1

%post
apt-get -y update
apt-get -y install make openjdk-11-jre git samtools gcc-4.8 g++-4.8 zlib1g-dev
apt-get clean
ln -s /usr/bin/g++-4.8 /usr/bin/g++
ln -s /usr/bin/gcc-4.8 /usr/bin/gcc
cd /tmp/
git clone https://github.com/MathijsSanders/AnnotateBAMStatistics.git
cd AnnotateBAMStatistics
make all
cp /tmp/AnnotateBAMStatistics/dist/Release/GNU-Linux/AnnotateBAMStatistics /usr/bin/
mkdir /code
cp /tmp/AnnotateBAMStatistics/runScript.sh /code/runScriptAnnotate.sh
cd ..
rm -rf /tmp/AnnotateBAMStatistics
git clone https://github.com/MathijsSanders/AdditionalBAMStatistics.git
cd AdditionalBAMStatistics/
mv additionalBamStatistics.jar runScript.sh /code/
mv /code/runScript.sh /code/runScriptAdditional.sh
cd ..
rm -rf /tmp/AdditionalBAMStatistics
git clone https://github.com/MathijsSanders/SangerLCMFiltering.git
cd SangerLCMFiltering
mv *.sh /code/
chmod u+x /code/*.sh
cd ../
rm -rf /tmp/SangerLCMFiltering

#======================================
# Preselect variants
#======================================

%apprun preselect 
exec /bin/bash /code/runScriptPreselect.sh "$@"

#======================================
# ImitateANNOVAR
#======================================

%apprun imitateANNOVAR
exec /bin/bash /code/runScriptImitateANNOVAR.sh "$@"

#======================================
# AnnotateBAMStatistics
#======================================

%apprun annotateBAMStatistics
exec /bin/bash /code/runScriptAnnotate.sh "$@"

#======================================
# AdditionalBAMStatistics
#======================================

%apprun additionalBAMStatistics
exec /bin/bash /code/runScriptAdditional.sh "$@"

#=====================================
# Filtering
#====================================

%apprun filtering
exec /bin/bash /code/runScriptFiltering.sh "$@"

%environment
export LC_ALL=C
```

## Collection

 - Name: [MathijsSanders/SangerLCMFilteringSingularity](https://github.com/MathijsSanders/SangerLCMFilteringSingularity)
 - License: None

