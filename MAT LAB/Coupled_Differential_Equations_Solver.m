%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%  Created by Daniel de las Heras Garcia,          %%
%%  Adelphi University 2022.                        %%
%%  Function that returns the solution to the       %% 
%%  to the initial value problem for a system of    %%
%%  n differential equations.                       %%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Input -- system - the system of DEs as a anonymous 
% function which returns an array
% initial - an array with the initial condition for
% Every variable

% Output -- ss - the solution of the system of DEs

function ss = coupled(system, initial, tEnd)
    
    % Calculates the number of equations
    dim = length(initial);
    
    % Uses the built-in function ode45 to find the 
    % solution to the IVP
    [tt, ss] = ode45(system,[0 tEnd], initial);
    
    % Loop which creates a graph with all the variables
    % From the system against time.
    for i= 1:dim
        plot(tt,ss(:,i))
        hold on
    end
    legend('Rabbits','Foxes')
    hold off
end
