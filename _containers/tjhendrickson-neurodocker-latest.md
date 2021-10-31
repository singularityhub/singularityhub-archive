---
id: 3953
name: "tjhendrickson/neurodocker"
branch: "master"
tag: "latest"
commit: "2bf06abef26016d5d6976b797a0f98731634457d"
version: "0546df693f173e36abd3984c1b2a1830"
build_date: "2018-08-13T16:19:56.982Z"
size_mb: 199
size: 68526111
sif: "https://datasets.datalad.org/shub/tjhendrickson/neurodocker/latest/2018-08-13-2bf06abe-0546df69/0546df693f173e36abd3984c1b2a1830.simg"
url: https://datasets.datalad.org/shub/tjhendrickson/neurodocker/latest/2018-08-13-2bf06abe-0546df69/
recipe: https://datasets.datalad.org/shub/tjhendrickson/neurodocker/latest/2018-08-13-2bf06abe-0546df69/Singularity
collection: tjhendrickson/neurodocker
---

# tjhendrickson/neurodocker:latest

```bash
$ singularity pull shub://tjhendrickson/neurodocker:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: alpine:3.7


%post
mkdir /opt
cd /opt
tmp_pkgs="curl gcc musl-dev python3-dev sqlite-dev git" 
apk add --update --no-cache git python3 py3-yaml rsync $tmp_pkgs 
git clone  https://github.com/kaczmarj/neurodocker.git
curl -fsSL https://bootstrap.pypa.io/get-pip.py | python3 - 
pip install --no-cache-dir reprozip 
#apk del $tmp_pkgs 
#rm -rf /var/cache/apk/* ~/.cache/pip/*

pip install --no-cache-dir -e /opt/neurodocker 
#neurodocker --help

%runscript
neurodocker
```

## Collection

 - Name: [tjhendrickson/neurodocker](https://github.com/tjhendrickson/neurodocker)
 - License: [Apache License 2.0](https://api.github.com/licenses/apache-2.0)

