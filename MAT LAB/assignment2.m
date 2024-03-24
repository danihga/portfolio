%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%  Sine plot through the domain -2pi < x < 2pi     %%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Setting x axis vector
x = linspace(-2*pi,2*pi,100);

% plotting sin function
plot(x, sin(x),"r");

% Setting the scale of x and y axis
axis([-2*pi 2*pi  -2 2]);

% Setting the plot title and axis labels 
title('sin(x) Function Plot');
xlabel('-2\pi < x < 2\pi'); 
ylabel('sin (x)'); 
