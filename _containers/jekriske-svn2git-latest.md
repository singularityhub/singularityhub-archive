---
id: 947
name: "jekriske/svn2git"
branch: "master"
tag: "latest"
commit: "58aeabda39748c5a21ad1cf16f1d0fc83df44db9"
version: "e32da2ae2220d9fbf0a7ffa720ea70d6"
build_date: "2017-11-28T19:11:34.770Z"
size_mb: 273
size: 35340319
sif: "https://datasets.datalad.org/shub/jekriske/svn2git/latest/2017-11-28-58aeabda-e32da2ae/e32da2ae2220d9fbf0a7ffa720ea70d6.simg"
url: https://datasets.datalad.org/shub/jekriske/svn2git/latest/2017-11-28-58aeabda-e32da2ae/
recipe: https://datasets.datalad.org/shub/jekriske/svn2git/latest/2017-11-28-58aeabda-e32da2ae/Singularity
collection: jekriske/svn2git
---

# jekriske/svn2git:latest

```bash
$ singularity pull shub://jekriske/svn2git:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: alpine:latest

%post
  echo http://dl-cdn.alpinelinux.org/alpine/edge/main > /etc/apk/repositories
  echo http://dl-cdn.alpinelinux.org/alpine/edge/community >> /etc/apk/repositories
  apk --no-cache add man openssh-client git git-doc git-subtree git-subtree-doc git-svn perl-git-svn git-perl subversion ruby git-bash-completion git-fast-import openssl jq
  gitlfs_version=`wget -qO- 'https://raw.githubusercontent.com/git-lfs/git-lfs/master/versioninfo.json' | jq -r '.StringFileInfo.ProductVersion'`
  wget -qO- https://github.com/git-lfs/git-lfs/releases/download/v${gitlfs_version}/git-lfs-linux-amd64-${gitlfs_version}.tar.gz | tar -xz
  mv git-lfs*/git-lfs /usr/bin/ && rm -rf git-lfs-* && git lfs install
  apk del jq
  gem install svn2git --no-ri --no-rdoc

%apprun git
  exec git "$@"

%apprun svn
  exec svn "$@"

%apprun svn2git
  exec svn2git "$@"

%runscript
  exec svn2git "$@"

%help
  For help use --help
```

## Collection

 - Name: [jekriske/svn2git](https://github.com/jekriske/svn2git)
 - License: None

