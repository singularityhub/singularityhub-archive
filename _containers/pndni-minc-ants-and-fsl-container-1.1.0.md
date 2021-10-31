---
id: 8412
name: "pndni/minc-ants-and-fsl-container"
branch: "1.1.0"
tag: "1.1.0"
commit: "58151aef526c18f82941579bc7321e684791b3f0"
version: "577936b7269d500a2b2352607c00c260"
build_date: "2019-04-13T15:19:01.419Z"
size_mb: 15899
size: 6157656095
sif: "https://datasets.datalad.org/shub/pndni/minc-ants-and-fsl-container/1.1.0/2019-04-13-58151aef-577936b7/577936b7269d500a2b2352607c00c260.simg"
url: https://datasets.datalad.org/shub/pndni/minc-ants-and-fsl-container/1.1.0/2019-04-13-58151aef-577936b7/
recipe: https://datasets.datalad.org/shub/pndni/minc-ants-and-fsl-container/1.1.0/2019-04-13-58151aef-577936b7/Singularity
collection: pndni/minc-ants-and-fsl-container
---

# pndni/minc-ants-and-fsl-container:1.1.0

```bash
$ singularity pull shub://pndni/minc-ants-and-fsl-container:1.1.0
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: pndni/minc-and-ants-container:1.1.0
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
    Version 1.1.0
```

## Collection

 - Name: [pndni/minc-ants-and-fsl-container](https://github.com/pndni/minc-ants-and-fsl-container)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

