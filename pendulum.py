import math

def calculate_period(length, gravity=9.81):
    """
    Calculates the period of a simple pendulum.
    
    Parameters:
    length (float): Length of the pendulum in meters.
    gravity (float): Acceleration due to gravity in m/s^2 (default 9.81 for Earth).
    
    Returns:
    float: The period of the pendulum in seconds.
    """
    if length < 0:
        raise ValueError("Pendulum length cannot be negative.")
        
    period = 2 * math.pi * math.sqrt(length / gravity)
    return period

if __name__ == "__main__":
    # Default test case
    test_length = 1.5  # meters
    
    try:
        result = calculate_period(test_length)
        print(f"--- Pendulum Simulation ---")
        print(f"Length: {test_length} m")
        print(f"Gravity: 9.81 m/s^2")
        print(f"Period: {result:.2f} seconds")
    except ValueError as e:
        print(f"Error: {e}")
