---
id: 910
name: "jekriske/git"
branch: "master"
tag: "2.15.0"
commit: "0f7a4876da6ab1aadabf67c8bc2ca1d5ed216c39"
version: "3f471dec8460239f2c4011ebdbbe3e77"
build_date: "2017-11-22T15:36:09.828Z"
size_mb: 212
size: 17182751
sif: "https://datasets.datalad.org/shub/jekriske/git/2.15.0/2017-11-22-0f7a4876-3f471dec/3f471dec8460239f2c4011ebdbbe3e77.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jekriske/git/2.15.0/2017-11-22-0f7a4876-3f471dec/
recipe: https://datasets.datalad.org/shub/jekriske/git/2.15.0/2017-11-22-0f7a4876-3f471dec/Singularity
collection: jekriske/git
---

# jekriske/git:2.15.0

```bash
$ singularity pull shub://jekriske/git:2.15.0
```

## Singularity Recipe

```singularity
BootStrap: docker
From: alpine:latest

%post
  echo http://dl-cdn.alpinelinux.org/alpine/edge/main > /etc/apk/repositories
  echo http://dl-cdn.alpinelinux.org/alpine/edge/community >> /etc/apk/repositories
  apk --no-cache add man openssh-client git git-doc git-subtree git-subtree-doc git-bash-completion git-fast-import openssl jq
  gitlfs_version=`wget -qO- 'https://raw.githubusercontent.com/git-lfs/git-lfs/master/versioninfo.json' | jq -r '.StringFileInfo.ProductVersion'`
  wget -qO- https://github.com/git-lfs/git-lfs/releases/download/v${gitlfs_version}/git-lfs-linux-amd64-${gitlfs_version}.tar.gz | tar -xz
  mv git-lfs*/git-lfs /usr/bin/ && rm -rf git-lfs-* && git lfs install
  apk del jq

%apprun git
  exec git "$@"

%runscript
  exec git "$@"

%help
  For help use --help
```

## Collection

 - Name: [jekriske/git](https://github.com/jekriske/git)
 - License: None

