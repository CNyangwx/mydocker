#
# source directory
#
SOURCE_DIR=/docker/

#
# Container Timezone
#
TZ=Asia/Shanghai

#
# Container package fetch url
#
# Can be empty, followings or others:
# mirrors.163.com
# mirrors.aliyun.com
# mirrors.ustc.edu.cn
#
CONTAINER_PACKAGE_URL=mirrors.aliyun.com

#
# g++
#
g++_VERSION=1.15.7-alpine
g++_HTTP_HOST_PORT=80
g++_HTTPS_HOST_PORT=443
g++_CONFD_DIR=/dnmp/services/g++/conf.d
g++_CONF_FILE=/dnmp/services/g++/g++.conf
g++_SSL_CERTIFICATE_DIR=/dnmp/services/g++/ssl
g++_LOG_DIR=/dnmp/logs/g++
# Available apps
g++_INSTALL_APPS=
# Available 
g++_EXTENSIONS=