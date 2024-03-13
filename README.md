# Book-Recommender-System

I am a hardcore book-lover and there is a term to descibe people like us: "bibliophiles". The moment we are about to finish reading a book, we already start planning what to read next. We can perhaps ask our friends around or search it over the internet, but all that takes some effort which usually results in procrastination. What if a simple app helps us make that decision and save our time? 

Well yes, its possible with the help of machine learning. We can cluster the similar books together using a class of machine learning algorithms called Clustering algorithms. Lets say we chose K-Means Clustering. If we feed the name of a book in the K-Means clustering model then it will find the closest cluster our book belongs to, and will suggest the top 5 books from that cluster. 

The number of clusters to take is decided by plotting the number of clusters against Within-Cluster Sum of Square (WCSS) distance which is also called the **elbow method**. WCSS is the sum of the squared distance between each point and the centroid in a cluster. The elbow method considers the trade-off between the inner-distances and the number of clusters. An example of how it looks like:

![elbow](https://github.com/shazam37/Book-Recommender-System/assets/119686545/d0805538-e382-4fbd-a109-8e3f8e5a1192)

The kink (red-dot) is the point in the plot beyond which we see no further significant improvement in WCSS. We settle with this number only. For our case, we chose to go with 6 clusters. 
