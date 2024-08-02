# Formula1 GridXGraph

Project to evaluate Formula1 drivers performance off the start line using data from [FastF1](https://docs.fastf1.dev/)

## Getting started

- Create a venv `python -m venv .venv` (or `python3`)
- Install dependencies `./.venv/bin/pip install -r requirements.txt`
- Run the application `.venv/bin/python src/app.py --year 2023 --drivers HAM VER NOR LEC SAI RUS`

### Results

After running the application, it will save the resulting plot graphs for each driver in your argument list in the following folder structure: `./output/{year}/{driver}`

### Caching

Fast-F1 has caching turned on by default, which will go to `/Users/$USER/Library/Caches/fastf1`. Mind you this can get pretty big pretty fast.

On top of that, `calculate_session_performances` uses memoisation techniques as well, which saves the results of the function call to a `cache` folder at the root of this repository. That way, once it has been called once, it won't have to go through Fast-F1 to retrieve all the data again.
