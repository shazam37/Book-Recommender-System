# Book-Recommender-System

I am a hardcore book-lover and there is a term to descibe people like us: "bibliophiles". The moment we are about to finish reading a book, we already start planning what to read next. We can perhaps ask our friends around or search it over the internet, but all that takes some effort which usually results in procrastination. What if a simple app helps us make that decision and save our time? 

Well yes, its possible with the help of machine learning. We can find the similar books by using a class of machine learning algorithms called unsupervised algorithms (they dont require labelled outputs for training). There are multiple unsupervised learning algorithm but we take NearestNeighbor algorithm. If we feed the name of a book in this model then it will find the closest points (or books in our case) around our searched point, and will suggest the top n closest books. But we need to decide the features on which our model should be trained. 

We get 3 types of data from Kaggle: users (users and their IDs), books (name of the books, their ids), ratings (the rating given to each book by each user). We filter those books out which have received less than 200 rating, we remove the null values, and then finally remove the duplicates. We merge all the 3 types of data together on their respective IDs and draw a pivot table about user-ids with the book title as index and the values as their ratings. This gives information about the ratings of each book (on a scale of 0-10) given by each user. 

The final dataframe looks like:

![Screenshot from 2024-03-13 20-51-11](https://github.com/shazam37/Book-Recommender-System/assets/119686545/d2608ce7-3bdc-4013-928f-94f74437a752)

We then feed this data into NearestNeighbor model and apply brute force algorithm to iteratively search for the nearest neighbors. Thus we get a model ready to give us suggestions about similar books. 

You can see the entire analysis in the analysis notebook. 

Finally, the prediction pipeline is packaged as a flask application ready to be deployed on Heroku (or any choice of cloud). Just install the requirements and run app.py. You can simply give the name of the book or select it from the drop-down and you will get the suggestions instantly. The app interface looks like:

![Screenshot from 2024-03-12 18-59-22](https://github.com/shazam37/Book-Recommender-System/assets/119686545/51824c4b-36ac-4204-a948-595abdd9d9c7)

It can be made more interactive by adding features such as getting the information about the similar books on clicking it, but for the time being, its enough to save a reader from facing a dry day! Happy reading!
