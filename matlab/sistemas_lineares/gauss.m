% Eliminação de Gauss

function roots = gauss(A, B)

n = size(A);

    for k = 1:n-1

        % Pivoteamento
        pivo = A(k, k);
        l_pivo = k;

            for i = k+1:n
                if abs(A(i, k)) > abs(pivo)
                    pivo = A(i, k);
                    l_pivo = i;
                    break;
                end
            end

            if pivo == 0
                disp("Matriz não singular");
            end

            if l_pivo ~= k
                % troca entre A(k, 1:end) e A(l_pivo, 1:end)
                c = A(k, 1:end);
                A(k, 1:end) = A(l_pivo, 1:end);
                A(l_pivo, 1:end) = c;
                % troca entre B(k) e B(l_pivo)
                d = B(l_pivo);
                B(l_pivo) = B(k);
                B(k) = d;
            end


        % Achar matriz triangular superior
        for i = k+1:n
            m = A(i, k)/A(k, k);
            A(i, k) = 0;
            for j = k+1:n
                A(i, j) = A(i, j) - m*A(k, j);
            end
            B(i) = B(i) - m*B(k);
        end

    end

R(n, 1) = B(n)/A(n,n);

for i = n-1:-1:1
    soma = 0;
    for j = i+1:n
        soma = soma + A(i, j)*R(j, 1);
    end
    R(i, 1) = (B(i) - soma)/A(i, i);
end

roots = R;

    



            