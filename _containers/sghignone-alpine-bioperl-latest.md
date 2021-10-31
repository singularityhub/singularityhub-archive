---
id: 12723
name: "sghignone/alpine-bioperl"
branch: "master"
tag: "latest"
commit: "c385bda901e20e09fd8f181a11cd01d67ed71b27"
version: "9a38428de713a044a6f261b55929d53a"
build_date: "2020-04-11T14:15:28.434Z"
size_mb: 409.0
size: 118292511
sif: "https://datasets.datalad.org/shub/sghignone/alpine-bioperl/latest/2020-04-11-c385bda9-9a38428d/9a38428de713a044a6f261b55929d53a.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/sghignone/alpine-bioperl/latest/2020-04-11-c385bda9-9a38428d/
recipe: https://datasets.datalad.org/shub/sghignone/alpine-bioperl/latest/2020-04-11-c385bda9-9a38428d/Singularity
collection: sghignone/alpine-bioperl
---

# sghignone/alpine-bioperl:latest

```bash
$ singularity pull shub://sghignone/alpine-bioperl:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: alpine:latest


%labels
	author Stefano Ghignone
	maintainer sghignone
	version 1.7.7
%post
	apk update && apk upgrade \
	&& apk add --no-cache sudo build-base curl wget \
	perl \
	perl-doc \
	perl-utils \
	perl-dev \
	perl-dbd-pg \
	perl-db_file \
	expat \
	expat-dev \
	libxml2-dev \
	libxslt-dev
	
	#testing dependencies
	curl -L http://cpanmin.us | perl - --sudo App::cpanminus
	cpanm --quiet --notest Bundle::BioPerl Parallel::ForkManager Tree BioPerl
```

## Collection

 - Name: [sghignone/alpine-bioperl](https://github.com/sghignone/alpine-bioperl)
 - License: None

