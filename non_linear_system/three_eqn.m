mySph =@(x,y,z) x.^2+y.^2+z.^2-3;
myPlane =@(x,y,z) 3*x-2*y+z-2;
myFun =@(x,y,z) sin(x).*cos(y) +z;

fimplicit3(myFun,'b','FaceAlpha',0.4)
hold on
fimplicit3(mySph,'y','FaceAlpha',0.4)
fimplicit3(myPlane,'r','FaceAlpha',0.4)
xlabel('x')
ylabel('y')
hold off

mySystem =@(w) [mySph(w(1),w(2),w(3));
                myPlane(w(1),w(2),w(3));
                myFun(w(1),w(2),w(3))];

%valor de chute para encontrar a raíz mais próxima de w0
w0 = [-0.5 -1.5 -0.5];
wRoot = fsolve(mySystem,w0);

hold on
plot3(wRoot(1),wRoot(2),wRoot(3),"m.","MarkerSize",40)
hold off