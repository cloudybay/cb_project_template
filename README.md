# 系統環境


**開發環境**
```
$ docker login registry.gitlab.com -u {gitlab_username}
$ docker pull registry.gitlab.com/cloudybay/{{ repository_name }}:base
$ docker run -it [--rm] --name {{ project_name }} [-p -v -w] registry.gitlab.com/cloudybay/{{ repository_name }}:base bash

```

- -v: 從 host 環境 mount 到容器內 {host路徑}:{容器路徑}
- -p: 從 host 環境 port 對應到容器內 port {host port}:{容器port}
- -w: workdir 進入容器時的所在路徑
- --rm: 離開容器後容器會自行消失

```

# 安裝虛擬環境
$ conda env create -f __setup/conda-environments.yml -n {{ project_name }}

# 進入 conda 虛擬環境
$ source activate {{ project_name }}

```

**範例:**
```
$ docker run -it --name {{ project_name }} -v $(pwd):/opt/CloudyBay/{{ project_name }} registry.gitlab.com/cloudybay/{{ repository_name }}:base bash
```
---

# 專案初始化順序

1. git clone git@gitlab.com:cloudybay/{{ repository_name }}.git or https://gitlab.com/cloudybay/{{ repository_name }}.git
2. 進入容器或是 conda 虛擬環境
3. 執行 python init_env.py
4. 修改 .env 內的參數
5. 複製 conf/dev.readme -> conf/dev
6. 修改 conf/dev/django_settings.py 內的參數
7. 啟動 django dev server `python manage.py runserver 0.0.0.0:{bind_port}`
