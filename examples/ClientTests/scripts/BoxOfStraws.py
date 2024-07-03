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
#
#
from __future__ import absolute_import, unicode_literals
import os
import time
import DDG4
from DDG4 import OutputLevel as Output
from g4units import GeV, MeV, m
#
#
"""

   dd4hep simulation example setup using the python configuration

   @author  M.Frank
   @version 1.0

"""


def run():
  args = DDG4.CommandLine()
  kernel = DDG4.Kernel()
  logger = DDG4.Logger('BoxOfStraws')
  install_dir = os.environ['DD4hepExamplesINSTALL']
  kernel.loadGeometry(str("file:" + install_dir + "/examples/ClientTests/compact/BoxOfStraws.xml"))

  DDG4.importConstants(kernel.detectorDescription(), debug=False)
  geant4 = DDG4.Geant4(kernel, tracker='Geant4TrackerCombineAction')
  geant4.printDetectors()
  # Configure UI
  if args.macro:
    ui = geant4.setupCshUI(macro=args.macro)
  else:
    ui = geant4.setupCshUI()
  if args.batch:
    ui.Commands = ['/run/beamOn ' + str(args.events), '/ddg4/UI/terminate']
  if args.print:
    logger.setPrintLevel(int(args.print))
  #
  # Configure field
  geant4.setupTrackingField(prt=True)
  #
  # Configure G4 geometry setup
  seq, act = geant4.addDetectorConstruction("Geant4DetectorGeometryConstruction/ConstructGeo")
  act.DebugVolumes = True
  #
  # Assign sensitive detectors according to the declarations 'tracker' or 'calorimeter', etc
  seq, act = geant4.addDetectorConstruction("Geant4DetectorSensitivesConstruction/ConstructSD")
  #
  # Assign sensitive detectors in Geant4 by matching a regular expression in the detector sub-tree
  seq, act = geant4.addDetectorConstruction("Geant4RegexSensitivesConstruction/ConstructSDRegEx")
  act.Detector = 'BoxOfStrawsDet'
  act.OutputLevel = Output.ALWAYS
  act.Regex = '/world_volume_(.*)/BoxOfStrawsDet_(.*)/row_(.*)/straw_(.*)'
  #
  # Configure I/O
  geant4.setupROOTOutput('RootOutput', 'BoxOfStraws_' + time.strftime('%Y-%m-%d_%H-%M'))
  #
  # Setup particle gun
  gun = geant4.setupGun("Gun", particle='e+', energy=10 * GeV, multiplicity=1)
  #
  # And handle the simulation particles.
  part = DDG4.GeneratorAction(kernel, "Geant4ParticleHandler/ParticleHandler")
  kernel.generatorAction().adopt(part)
  part.SaveProcesses = ['Decay']
  part.MinimalKineticEnergy = 100 * MeV
  user = DDG4.Action(kernel, "Geant4TCUserParticleHandler/UserParticleHandler")
  user.TrackingVolume_Zmax = 2.5 * m
  user.TrackingVolume_Rmax = 2.5 * m
  part.adopt(user)
  #
  # Map sensitive detectors of type 'BoxOfStraws' to Geant4CalorimeterAction
  sd = geant4.description.sensitiveDetector(str('BoxOfStrawsDet'))
  logger.info(f'+++ BoxOfStraws: SD type: {str(sd.type())}')
  seq, act = geant4.setupDetector(name='BoxOfStrawsDet', action='MyTrackerSDAction')
  act.HaveCellID = False
  #
  # Now build the physics list:
  phys = geant4.setupPhysics(str('QGSP_BERT'))
  phys.dump()
  geant4.execute()


if __name__ == "__main__":
  run()
