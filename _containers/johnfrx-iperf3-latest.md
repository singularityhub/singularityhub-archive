---
id: 7956
name: "johnfrx/iperf3"
branch: "master"
tag: "latest"
commit: "f5ed97682dd3e4f50d4b00a1b63621253d6264a9"
version: "10dcfd5215e3343f930c17293fcf2dac"
build_date: "2019-03-27T08:48:38.120Z"
size_mb: 308
size: 113315871
sif: "https://datasets.datalad.org/shub/johnfrx/iperf3/latest/2019-03-27-f5ed9768-10dcfd52/10dcfd5215e3343f930c17293fcf2dac.simg"
url: https://datasets.datalad.org/shub/johnfrx/iperf3/latest/2019-03-27-f5ed9768-10dcfd52/
recipe: https://datasets.datalad.org/shub/johnfrx/iperf3/latest/2019-03-27-f5ed9768-10dcfd52/Singularity
collection: johnfrx/iperf3
---

# johnfrx/iperf3:latest

```bash
$ singularity pull shub://johnfrx/iperf3:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:latest

%post
yum -y install epel-release
yum -y update
yum -y install iperf3
```

## Collection

 - Name: [johnfrx/iperf3](https://github.com/johnfrx/iperf3)
 - License: None

