# -*- coding: utf-8 -*-
import numpy as np

# Constantes
UA = 149597870.7  # 1 Astronomical unit (km)

# Default orbital parameters
ORBIT = {
    'saturn_orbit': 15.945,             # 1 Saturn orbit (days)
    'sun_orbit':    10751,              # 1 Sun orbit (days)
    'obliquity':    26.730882944988142,
    'vernal_equinox': '1980-02-22',     # Date of the first vernal equinox (before Voyager 1)
    'ellipse': {
        'A': 6.1664830805512354,
        'B': 6.0482745790986066,
        'C': 101.03535416292833,
    },
}

def readDate(date):
    '''Read date as datetime64'''
    if type(date) == str:
        date = np.datetime64(
            date.replace('/', '-').replace(' ', 'T').split('T')[0], 'D')
    return date

class Orbit:
    '''Titan orbit functions and parametes'''

    def __init__(self):
        '''Init default parameters'''
        self.Tday = ORBIT['saturn_orbit']

        # Default orbit parameters calculated with NAIF Space Kernels
        self.obl   = ORBIT['obliquity']
        self.orbit = np.timedelta64(ORBIT['sun_orbit'], 'D')
        self.eq_v  = np.datetime64(ORBIT['vernal_equinox'])
        self.A     = ORBIT['ellipse']['A']
        self.B     = ORBIT['ellipse']['B']
        self.C     = ORBIT['ellipse']['C']
        return

    def __repr__(self):
        return 'Titan orbit functions and parametes'

    def Ls(self, date, eps=1.e-7, imax=25):
        '''Calculate the solar longitude corresponding to a date.

        Parameters
        -----------
        date : str, numpy.datetime64
            Input date (YYYY-MM-DD or YYYY/MM/DD or YYYY-MM-DDThh:mm:ss.ms)
        eps : float, optional
            Precision of the convergence
        imax : int, optional
            Number maximum of iteration to reach the convergence, throw a ValueError otherwise.

        Note
        -----
        The value of Ls is the solution of a transcendental equation which
        is numerically solved with the Newton method:

        L_s^0 = 360 · (Date - Eq^V)/Orbit) - B
        
        L_s^(n+1) = L_s^n - (
            L_s^n - L_s^0 + A · sin(2·pi·(L_s^n - C)/360)
        )/(
            1 + A · 2·pi/360 · cos(2·pi·(L_s^n - C)/360)
        )

        Return
        -------
        Ls : real
            Solar latitude corresponding to the input date
        '''
        date = readDate(date)

        Ls_0 = ( (360.*(date - self.eq_v).astype(int))/self.orbit.astype(float) - self.B ) % 360
        Ls   = Ls_0
        for ii in range(imax):
            dLs = - (Ls - Ls_0 + self.A * np.sin(2*np.pi*(Ls - self.C)/360.))         \
                / (1 + self.A * 2*np.pi/360. * np.sin(2*np.pi*(Ls - self.C)/360.))
            Ls = Ls + dLs
            if np.abs(dLs) < eps:
                break
        else:
            raise ValueError('Max number of iteration reach without getting convergence.')
        return Ls % 360

    def date(self, Ls, Ty=0):
        '''Calculate the date corresponding to a solar longitude.

        Parameters
        -----------
        Ls : real
            Input solar latitude
        Ty : int, optional
            Number of Titan year after 1980-02-22 (Vernal Equinox before Voyager 1)

        Return
        -------
        date : numpy.datetime64
            Date corresponding to the input solar latitude
        '''
        date = np.round(
            self.orbit.astype(int)/360. * (
                Ls + self.A * np.sin(2*np.pi*(Ls - self.C)/360.) + self.B + 360 * Ty
            )
        )
        return self.eq_v + np.timedelta64(int(date), 'D')


orbit = Orbit()
