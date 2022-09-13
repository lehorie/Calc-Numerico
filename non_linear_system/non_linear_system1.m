g = @(x,y) 2*x.*y-2*y.^2-1;
h = @(x,y) y.^3 - cos(x);

fimplicit(g,[-3 3])
hold on
fimplicit(h,[-3 3])
hold off
root = @(w) [g(w(1),w(2));
            h(w(1), w(2))];
w0 = root([-1 -2]);
wRoot = fsolve(root,w0);