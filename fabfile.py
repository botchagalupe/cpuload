from fabric.api import *

env.hosts = ['ubuntu@54.226.181.107:22','ubuntu@54.211.131.14','ubuntu@54.242.21.58','ubuntu@54.234.56.75','ubuntu@54.227.183.52','ubuntu@23.20.187.95','ubuntu@23.22.43.29','ubuntu@54.234.127.71']
env.password="ubuntu"
def deploy():
    sudo("apt-get install git")
    sudo("apt-get install python-setuptools")
    sudo ("easy_install supervisor")
    sudo ("rm -rf /tmp/cpuload")
    run ("git clone https://github.com/avivl/cpuload.git /tmp/cpuload" )
    sudo ("chmod +x /tmp/cpuload/instruy.sh")
    sudo ("/tmp/cpuload/instruby.sh")
    sudo ("mkdir -p /var/log/supervisord/")
    sudo ("supervisord -c /tmp/cpuload/supervisord.conf")
   # run ("python /tmp/cpuload/cpuloader.py")


