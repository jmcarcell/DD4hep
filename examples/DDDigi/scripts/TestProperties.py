# ==========================================================================
#  AIDA Detector description implementation
# --------------------------------------------------------------------------
# Copyright (C) Organisation europeenne pour la Recherche nucleaire (CERN)
# All rights reserved.
#
# For the licensing terms see $DD4hepINSTALL/LICENSE.
# For the list of contributors see $DD4hepINSTALL/doc/CREDITS.
#
# ==========================================================================
from __future__ import absolute_import


def yes_no(val):
  if val:
    return "YES"
  return "NO "


def run():
  import DigiTest
  digi = DigiTest.Test(geometry=None)
  info = digi.info
  num_tests = 0
  histo = digi.create_action('DigiDepositEnergyMonitor/TestHisto')
  histo.histo1D_deposits = ("Energy", u"Some main deposit Title", 101, -0.5, 100.5)
  num_tests = num_tests + 1
  histo.histo1D_delta = ("Delta", u"Some delta Title", 50, -5, 5)
  num_tests = num_tests + 1
  histo.printProperties()
  info('property: histo1D_deposits =       %s [%s]' %
       (str(histo.histo1D_deposits), str(histo.histo1D_deposits.__class__),))
  num_tests = num_tests + 1

  input = digi.input_action('DigiParallelActionSequence/Test')

  input.add_property('property_int', 1)
  info('property: has_property =           %s  [%s]' %
       (yes_no(input.hasProperty('property_int')), str(input.property_int.__class__),))
  info('property: property_int =           %s' % (str(input.property_int),))
  input.property_int = 123456
  info('property: property_int =           %s' % (str(input.property_int),))
  if input.hasProperty('property_int'):
    num_tests = num_tests + 1

  input.add_vector_property('property_vector_int', [1, 2, 3])
  info('property: has_property =           %s [%s]' %
       (yes_no(input.hasProperty('property_vector_int')), str(input.property_vector_int.__class__), ))
  info('property: property_vector_int =    %s' % (str(input.property_vector_int),))
  input.property_vector_int = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
  info('property: property_vector_int =    %s' % (str(input.property_vector_int),))
  if input.hasProperty('property_vector_int'):
    num_tests = num_tests + 1

  input.add_list_property('property_list_int', [1, 2, 3])
  info('property: has_property =           %s [%s]' %
       (yes_no(input.hasProperty('property_list_int')), str(input.property_list_int.__class__),))
  info('property: property_list_int =      %s' % (str(input.property_list_int),))
  input.property_list_int = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
  info('property: property_list_int =      %s' % (str(input.property_list_int),))
  if input.hasProperty('property_list_int'):
    num_tests = num_tests + 1

  input.add_set_property('property_set_int', [1, 2, 3])
  info('property: has_property =           %s [%s]' %
       (yes_no(input.hasProperty('property_set_int')), str(input.property_set_int.__class__),))
  info('property: property_set_int =       %s' % (str(input.property_set_int),))
  input.property_set_int = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
  info('property: property_set_int =       %s' % (str(input.property_set_int),))
  if input.hasProperty('property_set_int'):
    num_tests = num_tests + 1

  input.add_property('property_double', 1.0)
  info('property: has_property =           %s [%s]' %
       (yes_no(input.hasProperty('property_double')), str(input.property_double.__class__),))
  info('property: property_double =        %s' % (str(input.property_double),))
  input.property_double = 123456.7
  info('property: property_double =        %s' % (str(input.property_double),))
  if input.hasProperty('property_double'):
    num_tests = num_tests + 1

  input.add_vector_property('property_vector_double', [1.1, 2, 3])
  info('property: has_property =           %s [%s]' %
       (yes_no(input.hasProperty('property_vector_double')), str(input.property_vector_double.__class__),))
  info('property: property_vector_double = %s' % (str(input.property_vector_double),))
  input.property_vector_double = [1.5, 2, 3, 4, 5, 6, 7, 8, 9, 0]
  info('property: property_vector_double = %s' % (str(input.property_vector_double),))
  if input.hasProperty('property_vector_double'):
    num_tests = num_tests + 1

  input.add_list_property('property_list_double', [1.1, 2, 3])
  info('property: has_property =           %s [%s]' %
       (yes_no(input.hasProperty('property_list_double')), str(input.property_list_double.__class__), ))
  info('property: property_list_double =   %s' % (str(input.property_list_double),))
  input.property_list_double = [1.5, 2, 3, 4, 5, 6, 7, 8, 9, 0]
  info('property: property_list_double =   %s' % (str(input.property_list_double),))
  if input.hasProperty('property_list_double'):
    num_tests = num_tests + 1

  input.add_set_property('property_set_double', [1.1, 2, 3])
  info('property: has_property =           %s [%s]' %
       (yes_no(input.hasProperty('property_set_double')), str(input.property_set_double.__class__),))
  info('property: property_set_double =    %s' % (str(input.property_set_double),))
  input.property_set_double = [1.5, 2, 3, 4, 5, 6, 7, 8, 9, 0]
  info('property: property_set_double =    %s' % (str(input.property_set_double),))
  if input.hasProperty('property_set_double'):
    num_tests = num_tests + 1

  input.add_property('property_string', "string_1")
  info('property: has_property =           %s [%s]' %
       (yes_no(input.hasProperty('property_string')), str(input.property_string.__class__),))
  info('property: property_string =        %s' % (input.property_string,))
  input.property_string = "string_1123456"
  info('property: property_string =        %s' % (input.property_string,))
  if input.hasProperty('property_string'):
    num_tests = num_tests + 1

  input.add_vector_property('property_vector_string', ["string1", "string2", "string3"])
  info('property: has_property =           %s [%s]' %
       (yes_no(input.hasProperty('property_vector_string')), str(input.property_vector_string.__class__),))
  info('property: property_vector_string = %s' % (input.property_vector_string,))
  input.property_vector_string = ["string1", "string2", "string3", "string4", "string5", "string6"]
  info('property: property_vector_string = %s' % (input.property_vector_string,))
  if input.hasProperty('property_vector_string'):
    num_tests = num_tests + 1

  input.add_position_property('property_position', (1., 2., 3.))
  info('property: has_property =           %s [%s]' %
       (yes_no(input.hasProperty('property_position')), str(input.property_position.__class__),))
  info('property: property_position =      %s' % (input.property_position,))
  input.property_position = (111.1, 222.2, 333.3)
  info('property: property_position =      %s' % (input.property_position,))
  if input.hasProperty('property_position'):
    num_tests = num_tests + 1

  info('We checked %d properties interactions.' % (num_tests,))
  if num_tests == 14:
    info('Property test PASSED')


if __name__ == '__main__':
  run()
