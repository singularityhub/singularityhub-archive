---
id: 888
name: "DaleDupont/singularity-ga4gh"
branch: "master"
tag: "latest"
commit: "bd21698426091821771d9f3a1049bf520a5f7b6f"
version: "8ccdb43121fbb9954c89947011d2830e"
build_date: "2017-12-19T06:40:02.490Z"
size_mb: 843
size: 330870815
sif: "https://datasets.datalad.org/shub/DaleDupont/singularity-ga4gh/latest/2017-12-19-bd216984-8ccdb431/8ccdb43121fbb9954c89947011d2830e.simg"
url: https://datasets.datalad.org/shub/DaleDupont/singularity-ga4gh/latest/2017-12-19-bd216984-8ccdb431/
recipe: https://datasets.datalad.org/shub/DaleDupont/singularity-ga4gh/latest/2017-12-19-bd216984-8ccdb431/Singularity
collection: DaleDupont/singularity-ga4gh
---

# DaleDupont/singularity-ga4gh:latest

```bash
$ singularity pull shub://DaleDupont/singularity-ga4gh:latest
```

## Singularity Recipe

```singularity
# bootstrap from docker ubuntu image
BootStrap: docker
From: ubuntu:latest

%post
    apt-get update  --fix-missing

    apt-get install -y tar git curl libcurl4-openssl-dev wget dialog \
    net-tools build-essential python python-dev python-distribute \
    python-pip zlib1g-dev libxslt1-dev libffi-dev libssl-dev

    mkdir -p /srv/ga4gh-server

    git clone -b auth-deploy-stable-test https://github.com/Bio-Core/ga4gh-server.git /srv/ga4gh-server

    # install python package requirements
    pip install -r /srv/ga4gh-server/requirements.txt

    pip install /srv/ga4gh-server

    # prepare sample/compliance data
    cd /srv/ga4gh-server/scripts

    python prepare_compliance_data.py -o /srv/ga4gh-compliance-data

%runscript

    exec ga4gh_server -P "${GA4GH_PORT}" -H "${GA4GH_IP}" -f "${GA4GH_CONFIG}"
```

## Collection

 - Name: [DaleDupont/singularity-ga4gh](https://github.com/DaleDupont/singularity-ga4gh)
 - License: None

