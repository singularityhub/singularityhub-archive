---
id: 13062
name: "fifthguy/seqtrace-container"
branch: "master"
tag: "latest"
commit: "f83abce588367a18a3d8ab349e7304392266a2c3"
version: "889f470c31403f6980a0379336d26dbad1fdd21364d49d0b8c1fd36fddc7ca91"
build_date: "2021-02-18T10:42:57.657Z"
size_mb: 231.9921875
size: 243261440
sif: "https://datasets.datalad.org/shub/fifthguy/seqtrace-container/latest/2021-02-18-f83abce5-889f470c/889f470c31403f6980a0379336d26dbad1fdd21364d49d0b8c1fd36fddc7ca91.sif"
url: https://datasets.datalad.org/shub/fifthguy/seqtrace-container/latest/2021-02-18-f83abce5-889f470c/
recipe: https://datasets.datalad.org/shub/fifthguy/seqtrace-container/latest/2021-02-18-f83abce5-889f470c/Singularity
collection: fifthguy/seqtrace-container
---

# fifthguy/seqtrace-container:latest

```bash
$ singularity pull shub://fifthguy/seqtrace-container:latest
```

## Singularity Recipe

```singularity
BootStrap: library
From: debian:9

%labels
Maintained by tzfifthguy1@gmail.com

%post
  apt-get update
  apt-get install -y python-gtk2 wget

  cd /opt

  wget https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/seqtrace/seqtrace-0.9.0.tar.gz 
  tar -xvf seqtrace-0.9.0.tar.gz
  rm seqtrace-0.9.0.tar.gz

  mkdir bin
  echo "#!/bin/bash" > bin/seqtrace
  echo "python /opt/seqtrace-0.9.0/seqtrace.py" >> bin/seqtrace

  cd 
  
  chmod 777 /opt/bin/seqtrace

%environment
	export PATH=/opt/bin:$PATH
```

## Collection

 - Name: [fifthguy/seqtrace-container](https://github.com/fifthguy/seqtrace-container)
 - License: [MIT License](https://api.github.com/licenses/mit)

