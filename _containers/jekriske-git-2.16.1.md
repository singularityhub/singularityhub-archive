---
id: 1555
name: "jekriske/git"
branch: "master"
tag: "2.16.1"
commit: "a9855cf47e9db9b22ae8b511a41383fccbd6ae30"
version: "91367f450443846294fe0d87f8a24951"
build_date: "2018-02-01T11:37:39.920Z"
size_mb: 37
size: 16482335
sif: "https://datasets.datalad.org/shub/jekriske/git/2.16.1/2018-02-01-a9855cf4-91367f45/91367f450443846294fe0d87f8a24951.simg"
url: https://datasets.datalad.org/shub/jekriske/git/2.16.1/2018-02-01-a9855cf4-91367f45/
recipe: https://datasets.datalad.org/shub/jekriske/git/2.16.1/2018-02-01-a9855cf4-91367f45/Singularity
collection: jekriske/git
---

# jekriske/git:2.16.1

```bash
$ singularity pull shub://jekriske/git:2.16.1
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

