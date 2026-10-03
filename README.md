# AI Recommendation Logic 🎬

A simple command-line movie recommendation system that suggests films based on your favorite genres, using similarity matching.

## Goal

Create a simple recommendation system based on user preferences.

## Features

- Takes user input (a list of favorite genres)
- Matches preferences against a movie catalog using **Jaccard similarity**
- Displays the top 3 recommendations with a match percentage
- Handles unknown genres and empty input gracefully
- Runs in a loop so you can try different preferences

## Skills Demonstrated

- Logic building
- Pattern matching
- Recommendation concepts

## Requirements

- Python 3.x (no external libraries needed)

## How to Run

```bash
python recommender.py
```

## Sample Output

```
Available genres:
action, adventure, animation, comedy, crime, drama, family, horror, musical, romance, sci-fi, teen, thriller

Enter your favorite genres, separated by commas: sci-fi, action

Top recommendations for you:
1. The Matrix  (100% match)  [action, sci-fi]
2. Inception  (67% match)  [action, sci-fi, thriller]
3. Mad Max: Fury Road  (67% match)  [action, adventure, sci-fi]

Try again with different genres? (y/n):
```

## How It Works

Every movie has a set of genre tags. For each movie, the program compares your chosen genres with the movie's genres:

```
similarity = shared genres / total distinct genres
```

For example, if you choose `sci-fi, action` and a movie is tagged `action, sci-fi, thriller`, you share 2 genres out of 3 distinct genres, giving a 67% match. Movies are ranked by score, and the top results are displayed.

## Project Structure

```
recommendation-system/
├── recommender.py
└── README.md
```

## Future Improvements

- Add more movies, or load them from a CSV or JSON file
- Let users rate movies and recommend based on ratings
- Add filters such as release year or rating
- Try other similarity measures, such as cosine similarity
- Build a simple GUI or web interface

## License

This project is open source and available for learning purposes.
