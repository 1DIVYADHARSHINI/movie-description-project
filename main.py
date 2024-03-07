from tkinter import *
import imdb
# search fun part
def search():
    root1 = Toplevel()
    root1.geometry('890x620+200+50')
    root1.title('Movie Information')
    root1.config(bg='salmon')
    # ... (existing code for labels and GUI elements)
    # imdb class
    imdbobj = imdb.IMDb()
    movie_name = movieEntry.get()
    movies = imdbobj.search_movie(movie_name)
    indax = movies[1].getID()
    movie = imdbobj.get_movie(indax)
    # Print information in the command line
    print(f'Title: {movie["title"]}')
    if 'director' in movie:
        print(f'Director: {", ".join(movie["director"])}')
    print(f'Year: {movie["year"]}')
    for runtime in movie['runtime']:
        hours = int(runtime) // 60
        minutes = int(runtime) % 60
        print(f'Runtime: {hours} hour {minutes} minutes')
    
    print(f'Genres: {", ".join(movie["genre"])}')
    print(f'Rating: {movie["rating"]}')
    
    cast = movie['cast']
    castlist = list(map(str, cast))
    slicelist = castlist[:10]
    print(f'Cast: {", ".join(slicelist)}')
    root1.mainloop()
root = Tk()
root.geometry('1057x705+100+50')  # width and height #705
root.title("movie description")
root.resizable(False, False)
bgimage = PhotoImage(file="C:\\Users\\Devil Dhivya\\PycharmProjects\\Movie_project\\bgimage.png")
bglabel = Label(root, image=bgimage)
bglabel.place(x=0, y=0)
# created movie label
movielabel = Label(root, text='Movie Name:', font=('alerian', 30, 'bold'), bg='#FE9136')
movielabel.place(x=370, y=470)
movieEntry = Entry(root, font=('FELIX TITTLEING', 20, 'bold'), relief=GROOVE, justify=CENTER)
movieEntry.place(x=640, y=480)
movieEntry.focus_set()
searchButton = Button(root, text='SEARCH', font=('FELIX TITLING', 15, 'bold'), relief=GROOVE, command=search)
searchButton.place(x=740, y=550)
root.mainloop()

