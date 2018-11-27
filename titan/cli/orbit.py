# -*- coding: utf-8 -*-
import argparse

from ..orbit import orbit

def cli_orbit(argv=None):
    parser = argparse.ArgumentParser(
        description="""Get Titan (Saturn's moon) orbital constrains""")

    parser.add_argument('values', nargs='+', type=str, metavar='date|Ls',
                        help='Calendar date  (YYYY-MM-DD or YYYY/MM/DD or YYYY-MM-DDThh:mm:ss.ms) or Solar longitude value(s)')

    parser.add_argument('-o', type=int, default=1, metavar='offset',
                        help='Titan year offset since 1980 (default: 1)')

    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')

    args, _ = parser.parse_known_args(argv)
    for val in args.values:
        try:
            Ls = float(val)
            date = orbit.date(Ls, Ty=args.o)
            
            if args.verbose:
                print("Ls: {}º (+ {} Titan year since 1980)-> {}".format(val, args.o, date))
            else:
                print(date)

        except ValueError:
            Ls = orbit.Ls(val)

            if args.verbose:
                print("{} -> Ls: {:.2f}º".format(val, Ls))
            else:
                print(Ls)
