#Movie Ratings

#an empty dictionary for all the movies and their ratings 
movie_ratings = {}

#insert 3 movie titles to the dictionary movie_ratings
for k in range(3):
    title = str(input("Enter movie name: "))
    movie_ratings[title] = 0
print(movie_ratings)

#scan for each movie in the movie_ratings key
for movie_name in movie_ratings:
     
    # A list for all the ratings from different users
    rating_list = []
    sum = 0
    
    # i'll take 3 ratings from 3 users through a loop for each movie
    for n in range(3):
        rating = int(input(f"Enter rating for {movie_name}: "))

        #add the rating to the rating list of this movie
        rating_list.append(rating)        
    print(f"{movie_name} ratings list: {rating_list} ")     

    # calculate the average of all the ratings of a movie from its rating_list
    for j in range(len(rating_list)):
        sum += rating_list[j]
    average = sum / len(rating_list)  
    print(f"{movie_name} average rating is: {average}")

    #add the average rating as a value for the keys in the main dictionary
    movie_ratings[movie_name]= average

#print the dictionary
print(movie_ratings)     

