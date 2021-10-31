---
id: 7730
name: "brucemoran/Singularity"
branch: "master"
tag: "aracne-ap.centos7"
commit: "b30f2442ae976bdf781048107efd8d4b7d6c11f4"
version: "e4953ac47e728fcffd015a5f1250eca3"
build_date: "2019-03-13T03:34:53.030Z"
size_mb: 910
size: 314417183
sif: "https://datasets.datalad.org/shub/brucemoran/Singularity/aracne-ap.centos7/2019-03-13-b30f2442-e4953ac4/e4953ac47e728fcffd015a5f1250eca3.simg"
url: https://datasets.datalad.org/shub/brucemoran/Singularity/aracne-ap.centos7/2019-03-13-b30f2442-e4953ac4/
recipe: https://datasets.datalad.org/shub/brucemoran/Singularity/aracne-ap.centos7/2019-03-13-b30f2442-e4953ac4/Singularity
collection: brucemoran/Singularity
---

# brucemoran/Singularity:aracne-ap.centos7

```bash
$ singularity pull shub://brucemoran/Singularity:aracne-ap.centos7
```

## Singularity Recipe

```singularity
Bootstrap:shub
From:brucemoran/Singularity:centos7-java8

%help
    Container for ARACNe-AP v0.1 30967ea10494fcb42c2bfd00604c94907da5397b

%post

    export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.201.b09-2.el7_6.x86_64

    ##install Apache ANT
    cd /usr/local
    wget https://www-eu.apache.org/dist/ant/binaries/apache-ant-1.9.13-bin.tar.gz
    tar -xf apache-ant-1.9.13-bin.tar.gz

    echo 'export ANT_HOME=/usr/local/apache-ant-1.9.13' >> $SINGULARITY_ENVIRONMENT
    echo 'export PATH=$PATH:${ANT_HOME}/bin' >> $SINGULARITY_ENVIRONMENT
    export ANT_HOME=/usr/local/apache-ant-1.9.13
    export PATH=$PATH:${ANT_HOME}/bin

    git clone https://github.com/califano-lab/ARACNe-AP
    cd ARACNe-AP
    git reset --hard 30967ea10494fcb42c2bfd00604c94907da5397b
    ant main

    ##create executable
    ##NB allows Xmx for resource allocation only
    chmod a+x /usr/local/ARACNe-AP/dist/aracne.jar
    echo -e "#! /bin/bash\njavamem=""\nif [[ \$1 =~ "-Xmx" ]];then javamem=\$1; shift 1; fi\nexec java \$javamem -jar /usr/local/ARACNe-AP/dist/aracne.jar "\$@"" > /usr/local/bin/ARACNe-AP
    chmod a+x /usr/local/bin/ARACNe-AP
```

## Collection

 - Name: [brucemoran/Singularity](https://github.com/brucemoran/Singularity)
 - License: None

