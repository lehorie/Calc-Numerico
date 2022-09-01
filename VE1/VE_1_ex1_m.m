clc
clear

syms x
f = inline (9.8*(sinh(x) - sin(x))/(2*x*x) - 1,'x');
df=inline (diff(f(x)), 'x');


y(1) = 1;
tolerance = 10^-5;
n= 100;

disp(' n       x(i+1)          |x(i+1) - x(i)|')

for i=1:n
    y(i+1) = y(i) - (f(y(i))/df(y(i)));

    fprintf(' %4d     %8.6f     %9.6f \n', i, y(i+1), abs(y(i+1)-y(i)));
    if abs(y(i+1) - y(i))<tolerance
        fprintf("Raiz aproximada = %.10f\n", y(i+1));
        return;
    end
end
disp('A raiz não foi encontrada')
