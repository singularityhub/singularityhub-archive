---
id: 4856
name: "LokiLuciferase/clusterdoom"
branch: "master"
tag: "latest"
commit: "33528bf4de6f50f6eeb842ad2987ac5661b95fd4"
version: "318f18213f93f993c07d161958dc2578"
build_date: "2019-12-28T23:41:01.164Z"
size_mb: 545
size: 256204831
sif: "https://datasets.datalad.org/shub/LokiLuciferase/clusterdoom/latest/2019-12-28-33528bf4-318f1821/318f18213f93f993c07d161958dc2578.simg"
url: https://datasets.datalad.org/shub/LokiLuciferase/clusterdoom/latest/2019-12-28-33528bf4-318f1821/
recipe: https://datasets.datalad.org/shub/LokiLuciferase/clusterdoom/latest/2019-12-28-33528bf4-318f1821/Singularity
collection: LokiLuciferase/clusterdoom
---

# LokiLuciferase/clusterdoom:latest

```bash
$ singularity pull shub://LokiLuciferase/clusterdoom:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: fedora:latest

%files
data/Doom1.WAD /opt
data/Doom2.WAD /opt
data/Doom3.WAD /opt

%post
    yum install chocolate-doom -y

%runscript
    dnum=$1
    exec chocolate-doom -iwad /opt/Doom$1.WAD
```

## Collection

 - Name: [LokiLuciferase/clusterdoom](https://github.com/LokiLuciferase/clusterdoom)
 - License: None

