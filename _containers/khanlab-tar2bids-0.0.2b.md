---
id: 2787
name: "khanlab/tar2bids"
branch: "master"
tag: "0.0.2b"
commit: "36a95829eecd6efe11969ecfdc8d5413d344fbc9"
version: "5b3a7f9c5b7dfa372307370e19685c10"
build_date: "2018-05-15T04:45:29.765Z"
size_mb: 2761
size: 905789471
sif: "https://datasets.datalad.org/shub/khanlab/tar2bids/0.0.2b/2018-05-15-36a95829-5b3a7f9c/5b3a7f9c5b7dfa372307370e19685c10.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/khanlab/tar2bids/0.0.2b/2018-05-15-36a95829-5b3a7f9c/
recipe: https://datasets.datalad.org/shub/khanlab/tar2bids/0.0.2b/2018-05-15-36a95829-5b3a7f9c/Singularity
collection: khanlab/tar2bids
---

# khanlab/tar2bids:0.0.2b

```bash
$ singularity pull shub://khanlab/tar2bids:0.0.2b
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


%runscript
exec /opt/tar2bids/tar2bids $@
```

## Collection

 - Name: [khanlab/tar2bids](https://github.com/khanlab/tar2bids)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

