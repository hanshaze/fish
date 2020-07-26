# Run HiddenEye in Docker Compose

![docker](https://img.shields.io/badge/Docker-v19.03.12-blue?style=plastic&logo=docker)
![dockercompose](https://img.shields.io/badge/Docker_Compose-v1.25.4-orange?style=plastic&logo=docker)
![Maintainer](https://img.shields.io/badge/Maintainer-Equinockx-success?style=plastic&logo=terraform)

# Requeriments

- [X] Docker
- [X] docker-compose

# Usage Mode

Clone the repo from Github
```bash
git clone https://github.com/DarkSecDevelopers/HiddenEye
cd HiddenEye/Docker
```

Run docker-compose

```bash
docker-compose up --build -d
```
Verify of the container is running with:

```bash
docker-compose ps
```

Executing HiddenEye inside of container

```bash
docker-compose exec hidden python3 HiddenEye.py
```




