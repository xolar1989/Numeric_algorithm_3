
from program.objects.Area import Area
from program.interpolation_solutions.Langrange import Langrange

from program.interpolation_solutions.Spline import Spline


if __name__ == '__main__':
    #
    kk = Area("DeathValley")
    # sol = Langrange(kk , 14 , False)
    # sol.create()
    # sol.show_plots()

    kk2 = Spline(kk ,20, True)

    kk2.create()

    kk2.show_plots()
