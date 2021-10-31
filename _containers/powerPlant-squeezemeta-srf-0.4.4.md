---
id: 8991
name: "powerPlant/squeezemeta-srf"
branch: "master"
tag: "0.4.4"
commit: "f52357afd803c803d0b50fc064449b4f96c2e56d"
version: "b4ab8d499923b20fde8ddfc63e8192e8"
build_date: "2021-01-17T14:58:26.899Z"
size_mb: 2177
size: 826109983
sif: "https://datasets.datalad.org/shub/powerPlant/squeezemeta-srf/0.4.4/2021-01-17-f52357af-b4ab8d49/b4ab8d499923b20fde8ddfc63e8192e8.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/squeezemeta-srf/0.4.4/2021-01-17-f52357af-b4ab8d49/
recipe: https://datasets.datalad.org/shub/powerPlant/squeezemeta-srf/0.4.4/2021-01-17-f52357af-b4ab8d49/Singularity
collection: powerPlant/squeezemeta-srf
---

# powerPlant/squeezemeta-srf:0.4.4

```bash
$ singularity pull shub://powerPlant/squeezemeta-srf:0.4.4
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:7

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version v0.4.4

%post
## Install prerequisites
yum -y install epel-release
yum -y install ruby perl-Tie-IxHash perl-DBI perl-DBD-mysql perl-XML-LibXML perl-DBD-SQLite perl-Time-Piece python-pip python-matplotlib R wget
python -m pip install scipy dendropy pysam

## Install SqueezeMeta
export VERSION="0.4.4"
cd /opt
wget https://github.com/jtamames/SqueezeMeta/archive/v$VERSION.tar.gz
tar -xzf v$VERSION.tar.gz

## Install R dependencies
Rscript -e 'install.packages("doMC", repos="https://cloud.r-project.org/")'
Rscript -e 'install.packages("ggplot2", repos="https://cloud.r-project.org/")'
Rscript -e 'install.packages("data.table", repos="https://cloud.r-project.org/")'
R CMD INSTALL /opt/SqueezeMeta-$VERSION/bin/DAS_Tool/package/DASTool_1.1.1.tar.gz

## Configure data location (must be bind-mounted)
echo '{"dataRoot": "/media/db", "remoteManifestURL": "https://data.ace.uq.edu.au/public/CheckM_databases/", "manifestType": "CheckM", "localManifestName": ".dmanifest", "remoteManifestName": ".dmanifest"}' > /opt/SqueezeMeta-$VERSION/lib/checkm/DATA_CONFIG

cp -a /opt/SqueezeMeta-$VERSION/scripts/SqueezeMeta_conf_original.pl /opt/SqueezeMeta-$VERSION/scripts/SqueezeMeta_conf.pl
sed -i 's/^\$databasepath\=\"\$installpath/\$databasepath\=\"\/media/' /opt/SqueezeMeta-$VERSION/scripts/SqueezeMeta_conf.pl

## Cleanup
rm -f v$VERSION.tar.gz
yum -y clean all

%runscript
if [ ! -f /media/db/.dmanifest ]; then
  exec /bin/echo -e "This container requires that you bind mount the location of SqueezeMeta data into /media. Please use \"singularity run -B <path_to_squeezemedia_data>:/media $SINGULARITY_NAME\" and try again. You can download the latest version of the data files by running the \"download_databases.pl\" script. See https://github.com/jtamames/SqueezeMeta#3-downloading-or-building-databases for more information."
else
  exec perl /opt/SqueezeMeta-0.4.4/scripts/SqueezeMeta.pl "$@"
fi

%environment
export LANG=C
```

## Collection

 - Name: [powerPlant/squeezemeta-srf](https://github.com/powerPlant/squeezemeta-srf)
 - License: None

