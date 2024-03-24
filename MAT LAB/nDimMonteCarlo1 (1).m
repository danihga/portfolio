%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%  Created by Daniel de las Heras Garcia,          %%
%%  Adelphi University 2022.                        %%
%%  Function that returns the volume of any         %% 
%%  dimensianal hypershpere using Montecarlo Method %%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Input -- num - the number of random points scatter 
% in the plane, dim - number of dimensions of the hypersphere

% Output -- volume - volume of the n-dimension hypershpere
function volume = nDimMonteCarlo1(num,dim)
    
    % Creates an array with random numbers with num rows 
    % and dim columns
    scatter = rand(num,dim);
    
    % Calculates the radius for every row
    radius = sum(scatter.^2,2);
    
    % Checks which points are within the radius = 1
    mask = radius < 1;
    
    % Counts the number of points within the sphere's 
    % radius
    inside = sum(double(mask));
    
    % Calculates the volume
    volume = (inside/num) * (2^dim); 
    
    
end