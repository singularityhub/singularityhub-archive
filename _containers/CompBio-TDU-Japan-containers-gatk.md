---
id: 2303
name: "CompBio-TDU-Japan/containers"
branch: "master"
tag: "gatk"
commit: "076f50dcb4ec55d1c08ed1905e101579b20a46b1"
version: "4ce8f549c4d9f59b92f0c52d13466be5"
build_date: "2019-01-21T15:26:39.030Z"
size_mb: 1617
size: 793116703
sif: "https://datasets.datalad.org/shub/CompBio-TDU-Japan/containers/gatk/2019-01-21-076f50dc-4ce8f549/4ce8f549c4d9f59b92f0c52d13466be5.simg"
url: https://datasets.datalad.org/shub/CompBio-TDU-Japan/containers/gatk/2019-01-21-076f50dc-4ce8f549/
recipe: https://datasets.datalad.org/shub/CompBio-TDU-Japan/containers/gatk/2019-01-21-076f50dc-4ce8f549/Singularity
collection: CompBio-TDU-Japan/containers
---

# CompBio-TDU-Japan/containers:gatk

```bash
$ singularity pull shub://CompBio-TDU-Japan/containers:gatk
```

## Singularity Recipe

```singularity
Bootstrap: docker
FROM: broadinstitute/gatk:gatkbase-2.0.2

%post
    apt-get clean -y
    apt-get autoclean -y
    apt-get autoremove -y
    VERSION=4.0.12.0
    export JAVA_HOME=/usr/lib/jvm/java-1.8-openjdk
    wget https://github.com/broadinstitute/gatk/releases/download/$VERSION/gatk-$VERSION.zip
    unzip gatk-$VERSION.zip
    rm -f gatk-$VERSION.zip
    mv gatk-$VERSION /data/
    rm -r /data/gatkdoc
    ulimit -c unlimited
```

## Collection

 - Name: [CompBio-TDU-Japan/containers](https://github.com/CompBio-TDU-Japan/containers)
 - License: None

