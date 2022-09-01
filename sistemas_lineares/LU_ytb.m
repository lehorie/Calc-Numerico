%% Descrição
%{
Autor: Thiago Martins Firmo
Título: Decomposição LU
Parâmetros de entrada: A [matriz de coefientes];
Parâmetro de saída: L[matriz inferior], U[matriz superior], Det[determinante];
%}

%% Preparação
clc                                             % limpeza do prompt de comando
clear all                                       % limpeza das variáveis armazenadas
close all                                       % fecha todas figuras

%% Entrada de Dados
A=[4 -1 0 -1;1 -2 1 0;0 4 -4 1;5 0 5 -1];
% A=[1 -3 2;-2 8 -1;4 -6 5];
 
%% Decomposição LU
n=length(A);                                    % ordem da matriz A
U=zeros(n);                                     % matriz de zeros para montagem da matriz superior
L=zeros(n);                                     % matriz de zeros para montagem da matriz inferior

for j=1:n                                       % criação de um vetor para alocação da posição dos pivôs
    pivot(j,1)=j;
end

Det=1;                                          % inicialização do determinante

for j=1:n-1                                     % decomposição via pivotação parcial
    p=j;
    Amax=abs(A(j,j));
    for k=j+1:n
        if abs(A(k,j))>Amax
            Amax=abs(A(k,j));
            p=k;
        end
    end
    if p~=j
        for k=1:n
            t=A(j,k);
            A(j,k)=A(p,k);
            A(p,k)=t;
        end
        m=pivot(j,1);
        pivot(j,1)=pivot(p,1);
        pivot(p,1)=m;
        Det=-Det;
    end
    Det=Det*A(j,j);
    if abs(A(j,j))~=0
        r=1/A(j,j);
        for l=j+1:n
            mult=A(l,j)*r;
            A(l,j)=mult;
            for m=j+1:n
                A(l,m)=A(l,m)-mult*A(j,m);
            end
        end
    end
end

Det=Det*A(n,n);

for j=1:n                                       % montagem das matrizes L e U
    for k=1:n
        if j<=k
            U(j,k)=A(j,k);
        else
            L(j,k)=A(j,k);
        end
    end
end

L=L+eye(n);                                     % adicionando a diagonal principal à matriz inferior

%% Conferência do resultado
B=L*U;

for j=1:n                                       % organizando as linhas do resultado
    A(pivot(j,1),:)=B(j,:);
end

%% Apresentação do Resultado
disp('Matriz L:');
disp(L);
disp('Matriz U:');
disp(U);
disp('Determinante:');
disp(Det);