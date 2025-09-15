movie_count = 0
best_movie = ""
current_top_score = 0
max_movies = 7

while movie_count < max_movies:
    movie_name = input()

    if movie_name == "STOP":
        break

    movie_count += 1

    ascii_sum = 0
    title_length = len(movie_name)

    for char in movie_name:
        ascii_sum += ord(char)

    for char in movie_name:
        if char.islower():
            ascii_sum -= 2 * title_length

        elif char.isupper():
            ascii_sum -= title_length

    if ascii_sum > current_top_score:
        current_top_score = ascii_sum
        best_movie = movie_name

    if movie_count == max_movies:
        print("The limit is reached.")


print(f"The best movie for you is {best_movie} with {current_top_score} ASCII sum.")


