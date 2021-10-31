---
id: 7029
name: "brucemoran/Singularity"
branch: "master"
tag: "centos7-java8"
commit: "8f60228e961a43d5bcff6383b871bd67f68d9003"
version: "37a89617ba33c31e300dde041548eda4"
build_date: "2020-10-14T00:29:26.035Z"
size_mb: 843
size: 286138399
sif: "https://datasets.datalad.org/shub/brucemoran/Singularity/centos7-java8/2020-10-14-8f60228e-37a89617/37a89617ba33c31e300dde041548eda4.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/brucemoran/Singularity/centos7-java8/2020-10-14-8f60228e-37a89617/
recipe: https://datasets.datalad.org/shub/brucemoran/Singularity/centos7-java8/2020-10-14-8f60228e-37a89617/Singularity
collection: brucemoran/Singularity
---

# brucemoran/Singularity:centos7-java8

```bash
$ singularity pull shub://brucemoran/Singularity:centos7-java8
```

## Singularity Recipe

```singularity
Bootstrap:shub
From:brucemoran/Singularity:centos7

%post

    yum -y install java-1.8.0-openjdk-devel-1.8.0.201.b09-2.el7_6.x86_64

    ##update alternatives
    update-alternatives --install "/usr/bin/java" "java" "/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.201.b09-2.el7_6.x86_64/bin/java" 1

    echo 'export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.201.b09-2.el7_6.x86_64 PATH=$PATH:$JAVA_HOME/bin' >> $SINGULARITY_ENVIRONMENT
```

## Collection

 - Name: [brucemoran/Singularity](https://github.com/brucemoran/Singularity)
 - License: None

