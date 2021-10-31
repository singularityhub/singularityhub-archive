---
id: 3750
name: "Hydrocarpentry/project_pydocker"
branch: "master"
tag: "latest"
commit: "3115e72a21c71969394c88b4893d250922fd5aae"
version: "3570f40fac218227ed9e09c1b04bf7fb"
build_date: "2018-07-29T13:44:03.079Z"
size_mb: 1283
size: 451678239
sif: "https://datasets.datalad.org/shub/Hydrocarpentry/project_pydocker/latest/2018-07-29-3115e72a-3570f40f/3570f40fac218227ed9e09c1b04bf7fb.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Hydrocarpentry/project_pydocker/latest/2018-07-29-3115e72a-3570f40f/
recipe: https://datasets.datalad.org/shub/Hydrocarpentry/project_pydocker/latest/2018-07-29-3115e72a-3570f40f/Singularity
collection: Hydrocarpentry/project_pydocker
---

# Hydrocarpentry/project_pydocker:latest

```bash
$ singularity pull shub://Hydrocarpentry/project_pydocker:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu

%post 
    apt-get update
    apt-get install -y python-pandas
    apt-get install -y r-base
    apt-get install wget   
    # Install required R packages
    R --slave -e 'install.packages("caret")'
    R --slave -e 'install.packages("randomForest")'

%files
    prepare_flood_events_table.py
    make_dly_obs_table_standalone.py
    by_event_for_model.py
    model_flood_counts_rf_ps_cln.r
    plot_count_model_results.py

%runscript
    python /prepare_flood_events_table.py 
    python /make_dly_obs_table_standalone.py
    python /by_event_for_model.py
    Rscript /model_flood_counts_rf_ps_cln.r
    python /plot_count_model_results.py out
```

## Collection

 - Name: [Hydrocarpentry/project_pydocker](https://github.com/Hydrocarpentry/project_pydocker)
 - License: None

