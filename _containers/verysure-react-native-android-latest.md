---
id: 13166
name: "verysure/react-native-android"
branch: "master"
tag: "latest"
commit: "f940404d40fa7f277818b0826b4cf2821d7ccf40"
version: "55b4e72f69e9c0ca33a5242217e956ff"
build_date: "2020-06-09T01:25:30.444Z"
size_mb: 2569.0
size: 1254498335
sif: "https://datasets.datalad.org/shub/verysure/react-native-android/latest/2020-06-09-f940404d-55b4e72f/55b4e72f69e9c0ca33a5242217e956ff.sif"
url: https://datasets.datalad.org/shub/verysure/react-native-android/latest/2020-06-09-f940404d-55b4e72f/
recipe: https://datasets.datalad.org/shub/verysure/react-native-android/latest/2020-06-09-f940404d-55b4e72f/Singularity
collection: verysure/react-native-android
---

# verysure/react-native-android:latest

```bash
$ singularity pull shub://verysure/react-native-android:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:bionic


%labels
    MAINTAINER verysure

%post
    dpkg --add-architecture i386
    apt-get -qq update --fix-missing 
    apt-get install -yq wget curl software-properties-common adb git 
    apt-get install -yq qemu libpulse0 libglu1-mesa xvfb libxcomposite-dev
    apt-get install -yq libc6:i386 libncurses5:i386 libstdc++6:i386 lib32z1 libbz2-1.0:i386 x11-apps

    # install nodejs
    curl -sL https://deb.nodesource.com/setup_13.x | bash -
    apt-get install -y nodejs

    # java
    wget -qO - https://adoptopenjdk.jfrog.io/adoptopenjdk/api/gpg/key/public | apt-key add -
    add-apt-repository --yes https://adoptopenjdk.jfrog.io/adoptopenjdk/deb/
    apt-get install -y software-properties-common
    add-apt-repository --yes https://adoptopenjdk.jfrog.io/adoptopenjdk/deb/
    apt-get update
    apt-get -y install adoptopenjdk-8-hotspot

    # yarn
    curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
    apt-get update
    apt-get -y install yarn

    # android-studio
    wget https://dl.google.com/dl/android/studio/ide-zips/3.6.3.0/android-studio-ide-192.6392135-linux.tar.gz -O /opt/android-studio.tar.gz
    cd /opt
    tar xzvf android-studio.tar.gz
    rm android-studio.tar.gz

    # end
    apt-get clean -yq

%environment
export ANDROID_SDK_ROOT=$HOME/Android/Sdk
export PATH=$PATH:/opt/android-studio/bin
export PATH=$PATH:$ANDROID_SDK_ROOT/emulator
export PATH=$PATH:$ANDROID_SDK_ROOT/tools
export PATH=$PATH:$ANDROID_SDK_ROOT/tools/bin
export PATH=$PATH:$ANDROID_SDK_ROOT/platform-tools
```

## Collection

 - Name: [verysure/react-native-android](https://github.com/verysure/react-native-android)
 - License: None

