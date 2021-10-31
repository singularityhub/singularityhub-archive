---
id: 3421
name: "khanlab/tar2bids"
branch: "master"
tag: "0.0.2d"
commit: "d136876bf7b1581d1d05238adb303d7f25272e81"
version: "d31017cfb5d0d7d61f49b36f5775f545"
build_date: "2020-02-11T10:50:41.673Z"
size_mb: 2762
size: 906711071
sif: "https://datasets.datalad.org/shub/khanlab/tar2bids/0.0.2d/2020-02-11-d136876b-d31017cf/d31017cfb5d0d7d61f49b36f5775f545.simg"
url: https://datasets.datalad.org/shub/khanlab/tar2bids/0.0.2d/2020-02-11-d136876b-d31017cf/
recipe: https://datasets.datalad.org/shub/khanlab/tar2bids/0.0.2d/2020-02-11-d136876b-d31017cf/Singularity
collection: khanlab/tar2bids
---

# khanlab/tar2bids:0.0.2d

```bash
$ singularity pull shub://khanlab/tar2bids:0.0.2d
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

