---
id: 6254
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "apollo_2.2.0"
commit: "1a59932d981be6f596394e40aebe7866da6b6f42"
version: "6e34769fcf62ae0bce3d441de5228dbe"
build_date: "2019-01-16T07:21:11.412Z"
size_mb: 3115
size: 1441058847
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/apollo_2.2.0/2019-01-16-1a59932d-6e34769f/6e34769fcf62ae0bce3d441de5228dbe.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/singularity-containers/apollo_2.2.0/2019-01-16-1a59932d-6e34769f/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/apollo_2.2.0/2019-01-16-1a59932d-6e34769f/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:apollo_2.2.0

```bash
$ singularity pull shub://TomHarrop/singularity-containers:apollo_2.2.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%help
    GMOD Apollo 2.2.0 

%labels
    MAINTAINER "Tom Harrop"
    VERSION "Apollo 2.2.0"

%post
    # versions
    export WEBAPOLLO_VERSION="37b4063baeaf24021445ca581701f230b3b5df41"
    export APOLLO_DOCKER_VERSION="606ce6ffbd378250f2a5459118afc3824539bcef"

    # deps
    apt-get update --fix-missing
    apt-get install -y \
        ant \
        build-essential \
        curl \
        git \
        libexpat1-dev \
        language-pack-en \
        libpng-dev \
        libpq-dev \
        maven \
        nano \
        netcat \
        openjdk-8-jdk \
        postgresql \
        postgresql-client \
        postgresql-common \
        ssl-cert \
        tomcat8 \
        unzip \
        wget \
        xmlstarlet \
        zip \
        zlib1g-dev

    # install node.js
    curl -sL https://deb.nodesource.com/setup_8.x | bash -
    apt-get update --fix-missing
    apt-get install -y \
        nodejs
    apt-get autoremove -y
    apt-get clean

    # select java 8 but ignore errors
    export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/
    update-java-alternatives \
        --set java-1.8.0-openjdk-amd64 \
        || true
    cp \
        /usr/lib/jvm/java-8-openjdk-amd64/lib/tools.jar \
        /usr/lib/jvm/java-8-openjdk-amd64/jre/lib/ext/tools.jar

    # download apollo
    useradd -ms /bin/bash -d /apollo apollo
    curl -L \
        https://github.com/GMOD/Apollo/archive/${WEBAPOLLO_VERSION}.tar.gz \
        | tar xzf - --strip-components=1 -C /apollo

    # download blat
    curl -s \
        "http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/blat/blat" \
        -o /usr/local/bin/blat
    chmod +x /usr/local/bin/blat

    # install yarn
    npm i -g yarn

    # download apollo bits and pieces
    wget \
        -O /apollo/apollo-config.groovy \
        https://raw.githubusercontent.com/GMOD/docker-apollo/${APOLLO_DOCKER_VERSION}/apollo-config.groovy
    wget \
        -O /build.sh \
        https://raw.githubusercontent.com/GMOD/docker-apollo/${APOLLO_DOCKER_VERSION}/build.sh
    chown -R apollo:apollo /apollo

    # install grails etc
    su apollo bash -c 'cd ; curl -s get.sdkman.io | bash'
    su apollo bash -c 'cd ; source /apollo/.sdkman/bin/sdkman-init.sh && yes | sdk install grails 2.5.5'
    su apollo bash -c 'cd ; source /apollo/.sdkman/bin/sdkman-init.sh && yes | sdk install gradle 3.2.1'

    # build apollo (fails intermittently downloading electron)
    rm /apollo/apollo-config.groovy
    cp /apollo/sample-postgres-apollo-config.groovy /apollo/apollo-config.groovy
    chown apollo:apollo /apollo/apollo-config.groovy
    su apollo bash -c 'cd /apollo ; source /apollo/.sdkman/bin/sdkman-init.sh ; ./apollo clean-all ; ./apollo deploy 2>&1 | tee deploy.log'

    # check database credentials in apollo-config.groovy
    # service postgresql start
    # add user to postgresql, e.g. su postgres ; createuser -RDIElPS test
    # initialise db, e.g. su postgres ; createdb apollo-production apollo-production
    # service postgresql restart
    # service tomcat8 restart

    # set tomcat8 user/group in /etc/default
    # set postresql user/group ?/etc/postgresql/10/main/environment


%startscript
    su apollo bash -c 'cd ; source /apollo/.sdkman/bin/sdkman-init.sh ; /apollo/apollo run-local'

%environment
    export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

