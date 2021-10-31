---
id: 2845
name: "jdwheaton/singularity-ngs"
branch: "master"
tag: "sra_tools"
commit: "c340d120f62540d323bba7f282da8f7d2b0347f6"
version: "2444e8a881a655c7adb0d10c7d3e777a"
build_date: "2018-05-20T23:46:11.593Z"
size_mb: 564
size: 172896287
sif: "https://datasets.datalad.org/shub/jdwheaton/singularity-ngs/sra_tools/2018-05-20-c340d120-2444e8a8/2444e8a881a655c7adb0d10c7d3e777a.simg"
url: https://datasets.datalad.org/shub/jdwheaton/singularity-ngs/sra_tools/2018-05-20-c340d120-2444e8a8/
recipe: https://datasets.datalad.org/shub/jdwheaton/singularity-ngs/sra_tools/2018-05-20-c340d120-2444e8a8/Singularity
collection: jdwheaton/singularity-ngs
---

# jdwheaton/singularity-ngs:sra_tools

```bash
$ singularity pull shub://jdwheaton/singularity-ngs:sra_tools
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:7

%post
	# Install required build tools
    yum -y update
    yum -y install tar wget
    cd /
    wget http://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/2.9.0/sratoolkit.2.9.0-centos_linux64.tar.gz
    tar -xvzf sratoolkit.2.9.0-centos_linux64.tar.gz
    rm sratoolkit.2.9.0-centos_linux64.tar.gz
    
%environment
	export PATH=$PATH:/sratoolkit.2.9.0-centos_linux64/bin
```

## Collection

 - Name: [jdwheaton/singularity-ngs](https://github.com/jdwheaton/singularity-ngs)
 - License: None

