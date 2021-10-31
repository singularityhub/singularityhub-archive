---
id: 12274
name: "thakk/Score-client"
branch: "master"
tag: "latest"
commit: "531741892967bb07a6f8570ad33dd1700c130b42"
version: "40d45f50fac70829a514b1db7dff2555"
build_date: "2020-02-13T13:48:25.683Z"
size_mb: 236.0
size: 108412959
sif: "https://datasets.datalad.org/shub/thakk/Score-client/latest/2020-02-13-53174189-40d45f50/40d45f50fac70829a514b1db7dff2555.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/thakk/Score-client/latest/2020-02-13-53174189-40d45f50/
recipe: https://datasets.datalad.org/shub/thakk/Score-client/latest/2020-02-13-53174189-40d45f50/Singularity
collection: thakk/Score-client
---

# thakk/Score-client:latest

```bash
$ singularity pull shub://thakk/Score-client:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: alpine:3.10.3
Stage: release

%post
    apk update
	apk add bash
	apk add fuse
	apk add fuse-dev
	apk add openjdk11-jdk
	apk add wget
	apk add curl

%appinstall scoreclient
	wget -O score-client-2.2.1.tar.gz https://artifacts.oicr.on.ca/artifactory/dcc-release/bio/overture/score-client/2.2.1/score-client-2.2.1-dist.tar.gz
	tar zxvf score-client-2.2.1.tar.gz
	rm score-client-2.2.1.tar.gz
	mv score-client-2.2.1 /usr/local/score-client
		
%apphelp scoreclient
	Score-client

%apprun scoreclient
	java -Xmx3G --illegal-access=deny -Dlogging.path=/tmp -Dspring.config.additional-location=/usr/local/score-client/conf/ -Dlogging.config=/usr/local/score-client/conf/logback.xml -cp /usr/local/score-client/lib/score-client.jar org.springframework.boot.loader.JarLauncher help

%labels
	Author "tomi.hakkinen@tuni.fi"
	Version 1.0
```

## Collection

 - Name: [thakk/Score-client](https://github.com/thakk/Score-client)
 - License: None

