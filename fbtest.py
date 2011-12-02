#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=2:sw=2:expandtab
#
# Copyright (c) 2010-2011, Nik Cubrilovic. All rights reserved.
#
# <nikcub@gmail.com> <http://nikcub.appspot.com>  
#
# Licensed under a BSD license. You may obtain a copy of the License at
#
#     http://nikcub.appspot.com/bsd-license
#
"""
  fbtest.py

  gen fb test accounts

  This source file is subject to the new BSD license that is bundled with this 
  package in the file LICENSE.txt. The license is also available online at the 
  URL: <http://nikcub.appspot.com/bsd-license.txt>

  :copyright: Copyright (C) 2011 Nik Cubrilovic and others, see AUTHORS
  :license: new BSD, see LICENSE for more details.
"""

__version__ = '0.0.1'
__author__ = 'Nik Cubrilovic <nikcub@gmail.com>'

import sys
import logging
from simplefb import FBGraph, json_parse, json_dump
try:
  from conf import disconnect_app as appdat
except ImportError:
  pass

# conf here. add 'access_token' if you have one otherwise the lib will req
default_conf = {
  'id': '',
  'secret': '',
}

commands = ['list', 'create', 'del', 'writehtml', 'writejson', 'help']

def main(appdat):
  print 'fbtest version(%s) by %s\n' % (__version__, __author__)

  if len(sys.argv) < 2 or sys.argv[1] not in commands or sys.argv[1] == 'help':
    print_help()
    return None
  
  comm = sys.argv[1]
  args = None if len(sys.argv) <= 2 else sys.argv[2]
  
  try:
    fb = FBGraph(appdat)
    us = read_users()
    
    print "%d tets users in local cahce" % len(us)

    if comm == 'list':
      s_users = fb.list_users()
      print '* Found %d users on server.' % len(s_users)
      for user in s_users:
        print user
      return 1
    
    if comm == 'create':
      num = 1 if not args else int(args)
      if num < 1 or num > 200:
        print 'dont be crazy'
        return 1
      print 'Creating %d users' % num
      for x in range(0, num):
        user = fb.create_user()
        if 'id' in user:
          us.append(user)
          write_users(us)
          print "created: %s : %s" % (user['name'], user['id'])
      return 1

    if comm == 'writejson':
      s_users = fb.list_users()
      print '* Found %d users on server.' % len(s_users)
      write_users(us)
      print "* wrote to file users.json"
      return 1

    if comm == 'writehtml':
      write_html(us, args)
      return 1
    
  except Exception, e:
    print "Error: %s" % str(e)
    return None

def print_help():
  print """usage: fbtest <command> [arguments]

  commands:
    list                  - list all test users
    create <num>          - create <num> of users
    del <id>              - delete test user with ID
    writehtml <file>      - write all users to html file
    writejson <file>      - write all users to json file
    help                  - show what you are looking at now, again
  
  the generated html file has login urls for each user
  
  pretty easy. 
"""

def write_html(users, filename=None):
  if not filename:
    filename = 'users.html'
  try:
    f = open(filename, 'w')
    f.write("<html><body><h1>FB Test Users</h1><table>")
    for u in users:
      f.write("<tr><td>%s</td><td>%s</td><td><a href=\"%s\">login url</a></td>" % (u['id'], u['name'], u['login_url']))
    f.write("</table></body></html>")
  except Exception, e:
    raise e
  finally:
    f.close()
  print "users written to %s" % filename
  
def write_users(users):
  try:
    f = open('users.json', 'w')
    for user in users:
      f.write(json_dump(user) + '\n')
  finally:
    f.close()

def read_users():
  users = []
  try:
    for userline in open('users.json'):
      user = json_parse(userline)
      users.append(user)
    return users
  except Exception, e:
    return []

if __name__ == '__main__':
  main(appdat)
