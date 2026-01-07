def calculate_bus_eta(distance_km, avg_speed_kmph, traffic_multiplier=1.0):
    """
    Calculate ETA (in hours) for a bus journey.
    """
    if distance_km <= 0:
        raise ValueError("Distance must be positive")
    if avg_speed_kmph <= 0:
        raise ValueError("Average speed must be positive")
    if traffic_multiplier <= 0:
        raise ValueError("Traffic multiplier must be positive")

    return (distance_km / avg_speed_kmph) * traffic_multiplier


if __name__ == "__main__":
    # CI test cases
    assert round(calculate_bus_eta(60, 60), 2) == 1.00
    assert round(calculate_bus_eta(120, 60), 2) == 2.00
    assert round(calculate_bus_eta(100, 50, 1.5), 2) == 3.00

    print("ETA calculator tests passed ✅")

