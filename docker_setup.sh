apt-get update -y
apt-get install jq awscli -y
##java
#apt install default-jre -y
#apt install default-jdk -y
##allure
curl -o allure-2.15.0.tgz -Ls https://github.com/allure-framework/allure2/releases/download/2.15.0/allure-2.15.0.tgz
tar -zxvf allure-2.15.0.tgz -C /opt/
ln -s /opt/allure-2.15.0/bin/allure /usr/bin/allure
allure --version
##chrome
curl -Lo /tmp/Google\ Chrome.dmg https://dl.google.com/chrome/mac/stable/GGRO/googlechrome.dmg
hdiutil attach /tmp/Google\ Chrome.dmg
ditto -rsrc /Volumes/Google\ Chrome/Google\ Chrome.app /Applications/Google\ Chrome.app
hdiutil detach /Volumes/Google\ Chrome
rm /tmp/Google\ Chrome.dmg
