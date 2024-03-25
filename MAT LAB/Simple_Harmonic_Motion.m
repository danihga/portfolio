%% A program by Daniel de las Heras
%  García, from Adelphi University.
%  A program to calculate the displacement of a spring 
%  following simple harmonic motion.

%% Validity
% The program gives a pretty good approximation 
% of simple harmonic motion, representing oscillations.



%% Simple Harmonic Motion Function
shm = @(w,b,x,x_1) (-w.^2*x-b*x_1);

%% Variables
dt      =   0.001;          % Time Step
w       =   15;             % Angular Velocity
b       =   -0.5;           % Damping Term
EndTime =   12;             % Time End
tt      =   0:dt:EndTime;   % Time Array
yy      =   size(tt);       % Function Values
yy_1    =   size(tt);       % First Derivative Values

%% Initial Values
yy(1)   =   1;          
yy_1(1) =   0;

%% Algorithm - Second Order Euler's Method
for i=2:length(tt)

    yy_1(i) =   yy_1(i-1)   +  dt  *   shm(w,b,yy(i-1),yy_1(i-1));
    yy(i)   =   yy(i-1)     +  dt  *   yy_1(i-1);

end

%% Plot
plot(tt,yy)
