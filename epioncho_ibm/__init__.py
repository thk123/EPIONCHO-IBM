version = 1.0
from .params import Params
from .state import RandomConfig, State, StateStats, run_simulation


def benchmarker_test_func(end_time: float, population: int) -> StateStats:
    params = Params(human_population=population)
    random_config = RandomConfig()
    initial_state = State.generate_random(random_config=random_config, params=params)
    initial_state.dist_population_age(num_iter=15000)
    new_state = run_simulation(initial_state, start_time=0, end_time=end_time)
    stats = new_state.to_stats()
    return stats
