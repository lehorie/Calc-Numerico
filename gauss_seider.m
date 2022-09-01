function x = gauss_seidel(A,b,es,maxit)
% A*x = b
% es critério de parada
%maxit maximo de iteracoes
%output: x

if nargin<4||isempty(maxit)
    maxit = 50;
end
if nargin<3||isempty(es)
    es = eps;
end

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
    d(i) = b(i)/A(i,i);
end
inter = 0;
while(1)
    xold = x;
    for i = 1:n
        x(i) = d(i) - C(i,:)*x;
        if x(i)~=0
            ea(i) = abs((x(i) - x(old))/x(i))*100
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
