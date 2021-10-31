---
id: 10572
name: "stephansmit/shipyard_containers"
branch: "master"
tag: "latest"
commit: "ebc0383623d1de81b5fd1a62d23a976f7320ef96"
version: "4e5743751fb36cde4bf66a9d3f001469"
build_date: "2019-08-12T09:23:54.172Z"
size_mb: 1130.0
size: 292134943
sif: "https://datasets.datalad.org/shub/stephansmit/shipyard_containers/latest/2019-08-12-ebc03836-4e574375/4e5743751fb36cde4bf66a9d3f001469.sif"
url: https://datasets.datalad.org/shub/stephansmit/shipyard_containers/latest/2019-08-12-ebc03836-4e574375/
recipe: https://datasets.datalad.org/shub/stephansmit/shipyard_containers/latest/2019-08-12-ebc03836-4e574375/Singularity
collection: stephansmit/shipyard_containers
---

# stephansmit/shipyard_containers:latest

```bash
$ singularity pull shub://stephansmit/shipyard_containers:latest
```

## Singularity Recipe

```singularity
# Singularity for Azure-CLI
Bootstrap: docker
From: ubuntu:16.04

%environment
LC_ALL="C.UTF-8"
LANG="C.UTF-8"
export LC_ALL
export LANG

%post

apt-get update && \
apt-get install -y curl git python3-pip musl build-essential python3 jq gettext-base \
                   python3-dev libffi-dev libssl-dev python3-pip\
                   ca-certificates openssh-client rsync bash&& \

echo "install shipyard" 
git clone -b master --single-branch --depth 5 https://github.com/Azure/batch-shipyard.git /opt/batch-shipyard/
cd /opt/batch-shipyard
python3 -m pip install --no-cache-dir -r requirements.txt
python3 -m pip install pykwalify
python3 -m compileall -f /opt/batch-shipyard/shipyard.py /opt/batch-shipyard/convoy

echo "install azure-cli"
curl -sL https://aka.ms/InstallAzureCLIDeb | bash



%runscript
exec "$@"
```

## Collection

 - Name: [stephansmit/shipyard_containers](https://github.com/stephansmit/shipyard_containers)
 - License: None

