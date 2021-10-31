---
id: 1788
name: "jekriske/shinyapp"
branch: "master"
tag: "latest"
commit: "cbab4f45b475849fb5a17f8f49b05882832245d6"
version: "085bc811a949a3372dcd3616d8b65993"
build_date: "2020-07-01T05:00:40.467Z"
size_mb: 985
size: 382349343
sif: "https://datasets.datalad.org/shub/jekriske/shinyapp/latest/2020-07-01-cbab4f45-085bc811/085bc811a949a3372dcd3616d8b65993.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jekriske/shinyapp/latest/2020-07-01-cbab4f45-085bc811/
recipe: https://datasets.datalad.org/shub/jekriske/shinyapp/latest/2020-07-01-cbab4f45-085bc811/Singularity
collection: jekriske/shinyapp
---

# jekriske/shinyapp:latest

```bash
$ singularity pull shub://jekriske/shinyapp:latest
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: jekriske/r-base

%labels
  Maintainer Jeff Kriske

%environment
  source /opt/rh/devtoolset-7/enable
  export SHINY_PORT=31337

%help
  This will run a simple shiny app from the gallery example at
  https://github.com/rstudio/shiny-examples/tree/master/050-kmeans-example

%runscript
  cd /myshinyapp
  exec R -e "options(browser='firefox');shiny::runApp(host='0.0.0.0', port=$SHINY_PORT, launch.browser=TRUE)"

%post
  source /opt/rh/devtoolset-7/enable
  yum update -y
  yum install -y firefox wget
  mkdir myshinyapp && cd myshinyapp
  wget https://raw.githubusercontent.com/rstudio/shiny-examples/master/050-kmeans-example/server.R
  wget https://raw.githubusercontent.com/rstudio/shiny-examples/master/050-kmeans-example/ui.R
  Rscript -e "install.packages('packrat', repos='http://cran.rstudio.com')"
  Rscript -e "packrat::init();install.packages('shiny', repos='http://cran.rstudio.com')"
  yum clean all && rm -rf /var/cache/yum
```

## Collection

 - Name: [jekriske/shinyapp](https://github.com/jekriske/shinyapp)
 - License: None

