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

import logging
from facebook import FBGraph, json_parse, json_dump
from conf import disconnect_app

def main(appdat):
  print 'fbtest version(%s) by %s\n' % (__version__, __author__)

  try:
    fb = FBGraph(appdat)
    s_users = fb.list_users()
    c_users = read_users()
    
    print '* Found %d users on server.' % len(s_users)
    print '* Found %d users in local cache.' % len(c_users)

    if len(s_users) > len(c_users):
      print '* Updating local cache..'
      write_users(s_users)
    
  except Exception, e:
    print "Error: %s" % str(e)
    return None


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
    raise e

if __name__ == '__main__':
  main(disconnect_app)
