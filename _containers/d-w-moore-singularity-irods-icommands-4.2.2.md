---
id: 2764
name: "d-w-moore/singularity-irods-icommands"
branch: "master"
tag: "4.2.2"
commit: "e3214a75c6181f5bbb1cee1697f7768bc647110b"
version: "6a78ed58f086f1e6666c935c1dbfdd66"
build_date: "2018-05-11T08:00:01.470Z"
size_mb: 480
size: 174522399
sif: "https://datasets.datalad.org/shub/d-w-moore/singularity-irods-icommands/4.2.2/2018-05-11-e3214a75-6a78ed58/6a78ed58f086f1e6666c935c1dbfdd66.simg"
url: https://datasets.datalad.org/shub/d-w-moore/singularity-irods-icommands/4.2.2/2018-05-11-e3214a75-6a78ed58/
recipe: https://datasets.datalad.org/shub/d-w-moore/singularity-irods-icommands/4.2.2/2018-05-11-e3214a75-6a78ed58/Singularity
collection: d-w-moore/singularity-irods-icommands
---

# d-w-moore/singularity-irods-icommands:4.2.2

```bash
$ singularity pull shub://d-w-moore/singularity-irods-icommands:4.2.2
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: xenial
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%help
  iRODS Version 4.2.2

  $ singularity run icommands.4.2.2.simg [icommand] [args]
  $ singularity run --app iinit icommands.4.2.2.simg
  $ singularity run --app iinit icommands.4.2.2.simg [args]
    Where [args] in
    --irods_host String
    --irods_port Integer
    --irods_user_name String
    --irods_zone_name String
    --irods_password String
    --irods_default_resource String
    --irods_home String

%setup
  mkdir -p ${SINGULARITY_ROOTFS}/code

%files
  iinit.sh /code/iinit.sh

%labels
  Maintainer Michael J. Stealey
  Maintainer_Email stealey@renci.org
  iRODS_Version 4.2.2

%environment
  export IRODS_VERSION=4.2.2

%post
  export IRODS_VERSION=4.2.2
  apt-get update
  apt-get install -y \
    wget \
    sudo \
    apt-transport-https
  wget https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64
  chmod +x jq-linux64
  mv jq-linux64 /usr/bin/jq
  wget -qO - https://packages.irods.org/irods-signing-key.asc | \
    sudo apt-key add -
  echo "deb [arch=amd64] https://packages.irods.org/apt/ xenial main" | \
    sudo tee /etc/apt/sources.list.d/renci-irods.list
  apt-get update
  apt-get install -y \
    irods-icommands=${IRODS_VERSION} \
    libxml2

%apprun iinit
  exec /bin/bash /code/iinit.sh "${@}"

%runscript
  exec "${@}"

%test
  exec ihelp
```

## Collection

 - Name: [d-w-moore/singularity-irods-icommands](https://github.com/d-w-moore/singularity-irods-icommands)
 - License: [MIT License](https://api.github.com/licenses/mit)

