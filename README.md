# hwf_privacy_preserving_api

## Dev Environment

```
virtualenv -p python3 venv
source ./venv/bin/activate
pip install -r requirements.txt
```

## Running

```
export FLASK_APP=api.py
flask run
```

Once `FLASK_APP` is defined in a shell session, the `export` step
may be skipped for subsequent runs.

## Vagrant
Clone Repo

```
cd Vagrant
vagrant up
vagrant ssh
```
This will start a local Ubuntu instance, configure it and provision it with the code

## AWS
Clone Repo

```
cd aws
run-ansible.sh
```
Set up your variables in run-ansible.sh and build-ec2.yml first, but this will create and configure an EC2 instance
