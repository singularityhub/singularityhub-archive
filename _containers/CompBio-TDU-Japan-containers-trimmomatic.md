---
id: 5618
name: "CompBio-TDU-Japan/containers"
branch: "master"
tag: "trimmomatic"
commit: "58478a9f251d425fc6f576e300ac0cf22907274b"
version: "f2b43e7d24aeb87e7f15b975cc561873"
build_date: "2018-11-16T10:50:05.350Z"
size_mb: 111
size: 73441311
sif: "https://datasets.datalad.org/shub/CompBio-TDU-Japan/containers/trimmomatic/2018-11-16-58478a9f-f2b43e7d/f2b43e7d24aeb87e7f15b975cc561873.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/CompBio-TDU-Japan/containers/trimmomatic/2018-11-16-58478a9f-f2b43e7d/
recipe: https://datasets.datalad.org/shub/CompBio-TDU-Japan/containers/trimmomatic/2018-11-16-58478a9f-f2b43e7d/Singularity
collection: CompBio-TDU-Japan/containers
---

# CompBio-TDU-Japan/containers:trimmomatic

```bash
$ singularity pull shub://CompBio-TDU-Japan/containers:trimmomatic
```

## Singularity Recipe

```singularity
Bootstrap: docker
FROM: openjdk:alpine

%post
    apk add --update --no-cache bash
    wget http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-0.36.zip
    unzip Trimmomatic-0.36.zip
    rm Trimmomatic-0.36.zip
    mv Trimmomatic-0.36 /data/

%runscript
    java -jar /data/trimmomatic-0.36.jar "$@"
```

## Collection

 - Name: [CompBio-TDU-Japan/containers](https://github.com/CompBio-TDU-Japan/containers)
 - License: None

