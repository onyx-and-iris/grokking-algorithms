import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

stations = {
    "kone": set(["id", "nv", "ut"]),
    "ktwo": set(["wa", "id", "mt"]),
    "kthree": set(["or", "nv", "ca"]),
    "kfour": set(["nv", "ut"]),
    "kfive": set(["ca", "az"]),
}


def fget():
    needed = set()
    for states in stations.values():
        needed |= states
    return needed


def greedy():
    states_needed = fget()
    logger.debug(states_needed)
    final_stations = set()

    while states_needed:
        best_station = None
        states_covered = set()
        for station, states in stations.items():
            covered = states_needed & states

            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered

        states_needed -= states_covered
        final_stations.add(best_station)

    return final_stations


final_stations = greedy()
print(f"final stations greedy approximation: {final_stations}")
