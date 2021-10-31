---
id: 2765
name: "d-w-moore/singularity-irods-icommands"
branch: "master"
tag: "latest"
commit: "165f6c2109a753baa6ea06130fc23affb70ae379"
version: "0ab02291ee6d9afe861c38733212b7dd"
build_date: "2020-06-07T09:16:14.063Z"
size_mb: 480
size: 174522399
sif: "https://datasets.datalad.org/shub/d-w-moore/singularity-irods-icommands/latest/2020-06-07-165f6c21-0ab02291/0ab02291ee6d9afe861c38733212b7dd.simg"
url: https://datasets.datalad.org/shub/d-w-moore/singularity-irods-icommands/latest/2020-06-07-165f6c21-0ab02291/
recipe: https://datasets.datalad.org/shub/d-w-moore/singularity-irods-icommands/latest/2020-06-07-165f6c21-0ab02291/Singularity
collection: d-w-moore/singularity-irods-icommands
---

# d-w-moore/singularity-irods-icommands:latest

```bash
$ singularity pull shub://d-w-moore/singularity-irods-icommands:latest
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

