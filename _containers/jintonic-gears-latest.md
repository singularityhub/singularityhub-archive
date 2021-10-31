---
id: 15322
name: "jintonic/gears"
branch: "master"
tag: "latest"
commit: "bbdbde21a3b518bbe73bce6f7a3a2f1a7062c528"
version: "bf81fc5635cbda478af08288bb151d6f"
build_date: "2021-01-21T04:25:51.939Z"
size_mb: 784.0
size: 329887775
sif: "https://datasets.datalad.org/shub/jintonic/gears/latest/2021-01-21-bbdbde21-bf81fc56/bf81fc5635cbda478af08288bb151d6f.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/jintonic/gears/latest/2021-01-21-bbdbde21-bf81fc56/
recipe: https://datasets.datalad.org/shub/jintonic/gears/latest/2021-01-21-bbdbde21-bf81fc56/Singularity
collection: jintonic/gears
---

# jintonic/gears:latest

```bash
$ singularity pull shub://jintonic/gears:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:ubuntu:latest

%labels
MAINTAINER jintonic

%post  
apt-get -y update
apt-get -y install rxvt-unicode vim vifm screen sc tmux w3m build-essential git cmake libx11-dev python3
git clone https://github.com/spack/spack.git
```

## Collection

 - Name: [jintonic/gears](https://github.com/jintonic/gears)
 - License: [MIT License](https://api.github.com/licenses/mit)

