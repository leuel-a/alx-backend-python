# Python - Async

This project is a collection of Python scripts demonstrating the use of asynchronous programming with asyncio and tasks. The project contains the following files:

1. `0-basic_async_syntax.py`: This script defines a simple asynchronous coroutine that waits for a random delay between 0 and a maximum delay, then returns the delay.

2. `1-concurrent_coroutines.py`: This script defines the `wait_n` function, which creates 'n' tasks that wait for a random delay and returns a list of the delays in ascending order.

3. `2-measure_runtime.py`: This script measures the total execution time for `wait_n` function and prints it.

4. `3-tasks.py`: This script defines the `task_wait_n` function, which creates 'n' tasks that wait for a random delay and returns a list of the delays as they complete.

5. `4-tasks.py`: This script defines the `task_wait_n` function, which creates 'n' tasks that wait for a random delay and returns a list of the delays as they complete.

## Usage

Each script can be run from the command line with Python 3. For example:

```bash
python3 0-basic_async_syntax.py
```

## Requirements

- Python 3
- `asyncio` library