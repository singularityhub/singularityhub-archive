---
id: 3923
name: "tjhendrickson/bids-app-host"
branch: "master"
tag: "latest"
commit: "da8046b80953737bb9a62d9116fe4688b271655e"
version: "885d4acba8ca9b46988535062da9325d"
build_date: "2018-08-10T20:17:51.219Z"
size_mb: 1733
size: 780832799
sif: "https://datasets.datalad.org/shub/tjhendrickson/bids-app-host/latest/2018-08-10-da8046b8-885d4acb/885d4acba8ca9b46988535062da9325d.simg"
url: https://datasets.datalad.org/shub/tjhendrickson/bids-app-host/latest/2018-08-10-da8046b8-885d4acb/
recipe: https://datasets.datalad.org/shub/tjhendrickson/bids-app-host/latest/2018-08-10-da8046b8-885d4acb/Singularity
collection: tjhendrickson/bids-app-host
---

# tjhendrickson/bids-app-host:latest

```bash
$ singularity pull shub://tjhendrickson/bids-app-host:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:xenial-20180726

%files
run.py /run.py
modified_files/generic-msi.s3cfg /etc/

%environment

#set up environment for runtime
export BIDS_ANALYSIS_ID
export BIDS_CONTAINER
export BIDS_DATASET_BUCKET
export BIDS_OUTPUT_BUCKET
export BIDS_SNAPSHOT_ID
export BIDS_ANALYSIS_LEVEL
export BIDS_ARGUMENTS
export GOPATH=${HOME}/go
export PATH=/usr/local/go/bin:${PATH}:${GOPATH}/bin
export SINGULARITY_PULLFOLDER=/
export SINGULARITY_LOCALCACHEDIR=/tmp
export SINGULARITY_CACHEDIR=/tmp


%post

#make /run.py executable
chmod +x /run.py

#make generic-msi.s3cfg copyable
chmod 555 -R /etc/

#make local folders
mkdir /snapshot
mkdir /output
mkdir /SW

#set up basic tools including python3
apt-get update
apt-get install bash jq curl util-linux python3-pip python3 python3-setuptools python3-dev dh-autoreconf build-essential libffi-dev libssl-dev uuid-dev libgpgme11-dev libarchive-dev git wget -y
apt-get -y upgrade

#install golang 1.10.2
cd /tmp
wget https://dl.google.com/go/go1.10.2.linux-amd64.tar.gz
tar -C /usr/local -xzf go1.10.2.linux-amd64.tar.gz
export PATH=/usr/local/go/bin:${PATH}:/root/go/bin

#clone singularity repository
mkdir -p /root/go/src/github.com/singularityware
cd /root/go/src/github.com/singularityware
git clone https://github.com/singularityware/singularity.git
cd singularity
git fetch

#install golang dependencies
go get -u -v github.com/golang/dep/cmd/dep
cd /root/go/src/github.com/singularityware/singularity
dep ensure -v

#now install singularity
cd /root/go/src/github.com/singularityware/singularity
./mconfig
cd ./builddir
make
make install
cd ..
./mconfig -p /usr/local -b ./buildtree

#singularity python3 api
export LC_ALL=C
cd /SW
git clone https://www.github.com/singularityhub/singularity-cli.git
cd singularity-cli/
python3 setup.py install
pip3 install -r requirements.txt

#install s3cmd version 2.0.2
apt-get update
cd /SW
wget -qO- https://sourceforge.net/projects/s3tools/files/s3cmd/2.0.2/s3cmd-2.0.2.tar.gz | tar zxv -C /SW
cd s3cmd-2.0.2
python3 setup.py install

#set up environment within container
export BIDS_ANALYSIS_ID
export BIDS_CONTAINER
export BIDS_DATASET_BUCKET
export BIDS_OUTPUT_BUCKET
export BIDS_SNAPSHOT_ID
export BIDS_ANALYSIS_LEVEL
export BIDS_ARGUMENTS
export GOPATH=${HOME}/go
export PATH=/usr/local/go/bin:${PATH}:${GOPATH}/bin
export SINGULARITY_PULLFOLDER=/
export SINGULARITY_LOCALCACHEDIR=/tmp
export SINGULARITY_CACHEDIR=/tmp

%runscript
/run.py
```

## Collection

 - Name: [tjhendrickson/bids-app-host](https://github.com/tjhendrickson/bids-app-host)
 - License: None

