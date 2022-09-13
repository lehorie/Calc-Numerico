A = [3 -.1 -.2; .1 7 -.3; .3 -.2 10];
b = [7.85; -19.3; 71.4];
%function x = gauss_seidel(A,b,es,maxit)
% A*x = b
% es critério de parada
%maxit maximo de iteracoes
%output: x
    maxit = 50;
    es = eps;
    
[m,n] = size(A);
if m~=n
    error("A matriz precisa ser quadrada")
end
C = A;

for i=1:n
    C(i,i) = 0;
    x(i) = 0;
end

x = x';
for i=1:n
    C(i,1:n) = C(i,1:n)/A(i,i);
end
for i=1:n
    d(i) = b(i)/A(i,i);
end
inter = 0;
while(1)
    xold = x;
    for i = 1:n
        x(i) = d(i) - C(i,:)*x;
        if x(i)~=0
            ea(i) = abs((x(i) - xold(i))/x(i))*100;
        end
    end
    inter = inter + 1;
    if max(ea) <= es || inter >= maxit
        break
    end
end
for i = 1:length(x)
    fprintf("\nx%d = %f\n", i, x(i));
end
