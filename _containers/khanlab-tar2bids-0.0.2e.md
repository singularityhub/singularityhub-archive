---
id: 5139
name: "khanlab/tar2bids"
branch: "master"
tag: "0.0.2e"
commit: "6c2cc9b5018eeb44d8758a5e75e86d173157c347"
version: "7be833ce68d33a14bcfd803021744dc9"
build_date: "2018-10-05T18:54:57.973Z"
size_mb: 2897
size: 918904863
sif: "https://datasets.datalad.org/shub/khanlab/tar2bids/0.0.2e/2018-10-05-6c2cc9b5-7be833ce/7be833ce68d33a14bcfd803021744dc9.simg"
url: https://datasets.datalad.org/shub/khanlab/tar2bids/0.0.2e/2018-10-05-6c2cc9b5-7be833ce/
recipe: https://datasets.datalad.org/shub/khanlab/tar2bids/0.0.2e/2018-10-05-6c2cc9b5-7be833ce/Singularity
collection: khanlab/tar2bids
---

# khanlab/tar2bids:0.0.2e

```bash
$ singularity pull shub://khanlab/tar2bids:0.0.2e
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: khanlab/heudiconv:0.4.3a


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

export PYTHONPATH=$PYTHONPATH:/opt/tar2bids/heuristics

%runscript
exec /opt/tar2bids/tar2bids $@
```

## Collection

 - Name: [khanlab/tar2bids](https://github.com/khanlab/tar2bids)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

