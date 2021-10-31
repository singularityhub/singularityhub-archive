---
id: 8385
name: "pndni/minc-ants-and-fsl-container"
branch: "1.0.0"
tag: "1.0.0"
commit: "ec91abfb00588884eeadef4ec9b1476f03a6ec61"
version: "58b853e8ffb1fa82d819f71413422de7"
build_date: "2019-04-12T04:45:46.861Z"
size_mb: 15899
size: 6157529119
sif: "https://datasets.datalad.org/shub/pndni/minc-ants-and-fsl-container/1.0.0/2019-04-12-ec91abfb-58b853e8/58b853e8ffb1fa82d819f71413422de7.simg"
url: https://datasets.datalad.org/shub/pndni/minc-ants-and-fsl-container/1.0.0/2019-04-12-ec91abfb-58b853e8/
recipe: https://datasets.datalad.org/shub/pndni/minc-ants-and-fsl-container/1.0.0/2019-04-12-ec91abfb-58b853e8/Singularity
collection: pndni/minc-ants-and-fsl-container
---

# pndni/minc-ants-and-fsl-container:1.0.0

```bash
$ singularity pull shub://pndni/minc-ants-and-fsl-container:1.0.0
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: pndni/minc-and-ants-container:1.0.1
# OSVersion: 7
# MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/x86_64/
# Include: yum
#
%post

    #######
    # fsl #
    #######
    wget --output-document=/root/fslinstaller.py https://fsl.fmrib.ox.ac.uk/fsldownloads/fslinstaller.py 
    python /root/fslinstaller.py -p -V 6.0.1 -d /opt/fsl
    rm /root/fslinstaller.py

%appenv fsl
    export FSLDIR=/opt/fsl
    source $FSLDIR/etc/fslconf/fsl.sh
    export PATH=$FSLDIR/bin:$PATH

%applabels fsl
    License https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Licence
    URL https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    Version 6.0.1

%apphelp fsl
    Before using FSL you must agree to the license at
    https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Licence

%labels
    Maintainer Steven Tilley
    Version 1.0.0
```

## Collection

 - Name: [pndni/minc-ants-and-fsl-container](https://github.com/pndni/minc-ants-and-fsl-container)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

