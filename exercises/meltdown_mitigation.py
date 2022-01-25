def is_criticality_balanced(temperature, neutrons_emitted):
    if (
        (temperature < 800)
        and (neutrons_emitted > 500)
        and (temperature * neutrons_emitted < 500000)
    ):
        return True
    else:
        return False


def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    efficiency = (generated_power / theoretical_max_power) * 100
    if efficiency >= 80:
        return "green"
    elif 60 <= efficiency < 80:
        return "orange"
    elif 30 <= efficiency < 60:
        return "red"
    elif efficiency < 30:
        return "black"


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    if temperature * neutrons_produced_per_second < threshold * 0.9:
        return "LOW"
    elif threshold * 0.9 < temperature * neutrons_produced_per_second < threshold * 1.1:
        return "NORMAL"
    else:
        return "DANGER"

