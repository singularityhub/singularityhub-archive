---
id: 3980
name: "ebioman/SmrtLinkSingularity"
branch: "add-license-1"
tag: "v23_legacy"
commit: "f6e3184f6f3587d7edf69afe22624254db18c0ae"
version: "c2502970e0364392a4ec0746d416e2a1"
build_date: "2018-08-14T19:41:13.176Z"
size_mb: 2985
size: 1140916255
sif: "https://datasets.datalad.org/shub/ebioman/SmrtLinkSingularity/v23_legacy/2018-08-14-f6e3184f-c2502970/c2502970e0364392a4ec0746d416e2a1.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ebioman/SmrtLinkSingularity/v23_legacy/2018-08-14-f6e3184f-c2502970/
recipe: https://datasets.datalad.org/shub/ebioman/SmrtLinkSingularity/v23_legacy/2018-08-14-f6e3184f-c2502970/Singularity
collection: ebioman/SmrtLinkSingularity
---

# ebioman/SmrtLinkSingularity:v23_legacy

```bash
$ singularity pull shub://ebioman/SmrtLinkSingularity:v23_legacy
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:latest

%labels
Maintainer by Emanuel Schmid @ VITAL-IT
Version v2.3.0.140936


%help
This is the old PacBio collection of tools as in smrtlink version V2.3.0 for RSII data
        
%post

# install software
yum update -y -q && yum install -y -q \
        build-essential \
        gcc-multilib \
        libboost-all-dev \
        libhdf5-serial-dev \
        zlib1g-dev \
        pkg-config \
        wget \
        rsync \
        unzip \
        which \
        bzip2 \
        dirname
    


echo "add new user if not existent"
        
SMRT_USER=smrtanalysis
if ! grep -c "smrtanalysis:" /etc/passwd
then
        useradd  -g users -d /home/$SMRT_USER -s /bin/bash -p PacBio $SMRT_USER
else
        echo    "user already exists"
fi

echo "generate a new PacBio root directory and make smrtuser owner"

SMRT=/opt/pacbio
if [ ! -d $SMRT ]
then
        mkdir $SMRT
        chown smrtanalysis:users $SMRT
fi



echo "now switch to smrt-user"

su $SMRT_USER
SMRT=/opt/pacbio
SMRT_ROOT="/opt/pacbio/smrtlink"
cd $SMRT

echo "download and extract smrtlink"
wget -c https://downloads.pacbcloud.com/public/software/installers/smrtanalysis_2.3.0.140936.run --no-check-certificate
chmod +x smrtanalysis_2.3.0.140936.run 

if [ -d $SMRT_ROOT ] 
then 
        rm -rf $SMRT_ROOT
        ./smrtanalysis_2.3.0.140936.run --batch --rootdir $SMRT_ROOT --ignore-syscheck --extract-only   
else 
        ./smrtanalysis_2.3.0.140936.run --batch  --rootdir $SMRT_ROOT --ignore-syscheck --extract-only
fi

echo "cleaning up"
rm smrtanalysis_2.3.0.140936.run
%environment
export PATH=/opt/pacbio/smrtlink/install/smrtanalysis_2.3.0.140936/analysis/bin/:$PATH
%runscript
exec /bin/bash "$@"
```

## Collection

 - Name: [ebioman/SmrtLinkSingularity](https://github.com/ebioman/SmrtLinkSingularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

