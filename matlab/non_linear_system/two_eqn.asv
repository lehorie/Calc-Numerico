circ = @(x,y) x^2 + 4*y.^2 - 5;
par = @(x,y) 2*x.^2 - 2*x -3*y -2.5;

fimplicit(circ,'b')
hold on
fimplicit(par,'y')
xlabel('x')
ylabel('y')
hold off

mySystem =@(w) [circ(w(1),w(2)),
                par(w(1),w(2))];

%valor de chute para encontrar a raíz mais próxima de w0
w0 = [-1 1];
wRoot = fsolve(mySystem,w0);
wRoot
hold on
plot(wRoot(1),wRoot(2),"m.")
hold off
