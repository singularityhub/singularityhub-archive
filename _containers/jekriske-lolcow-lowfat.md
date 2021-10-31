---
id: 700
name: "jekriske/lolcow"
branch: "master"
tag: "lowfat"
commit: "2b64452c3956d3eaa932690f4c04be23b8212984"
version: "7899209b8e9cb5e8363707be57bfe9a1"
build_date: "2020-08-02T16:26:43.616Z"
size_mb: 187
size: 3563551
sif: "https://datasets.datalad.org/shub/jekriske/lolcow/lowfat/2020-08-02-2b64452c-7899209b/7899209b8e9cb5e8363707be57bfe9a1.simg"
url: https://datasets.datalad.org/shub/jekriske/lolcow/lowfat/2020-08-02-2b64452c-7899209b/
recipe: https://datasets.datalad.org/shub/jekriske/lolcow/lowfat/2020-08-02-2b64452c-7899209b/Singularity
collection: jekriske/lolcow
---

# jekriske/lolcow:lowfat

```bash
$ singularity pull shub://jekriske/lolcow:lowfat
```

## Singularity Recipe

```singularity
BootStrap: docker
From: busybox:latest
IncludeCmd: no

%labels
  Maintainer: Jeff Kriske

%help
  A low fat version of lolcow

%setup
    wget https://tukaani.org/xz/xz-5.2.3.tar.gz
    tar -xf xz-5.2.3.tar.gz
    cd xz-5.2.3 && ./configure && make && cd ..
    cp xz-5.2.3/src/xz/xz .
    export PATH=`pwd`:$PATH
    wget https://github.com/upx/upx/releases/download/v3.94/upx-3.94-amd64_linux.tar.xz
    tar -xf upx-3.94-amd64_linux.tar.xz upx-3.94-amd64_linux/upx --strip-components=1
    wget https://redirector.gvt1.com/edgedl/go/go1.9.2.linux-amd64.tar.gz
    tar -xf go1.9.2.linux-amd64.tar.gz
    export PATH=`pwd`/go/bin:$PATH
    export GOROOT=`pwd`/go
    export GOPATH=`pwd`/go_tmp
    export CGO_ENABLED=0
    go get -ldflags="-s -w" -installsuffix cgo -u github.com/bmc/fortune-go
    mv go_tmp/bin/fortune-go fortune
    go get -ldflags="-s -w" -installsuffix cgo -u github.com/syohex/gowsay
    mv go_tmp/bin/gowsay cowsay
    go get -ldflags="-s -w" -installsuffix cgo -u github.com/cezarsa/glolcat
    mv go_tmp/bin/glolcat lolcat
    git clone https://github.com/shlomif/fortune-mod.git
    cd fortune-mod/fortune-mod/datfiles
    cat [a-z]* >> Fortunes || true
    mv Fortunes ../../../fortunes
    cd ../../../
    upx cowsay
    upx lolcat
    upx fortune
    rm -rf go* *.tar.[xg]z fortune-mod xz* upx .libs 

%apprun lolcat
  exec lolcat "$@"

%apprun cowsay
  exec cowsay "$@"

%apprun fortune
  exec fortune "$@"

%apprun lolcow
  fortune | cowsay | lolcat

%environment
    export FORTUNE_FILE=/fortunes

%runscript
    fortune | cowsay | lolcat

%files
   lolcat   /bin
   cowsay   /bin
   fortune  /bin
   fortunes /
```

## Collection

 - Name: [jekriske/lolcow](https://github.com/jekriske/lolcow)
 - License: None

