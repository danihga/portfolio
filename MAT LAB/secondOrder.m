%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%  Created by Daniel de las Heras Garcia,          %%
%%  Adelphi University 2022.                        %%
%%  Function that returns the answer to the initial %%
%%  value problem of a second order.                %% 
%   differential equation.                          %%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%% Input --     a first order differential equation function(time, x, x') 
%               x0 = initial condition
%               x1_0 = second initial condition
%               a,b = time limits
%               h = step size
%% Output --    answer to initial value problem
function [x] = secondOrder(second,x0, x1_0, a,b,h)
    
    % Array that determines all vales of t within a and b with step size h
    time    =   a:h:b;
    x       =   zeros(size(time));
    x1      =   zeros(size(time));

    % Sets the initial condition as the first term of x
    x(1)    =   x0;

    % Sets the initial condition as the first term of x1
    x1(1)   =   x1_0;

    for i   =   1:(length(time)-1)
        
        % Euler's method to find f(t+h) and f'(t+h)
        x(i+1)    =   x(i) + h * x1(i);
        x1(i+1)   =   x1(i) + h * second(time(i),x(i),x1(i));
       
    end
    plot(time,x)

end
