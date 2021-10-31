---
id: 775
name: "alfpark/batch-shipyard-singularity"
branch: "master"
tag: "cli"
commit: "94735e46d0db3f468b3e3f3d87397e569c6ebc8c"
version: "77b987f20f69a580fd956e8da69a57d4"
build_date: "2019-08-02T22:01:05.431Z"
size_mb: 139
size: 28938271
sif: "https://datasets.datalad.org/shub/alfpark/batch-shipyard-singularity/cli/2019-08-02-94735e46-77b987f2/77b987f20f69a580fd956e8da69a57d4.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/alfpark/batch-shipyard-singularity/cli/2019-08-02-94735e46-77b987f2/
recipe: https://datasets.datalad.org/shub/alfpark/batch-shipyard-singularity/cli/2019-08-02-94735e46-77b987f2/Singularity
collection: alfpark/batch-shipyard-singularity
---

# alfpark/batch-shipyard-singularity:cli

```bash
$ singularity pull shub://alfpark/batch-shipyard-singularity:cli
```

## Singularity Recipe

```singularity
# Singularity for Azure/batch-shipyard (cli)

Bootstrap: docker
From: alpine:3.6

%post
apk update
apk add --update --no-cache \
    musl build-base python3 python3-dev libressl-dev libffi-dev \
    ca-certificates libressl openssh-client rsync git bash
git clone -b master --single-branch --depth 5 https://github.com/Azure/batch-shipyard.git /opt/batch-shipyard
cd /opt/batch-shipyard
rm -rf .git
rm -f .git* .travis.yml *.yml install*
pip3 install --no-cache-dir -r requirements.txt
python3 -m compileall -f /opt/batch-shipyard/shipyard.py /opt/batch-shipyard/convoy
apk del --purge build-base python3-dev libressl-dev libffi-dev git
rm /var/cache/apk/*

%runscript
exec /opt/batch-shipyard/shipyard.py "$@"
```

## Collection

 - Name: [alfpark/batch-shipyard-singularity](https://github.com/alfpark/batch-shipyard-singularity)
 - License: None

