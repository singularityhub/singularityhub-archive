---
id: 7966
name: "dp2ski/julia_aci"
branch: "master"
tag: "rec"
commit: "b8e9208c9d9988c40fd8e6e882d7fd90e225a8ba"
version: "f025eeaef324c263c0822ec85872c79f"
build_date: "2019-03-28T19:02:13.851Z"
size_mb: 2109
size: 706949151
sif: "https://datasets.datalad.org/shub/dp2ski/julia_aci/rec/2019-03-28-b8e9208c-f025eeae/f025eeaef324c263c0822ec85872c79f.simg"
url: https://datasets.datalad.org/shub/dp2ski/julia_aci/rec/2019-03-28-b8e9208c-f025eeae/
recipe: https://datasets.datalad.org/shub/dp2ski/julia_aci/rec/2019-03-28-b8e9208c-f025eeae/Singularity
collection: dp2ski/julia_aci
---

# dp2ski/julia_aci:rec

```bash
$ singularity pull shub://dp2ski/julia_aci:rec
```

## Singularity Recipe

```singularity
# julia image for with additional packages

BootStrap: docker
From: julia:1.1.0

%runscript
    exec /usr/local/julia/bin/julia "$@"

%environment

%post
    apt-get update && apt-get install -y --no-install-recommends apt-utils
    apt-get install -y build-essential
    apt-get install -y fontconfig
        
    apt-get install -y gettext-base libcroco3 libglib2.0-0 libglib2.0-data libgpm2 libicu57 libncurses5 libxml2 sgml-base shared-mime-info xdg-user-dirs xml-core gettext fontconfig-config fonts-dejavu-core libbsd0 libexpat1 libfontconfig1 libfreetype6 libpixman-1-0 libpng16-16 libx11-6 libx11-data libxau6 libxcb-render0 libxcb-shm0 libxcb1 libxdmcp6 libxext6 libxrender1 ucf libdatrie1 libgraphite2-3 libharfbuzz0b libpango-1.0-0 libpangocairo-1.0-0 libpangoft2-1.0-0 libpangox-1.0-0 libpangoxft-1.0-0 libthai-data libthai0 libxft2 libpango1.0-0 libgdk-pixbuf2.0-0 libgdk-pixbuf2.0-common libjbig0 libjpeg62-turbo librsvg2-common libtiff5 librsvg2-bin librsvg2-2

    apt-get install -y clang libdbus-1-dev libgtk-3-dev \
                       libnotify-dev libgnome-keyring-dev libgconf2-dev \
                       libasound2-dev libcap-dev libcups2-dev libxtst-dev \
                       libxss1 libnss3-dev gcc-multilib g++-multilib curl \
                       gperf bison python-dbusmock

    apt-get install -y python3.5-dev        #required for PyCall
    apt-get install -y unzip                #required for electron
    apt-get install -y libgtk2.0-0          

    /usr/local/julia/bin/julia -e 'using Pkg; Pkg.add("Mimi")'
    /usr/local/julia/bin/julia -e 'using Pkg; Pkg.build("Mimi")'
    /usr/local/julia/bin/julia -e 'using Mimi'
    
    #------------------------------------------------------------------------------
    # Create local binding points for our ICS-ACI
    #------------------------------------------------------------------------------
    mkdir -p /storage/home
    mkdir -p /storage/work
    mkdir -p /gpfs/scratch
    mkdir -p /gpfs/group
    mkdir -p /var/spool/torque
```

## Collection

 - Name: [dp2ski/julia_aci](https://github.com/dp2ski/julia_aci)
 - License: None

