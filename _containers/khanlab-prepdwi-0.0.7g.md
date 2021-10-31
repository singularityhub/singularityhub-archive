---
id: 3001
name: "khanlab/prepdwi"
branch: "master"
tag: "0.0.7g"
commit: "6bb5ac1e7dc9c1a0a451d4f1d5de318a12621945"
version: "be4879da8cdb43118dc33afc0767d56a"
build_date: "2018-08-22T18:51:06.427Z"
size_mb: 15395
size: 6240780319
sif: "https://datasets.datalad.org/shub/khanlab/prepdwi/0.0.7g/2018-08-22-6bb5ac1e-be4879da/be4879da8cdb43118dc33afc0767d56a.simg"
url: https://datasets.datalad.org/shub/khanlab/prepdwi/0.0.7g/2018-08-22-6bb5ac1e-be4879da/
recipe: https://datasets.datalad.org/shub/khanlab/prepdwi/0.0.7g/2018-08-22-6bb5ac1e-be4879da/Singularity
collection: khanlab/prepdwi
---

# khanlab/prepdwi:0.0.7g

```bash
$ singularity pull shub://khanlab/prepdwi:0.0.7g
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: khanlab/neuroglia-dwi:v1.3.1


%labels
Maintainer "Ali Khan"

#########
%setup
#########
mkdir -p $SINGULARITY_ROOTFS/opt/prepdwi
cp -Rv . $SINGULARITY_ROOTFS/opt/prepdwi


#########
%post
#########


echo addpath\(genpath\(\'/opt/prepdwi/octave\'\)\)\; >> /etc/octave.conf 
apt-get install -y bc

#########
%environment
#########

export PATH=/opt/prepdwi/bin:$PATH

#########
%runscript
#########

exec /opt/prepdwi/prepdwi $@
```

## Collection

 - Name: [khanlab/prepdwi](https://github.com/khanlab/prepdwi)
 - License: None

