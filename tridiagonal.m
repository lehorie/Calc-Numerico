function x = tridiagonal(e,f,g,r)
%input: 
%e = diagonal inferior
%f = diagonal principal
%g = diagonal superior
%r = vetor do lado direito
%x = resultado

n = length(f);
for k=2:n
    factor = e(k)/f(k-1);
    f(k) = f(k) - factor*g(k-1);
    r(k) = r(k) - factor*r(k-1);
end

x(n) = r(n)/f(n);
for k= n-1:-1:1
    x(k) = (r(k)-g(k)*x(k+1))/f(k);
end
for i = 1:length(x)
    fprintf("\nx%d = %f\n", i, x(i));
end
