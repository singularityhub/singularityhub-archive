---
id: 12884
name: "jacobhepkema/singularity_custom_meme"
branch: "master"
tag: "latest"
commit: "de52d062d53b3b2d228c7c7a10da854f671e8751"
version: "130bd9cec48bf0eeb0b7c17401c9cf3a"
build_date: "2021-03-11T15:03:15.089Z"
size_mb: 865.0
size: 289157151
sif: "https://datasets.datalad.org/shub/jacobhepkema/singularity_custom_meme/latest/2021-03-11-de52d062-130bd9ce/130bd9cec48bf0eeb0b7c17401c9cf3a.sif"
url: https://datasets.datalad.org/shub/jacobhepkema/singularity_custom_meme/latest/2021-03-11-de52d062-130bd9ce/
recipe: https://datasets.datalad.org/shub/jacobhepkema/singularity_custom_meme/latest/2021-03-11-de52d062-130bd9ce/Singularity
collection: jacobhepkema/singularity_custom_meme
---

# jacobhepkema/singularity_custom_meme:latest

```bash
$ singularity pull shub://jacobhepkema/singularity_custom_meme:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

# Based on https://github.com/icaoberg/docker-meme-suite/blob/master/Dockerfile

%labels
  Maintainer @jacobhepkema
  Version v0.3

%post
  # Install prerequisites
  apt-get update && apt-get install -y procps libopenmpi-dev openmpi-bin ghostscript libgs-dev libgd-dev libexpat1-dev zlib1g-dev libxml2-dev autoconf automake libtool libhtml-template-compiled-perl libxml-opml-simplegen-perl libxml-libxml-debugging-perl sudo curl openssh-server git
  
  PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install Log::Log4perl'
  PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install Math::CDF'
  PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install CGI'
  PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install HTML::PullParser'
  PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install HTML::Template'
  PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install XML::Simple'
  PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install XML::Parser::Expat'
  PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install XML::LibXML'
  PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install XML::LibXML::Simple'
  PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install XML::Compile'
  PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install XML::Compile::SOAP11'
  PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install XML::Compile::WSDL11'
  PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install XML::Compile::Transport::SOAPHTTP'
  
  mkdir /opt/meme
  # Get custom meme suite
  cd /opt/meme && git clone https://github.com/jacobhepkema/memesuite.git 
  cd /opt/meme/memesuite && autoreconf -f -i && ./configure --prefix=/opt  --enable-build-libxml2 --enable-build-libxslt  --with-url=http://meme-suite.org && make && make install && rm -rfv /opt/meme
  
  export PATH=/opt/bin:$PATH
  
# smoke test
meme -version

%runscript
  exec /bin/bash "$@"
```

## Collection

 - Name: [jacobhepkema/singularity_custom_meme](https://github.com/jacobhepkema/singularity_custom_meme)
 - License: None

