---
id: 12521
name: "MetaboIGNITER/container-metfrag-cli-batch"
branch: "develop"
tag: "latest"
commit: "d3a529da5464d438f14637d87e1db538c6bb23dc"
version: "2e21a4081e05cb25d6bfd236fb423696"
build_date: "2020-03-13T12:15:35.617Z"
size_mb: 287.0
size: 140685343
sif: "https://datasets.datalad.org/shub/MetaboIGNITER/container-metfrag-cli-batch/latest/2020-03-13-d3a529da-2e21a408/2e21a4081e05cb25d6bfd236fb423696.sif"
url: https://datasets.datalad.org/shub/MetaboIGNITER/container-metfrag-cli-batch/latest/2020-03-13-d3a529da-2e21a408/
recipe: https://datasets.datalad.org/shub/MetaboIGNITER/container-metfrag-cli-batch/latest/2020-03-13-d3a529da-2e21a408/Singularity
collection: MetaboIGNITER/container-metfrag-cli-batch
---

# MetaboIGNITER/container-metfrag-cli-batch:latest

```bash
$ singularity pull shub://MetaboIGNITER/container-metfrag-cli-batch:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: quay.io/biocontainers/metfrag:2.4.5--1
%files
runTest1.sh /usr/local/bin/runTest1.sh
metfrag.sh /usr/local/bin/metfrag.sh
run_metfrag.sh /usr/local/bin/run_metfrag.sh
%labels
software.version=2.4.5
version=0.9
software=metfrag-cli-batch
MAINTAINER PhenoMeNal-H2020 Project ( phenomenal-h2020-users@googlegroups.com )
Description="MetFrag command line interface for batch processing."
%post
#FROM ubuntu:16.04




# Update & upgrade sources
#RUN apt-get -y update

# Install development files needed
#RUN apt-get -y install wget openjdk-8-jdk-headless parallel zip 

# Clean up
#RUN apt-get -y clean && apt-get -y autoremove && rm -rf /var/lib/{cache,log}/ /tmp/* /var/tmp/*

# Install MetFrag
#RUN wget -O /usr/local/bin/MetFragCLI.jar http://msbi.ipb-halle.de/~cruttkie/92f73acb731145c73ffa3dfb8fd59581bee0d844963889338c3ec173874b5a5f/MetFrag-2.4.3.jar

wget http://central.maven.org/maven2/net/sf/jni-inchi/jni-inchi/0.8/jni-inchi-0.8.jar && mkdir -p /root/.jnati/repo/ && jar xf jni-inchi-0.8.jar && mv META-INF/jniinchi /root/.jnati/repo/

# Add testing to container
chmod +x /usr/local/bin/runTest1.sh

# Add metfrag.sh
chmod +x /usr/local/bin/metfrag.sh

# Add run_metfrag.sh
chmod +x /usr/local/bin/run_metfrag.sh

# Define Entry point script

%runscript
exec metfrag "$@"
%startscript
exec metfrag "$@"
```

## Collection

 - Name: [MetaboIGNITER/container-metfrag-cli-batch](https://github.com/MetaboIGNITER/container-metfrag-cli-batch)
 - License: None

