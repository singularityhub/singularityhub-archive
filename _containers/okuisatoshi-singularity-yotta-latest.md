---
id: 11073
name: "okuisatoshi/singularity-yotta"
branch: "master"
tag: "latest"
commit: "9fa6fef77e21651b501b6f3341736333e3d586b2"
version: "c242de8d1801542688eac43adda2c3df"
build_date: "2019-09-30T13:29:05.671Z"
size_mb: 2186.0
size: 685862943
sif: "https://datasets.datalad.org/shub/okuisatoshi/singularity-yotta/latest/2019-09-30-9fa6fef7-c242de8d/c242de8d1801542688eac43adda2c3df.sif"
url: https://datasets.datalad.org/shub/okuisatoshi/singularity-yotta/latest/2019-09-30-9fa6fef7-c242de8d/
recipe: https://datasets.datalad.org/shub/okuisatoshi/singularity-yotta/latest/2019-09-30-9fa6fef7-c242de8d/Singularity
collection: okuisatoshi/singularity-yotta
---

# okuisatoshi/singularity-yotta:latest

```bash
$ singularity pull shub://okuisatoshi/singularity-yotta:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From: ubuntu:rolling

%post

apt-get update
apt-get install -y python-setuptools cmake build-essential ninja-build python-dev libffi-dev libssl-dev python3-pip srecord gcc-arm-none-eabi
apt-get clean

pip3 install yotta

# Workaround for suppressing error: "'RegistryThingVersion' object has no attribute 'truncate'"
# See: https://github.com/ARMmbed/yotta/issues/856
sed -i \
    -e '/__ge__/{n;a \\n    def truncate(self, level):\n        return self.version.truncate(level)'\
    -e '}'\
    /usr/local/lib/python3.7/dist-packages/yotta/lib/version.py

%runscript

exec /usr/local/bin/yotta "$@"
```

## Collection

 - Name: [okuisatoshi/singularity-yotta](https://github.com/okuisatoshi/singularity-yotta)
 - License: None

