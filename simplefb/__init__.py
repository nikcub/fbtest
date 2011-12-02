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
  facebook.py

  facebook graph client

  This source file is subject to the new BSD license that is bundled with this 
  package in the file LICENSE.txt. The license is also available online at the 
  URL: <http://nikcub.appspot.com/bsd-license.txt>

  :copyright: Copyright (C) 2011 Nik Cubrilovic and others, see AUTHORS
  :license: new BSD, see LICENSE for more details.
"""

__version__ = '0.0.1'
__author__ = 'Nik Cubrilovic <nikcub@gmail.com>'

import urllib
from names import gen_name

try:
  import json
  json_parse = lambda s: json.loads(s)
  json_dump = lambda s: json.dumps(s)
except ImportError:
  try:
    import simplejson
    json_parse = lambda s: simplejson.loads(s)
    json_dump = lambda s: simplejson.dumps(s)
  except ImportError:
    try:
      # For Google AppEngine
      from django.utils import simplejson
      json_parse = lambda s: simplejson.loads(s)
      json_dump = lambda s: simplejson.dumps(s)
    except ImportError:
      logging.exception('no json parser')

class FBGraph(object):
  
  def __init__(self, appdat):
    self.appdat = appdat
    self.appid = appdat['id']
    self.appsecret = appdat['secret']
    
    if not 'access_token' in appdat:
      r = get_oauth_access_token()
      if r:
        print " got new access token (you might want to store it in conf): %s" %r
        self.accesstoken = self.appdat['access_token'] = r
      else:
        raise "no access token :("
    else:
      self.accesstoken = appdat['access_token']

  def get_oauth_access_token(self):
    post_args = None
    get_args = {'client_id': self.appid, 'client_secret': self.appsecret, 'grant_type': 'client_credentials'}
    response = self.request('/oauth/access_token', get_args)
    if response:
      name, value = response.split('=', 1)
      if name != 'access_token':
        raise 'could no get access token (invalid resp)'
      return value
    raise 'could not get access token (no resp)'

  def create_user(self, name=None):
    get_params = {
      'installed': True,
      'name': gen_name(),
      'permissions': 'read_stream',
      'method': 'post',
      'access_token': self.accesstoken
    }
    newuser = self.request('/accounts/test-users', get_params, None, self.appid)
    return newuser

  def list_users(self):
    get_params = {
      'access_token': self.accesstoken
    }
    dat = self.request('/accounts/test-users', get_params, None, self.appid)
    if not type(dat) == type({}) or 'data' not in dat:
      raise 'invalid response'
    return dat['data']

  def request(self, path, get_args=None, post_args=None, app_id=None):
    post_data = None if post_args is None else urllib.urlencode(post_args)
    get_data = None if get_args is None else urllib.urlencode(get_args)
    req_url = "https://graph.facebook.com"
    req_url = req_url if app_id is None else req_url + '/' + app_id
    req_url += path
    req_url = req_url if get_data is None else req_url + '?' + get_data
    filereq = urllib.urlopen(req_url, post_data)
    try:
      response = filereq.read()
      response = json_parse(response)
    finally:
      filereq.close()
      return response
