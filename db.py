import mysql.connector
class Popcorn:
    def __init__(self):
        self.connect()
    def connect(self):
        self.con = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "root",
            database = "Cinebase"
            )
        self.cur = self.con.cursor()


    def upload(self,username,password,email):
        self.connect() #Connect to the database
        print("🚀 Uploading user details... Please wait! 📂")
         #Insert user details into the users tab
        try:
            self.cur.execute("insert into users(username,password,email) values (%s,%s,%s)",(username,password,email)) #Insert user details into the users table
        except Exception:
            print("primary key violation.. User already exists.. Please try with a different username..")
             #If the user already exists
        self.con.commit() #Commit the changes to the database

        print("\n✅ Details uploaded successfully!!! ")
        print("🔓 You are now **FREE** to LOGIN and explore! ")
        self.cur.close() #Close the cursor
        self.con.close() #Close the connection
        

    def logins(self,username,password):
        while True:
            self.connect()
            self.cur.execute("select username from users where username = %s and password = %s",(username,password)) #Login as existing user
            result = self.cur.fetchone() #Fetch that user details from the database
            if result:
                self.logged_in_user = username  # Store the logged-in username for later use
                print(f"✅ Login successful!! Welcome {username}!!")
                break
            else:
                print("❌ Invalid username or password.. Please Try again!!")
                username = input("🔑 Username: ")
                password = input("🔒 Password: ")
            # Close the cursor and connection
            self.cur.close()
            self.con.close()

    def fetch_user_id(self,username): #Fetch user id from the database
        self.connect()
        self.cur.execute("select user_id from users where username = %s",(username,))
        data = self.cur.fetchone()
        print(data, type(data[0]))
        


    def add_a_movie(self,title,genre,release_year): #Add a movie to the database
        if not title or not genre or not release_year:
            print("❌ Please provide all movie details.")
            return
        self.connect()
        try:
            self.cur.execute("select title from movies where title = %s",(title,)) #Check if the movie already exists
            if self.cur.fetchone():
                print("❌ Movie already exists in the database. Please try with a different title.")
                self.cur.close()
                self.con.close()
                return
        except mysql.connector.Error as err:
            print(f"❌ Error checking movie existence: {err}")
            self.cur.close()
            self.con.close()
            return
        # Insert movie details into the movies table
        try:
            self.cur.execute("insert into movies(title,genre,release_year) values (%s,%s,%s)",(title,genre,release_year))
            self.con.commit()
            print(f"Your movie details 🎬 🍿\n title : {title} \n genre : {genre} \n year_of_release = {release_year} \n have been successfully stored! 🎬 🍿")
        except mysql.connector.Error as err:
            print(f"❌ Error inserting movie: {err}")   
        finally:
            self.cur.close()
            self.con.close()

    def search_a_movie(self): #Search a movie in the database
        self.connect()
        while True:
                print("\n🎬 Movie Search Options 🎬")
                print('''
                    1. Search by year
                    2. Search by Movie name
                    3. Search by Genre
                    4. Quit Search
                    ''')
                try:
                    opt = int(input("Select your choice: "))
                except ValueError:
                    print("❌ Please enter a valid option (1-4).")
                    continue
                if opt == 1:
                    try:
                        year = int(input("Enter year of release:  "))
                        self.cur.execute("select * from movies where release_year = %s",(year,))
                        data = self.cur.fetchall()
                        if data:
                            print("----------------------------------------------------------------------")
                            print("ID\tTitle\t\t\tGenre\t\tYear of Release")
                            print("----------------------------------------------------------------------")
                            for row in data:
                                print(f"{row[0]}\t{row[1]}\t\t{row[2]}\t\t{row[3]}")
                        else:   
                            print("🚫 No movies found for the given year.")
                    except ValueError:
                        print("❌ Please enter a valid year.")
                    except Exception as e:
                        print(f"❌ Error occurred: {e}")
                        


                elif opt == 2:
                    try:
                        name = input("🎬 Enter title of the film:  ")
                        self.cur.execute("select * from movies where title = %s",(name,))
                        data = self.cur.fetchall()
                        if data:
                            print("Results:")
                            for row in data:
                                print(row)
                    except Exception as e:
                        print(f"❌ Error occurred: {e}")
                 
                        
                elif opt == 3:
                    try:
                        movie_genre = input("🎭 Enter the genre of the film:  ")
                        self.cur.execute("select * from movies where genre = %s",(movie_genre,))
                        data = self.cur.fetchall()
                        if data:
                            print("📽️ Results:")
                            for row in data:
                                print(row)
                        else:
                            print("🚫 No movies found for the given genre.")
                    except Exception as e:
                        print(f"❌ Error occurred: {e}")
                        
                elif opt == 4:
                    print("🔚 Exiting search...")
                    break
                else:
                    print("❌ Please select valid choice...")
        self.cur.close()  # Close the cursor
        self.con.close()  # Close the connection


    def view_all(self): #View all movies and reviews in the database
        self.connect()
        
        self.cur.execute("SELECT * FROM movies")
        d = self.cur.fetchall()
        if not d:
            print("🚫 No movies found in the database.")
            return
        else:
            print("------------------------------------------------------------------")
            print("ID\tTitle\t\t\tGenre\t\tYear of Release")
            print("------------------------------------------------------------------")
            for row in d:
                print(f"{row[0]}\t{row[1]:<20}\t{row[2]:<15}\t{row[3]}".format(*row))
            print("------------------------------------------------------------------")
       
        self.cur.execute("SELECT rating,comments from reviews join movies on reviews.movie_id = movies.movie_id")
        data = self.cur.fetchall()
        if not data:
            print("🚫 No reviews found.")
            return 
        else:
            print("----------------------------------------------------")
            print("Rating\t\tComments")
            print("----------------------------------------------------")
            for mov in data:
                print(f"{mov[0]:<10}\t{mov[1]}")
                print("------------------------------------------------------")
        self.cur.close()  # Close the cursor
        self.con.close()  # Close the connection


    def top_movies(self): #View top rated movies in the database
        self.connect()
        try:
            self.cur.execute('''
                            SELECT 
                                movies.title, 
                                movies.genre,
                                reviews.rating,
                                movies.release_year 
                            FROM 
                                reviews 
                            INNER JOIN 
                                movies 
                            ON 
                                reviews.movie_id = movies.movie_id 
                            ORDER BY 
                                reviews.rating DESC''')
            data = self.cur.fetchall()
            if not data:    
                print("🚫 Details not found in the database.")
                return
            print('--------------------------------------------------')
            print("----------------TOP RATED MOVIES------------------")
            print('--------------------------------------------------')
            print("--------------------------------------------------")
            print(f"{'Title':<30}{'Genre':<20}{'Rating ':<15}")
            print("-" * 65)
            for row in data:
                print(f"{row[0]:<30}{row[1]:<20}{row[2]:<15}")

        except mysql.connector.Error as err:
            print("❌ Error fetching top rated movies.")    

    def write_review(self, movie_id, rating, comments):  # Write a review for a movie in the database
        try:
            self.connect()

            # Check if user is logged in
            if self.logged_in_user == "":
                print("❌ You must be logged in to write a review.")
                return

            # Get user_id from username
            self.cur.execute("SELECT user_id FROM users WHERE username = %s", (self.logged_in_user,))
            user_data = self.cur.fetchone()
            
            if user_data is None:
                print("❌ User not found in the database.")
                return
            
            user_id = user_data[0]  # Insert review with user_id
            
            # Insert review into the database
            self.cur.execute(
                "INSERT INTO reviews (movie_id, rating, comments, user_id) VALUES (%s, %s, %s, %s)",
                (movie_id, rating, comments, user_id)
            )
            self.con.commit()

            print("✔ Your review has been added successfully!")
        
        except mysql.connector.Error as err:
            print(f"❌ Database error: {err}")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
        finally:
            self.cur.close()
            self.con.close()


    def get_movie_name(self, movie_id):  # Get movie name by movie id
        try:
            self.connect()
            self.cur.execute("SELECT title FROM movies WHERE movie_id = %s", (movie_id,))
            moviename = self.cur.fetchone()
            if not moviename:
                print("Movie not found..")
                return None
            return moviename[0]
        except mysql.connector.Error as err:
            print(f"❌ Database error: {err}")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
        finally:
            self.cur.close()
            self.con.close()

    def update_review(self):  # Update a review in the database
        try:
            self.connect()  

            # Check if a user is logged in
            if not self.logged_in_user:
                print("Access denied: No user is logged in.")
                return

            # Fetch reviews only for the logged-in user
            self.cur.execute("""
                SELECT reviews.review_id, reviews.movie_id, movies.title, reviews.rating, reviews.comments 
                FROM reviews
                JOIN movies ON reviews.movie_id = movies.movie_id
                WHERE reviews.user_id = (SELECT user_id FROM users WHERE username = %s);
            """, (self.logged_in_user,))

            reviews = self.cur.fetchall()

            if not reviews:
                print("🔎 You haven't submitted any reviews yet.")
                return

            # Displaying the previous reviews given by the user (if there are any)
            print("\n-------------------Your Reviews:--------------------")
            for review in reviews:
                print(f" 🆔 Review ID: {review[0]}, 🎬 Movie: {review[2]},  ⭐ Rating: {review[3]}, 💬 Comments: {review[4]}")

            # which review to update
            review_id = int(input("🆔 Enter the Review ID of the review you want to update: "))

            # Make sure the selected Review ID belongs to the logged-in user
            review_exists = any(review[0] == review_id for review in reviews)
            if not review_exists:
                print("🚫 Access restricted: You can only update your own reviews.")
                return

            # Get new rating and comments
            print("🔄 Updating your review...")
            new_rating = float(input("⭐ Enter new rating: "))
            new_comments = input("💬 Enter new comments: ")

            # Update review only for the logged-in user
            self.cur.execute("""
                UPDATE reviews 
                SET rating = %s, comments = %s 
                WHERE review_id = %s;
            """, (new_rating, new_comments, review_id))

            self.con.commit()
            print("✔ Your review has been updated successfully!")
        except mysql.connector.Error as err:
            print(f"❌ Database error: {err}")
        except ValueError:
            print("❌ Invalid rating entered. Please enter a valid number for rating.")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
        finally:
            self.cur.close()
            self.con.close()

    def delete_review(self, movie_id):  # Delete a review in the database
        try:
            self.connect()  

            # Check if a user is logged in
            if not self.logged_in_user:
                print("🚫 Access denied: No user is logged in.")
                return

            # Fetch reviews only for the logged-in user
            self.cur.execute("""
                SELECT reviews.review_id, reviews.movie_id, movies.title, reviews.rating, reviews.comments 
                FROM reviews
                JOIN movies ON reviews.movie_id = movies.movie_id
                WHERE reviews.user_id = (SELECT user_id FROM users WHERE username = %s);
            """, (self.logged_in_user,))

            reviews = self.cur.fetchall()

            if not reviews:
                print("📭 You haven't submitted any reviews yet.")
                return

            # Displaying the previous reviews given by the user (if there are any)
            print("\n-------------------Your Reviews:--------------------")
            for review in reviews:
                print(f"Review ID: {review[0]}, Movie: {review[2]}, Rating: {review[3]}, Comments: {review[4]}")

            # which review to delete
            review_id = int(input("🆔 Enter the Review ID of the review you want to delete: "))

            # Make sure the selected Review ID belongs to the logged-in user
            review_exists = any(review[0] == review_id for review in reviews)
            if not review_exists:
                print("🚫 Access restricted: You can only delete your own reviews.")
                return

            # Delete review only for the logged-in user
            self.cur.execute("""
                DELETE FROM reviews 
                WHERE review_id = %s;
            """, (review_id,))  # Main query to delete the review

            self.con.commit()
            print("🗑️ Your review has been deleted successfully!")
        except mysql.connector.Error as err:
            print(f"❌ Database error: {err}")
        except ValueError:
            print("❌ Invalid input. Please enter a valid Review ID.")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
        finally:
            self.cur.close()
            self.con.close()
