from fabric.api import *

env.hosts = ['ubuntu@54.226.181.107:22']

def deploy():
    sudo("apt-get install git")
    sudo("apt-get install python-setuptools")
    sudo ("easy_install supervisor")
    sudo ("rm -rf /tmp/cpuload")
    run ("git clone https://github.com/avivl/cpuload.git /tmp/cpuload" )
   # run ("python /tmp/cpuload/cpuloader.py")


