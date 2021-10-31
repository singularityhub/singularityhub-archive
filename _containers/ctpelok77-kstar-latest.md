---
id: 13368
name: "ctpelok77/kstar"
branch: "master"
tag: "latest"
commit: "e5505add9eb465f12082f622f7aae86f8c229af5"
version: "15b36ed096be7362dc6de41603f96d35"
build_date: "2021-04-06T12:12:19.084Z"
size_mb: 105.0
size: 38199327
sif: "https://datasets.datalad.org/shub/ctpelok77/kstar/latest/2021-04-06-e5505add-15b36ed0/15b36ed096be7362dc6de41603f96d35.sif"
url: https://datasets.datalad.org/shub/ctpelok77/kstar/latest/2021-04-06-e5505add-15b36ed0/
recipe: https://datasets.datalad.org/shub/ctpelok77/kstar/latest/2021-04-06-e5505add-15b36ed0/Singularity
collection: ctpelok77/kstar
---

# ctpelok77/kstar:latest

```bash
$ singularity pull shub://ctpelok77/kstar:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ctpelok77/kstar:latest

%setup
    # Just for diagnosis purposes
    hostname -f > $SINGULARITY_ROOTFS/etc/build_host
%runscript
    # This will be called whenever the Singularity container is invoked
    python3 /workspace/kstar/fast-downward.py --build release64 $@

%post

%labels
Name        K*
Description The K* planner
Authors     Michael Katz <michael.katz1@ibm.com>, Shirin Sohrabi <ssohrab@us.ibm.com>, Octavian Udrea <udrea@us.ibm.com> and Dominik Winterer <dominik_winterer@gmx.de>
```

## Collection

 - Name: [ctpelok77/kstar](https://github.com/ctpelok77/kstar)
 - License: [Other](None)

