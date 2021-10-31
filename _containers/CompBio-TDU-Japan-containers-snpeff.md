---
id: 2305
name: "CompBio-TDU-Japan/containers"
branch: "master"
tag: "snpeff"
commit: "68ea77101b3b0fd5937328277b74e69fcc0a9746"
version: "bce05d30cf40b4624a1adc63d157ab36"
build_date: "2018-03-27T03:22:06.198Z"
size_mb: 264
size: 143441951
sif: "https://datasets.datalad.org/shub/CompBio-TDU-Japan/containers/snpeff/2018-03-27-68ea7710-bce05d30/bce05d30cf40b4624a1adc63d157ab36.simg"
url: https://datasets.datalad.org/shub/CompBio-TDU-Japan/containers/snpeff/2018-03-27-68ea7710-bce05d30/
recipe: https://datasets.datalad.org/shub/CompBio-TDU-Japan/containers/snpeff/2018-03-27-68ea7710-bce05d30/Singularity
collection: CompBio-TDU-Japan/containers
---

# CompBio-TDU-Japan/containers:snpeff

```bash
$ singularity pull shub://CompBio-TDU-Japan/containers:snpeff
```

## Singularity Recipe

```singularity
Bootstrap: docker
FROM: openjdk:alpine

%post
    apk --update --no-cache add bash
    wget https://jaist.dl.sourceforge.net/project/snpeff/snpEff_latest_core.zip
    unzip snpEff_latest_core.zip
    rm -rf snpEff_latest_core.zip
    sed -i "s/.\/data\/$/~\/\.snpEff\/data/g" /snpEff/snpEff.config

%runscript
    /snpEff/scripts/snpEff "$@"
```

## Collection

 - Name: [CompBio-TDU-Japan/containers](https://github.com/CompBio-TDU-Japan/containers)
 - License: None

