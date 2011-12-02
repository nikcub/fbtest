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
  names.py

  module with common first and surnames and utility functions

  all data taken from wikipedia
  
  This source file is subject to the new BSD license that is bundled with this 
  package in the file LICENSE.txt. The license is also available online at the 
  URL: <http://nikcub.appspot.com/bsd-license.txt>

  :copyright: Copyright (C) 2011 Nik Cubrilovic and others, see AUTHORS
  :license: new BSD, see LICENSE for more details.
"""

__version__ = '0.0.1'
__author__ = 'Nik Cubrilovic <nikcub@gmail.com>'

from random import choice

na_surnames = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Miller', 'Davis', 'García', 'Rodríguez', 'Wilson', 'Martínez', 'Anderson', 'Taylor', 'Thomas', 'Hernández', 'Moore', 'Martin', 'Jackson', 'Thompson', 'White', 'López', 'Lee', 'González', 'Harris', 'Clark', 'Lewis', 'Robinson', 'Walker', 'Pérez', 'Hall', 'Young', 'Allen', 'Sánchez', 'Wright', 'King', 'Scott', 'Green', 'Baker', 'Adams', 'Nelson', 'Hill', 'Ramírez', 'Campbell', 'Mitchell', 'Roberts', 'Carter', 'Phillips', 'Evans', 'Turner', 'Torres', 'Parker', 'Collins', 'Edwards', 'Stewart', 'Flores', 'Morris', 'Nguyen', 'Murphy', 'Rivera', 'Cook', 'Rogers', 'Morgan', 'Peterson', 'Cooper', 'Reed', 'Bailey', 'Bell', 'Gómez', 'Kelly', 'Howard', 'Ward', 'Cox', 'Díaz', 'Richardson', 'Wood', 'Watson', 'Brooks', 'Bennett', 'Gray', 'James', 'Reyes', 'Cruz', 'Hughes', 'Price', 'Myers', 'Long', 'Foster', 'Sanders', 'Ross', 'Morales', 'Powell', 'Sullivan', 'Russell', 'Ortiz', 'Jenkins', 'Gutiérrez', 'Perry', 'Butler', 'Barnes', 'Fisher']
oc_males = ['Jack', 'Cooper', 'Oliver', 'Noah', 'Thomas', 'Lucas', 'Lachlan', 'William', 'Jackson', 'Charlie']
oc_females = ['Lily','Ruby','Charlotte','Chloe', 'Sophie', 'Olivia', 'Isabella', 'Mia', 'Emily', 'Ava', 'Amelia']

def gen_name():
  """Return a random name from a random sex
  """
  return choice(globals()[choice(['oc_males', 'oc_females'])]) + ' ' + choice(na_surnames)