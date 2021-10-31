---
id: 2755
name: "khanlab/tar2bids"
branch: "master"
tag: "0.0.2a"
commit: "ce177bb227485005d2acfa1e0dd546240306b967"
version: "42199ef7f869162f26762491759ea24d"
build_date: "2018-05-10T14:15:20.096Z"
size_mb: 2708
size: 876892191
sif: "https://datasets.datalad.org/shub/khanlab/tar2bids/0.0.2a/2018-05-10-ce177bb2-42199ef7/42199ef7f869162f26762491759ea24d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/khanlab/tar2bids/0.0.2a/2018-05-10-ce177bb2-42199ef7/
recipe: https://datasets.datalad.org/shub/khanlab/tar2bids/0.0.2a/2018-05-10-ce177bb2-42199ef7/Singularity
collection: khanlab/tar2bids
---

# khanlab/tar2bids:0.0.2a

```bash
$ singularity pull shub://khanlab/tar2bids:0.0.2a
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: khanlab/heudiconv:0.4.3

%setup
mkdir -p $SINGULARITY_ROOTFS/opt/tar2bids
cp -Rv . $SINGULARITY_ROOTFS/opt/tar2bids

%post

## Install bids-validator
apt-get update && \
apt-get install -y curl git && \
curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
apt-get remove -y curl && \
apt-get install -y nodejs && \
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

git clone http://github.com/INCF/bids-validator /opt/bids-validator
cd /opt/bids-validator
TAG=0.26.5
git checkout $TAG
sed -i -E "s/0.0.0/$TAG/" package.json
npm install -g /opt/bids-validator


#install gnu parallel
apt-get update
apt-get install -y parallel


#need the below to avoid warnings when running gnu-parallel
apt-get install -y locales
echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
echo "LANG=en_US.UTF-8" > /etc/locale.conf
echo "LC_ALL=en_US.UTF-8" >> /etc/locale.conf
locale-gen en_US.UTF-8


%environment
export LANGUAGE="en_US.UTF-8"
export LC_ALL="en_US.UTF-8"
export LANG="en_US.UTF-8"


%runscript
exec /opt/tar2bids/tar2bids $@
```

## Collection

 - Name: [khanlab/tar2bids](https://github.com/khanlab/tar2bids)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

