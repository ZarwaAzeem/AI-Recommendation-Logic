MOVIES = [
    {"title": "Inception", "tags": {"sci-fi", "thriller", "action"}},
    {"title": "The Matrix", "tags": {"sci-fi", "action"}},
    {"title": "Interstellar", "tags": {"sci-fi", "drama", "adventure"}},
    {"title": "The Dark Knight", "tags": {"action", "crime", "thriller"}},
    {"title": "Mad Max: Fury Road", "tags": {"action", "adventure", "sci-fi"}},
    {"title": "The Hangover", "tags": {"comedy"}},
    {"title": "Superbad", "tags": {"comedy", "teen"}},
    {"title": "Home Alone", "tags": {"comedy", "family"}},
    {"title": "Toy Story", "tags": {"animation", "family", "comedy", "adventure"}},
    {"title": "Finding Nemo", "tags": {"animation", "family", "adventure"}},
    {"title": "The Notebook", "tags": {"romance", "drama"}},
    {"title": "Pride and Prejudice", "tags": {"romance", "drama"}},
    {"title": "La La Land", "tags": {"romance", "musical", "drama"}},
    {"title": "The Conjuring", "tags": {"horror", "thriller"}},
    {"title": "A Quiet Place", "tags": {"horror", "thriller", "sci-fi"}},
    {"title": "Get Out", "tags": {"horror", "thriller"}},
    {"title": "The Shawshank Redemption", "tags": {"drama", "crime"}},
    {"title": "Forrest Gump", "tags": {"drama", "romance", "comedy"}},
    {"title": "Spirited Away", "tags": {"animation", "adventure", "family"}},
    {"title": "Knives Out", "tags": {"crime", "comedy", "thriller"}},
]


def get_all_tags():
    """Return a sorted list of every genre used in the catalog."""
    tags = set()
    for movie in MOVIES:
        tags |= movie["tags"]
    return sorted(tags)


def ask_preferences(all_tags):
    """Step 1: Take user input (choices or interests)."""
    print("\nAvailable genres:")
    print(", ".join(all_tags))

    while True:
        raw = input("\nEnter your favorite genres, separated by commas: ")
        choices = {item.strip().lower() for item in raw.split(",") if item.strip()}

        valid = choices & set(all_tags)
        unknown = choices - set(all_tags)

        if unknown:
            print("Ignoring unknown genres:", ", ".join(sorted(unknown)))
        if valid:
            return valid
        print("Please enter at least one genre from the list.")


def similarity(user_tags, movie_tags):
    """Step 2: Jaccard similarity = shared genres / total distinct genres."""
    shared = user_tags & movie_tags
    total = user_tags | movie_tags
    return len(shared) / len(total)


def recommend(user_tags, top_n=3):
    """Score every movie and return the best matches."""
    scored = []
    for movie in MOVIES:
        score = similarity(user_tags, movie["tags"])
        if score > 0:
            scored.append((score, movie))

    # Highest score first; ties are sorted alphabetically by title
    scored.sort(key=lambda pair: (-pair[0], pair[1]["title"]))
    return scored[:top_n]


def display(recommendations):
    """Step 3: Display recommended items."""
    if not recommendations:
        print("\nSorry, no matching movies found.")
        return

    print("\nTop recommendations for you:")
    for rank, (score, movie) in enumerate(recommendations, start=1):
        genres = ", ".join(sorted(movie["tags"]))
        print(f"{rank}. {movie['title']}  ({score:.0%} match)  [{genres}]")


def main():
    print("Welcome to the Movie Recommender!")
    all_tags = get_all_tags()

    while True:
        prefs = ask_preferences(all_tags)
        display(recommend(prefs))

        again = input("\nTry again with different genres? (y/n): ").strip().lower()
        if again != "y":
            print("Enjoy your movie! Goodbye!")
            break


if __name__ == "__main__":
    main()
