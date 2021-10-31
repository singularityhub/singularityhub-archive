---
id: 5563
name: "ISU-HPC/braker"
branch: "master"
tag: "2.1.2"
commit: "f3018f71a5894ccb54e2173da5d58fc158d02f4b"
version: "0a70205dd132a8844555c6042eb6d9c7"
build_date: "2020-03-24T17:25:12.869Z"
size_mb: 3134
size: 1071603743
sif: "https://datasets.datalad.org/shub/ISU-HPC/braker/2.1.2/2020-03-24-f3018f71-0a70205d/0a70205dd132a8844555c6042eb6d9c7.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ISU-HPC/braker/2.1.2/2020-03-24-f3018f71-0a70205d/
recipe: https://datasets.datalad.org/shub/ISU-HPC/braker/2.1.2/2020-03-24-f3018f71-0a70205d/Singularity
collection: ISU-HPC/braker
---

# ISU-HPC/braker:2.1.2

```bash
$ singularity pull shub://ISU-HPC/braker:2.1.2
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

