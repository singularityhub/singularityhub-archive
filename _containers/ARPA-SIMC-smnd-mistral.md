---
id: 7864
name: "ARPA-SIMC/smnd"
branch: "master"
tag: "mistral"
commit: "949e2b432f9c1d725ceed8034f379e2664dfbb70"
version: "a903325a9110b99ee17760a918632652"
build_date: "2019-04-17T14:27:57.721Z"
size_mb: 1696
size: 452329503
sif: "https://datasets.datalad.org/shub/ARPA-SIMC/smnd/mistral/2019-04-17-949e2b43-a903325a/a903325a9110b99ee17760a918632652.simg"
url: https://datasets.datalad.org/shub/ARPA-SIMC/smnd/mistral/2019-04-17-949e2b43-a903325a/
recipe: https://datasets.datalad.org/shub/ARPA-SIMC/smnd/mistral/2019-04-17-949e2b43-a903325a/Singularity
collection: ARPA-SIMC/smnd
---

# ARPA-SIMC/smnd:mistral

```bash
$ singularity pull shub://ARPA-SIMC/smnd:mistral
```

## Singularity Recipe

```singularity
BootStrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum

# If you want the updates (available at the bootstrap date) to be installed
# inside the container during the bootstrap instead of the General Availability
# point release (7.x) then uncomment the following line
UpdateURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/updates/$basearch/

%runscript
    exec "$@"

%environment
    PATH=/usr/bin:/usr/sbin
    export PATH
    
%post
    yum install -q -y epel-release
    yum install -q -y yum-plugin-copr
    yum copr enable -q -y simc/stable epel-7
# install smnd packages from simc repository
    yum install -q -y wreport bufr2netcdf dballe arkimet libsim
    yum install -q -y ecflow ecflow-ui ecflow-server ecflow-python Metview Magics python3-Magics eccodes eccodes-doc eccodes-simc libemos ksh
# temporary for metview, improve spec
    yum install -q -y vi hostname xorg-x11-utils xterm xkeyboard-config
```

## Collection

 - Name: [ARPA-SIMC/smnd](https://github.com/ARPA-SIMC/smnd)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

