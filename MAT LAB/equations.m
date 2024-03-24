# Program by Daniel de las Heras 
# Try different initial values for the
# Prey-predator model 

# Defines an anonimous function which returns an array
# with the system of DE
drdf    = @(tt,rf) [2*rf(1)-0.01*rf(1)*rf(2),-rf(2)+0.01*rf(1)*rf(2)];

# Sets the final time
tEnd = 150;

# Calculates the model with initial values Rabbits = 200,
# Foxes = 200
coupled(drdf, [200 200], tEnd);

# Calculates the model with initial values Rabbits = 200,
# Foxes = 5
coupled(drdf, [200 5], tEnd);

# Calculates the model with initial values Rabbits = 100,
# Foxes = 200
coupled(drdf, [100 200], tEnd);

# Calculates the model with initial values Rabbits = 110,
# Foxes = 200
coupled(drdf, [110 200], tEnd);
