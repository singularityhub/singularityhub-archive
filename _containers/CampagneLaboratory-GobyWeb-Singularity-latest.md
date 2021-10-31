---
id: 1368
name: "CampagneLaboratory/GobyWeb-Singularity"
branch: "master"
tag: "latest"
commit: "25989927362f7a5e8cc388d57d6fccb8edb498cd"
version: "e01b7773699ff59dda27798a31069448"
build_date: "2018-01-18T18:06:22.613Z"
size_mb: 1505
size: 506298399
sif: "https://datasets.datalad.org/shub/CampagneLaboratory/GobyWeb-Singularity/latest/2018-01-18-25989927-e01b7773/e01b7773699ff59dda27798a31069448.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/CampagneLaboratory/GobyWeb-Singularity/latest/2018-01-18-25989927-e01b7773/
recipe: https://datasets.datalad.org/shub/CampagneLaboratory/GobyWeb-Singularity/latest/2018-01-18-25989927-e01b7773/Singularity
collection: CampagneLaboratory/GobyWeb-Singularity
---

# CampagneLaboratory/GobyWeb-Singularity:latest

```bash
$ singularity pull shub://CampagneLaboratory/GobyWeb-Singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: artifacts/base:1.5.4

%runscript

  echo "Nothing to do here"

%post
 
   echo "Here we are installing software and other dependencies for the container!"
   mkdir /gobyweb
   cp ${HOME}/.bashrc /gobyweb
   mkdir -p /scratchLocal/gobyweb2
   mkdir -p /scratchLocal/gobyweb2/ARTIFACT_REPOSITORY-dev	
   mkdir -p /athena/campagnelab/store/data/gobyweb/dev/FILESET_AREA
   mkdir -p /athena/campagnelab/scratch/data/gobyweb/dev/GOBYWEB_SGE_JOBS	
   #libs needed by the R package Cairo
   yum install -y libXt-devel giflib-devel libjpeg-turbo-devel
   yum install -y cairo cairo-devel cairomm-devel pango pango-devel pangomm pangomm-devel
   yum clean all		
   rm -fr /etc/mail
   mkdir -p /home/gobyweb/mail

%test

  if [ ! -d /scratchLocal/gobyweb2 ]; then
	echo "%post did not run correctly"
	exit 127
  fi
  if [ ! -d /scratchLocal/gobyweb2/ARTIFACT_REPOSITORY-dev ]; then
        echo "%post did not run correctly"
        exit 127
  fi
```

## Collection

 - Name: [CampagneLaboratory/GobyWeb-Singularity](https://github.com/CampagneLaboratory/GobyWeb-Singularity)
 - License: None

