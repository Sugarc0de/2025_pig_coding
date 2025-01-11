# there are n countries and m goods for import and export. Eath country should have trade balance
# with equal value of import and export. Given the price for pig is $1000, determine if there is a
# unique pricing for all the other goods, ambiguous solution (many prices are possible), or no solution (inconsistent).

import numpy as np
from scipy.linalg import lstsq

PIG_UNIT_PRICE = 1000

items = [  # list of lists. The first list is the import, second list is the export
    [[1, 1, 0], [0, 0, 8.75]],  #
    [[2, 0, 8], [0, 2, 0.5]],  #
    # [[1, 0, 3.75], [0, 1, 0]],  #
    # [[0, 0, 2.5], [1, 0, 0]],
]

# items = [  # list of lists. The first list is the import, second list is the export
#     [[1, 0, 0], [0, 3, 0]],  #
#     [[2, 0, 0], [0, 6, 0]],  #
#     [[1, 0, 0], [0, 0, 1]],  #
# ]


def solve(items, item_names=["pig", "car", "wool"]):
    M_imp, M_exp, b_imp, b_exp = [], [], [], []
    pig_ix = item_names.index("pig")
    for item_per_country in items:
        imp = item_per_country[0]
        exp = item_per_country[1]
        M_imp.append(imp[:pig_ix] + imp[pig_ix + 1 :])
        M_exp.append(exp[:pig_ix] + exp[pig_ix + 1 :])
        b_imp.append(
            [imp[pig_ix]]
        )  # Add a bracket outside so numpy will create column vector
        b_exp.append([exp[pig_ix]])

    M_imp = np.array(M_imp)
    M_exp = np.array(M_exp)
    b_imp = np.array(b_imp) * PIG_UNIT_PRICE
    b_exp = np.array(b_exp) * PIG_UNIT_PRICE

    # print("M_imp: ", M_imp)
    # print("M_exp: ", M_exp)
    # print("b_imp: ", b_imp)
    # print("b_exp: ", b_exp)

    p, res, rnk, s = lstsq(M_imp - M_exp, b_exp - b_imp)

    # print(p, res, rnk)
    if rnk < len(item_names) - 1:
        return "ambiguous"  # more than 1 solution

    if not res or res[0] < 0.000001:  # residual == 0
        return p
    else:
        return "inconsistent"  # no solution


print(solve(items))
