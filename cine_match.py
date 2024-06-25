import tkinter as tk
from tkinter import messagebox, ttk

movies = []
movies_index = {}

def add_movie(title, genre, rating):
    movie = {
        "title": title,
        "genre": genre,
        "rating": float(rating)
    }
    movies.append(movie)
    movies_index[title.lower()] = movie
    messagebox.showinfo("Success", f"Movie '{title}' added successfully!")

def search_movies_by_title(title):
    return [movie for movie in movies if title.lower() in movie["title"].lower()]

def search_movies_by_genre(genre):
    return [movie for movie in movies if genre.lower() in movie["genre"].lower()]

def recommend_top_movies(n):
    sorted_movies = sorted(movies, key=lambda x: x["rating"], reverse=True)
    return sorted_movies[:n]

def delete_movie(title):
    title_lower = title.lower()
    if title_lower in movies_index:
        movie = movies_index.pop(title_lower)
        movies.remove(movie)
        return True
    return False

def add_movie_ui():
    title = entry_title.get()
    genre = entry_genre.get()
    rating = entry_rating.get()
    if title and genre and rating:
        add_movie(title, genre, rating)
        entry_title.delete(0, tk.END)
        entry_genre.delete(0, tk.END)
        entry_rating.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "All fields are required!")

def search_movies_ui():
    title = search_entry.get()
    if title:
        results = search_movies_by_title(title)
        display_results(results)
    else:
        genre = search_entry.get()
        results = search_movies_by_genre(genre)
        display_results(results)

def recommend_movies_ui():
    try:
        n = int(recommend_entry.get())
        results = recommend_top_movies(n)
        display_results(results)
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid number.")

def delete_movie_ui():
    title = delete_entry.get()
    if delete_movie(title):
        messagebox.showinfo("Success", f"Movie '{title}' deleted successfully!")
        delete_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Not Found", f"Movie '{title}' not found.")

def display_results(results):
    result_list.delete(0, tk.END)
    if results:
        for movie in results:
            result_list.insert(tk.END, f"{movie['title']} | {movie['genre']} | {movie['rating']}")
    else:
        result_list.insert(tk.END, "No results found.")

root = tk.Tk()
root.title("CineMatch - Movie Recommendation System")

frame_add = ttk.LabelFrame(root, text="Add Movie")
frame_add.pack(padx=10, pady=10, fill="x")

frame_search = ttk.LabelFrame(root, text="Search Movies")
frame_search.pack(padx=10, pady=10, fill="x")

frame_recommend = ttk.LabelFrame(root, text="Recommend Movies")
frame_recommend.pack(padx=10, pady=10, fill="x")

frame_delete = ttk.LabelFrame(root, text="Delete Movie")
frame_delete.pack(padx=10, pady=10, fill="x")

frame_results = ttk.LabelFrame(root, text="Results")
frame_results.pack(padx=10, pady=10, fill="x")

ttk.Label(frame_add, text="Title:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_title = ttk.Entry(frame_add, width=30)
entry_title.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_add, text="Genre:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_genre = ttk.Entry(frame_add, width=30)
entry_genre.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame_add, text="Rating:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_rating = ttk.Entry(frame_add, width=30)
entry_rating.grid(row=2, column=1, padx=5, pady=5)

ttk.Button(frame_add, text="Add Movie", command=add_movie_ui).grid(row=3, columnspan=2, pady=10)

ttk.Label(frame_search, text="Search by Title or Genre:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
search_entry = ttk.Entry(frame_search, width=30)
search_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Button(frame_search, text="Search", command=search_movies_ui).grid(row=1, columnspan=2, pady=10)

ttk.Label(frame_recommend, text="Top N Movies:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
recommend_entry = ttk.Entry(frame_recommend, width=10)
recommend_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Button(frame_recommend, text="Recommend", command=recommend_movies_ui).grid(row=1, columnspan=2, pady=10)

ttk.Label(frame_delete, text="Title:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
delete_entry = ttk.Entry(frame_delete, width=30)
delete_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Button(frame_delete, text="Delete", command=delete_movie_ui).grid(row=1, columnspan=2, pady=10)

result_list = tk.Listbox(frame_results, width=50)
result_list.pack(padx=5, pady=5)

root.mainloop()
