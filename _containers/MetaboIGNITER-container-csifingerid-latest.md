---
id: 11249
name: "MetaboIGNITER/container-csifingerid"
branch: "master"
tag: "latest"
commit: "7e5c0c65c3331164c02787beec240c154adae4ea"
version: "2df8945b6073c36177e31487cb9548b5"
build_date: "2019-10-14T12:14:45.304Z"
size_mb: 746.0
size: 320073759
sif: "https://datasets.datalad.org/shub/MetaboIGNITER/container-csifingerid/latest/2019-10-14-7e5c0c65-2df8945b/2df8945b6073c36177e31487cb9548b5.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/MetaboIGNITER/container-csifingerid/latest/2019-10-14-7e5c0c65-2df8945b/
recipe: https://datasets.datalad.org/shub/MetaboIGNITER/container-csifingerid/latest/2019-10-14-7e5c0c65-2df8945b/Singularity
collection: MetaboIGNITER/container-csifingerid
---

# MetaboIGNITER/container-csifingerid:latest

```bash
$ singularity pull shub://MetaboIGNITER/container-csifingerid:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: metaboigniter/container-rbase:v3.4.1-1xenial0_cv0.2
%files
sirius-linux64-headless-4.0.1 /usr/local/bin/CSI
scripts/*.r /usr/local/bin/
runTest1.sh /usr/local/bin/runTest1.sh
%labels
software.version=4.0.1
version=4.0.1
software=CSIFingerID
MAINTAINER PhenoMeNal-H2020 Project ( phenomenal-h2020-users@googlegroups.com )
Description="Metabolite identification"
%post






R -e 'install.packages(c("R.utils","tools"),repos = "http://cran.us.r-project.org")'
# Update & upgrade sources
apt-get -y update

# Install development files needed
apt-get -y install wget default-jre-headless unzip

# Clean up
apt-get -y clean && apt-get -y autoremove && rm -rf /var/lib/{cache,log}/ /tmp/* /var/tmp/*



chmod +x /usr/local/bin/*.r

# Add testing to container
chmod +x /usr/local/bin/runTest1.sh

# Define Entry point script
#ENTRYPOINT ["java", "-cp", "/usr/local/bin/passatutto.jar"]
%runscript
exec /bin/bash "$@"
%startscript
exec /bin/bash "$@"
```

## Collection

 - Name: [MetaboIGNITER/container-csifingerid](https://github.com/MetaboIGNITER/container-csifingerid)
 - License: None

