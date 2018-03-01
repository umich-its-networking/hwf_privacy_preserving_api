#!/bin/bash
# This assumes you have a profile set in ~/.aws
# And a EC2 keypair and all that
# Also make sure to customize the variables in build-ec2.yml
export AWS_REGION="us-east-1"
export AWS_PROFILE="cloud-ambassadors"
KEYFILE=~/.ssh/dnowell-ca.pem
ansible-playbook build-ec2.yml
AWSIP=`cat /tmp/aws_public_ip`
echo $AWSIP
cd ../Vagrant
ansible-playbook -i "${AWSIP}," playbook.yml --key-file $KEYFILE --user ubuntu -e 'ansible_python_interpreter=/usr/bin/python3'

