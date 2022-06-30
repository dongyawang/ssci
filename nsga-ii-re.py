from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.algorithms.moo.ctaea import CTAEA
from pymoo.algorithms.moo.nsga3 import NSGA3

from pymoo.factory import  get_reference_directions
from pymoo.optimize import minimize

from pymoo.visualization.scatter import Scatter
from reproblem import *

problem = CRE22()
ref_dirs = get_reference_directions("das-dennis", 2, n_partitions=64)

algorithm = NSGA2(pop_size=100)
algorithm = NSGA3(pop_size=92,
                  ref_dirs=ref_dirs)
# IBEA
algorithm = CTAEA(ref_dirs=ref_dirs)

res = minimize(problem,
               algorithm,
               ('n_gen', 200),
               seed=1,
               verbose=False)

plot = Scatter()
plot.add(problem.pareto_front(), plot_type="line", color="black", alpha=0.7)
plot.add(res.F, facecolor="none", edgecolor="red")
plot.show()
