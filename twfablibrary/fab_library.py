from fabric.api import *
from fabric.state import output
import os

def update_package_list():
    sudo('apt-get update')

def upgrade():
    sudo('apt-get -y upgrade')

def dist_upgrade():
    sudo('apt-get -y dist-upgrade')

def install_package(package):
    with settings(hide('warnings', 'stderr'), warn_only= True):
        result = sudo('dpkg-query -p %s' % package)
    if result.failed is False:
        warn('%s is already installed' % package)
    else:
        sudo('apt-get -y --no-upgrade install %s' % package)

def remove_package(package):
    with settings(hide('warnings', 'stderr'), warn_only= True):
        result = sudo('dpkg-query --show %s' % package)
    if result.failed is False:
        sudo('apt-get -y remove %s' % package)
    else:
        warn('%s is not installed' % package)

def git_clone_or_update(path, git_path, sudo_user = "", checkout_path = None):

    # get the package name
    split = git_path.split('/')
    name = split[-1].split('.')[0]

    with cd(path):
        result = run('ls')
        if name in result:
            with cd(os.path.join(path, name)):
                run('git pull') if not sudo_user else sudo('git pull', user = sudo_user)
        elif '.git' in result:
            run('git pull') if not sudo_user else sudo('git pull', user = sudo_user)
        else:
            if sudo_user and checkout_path:
                sudo('git clone %s %s' % (git_path, checkout_path), user = sudo_user)
            elif sudo_user:
                sudo('git clone %s' % git_path, user = sudo_user)
            elif checkout_path:
                run('git clone %s %s' % (git_path, checkout_path))
            else:
                run('git clone %s' % git_path)

    return name

def add_key():
    run('mkdir -p .ssh')
    with cd('.ssh'):
        put('~/.ssh/authorized_keys', 'authorized_keys')


def xrun(command, hidden='', *args, **kwargs):
    old_state = output.running
    output.running = False
    print '[%s] run: %s' % (env.host_string, command)
    run(command + hidden, *args, **kwargs)
    output.running = old_state

def xsudo(command, hidden='', *args, **kwargs):
    old_state = output.running
    output.running = False
    print '[%s] sudo: %s' % (env.host_string, command)
    sudo(command + hidden, *args, **kwargs)
    output.running = old_state
    
def add_group(groupname):
    with settings(warn_only = True):
        sudo('sudo addgroup --system %s' % groupname)
        
def add_user_nologin(username, groupname, home):
    with settings(warn_only = True):
        sudo('sudo adduser --system --home %s --shell /bin/bash --ingroup %s --disabled-password --disabled-login %s' % (home, groupname, username))
