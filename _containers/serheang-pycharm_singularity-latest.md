---
id: 10289
name: "serheang/pycharm_singularity"
branch: "master"
tag: "latest"
commit: "99b018df538629df9a0c932c729a1659d98967d9"
version: "b921e92e99d7850327bb40d4853d30df05d6f694fdb712a0a3f68fdd04e58c0b"
build_date: "2019-09-27T06:13:47.216Z"
size_mb: 484.453125
size: 507985920
sif: "https://datasets.datalad.org/shub/serheang/pycharm_singularity/latest/2019-09-27-99b018df-b921e92e/b921e92e99d7850327bb40d4853d30df05d6f694fdb712a0a3f68fdd04e58c0b.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/serheang/pycharm_singularity/latest/2019-09-27-99b018df-b921e92e/
recipe: https://datasets.datalad.org/shub/serheang/pycharm_singularity/latest/2019-09-27-99b018df-b921e92e/Singularity
collection: serheang/pycharm_singularity
---

# serheang/pycharm_singularity:latest

```bash
$ singularity pull shub://serheang/pycharm_singularity:latest
```

## Singularity Recipe

```singularity
bootstrap: docker
from:alpine:latest

%labels
  MAINTAINER setan
  WHATAMI pycharm-edu
  VERSION 2019.2

%environment
  export PATH=/usr/local/bin:$PATH

%post
  export PYCHARM="pycharm-edu-2019.2.1"
  apk update
  apk add wget 
  apk add python py-pip 
  apk add python3 py3-pip 
  apk add openjdk11-jre
  apk add libcanberra-gtk3
  apk add xfce4 xfce4-terminal
  ## PREP
  rm -rf /opt/${PYCHARM}
  rm -f /opt/pycharm
  rm -f /usr/local/bin/pycharm
  rm -f /usr/local/bin/inspect

  ## Get PyCharm
  wget https://download.jetbrains.com/python/${PYCHARM}.tar.gz
  tar zxvf ${PYCHARM}.tar.gz -C /opt
  ln -s /opt/${PYCHARM} /opt/pycharm
  ln -s /opt/pycharm/bin/pycharm.sh /usr/local/bin/pycharm
  ln -s /opt/pycharm/bin/inspect.sh /usr/local/bin/inspect

  ## CLEANUP
  rm ${PYCHARM}.tar.gz

%runscript
  echo "Run Pycharm in alpine container"
  ## piping error to /dev/null to reduce clutter on screen
  /opt/pycharm/bin/pycharm.sh 2>/dev/null
```

## Collection

 - Name: [serheang/pycharm_singularity](https://github.com/serheang/pycharm_singularity)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

