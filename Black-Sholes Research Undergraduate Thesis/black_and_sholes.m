% Algorithm to calculate the price of a European option

% Parameters
r = 0.2;		% Interest rate
sigma = 0.25; 		% Volatility of the underlying
Nt = 1600; 		% Number of time steps
Ns = 160; 		% Number of asset price steps
Smax = 20; 		% Maximum asset price considered
Smin = 0; 		% Minimum asset price considered
T = 1; 			% Maturation (expiry) of the contract
E = 10; 		% Exercise price of the underlying

% Stepper variables
dt = (T/Nt); 		% Time step
ds = (Smax-Smin)/Ns; 	% Price step

% Initializing the matrix of the option value
V(1:Ns+1, 1:Nt+1) = 0.0;

% Create an array with the input values of the price and the time to expiration
S = Smin+(0:Ns)*ds;
tau = (0:Nt)*dt;

% Initial conditions prescribed by the European Call payoff at expiry:
V(S,tau=0) = max (S-E,0)
V(1:Ns+1,1) = max (S-E, 0);

% Boundary conditions prescribed by the European Call:
V(1,1: Nt+1) = 0; 	% V(0, t) =0
V(Ns+1,1:Nt+1) = Smax-E*exp(-r*tau);
% V(S, t) = S-Exp[-r (T-t)] as S -> infininty

% Implementing the explicit algorithm
for j = 1:Nt 		% Time loop
	for n = 2:Ns % Asset loop
 		V(n,j+1) = 0.5*dt*(sigma*sigma*n*n-r*n)*V(n-1,j)+(1-

dt*(sigma*sigma*n*n+r))*V(n,j)+0.5*dt*(sigma*sigma*n*n+r*n)*V(n+1,j);
	end
end

% Figure of the values of the option, V(S,tau), as a function of S at 3 different times: tau=0(t=T), tau=T/2(t=T/2) and tau=T(t=0).
figure (1)
plot (S, V(:,1), 'r-', S, V(:,round(Nt/2)), 'g-', S, V(:,Nt+1), 'b-');
xlabel ('S');
ylabel ('V(S, tau)');
title ('European Call Option within the Explicit Method');

% 3D plots of the Value of the option, V(S, tau)
figure (2)
mesh (tau, S, V);
xlabel ('tau');
ylabel ('S');
title ('European Call Option value, V(S,tau), within the Explicit
Method');
