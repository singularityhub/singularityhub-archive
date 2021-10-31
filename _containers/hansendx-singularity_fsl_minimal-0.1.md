---
id: 1649
name: "hansendx/singularity_fsl_minimal"
branch: "master"
tag: "0.1"
commit: "8146a3a95efa605f9defd740c4df909f9bd800da"
version: "2b28b320aea3eb46b5a200c2792e1a12"
build_date: "2020-01-08T19:37:27.184Z"
size_mb: 3393
size: 2921504799
sif: "https://datasets.datalad.org/shub/hansendx/singularity_fsl_minimal/0.1/2020-01-08-8146a3a9-2b28b320/2b28b320aea3eb46b5a200c2792e1a12.simg"
url: https://datasets.datalad.org/shub/hansendx/singularity_fsl_minimal/0.1/2020-01-08-8146a3a9-2b28b320/
recipe: https://datasets.datalad.org/shub/hansendx/singularity_fsl_minimal/0.1/2020-01-08-8146a3a9-2b28b320/Singularity
collection: hansendx/singularity_fsl_minimal
---

# hansendx/singularity_fsl_minimal:0.1

```bash
$ singularity pull shub://hansendx/singularity_fsl_minimal:0.1
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: stable
MirrorURL: http://ftp.us.debian.org/debian/

%post

apt-get update
apt-get install gnupg2 wget eatmydata -y 


wget -O- http://neuro.debian.net/lists/stretch.de-md.full | tee /etc/apt/sources.list.d/neurodebian.sources.list

while true; do
	apt-key adv --recv-keys --keyserver hkp://eu.pool.sks-keyservers.net:80 0xA5D32F012649A5A9 || continue
	break
done

# hkp://pool.sks-keyservers.net:80 0xA5D32F012649A5A9

apt-get update 

eatmydata apt-get install fsl-5.0-complete -y

cp /etc/fsl/5.0/fsl.sh /.singularity.d/env/90-environment.sh

#cleanup
apt-get purge gnupg2 wget eatmydata -y
apt-get autoclean -y
apt-get autoremove -y
rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [hansendx/singularity_fsl_minimal](https://github.com/hansendx/singularity_fsl_minimal)
 - License: None

