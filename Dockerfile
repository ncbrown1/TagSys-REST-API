FROM 		fedora
MAINTAINER 	Nick Brown "ncbrown@engineering.ucsb.edu"

RUN yum -y update
RUN yum -y install python-pip python-devel
RUN yum -y groupinstall "Development tools"
RUN yum -y install openssl-devel mysql-devel
RUN mkdir ~/helpdesk-web
RUN yum -y install python-ldap
RUN pip install django MySQL-python Pillow django-registration django-filter djangorestframework django-auth-ldap django-widget-tweaks flup httplib2 requests wsgiref
ADD helpdesk-web /helpdesk-web
RUN python /helpdesk-web/manage.py collectstatic --noinput
EXPOSE 5000
