---
id: 5584
name: "sbilge/ClinicalReportingPipeline"
branch: "master"
tag: "filedeploy"
commit: "3d5271712864e6b774c73cbf9472db1b5104e3ca"
version: "4859de263452e344c88f486c5baaa5bd"
build_date: "2018-11-19T13:45:58.794Z"
size_mb: 1685
size: 632848415
sif: "https://datasets.datalad.org/shub/sbilge/ClinicalReportingPipeline/filedeploy/2018-11-19-3d527171-4859de26/4859de263452e344c88f486c5baaa5bd.simg"
url: https://datasets.datalad.org/shub/sbilge/ClinicalReportingPipeline/filedeploy/2018-11-19-3d527171-4859de26/
recipe: https://datasets.datalad.org/shub/sbilge/ClinicalReportingPipeline/filedeploy/2018-11-19-3d527171-4859de26/Singularity
collection: sbilge/ClinicalReportingPipeline
---

# sbilge/ClinicalReportingPipeline:filedeploy

```bash
$ singularity pull shub://sbilge/ClinicalReportingPipeline:filedeploy
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ensemblorg/ensembl-vep:release_93

%labels
Maintainer sueruen@informatik.uni-tuebingen.de
Version V93

%files
# get copy_data to the image
copy_data.sh /opt/vep

%post
cd /opt/vep
# installing API version 93 in the container
perl src/ensembl-vep/INSTALL.pl --VERSION 93 -a a 
chmod +x copy_data.sh

%runscript
cd /opt/vep
./copy_data.sh
```

## Collection

 - Name: [sbilge/ClinicalReportingPipeline](https://github.com/sbilge/ClinicalReportingPipeline)
 - License: [MIT License](https://api.github.com/licenses/mit)

