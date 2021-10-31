---
id: 14626
name: "shreyaskamathkm/singularity_meshroom"
branch: "main"
tag: "latest"
commit: "2061772aa3b14dde25c022efb82972ba1a366f7c"
version: "bc250812e7ed4d9ecae6b3f65c2d1ee3"
build_date: "2020-10-18T15:58:27.291Z"
size_mb: 628.0
size: 207716383
sif: "https://datasets.datalad.org/shub/shreyaskamathkm/singularity_meshroom/latest/2020-10-18-2061772a-bc250812/bc250812e7ed4d9ecae6b3f65c2d1ee3.sif"
url: https://datasets.datalad.org/shub/shreyaskamathkm/singularity_meshroom/latest/2020-10-18-2061772a-bc250812/
recipe: https://datasets.datalad.org/shub/shreyaskamathkm/singularity_meshroom/latest/2020-10-18-2061772a-bc250812/Singularity
collection: shreyaskamathkm/singularity_meshroom
---

# shreyaskamathkm/singularity_meshroom:latest

```bash
$ singularity pull shub://shreyaskamathkm/singularity_meshroom:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:10.1-base-centos7



%files
./requirements.txt /meshroom/
./files/Meshroom-2020.1.0-linux-cuda10.tar.gz /opt/



%post
yum install -y gcc python3-devel wget python3-pip python3 \
&& pip3 install --user -r /meshroom/requirements.txt \
&& yum remove -y gcc

%post
cd /opt && tar zxf Meshroom-2020.1.0-linux-cuda10.tar.gz && rm Meshroom-2020.1.0-linux-cuda10.tar.gz

yum install -y yum-utils && yum-config-manager --add-repo \
https://download.docker.com/linux/centos/docker-ce.repo && \
yum install -y docker-ce-cli

%files
./files/github/* /meshroom/
./files/others/instant-meshes-linux/* /opt/Meshroom-2020.1.0/aliceVision/bin/
./files/others/meshroom_external_plugins-master/* /opt/Meshroom-2020.1.0/lib/meshroom/nodes/aliceVision/


%post
cp /meshroom/meshroom/nodes/aliceVision/* /opt/Meshroom-2020.1.0/lib/meshroom/nodes/aliceVision/ \
&& cp /meshroom/bin/* /meshroom \
&& chmod 755 /meshroom/meshroom_*


PATH="/opt/Meshroom-2020.1.0:/meshroom:${PATH}"
PYTHONPATH="$PYTHONPATH:/opt/Meshroom-2020.1.0"

%environment
export PATH="/opt/Meshroom-2020.1.0:/meshroom:${PATH}"
export PYTHONPATH="$PYTHONPATH:/opt/Meshroom-2020.1.0"
```

## Collection

 - Name: [shreyaskamathkm/singularity_meshroom](https://github.com/shreyaskamathkm/singularity_meshroom)
 - License: None

