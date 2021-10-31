---
id: 7776
name: "sbilge/ClinVAP"
branch: "master"
tag: "report"
commit: "490dbe8a3e9282b3d8bf539b282eade2592009c5"
version: "dfaa12040130992aa7e5399213c6b9a5"
build_date: "2019-03-14T15:44:01.582Z"
size_mb: 3126
size: 1154015263
sif: "https://datasets.datalad.org/shub/sbilge/ClinVAP/report/2019-03-14-490dbe8a-dfaa1204/dfaa12040130992aa7e5399213c6b9a5.simg"
url: https://datasets.datalad.org/shub/sbilge/ClinVAP/report/2019-03-14-490dbe8a-dfaa1204/
recipe: https://datasets.datalad.org/shub/sbilge/ClinVAP/report/2019-03-14-490dbe8a-dfaa1204/Singularity
collection: sbilge/ClinicalReportingPipeline
---

# sbilge/ClinVAP:report

```bash
$ singularity pull shub://sbilge/ClinVAP:report
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ensemblorg/ensembl-vep:release_93


%files
vep_docker.ini /opt/vep/
make_report.sh /opt/vep
reporting.R /opt/vep
driver_db_dump.json /opt/vep
clinicalreporting_docxtemplater /opt/vep/clinicalreporting_docxtemplater

%labels
Maintainer sueruen@informatik.uni-tuebingen.de
Version V93

%post
# download plugin and fixing VEP base version 93. 
mkdir -p /opt/vep/.vep/Plugins
chmod 755 /opt/vep/.vep/Plugins

useradd -r -m -U -d /opt/plugin -s /bin/bash -c "VEP User" -p '' veplugin
usermod -a -G sudo veplugin
su -c "perl /opt/vep/src/ensembl-vep/INSTALL.pl -n -a p -g LoFtool" veplugin

cp /opt/plugin/.vep/Plugins/LoFtool.pm /opt/vep/.vep/Plugins
cp /opt/plugin/.vep/Plugins/plugin_config.txt /opt/vep/.vep/Plugins

# install R
sh -c 'echo "deb http://cran.rstudio.com/bin/linux/ubuntu xenial/" >> /etc/apt/sources.list' && \
  sh -c 'echo "deb http://ftp.halifax.rwth-aachen.de/ubuntu xenial-backports main restricted universe" >> /etc/apt/sources.list' && \
  gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9 && \
  gpg -a --export E084DAB9 | apt-key add -

apt-get -y update && \
  apt-get install -y r-base libxml2-dev libcurl4-openssl-dev libssh2-1-dev libcairo2-dev samtools libpq-dev nodejs npm libreoffice
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# install R packages
Rscript -e 'install.packages(c("dplyr", "dtplyr", "tidyr", "stringr", "splitstackshape", "optparse", "readr", "RCurl", "devtools", "log4r", "futile.logger", "fs"), dependencies = TRUE, repos = "https://cloud.r-project.org")'
Rscript -e 'devtools::install_github("colearendt/tidyjson@d79f3ff0a3279adef07819af4ab572f9ba46f3c0")'
Rscript -e 'devtools::install_github("aryoda/tryCatchLog@aa115fe2bd7b6569492eb0a9673f028ee6ec40a2")'
Rscript -e 'source("https://bioconductor.org/biocLite.R"); biocLite(c("VariantAnnotation", "rjson"), ask = FALSE, suppressUpdates = TRUE)'


# install LoFtool plugin
cd /opt/vep
wget https://github.com/konradjk/loftee/archive/v0.3-beta.zip 
unzip v0.3-beta.zip
rm v0.3-beta.zip
cp loftee-0.3-beta/LoF.pm /opt/vep/.vep/Plugins

# this is required for loftee-0.3-beta
cpanm DBD::SQLite
echo 'export PERL5LIB=/opt/vep/loftee-0.3-beta/:$PERL5LIB' >> $SINGULARITY_ENVIRONMENT

# install packages for clinicalreporting_docxtemplater
cd /opt/vep/clinicalreporting_docxtemplater && \
npm install

# make scripts executable
cd /opt/vep && \
chmod +x make_report.sh reporting.R

## put ini file in its default location with its default name
mv vep_docker.ini  vep.ini && \
mv vep.ini /opt/vep/.vep

%runscript
exec /bin/bash /opt/vep/make_report.sh "$@"
```

## Collection

 - Name: [sbilge/ClinVAP](https://github.com/sbilge/ClinVAP)
 - License: [MIT License](https://api.github.com/licenses/mit)

