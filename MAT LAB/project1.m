%% By Daniel de las Heras
%  García, from Adelphi University.
%  A program that approximates the function f(x) = x
%  Using a series.

%% INPUT VARIABLES
zeta        =       2.5;                % Input of the function 
N           =       10000;              % Limit of the series

%% DECLARING ARRAYS --  ALL HAVE SIZE EQUAL TO THE NUMBER OF INTERATIONS
%  WE WILL CARRY OUT
sigma        =       zeros(N,1);    % Array to store the sum of the error
                                    % point
series      =       zeros(N,1);     % Array which stores the estimated 
                                    % values of the function at each
                                    % iteration

%% SETTING THE FIRST VALUES OF THE ARRAYS
series(1)   =       (((-1).^(2))/1)*sin(1 * zeta);  % First term of the 
                                                    % approximation
sigma(1)    =       sqrt(sum(zeta-series(1)));      % First term of the 
                                                    % errors

%% ALGORITHM --  CALCULATE THE APPROXIMATION GIVEN A NUMBER OF ITERATIONS.
%                SERIES SHOULD GO TO INFINITY BUT WE CANNOT ACCOMPLISH THAT 
%                NUMERICALLY SO WE USE A LIMIT N
for i       =       2:N
    
    % Series implementation code
    series(i)      =    series(i-1) + (((-1)^(i+1))/i) * sin(i * zeta);

    % Calculates the total error at each step
    errorStep      =    (zeta-(series(1:i)*2)).^2;
    sigma(i)       =    sqrt(sum(errorStep));
end

% Multiplies every value by two to complete the series
series = 2 * series;

%% PLOT

% Plot of the function approximation against the limit of the series N
plot(1:N,series)

hold on 

% Plot of the total error given the limit of the series N
plot(1:N,sigma)
