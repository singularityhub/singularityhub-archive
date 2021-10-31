---
id: 9149
name: "motroy/singularity-roary-piggy"
branch: "master"
tag: "latest"
commit: "6e51c767b1555297082478dd849a355a64ea6aab"
version: "381f251ef95188631ab35ead1091e359"
build_date: "2020-02-05T13:03:27.091Z"
size_mb: 727
size: 242462751
sif: "https://datasets.datalad.org/shub/motroy/singularity-roary-piggy/latest/2020-02-05-6e51c767-381f251e/381f251ef95188631ab35ead1091e359.simg"
url: https://datasets.datalad.org/shub/motroy/singularity-roary-piggy/latest/2020-02-05-6e51c767-381f251e/
recipe: https://datasets.datalad.org/shub/motroy/singularity-roary-piggy/latest/2020-02-05-6e51c767-381f251e/Singularity
collection: motroy/singularity-roary-piggy
---

# motroy/singularity-roary-piggy:latest

```bash
$ singularity pull shub://motroy/singularity-roary-piggy:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%environment
export PATH="/Software/roary/sanger-pathogens-Roary-db170bf/:/Software/roary/sanger-pathogens-Roary-db170bf/bin:/Software/piggy/scripts_piggy:/Software/piggy/:/Software/piggy/bin:/Databases/:$PATH"

%post
apt update && apt install -y git curl wget less locate unzip build-essential perl libexpat1-dev expat bedtools cd-hit ncbi-blast+ mcl parallel cpanminus prank mafft fasttree
cpanm --force --notest Array::Utils Bio::Perl Exception::Class File::Basename File::Copy File::Find::Rule File::Grep File::Path File::Slurper File::Spec File::Temp File::Which FindBin Getopt::Long Graph Graph::Writer::Dot List::Util Log::Log4perl Moose Moose::Role Text::CSV PerlIO::utf8_strict Devel::OverloadInfo Digest::MD5::File Bio::Roary
mkdir -p /Software/ && cd /Software/
mkdir roary && cd roary
wget https://github.com/sanger-pathogens/Roary/tarball/master/sanger-pathogens-Roary-v3.12.0-17-gdb170bf.tar.gz
tar zxvf sanger-pathogens-Roary-v3.12.0-17-gdb170bf.tar.gz
cd /Software
git clone https://github.com/harry-thorpe/piggy
mkdir -p /Databases/ && cd /Databases
export PATH="/Software/roary/sanger-pathogens-Roary-db170bf/:/Software/roary/sanger-pathogens-Roary-db170bf/bin:/Software/piggy/scripts_piggy:/Software/piggy/:/Software/piggy/bin:/Databases/:$PATH"
```

## Collection

 - Name: [motroy/singularity-roary-piggy](https://github.com/motroy/singularity-roary-piggy)
 - License: [MIT License](https://api.github.com/licenses/mit)

