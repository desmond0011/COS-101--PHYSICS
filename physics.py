# Physics Formulas

# 1. Speed = Distance / Time
def speed(distance, time):
    return distance / time

# 2. Force = Mass x Acceleration
def force(mass, acceleration):
    return mass * acceleration

# 3. Kinetic Energy = 1/2 x Mass x Velocity^2
def kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2

# 4. Potential Energy = Mass x Gravity x Height
def potential_energy(mass, height):
    return mass * 9.8 * height

# 5. Density = Mass / Volume
def density(mass, volume):
    return mass / volume

print("Speed:", speed(100, 20), "m/s")
print("Force:", force(10, 5), "N")
print("Kinetic Energy:", kinetic_energy(2, 10), "J")
print("Potential Energy:", potential_energy(5, 10), "J")
print("Density:", density(20, 4), "kg/m^3")
