"""
Main
"""
import random as rnd
import argparse
from tent_map import TentMap


def main():
    """Main function"""
    parser = argparse.ArgumentParser(
        description='It shows tent map distribution')
    parser.add_argument("-a", "--alpha", nargs='?',
                        help="alpha param value", default=2, type=float)
    parser.add_argument("-x", "--initial-cond", nargs='?',
                        help="x_0 value", default=-1, type=float)
    parser.add_argument("-p", "--parts", nargs='?',
                        help="the number of parts on which [0; 1] segment will be divided",
                        default=10, type=int)
    parser.add_argument("-i", "--iterations", nargs='?',
                        help="the number of iterations", default=100000, type=int)
    args = parser.parse_args()
    tent_map = TentMap(
        rnd.random() if args.initial_cond is -1 else args.initial_cond,
        args.parts)
    tent_map.find_distribution(args.alpha, args.iterations)
    tent_map.plot()

if __name__ == "__main__":
    main()
