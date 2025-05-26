import math
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

def find_pdf(num_dice, num_success, prob_success):
    prob_fail = 1 - prob_success
    nCr = math.comb(num_dice, num_success)
    prob = nCr * (prob_success ** num_success) * (prob_fail ** (num_dice - num_success))
    return prob

def find_cdf(count, pdf_list, dice_vals_list): # Probability that there are {count} or more of a number rolled
    prob = 0
    for i in range(len(pdf_list)):
        if (dice_vals_list[i] < count):
            pass
        else:
            prob = prob + pdf_list[i]
    return prob


def binomial_parameters(num_dice, prob_success):
    expected_value = num_dice * prob_success
    variance = num_dice * prob_success * (1 - prob_success)
    return expected_value, variance

if __name__ == "__main__":
    num_dice = 100
    prob_success = 1 / 6
    prob_list = []
    dice_vals = range(num_dice+1)

    for die in dice_vals:
        prob_list.append(find_pdf(num_dice, die, prob_success))

    expected_val, var = binomial_parameters(num_dice, prob_success)
    x = np.linspace(0, num_dice, 200)
    pdf = norm.pdf(x, expected_val, var ** 0.5)

    count = 1
    print(f"\n\nGiven {num_dice} dice, the probability that {count} or more dice roll a 6 is {100 * find_cdf(count, prob_list, dice_vals):.3f}%\n\n")
    plt.plot(x, pdf, color='r')
    plt.bar(dice_vals, [i for i in prob_list])
    plt.show()
