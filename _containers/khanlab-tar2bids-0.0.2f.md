---
id: 5230
name: "khanlab/tar2bids"
branch: "master"
tag: "0.0.2f"
commit: "ce0f29ed2f19f235cf7887b7803b25585dfe5719"
version: "e58285669d25d06709d321cdf94bb0cb"
build_date: "2018-10-16T01:45:57.615Z"
size_mb: 2898
size: 919244831
sif: "https://datasets.datalad.org/shub/khanlab/tar2bids/0.0.2f/2018-10-16-ce0f29ed-e5828566/e58285669d25d06709d321cdf94bb0cb.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/khanlab/tar2bids/0.0.2f/2018-10-16-ce0f29ed-e5828566/
recipe: https://datasets.datalad.org/shub/khanlab/tar2bids/0.0.2f/2018-10-16-ce0f29ed-e5828566/Singularity
collection: khanlab/tar2bids
---

# khanlab/tar2bids:0.0.2f

```bash
$ singularity pull shub://khanlab/tar2bids:0.0.2f
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

