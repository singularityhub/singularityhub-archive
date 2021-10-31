---
id: 11968
name: "matthew-kusz/run-Blender"
branch: "master"
tag: "latest"
commit: "53b74b04dc421d379a743c4d3c79f97dc657213c"
version: "929ec71d53fea4aa6b16054da757e7ba"
build_date: "2020-01-09T15:36:51.486Z"
size_mb: 865.0
size: 339148831
sif: "https://datasets.datalad.org/shub/matthew-kusz/run-Blender/latest/2020-01-09-53b74b04-929ec71d/929ec71d53fea4aa6b16054da757e7ba.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/matthew-kusz/run-Blender/latest/2020-01-09-53b74b04-929ec71d/
recipe: https://datasets.datalad.org/shub/matthew-kusz/run-Blender/latest/2020-01-09-53b74b04-929ec71d/Singularity
collection: matthew-kusz/run-Blender
---

# matthew-kusz/run-Blender:latest

```bash
$ singularity pull shub://matthew-kusz/run-Blender:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%post

# We need gnupg to setup the PPA
apt-get update
apt-get install -y gnupg clinfo

# We will use a ppa to get the latest blender
echo "deb http://ppa.launchpad.net/thomas-schiex/blender/ubuntu bionic main" >> /etc/apt/sources.list
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys D32A3245446233723DECE00F7281E3E842A98114

# Install blender
apt-get update
apt-get install -y x11-utils
apt-get install -y alsa-utils
apt-get install -y avahi-utils
apt-get install -y blender

%hel
$ singularity run blender.sif [scene file] [output directory] <frame | start frame:end frame>

Example:
Using `my_scene.blend`, render all frames, and output into `run/output`

    $ singularity run blender.sif my_scene.blend run/output

Using `my_scene.blend`, render frames 100->200, and output into `run/output`

    $ singularity run blender.sif my_scene.blend run/output 100:200

Using `my_scene.blend`, render frame 5, and output into `run/output`

    $ singularity run blender.sif my_scene.blend run/output 5

%runscript
FRAME="-a"
if [ -n "$3" ]; then
    if echo $3 | grep -q ":"; then
        STARTF=$(echo $3 | cut -f 1 -d ':')
        ENDF=$(echo $3 | cut -f 2 -d ':')

        FRAME="-s ${STARTF} -e ${ENDF} -a"
    else
        FRAME="-f $3"
    fi
fi

echo "Command to run is: /usr/bin/blender -b -noaudio $1 -o $2 ${FRAME}"
/usr/bin/blender -b -noaudio $1 -o $2 ${FRAME}
```

## Collection

 - Name: [matthew-kusz/run-Blender](https://github.com/matthew-kusz/run-Blender)
 - License: None

