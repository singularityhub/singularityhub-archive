---
id: 7119
name: "OSC/centos7-launcher"
branch: "master"
tag: "latest"
commit: "02a3f1d4b5581d4815c5d7fbc2b335f8c54898bd"
version: "b97ce30c2b35f67b28d7a6830dca5bbe"
build_date: "2021-04-19T17:49:24.286Z"
size_mb: 333
size: 104374303
sif: "https://datasets.datalad.org/shub/OSC/centos7-launcher/latest/2021-04-19-02a3f1d4-b97ce30c/b97ce30c2b35f67b28d7a6830dca5bbe.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/OSC/centos7-launcher/latest/2021-04-19-02a3f1d4-b97ce30c/
recipe: https://datasets.datalad.org/shub/OSC/centos7-launcher/latest/2021-04-19-02a3f1d4-b97ce30c/Singularity
collection: OSC/centos7-launcher
---

# OSC/centos7-launcher:latest

```bash
$ singularity pull shub://OSC/centos7-launcher:latest
```

## Singularity Recipe

```singularity
Bootstrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum

%labels
  Maintainer OSC Gateways

%help
This will run RStudio Server which must be mounted with dependencies into the container

%apprun rserver
  if ! [[ "$USER_PATH" = "" ]]; then
    export PATH="$USER_PATH"
  fi

  exec rserver "${@}"

%runscript
  if ! [[ "$USER_PATH" = "" ]]; then
    export PATH="$USER_PATH"
  fi

  exec rserver "${@}"

%post
yum install -y which
```

## Collection

 - Name: [OSC/centos7-launcher](https://github.com/OSC/centos7-launcher)
 - License: None

