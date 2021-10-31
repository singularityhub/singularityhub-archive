---
id: 5518
name: "ISU-HPC/braker"
branch: "master"
tag: "latest"
commit: "2ce4e02698ccab73b05c71e510f0725c64cacc78"
version: "0c2627bcba94e2fe054dd7df916f9e3d"
build_date: "2020-03-20T15:30:22.236Z"
size_mb: 3134
size: 1071599647
sif: "https://datasets.datalad.org/shub/ISU-HPC/braker/latest/2020-03-20-2ce4e026-0c2627bc/0c2627bcba94e2fe054dd7df916f9e3d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ISU-HPC/braker/latest/2020-03-20-2ce4e026-0c2627bc/
recipe: https://datasets.datalad.org/shub/ISU-HPC/braker/latest/2020-03-20-2ce4e026-0c2627bc/Singularity
collection: ISU-HPC/braker
---

# ISU-HPC/braker:latest

```bash
$ singularity pull shub://ISU-HPC/braker:latest
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: ISU-HPC/augustus


%labels
MAINTAINER ynanyam@iastate.edu

%post

#Install GeneMark
cd /
wget http://topaz.gatech.edu/GeneMark/tmp/GMtool_8oebP/gm_et_linux_64.tar.gz
tar xvf gm_et_linux_64.tar.gz
rm gm_et_linux_64.tar.gz
cd gm_et_linux_64
wget http://topaz.gatech.edu/GeneMark/tmp/GMtool_8oebP/gm_key_64.gz
echo 'export PATH=/gm_et_linux_64/gmes_petap:$PATH' >>$SINGULARITY_ENVIRONMENT
#Install perl dependencies
echo 'export LANG=C' >>$SINGULARITY_ENVIRONMENT
cpan App::cpanminus
cpanm YAML File::Spec::Functions Hash::Merge List::Util Logger::Simple \
  Module::Load::Conditional Parallel::ForkManager POSIX Scalar::Util::Numeric File::Which

#Install blast,biotools and bamtools
apt-get install -y ncbi-blast+ bamtools python3-biopython

#Install braker and set required variables
cd /
wget https://github.com/Gaius-Augustus/BRAKER/archive/v2.1.2.tar.gz

tar xvf v2.1.2.tar.gz
rm v2.1.2.tar.gz
echo 'export PATH=/augustus/scripts:/BRAKER-2.1.2/scripts:$PATH' >>$SINGULARITY_ENVIRONMENT
echo 'export AUGUSTUS_SCRIPTS_PATH=/augustus/scripts' >>$SINGULARITY_ENVIRONMENT
echo 'export AUGUSTUS_BIN_PATH=/augustus/bin' >>$SINGULARITY_ENVIRONMENT
```

## Collection

 - Name: [ISU-HPC/braker](https://github.com/ISU-HPC/braker)
 - License: None

