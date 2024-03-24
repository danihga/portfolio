%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%  Created by Daniel de las Heras Garcia,          %%
%%  Adelphi University 2022.                        %%
%%  Function that returns the answer to the initial %%
%%  value proble of a differential equation.         %%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%% Input --     a first order differential equation function(time, x) 
%               f1 = initial condition
%               a,b = time limits
%               h = step size
%% Output --    answer to initial value problem
function f = firstOrder(func,f1,a,b,h)

    % Array that determines all vales of t within a and b with step size h
    time    =   a:h:b;
    
    % Output array of values
    f       =   zeros(size(time));

    % Sets the initial condition as the first term of f
    f(1)    =   f1;
    
    % Euler's method to find f(t+h)
    for i   =   2:length(time)
   
       f(i) =   f(i-1) + h * func(time(i-1),f(i-1));

    end

end