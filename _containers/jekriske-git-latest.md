---
id: 909
name: "jekriske/git"
branch: "master"
tag: "latest"
commit: "0f7a4876da6ab1aadabf67c8bc2ca1d5ed216c39"
version: "a4942a407e99ea0688e9fcae41b5d4e2"
build_date: "2019-12-07T22:51:48.674Z"
size_mb: 37
size: 16457759
sif: "https://datasets.datalad.org/shub/jekriske/git/latest/2019-12-07-0f7a4876-a4942a40/a4942a407e99ea0688e9fcae41b5d4e2.simg"
url: https://datasets.datalad.org/shub/jekriske/git/latest/2019-12-07-0f7a4876-a4942a40/
recipe: https://datasets.datalad.org/shub/jekriske/git/latest/2019-12-07-0f7a4876-a4942a40/Singularity
collection: jekriske/git
---

# jekriske/git:latest

```bash
$ singularity pull shub://jekriske/git:latest
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

