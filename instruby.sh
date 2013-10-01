#!/bin/bash - 
#===============================================================================
#
#          FILE: instruby.sh
# 
#         USAGE: ./instruby.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 10/01/2013 17:08
#      REVISION:  ---
#===============================================================================

wget -O ruby-install-0.3.0.tar.gz https://github.com/postmodern/ruby-install/archive/v0.3.0.tar.gz
tar -xzvf ruby-install-0.3.0.tar.gz
cd ruby-install-0.3.0/
sudo make install
ruby-install ruby 1.9.3
wget -O chruby-0.3.7.tar.gz https://github.com/postmodern/chruby/archive/v0.3.7.tar.gz
tar -xzvf chruby-0.3.7.tar.gz
cd chruby-0.3.7/
sudo make install
echo "source /usr/local/share/chruby/chruby.sh" >/etc/profile.d/chruby.sh
chruby 1.9.3
gem install riemann-tools --no-ri --no-rdoc
