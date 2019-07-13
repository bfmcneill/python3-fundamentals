# create a list of movies
list_of_movies = None

list_of_movies = [
    'Toy Story',
    'Lion King', 
    'Coco'
    ]


# cycle through each movie title in the list of movies
#    starting from the first item and ending at the last item
for movie_title in list_of_movies:
    print('***{}***'.format(movie_title))
    
    # create an empty variable called word
    word = ''  

    # cycle through each letter in the movie title
    for letter in movie_title:        
        print('  {}'.format(letter))
        word += letter
    
    print("The letters create the word variable >>{}".format(word))
    print("The movie title is the same as the word variable: {}".format(movie_title == word))
    print('\n\n')
    word = ''  
    
