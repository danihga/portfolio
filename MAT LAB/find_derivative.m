%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%  Created by Daniel de las Heras Garcia,          %%
%%  Adelphi University 2022.                        %%
%%  Function that returns the derivative of         %%
%%  a function at a point.                          %%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%% Input --     a mathematical function, a point to evaluate
%               the derivative and a step size.
%% Output --    derivative of the input function at a point

function df = deriv(f,x,h)
    
    % Uses the definition of a function
    df  =   (f(x+h)-f(x))/h;

end
