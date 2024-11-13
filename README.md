# Machine-Learning-Project
Complete Machine Learning Project

### Software and account requiremets

1. [Github Account](https://github.com/JotiRoy01/Machine-Learning-Project.git)

2. [Heroku Account](https://dashboard.heroku.com/apps#)


Create conda environment

```bash
conda init
```
```bash
source activate base
```
```bash
conda create -p <envname> python==3.10 -y
```
* here -p is a prefix.it create environment folder in current location.we can also write
```bash
conda create --prefix ./<envname> python==3.10 -y
```
* Check conda environment
```bash
conda info --envs
```

* Create requirements.txt file
```bash
touch requirements.txt
```
* Install requirements.txt
```bash
pip install -r requirements.txt
```

> Note: To ignore file or folder from git we can write name of file or folder in .gitignore file

* To check remote url
```bash
git remote -v
```
* To setup CI/CD pipeline in heroku we need 3 information
```bash
1. HEROKU_EMAIL: jotiroy2811@gmail.com
2. HEROKU_API_KEY: HRKU-2209da98-d709-435e-80c3-3b08bdb9a45d
3. HEROKU_APP_NAME: first-ml-regression-app
```
BUILD DOCKER IMAGE
```bash
docker build -t <image_name>:<tagname> .
```
> Note Image name for docker must be lowercase
* To list docker image
```bash
docker images
```
* Run docker image
```bash
docker run -p 5000:5000 -e PORT=5000 8df3e931f286
docker run -p 8000:8000 -e PORT=8000 8df3e931f286
docker run -p 8089:8089 -e PORT=8089 8df3e931f286
```
* To check running container in docker 
```bash
docker ps
```
* To stop docker container
```bash
docker stop <container_id>
```
* Create folder
```bash
mkdir -p .github/workflows
touch .githup/workflow/main.yaml
mkdir housing
touch housing/__init__.py
touch setup.py
```
* Intall setup.py tools
```bash
python setup.py install
```
* Intall Package or our own Library in that case "housing"
```bash
pip install -e .
```
* create bash file for initial setup
```bash
touch init_setup.sh
```
* To run init_setup.sh file
```bash
bash init_setup.sh
```
