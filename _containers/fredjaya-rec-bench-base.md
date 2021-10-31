---
id: 9817
name: "fredjaya/rec-bench"
branch: "dev"
tag: "base"
commit: "e215b87783a5be2c3aff2752733f87ec34419704"
version: "ef4c3b2f42fb2dcbf1d401e2a23ea1dd"
build_date: "2019-06-25T09:15:37.230Z"
size_mb: 539
size: 183930911
sif: "https://datasets.datalad.org/shub/fredjaya/rec-bench/base/2019-06-25-e215b877-ef4c3b2f/ef4c3b2f42fb2dcbf1d401e2a23ea1dd.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/fredjaya/rec-bench/base/2019-06-25-e215b877-ef4c3b2f/
recipe: https://datasets.datalad.org/shub/fredjaya/rec-bench/base/2019-06-25-e215b877-ef4c3b2f/Singularity
collection: fredjaya/rec-bench
---

# fredjaya/rec-bench:base

```bash
$ singularity pull shub://fredjaya/rec-bench:base
```

## Singularity Recipe

```singularity
# https://public.confluence.arizona.edu/display/UAHPC/Singularity+Tutorials#SingularityTutorials-CentOSwithTensorflowExample

BootStrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum wget

%post
    # Add OS packages
    yum -y install gcc centos-release-scl openssl-devel bzip2-devel libffi-devel epel-release tar.x86_64 gzip make unzip scl-utils-build devtoolset-6

%setup
    # Bind-mount the hosts directories
    mkdir -p ${SINGULARITY_ROOTFS}/opt
    mkdir -p ${SINGULARITY_ROOTFS}/scratch
    mkdir -p ${SINGULARITY_ROOTFS}/shared
```

## Collection

 - Name: [fredjaya/rec-bench](https://github.com/fredjaya/rec-bench)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

