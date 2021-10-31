---
id: 1682
name: "CAIsr/antsCorticalThickness"
branch: "master"
tag: "latest"
commit: "387cf89ff0e29e58417be85c71977931d5ca6158"
version: "d63ef4c06f355297d42a9451a9d64814"
build_date: "2018-02-09T16:52:43.174Z"
size_mb: 1655
size: 582897695
sif: "https://datasets.datalad.org/shub/CAIsr/antsCorticalThickness/latest/2018-02-09-387cf89f-d63ef4c0/d63ef4c06f355297d42a9451a9d64814.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/CAIsr/antsCorticalThickness/latest/2018-02-09-387cf89f-d63ef4c0/
recipe: https://datasets.datalad.org/shub/CAIsr/antsCorticalThickness/latest/2018-02-09-387cf89f-d63ef4c0/Singularity
collection: CAIsr/antsCorticalThickness
---

# CAIsr/antsCorticalThickness:latest

```bash
$ singularity pull shub://CAIsr/antsCorticalThickness:latest
```

## Singularity Recipe

```singularity
BootStrap:docker
From:caid/antscorticalthickness

%files

%labels
MAINTAINER Steffen.Bollmann@cai.uq.edu.au

%environment

%runscript
echo "This gets run when you run the image!"

%post
echo "This section happens once after bootstrap to build the image."
```

## Collection

 - Name: [CAIsr/antsCorticalThickness](https://github.com/CAIsr/antsCorticalThickness)
 - License: None

