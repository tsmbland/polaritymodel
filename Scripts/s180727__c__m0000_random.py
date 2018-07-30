"""
180727
m0000
Testing random parameter sets on cluster (control)

"""

import M as x
import Models.m0000 as m0000
import sys

# x.datadirec = '../working/Tom/ModelData'
#
# p0 = m0000.Params(Da=0.28, Dp=0.15, konA=0.0085, koffA=0.0054, konP=0.0474, koffP=0.0073, kAP=0.19, kPA=2, ePneg=1,
#                   eAneg=2,
#                   pA=1.56, pP=1, L=67.3, xsteps=500, psi=0.174, Tmax=1000, deltat=0.01, Aeqmin=0, Aeqmax=0.5, Peqmin=0.5,
#                   Peqmax=1)
#
# params = ['konA', 'koffA', 'konP', 'koffP', 'kAP', 'kPA']
# ranges = [[0.001, 1], [0.001, 1], [0.001, 1], [0.001, 1], [0.01, 10], [0.01, 10]]
#
# x.alg_parsim_rand_clust(m=m0000.Model(p0), params=params, ranges=ranges, nsims=960, jobid=3, subjobid=0, cores=32,
#                         compression=2, node=int(sys.argv[1]), funcs=[x.mse, x.asi_a, x.asi_p])


############# Local: ################

x.datadirec = '../../../../../../../Volumes/lab-goehringn/working/Tom/ModelData'

# x.save_scores_batch(3, 0)

x.alg_singlesim(m0000.Model(x.loaddata(3, 0, 340).params), compression=0)
x.sliderplot()