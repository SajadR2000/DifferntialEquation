# DifferntialEquation
This project solves Differential Equations by Runge-Kutta and Euler methods
First you need to define an ODE(a0x^b0y(n) + a1b1y(n-1)+ ... + a = 0 by giving  the Equation class vector of coefficients and vector of degree
which indicate coefficient of each term and degree of x in each term respectively(if one doesn't exsit it's coeffitient and degree is zero).
then you have to give the begining and end of the interval you want the answer on and the initial conditions and step size, to the functions equation_solver_rungekutta or
equation_solver_euler.these functions will give you the list of X and Y(x).which you could paint the graph of using the painter.
