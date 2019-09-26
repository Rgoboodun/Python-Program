import numpy as np
import matplotlib.pyplot as plt


def estimate_coef(x, y):
    # number of observation/points
    n = np.size(x)

    # mean of x and y vector
    m_x, m_y = np.mean(x), np.mean(y)

    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx = np.sum(x*x) - n*m_x*m_x

    # calculating regression coef
    b_1 = SS_xy/SS_xx
    b_0 = m_y - b_1*m_x

    return (b_0, b_1)


def plot_regression_line(x, y, b):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color="g", marker = "o", s=30)

    # predicted response vector
    y_pred = b[0] + b[1]*x

    # plotting the regression line
    plt.plot(x, y_pred, color="b")

    # putting labels
    plt.xlabel('x')
    plt.ylabel('y')

    # function to show plot
    plt.show()


def main():
    # observation
    x = np.array([25, 17, 12, 8, 3, 15, 37, 20, 4])
    y = np.array([8, 14, 26, 35, 45, 18, 4, 15, 40])

    # estimating coefficients
    b = estimate_coef(x, y)
    print("Estimate coefficient:\nb_0 = {} \nb_1 = {}".format(b[0], b[1]))

    # plotting regression line
    plot_regression_line(x, y, b)


if __name__ == '__main__':
    main()
