---
id: 8057
name: "pndni/centos7-base"
branch: "1.0.0"
tag: "1.0.0"
commit: "30b27728b4d6291baa5c12e3db67e045814a082a"
version: "89c90b91b4088812df687ed177704324"
build_date: "2021-01-29T11:22:40.311Z"
size_mb: 280
size: 83243039
sif: "https://datasets.datalad.org/shub/pndni/centos7-base/1.0.0/2021-01-29-30b27728-89c90b91/89c90b91b4088812df687ed177704324.simg"
url: https://datasets.datalad.org/shub/pndni/centos7-base/1.0.0/2021-01-29-30b27728-89c90b91/
recipe: https://datasets.datalad.org/shub/pndni/centos7-base/1.0.0/2021-01-29-30b27728-89c90b91/Singularity
collection: pndni/centos7-base
---

# pndni/centos7-base:1.0.0

```bash
$ singularity pull shub://pndni/centos7-base:1.0.0
```

## Singularity Recipe

```singularity
Bootstrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/x86_64/
Include: yum
```

## Collection

 - Name: [pndni/centos7-base](https://github.com/pndni/centos7-base)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

