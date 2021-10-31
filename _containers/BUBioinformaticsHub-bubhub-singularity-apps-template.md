---
id: 5239
name: "BUBioinformaticsHub/bubhub-singularity-apps"
branch: "master"
tag: "template"
commit: "8166e4a2c15de95410ccf1ae1d84c2d790b07baf"
version: "91d7f6df79d3c1baadfd27b32572075d"
build_date: "2018-10-16T23:20:50.103Z"
size_mb: 351
size: 135483423
sif: "https://datasets.datalad.org/shub/BUBioinformaticsHub/bubhub-singularity-apps/template/2018-10-16-8166e4a2-91d7f6df/91d7f6df79d3c1baadfd27b32572075d.simg"
url: https://datasets.datalad.org/shub/BUBioinformaticsHub/bubhub-singularity-apps/template/2018-10-16-8166e4a2-91d7f6df/
recipe: https://datasets.datalad.org/shub/BUBioinformaticsHub/bubhub-singularity-apps/template/2018-10-16-8166e4a2-91d7f6df/Singularity
collection: BUBioinformaticsHub/bubhub-singularity-apps
---

# BUBioinformaticsHub/bubhub-singularity-apps:template

```bash
$ singularity pull shub://BUBioinformaticsHub/bubhub-singularity-apps:template
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:latest

%help
echo "Usage: singularity run "


%runscript
$@


%post
apt-get update --fix-missing
apt-get --no-install-recommends -y install \
    git build-essential wget unzip ca-certificates

# squelch perl complaining about locale settings it doesn't understand
LANG=C
LANGUAGE=$LANG
LC_ALL=$LANG
export LANG LANGUAGE LC_ALL

# these are specific to scc
# create the directories in case OverlayFS support wasn't built in
for d in /scratch /share /project /projectnb /restricted /usr1 /usr2 /usr3 /usr4 /var/spool/sge;
do
  rm -rf $d
  mkdir $d
done
```

## Collection

 - Name: [BUBioinformaticsHub/bubhub-singularity-apps](https://github.com/BUBioinformaticsHub/bubhub-singularity-apps)
 - License: None

