---
id: 11662
name: "Cloud-PG/CachingOnDemand_singularity"
branch: "master"
tag: "latest"
commit: "18dda78d72e42560753177c83733712e59c10594"
version: "467d8bdee2df64edc822f50ded501504"
build_date: "2019-11-20T14:05:44.068Z"
size_mb: 633.0
size: 232063007
sif: "https://datasets.datalad.org/shub/Cloud-PG/CachingOnDemand_singularity/latest/2019-11-20-18dda78d-467d8bde/467d8bdee2df64edc822f50ded501504.sif"
url: https://datasets.datalad.org/shub/Cloud-PG/CachingOnDemand_singularity/latest/2019-11-20-18dda78d-467d8bde/
recipe: https://datasets.datalad.org/shub/Cloud-PG/CachingOnDemand_singularity/latest/2019-11-20-18dda78d-467d8bde/Singularity
collection: Cloud-PG/CachingOnDemand_singularity
---

# Cloud-PG/CachingOnDemand_singularity:latest

```bash
$ singularity pull shub://Cloud-PG/CachingOnDemand_singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: cloudpg/centos-7-grid

%help
The log directory should have the correct permisions:
- sudo chown -R 998:996 /var/log/xrootd
Start the service with:
- sudo singularity instance start -B /var/log/xrootd/:/var/log/xrootd/ shub://Cloud-PG/CachingOnDemand_singularity:latest proxy

%post
    yum -y install epel-release
    yum -y install sudo xrootd-server 
    # ca-policy-egi-core ca-policy-lcg
    #/usr/sbin/fetch-crl -q

%files
    config/proxy.cfg /etc/xrootd/xrootd-proxy.cfg
    scripts/entrypoint.sh /opt


%post
    chmod +x /opt/entrypoint.sh

%startscript
    echo -e "Starting XROOTD proxy vs $REMOTE_HOST:$REMOTE_PORT \n Listening on $PROXY_PORT"
    exec /opt/entrypoint.sh

%labels
    Maintainer Diego Ciangottini
    Version v1.0
```

## Collection

 - Name: [Cloud-PG/CachingOnDemand_singularity](https://github.com/Cloud-PG/CachingOnDemand_singularity)
 - License: None

