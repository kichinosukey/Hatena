
import argparse
import sys
import random

import matplotlib.pyplot as plt

EPSILON = sys.float_info.epsilon

def clip(v, vmin, vmax):
    return max(vmin, min(v, vmax))

def cross_over(x1, x2, lb, ub, distribution_index=1):

    # in case x1 and x2 are not very close each other
    if (x2 - x1) > EPSILON:
        if x2 > x1:
            y2 = x2
            y1 = x1
        else:
            y2 = x1
            y1 = x2

        beta = 1.0 / (1.0 + (2.0 * (y1 - lb) / (y2 -y1)))
        alpha = 2.0 - pow(beta, distribution_index + 1.0)
        rand = random.uniform(0.0, 1.0)

        if (rand <= 1.0 / alpha):
            betaq = (alpha*rand) ** (1/(distribution_index+1))
        else:
            betaq = 1/(2 - rand*alpha)**(1/(distribution_index))
        
        x1 = 0.5*((y1 + y2) - betaq*(y2 - y1))

        beta = 1.0 / (1.0 + (2 * (lb - y2) / (y2 - y1)))
        alpha = (2 - pow(beta, distribution_index+1))

        if (rand <= 1.0 / alpha):
            betaq = (rand*alpha) ** (1/(distribution_index+1))
        else:
            betaq = (1/(2 - rand*alpha)) ** (1/(distribution_index+1))
        
        x2 = 0.5*((y1+y2) + betaq*(y2-y1))

        # randomly swap the values
        if bool(random.getrandbits(1)):
            x1, x2 = x2, x1
        
        x1 = clip(x1, lb, ub)
        x2 = clip(x2, lb, ub)

    return x1, x2

def plot(l, dist_idx):
    result1 = [cross_over(l[0], l[1], l[2], l[3], dist_idx)[0] for i in range(10000)]
    result2 = [cross_over(l[0], l[1], l[2], l[3], dist_idx)[1] for i in range(10000)]

    fig = plt.figure()
    plt.scatter(result1, result2, color='k', marker='o')
    plt.show()

def set_argparse():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest='command')

    # sbx_parser
    sbx_parser = subparser.add_parser('sbx', help='Run cross over once')
    sbx_parser.add_argument('-l', '--list', type=list, default=[0.3, 0.6, 0, 1, 10])

    # plot_parser
    plot_parser = subparser.add_parser('plot', help='Plot ')
    plot_parser.add_argument('-l', '--list', type=list, default=[0.3, 0.6, 0, 1])
    plot_parser.add_argument('-d', '--dist_idx', type=int, default=10)

    return parser.parse_args()

if __name__ == '__main__':

    args = set_argparse()

    if args.command == 'sbx':
        l = args.list
        print(cross_over(l[0], l[1], l[2], l[3], l[4]))
    
    elif args.command == 'plot':
        plot(args.list, args.dist_idx)