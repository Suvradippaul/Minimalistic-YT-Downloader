from tkinter import *
from tkinter import messagebox
from pytube import YouTube
from tkinter import filedialog
from tkinter import ttk

root = Tk()
root.geometry('500x300')
root.title("Minimalist Youtube Video downloader")

link = StringVar()
var = IntVar()
folderPath = StringVar()

Label(root, text = 'Minimalist Youtube Video downloader', font = ("consolas",16)).place(relx=0.5, rely=0.1,anchor = "center")

Label(root, text = 'Paste link here:').place(relx=0.2, rely=0.2, anchor = "center")

link_enter = Entry(root, width = 40, textvariable = link).place(relx=0.55, rely=0.2,
anchor = "center")

folder_enter = Entry(root, width = 40, textvariable = folderPath).place(relx=0.55, rely=0.3, anchor="center")

Label(root, text = "Choose Resolution").place(relx = 0.5, rely = 0.45, anchor = "center")

radio = Radiobutton(root, text = "360p",variable=var, value=1).place(relx = 0.5, rely = 0.55, anchor = "center")

radio = Radiobutton(root, text = "720p", variable=var, value=2).place(relx = 0.5, rely = 0.65, anchor = "center")

def get_folderPath():
    folder_selected = filedialog.askdirectory()
    folderPath.set(folder_selected)
    
def do_stuff():
    folder = folderPath.get()
    print("The folder is ", folder)

def showdetails():
    url = YouTube(str(link.get()))
    title = url.title
    length = url.length
    hours = length//3600
    remaining = length - 3600*hours
    minutes = remaining//60
    second = length%60
    choice = var.get()

    if choice == 1:
        video = url.streams.get_by_itag(18)
        size = round(video.filesize/1048576, 2)
    else:
        video = url.streams.get_by_itag(22)
        size = round(video.filesize/1048576, 2)
    response = messagebox.askyesno("Information", f"Video title: {title} \nDuration: {hours}hours {minutes}minutes {second}seconds. \nFilesize: {size} MB \nDo you want to download this?")
    
    if response :
        download()
    else:
        messagebox.showwarning("Warning", "Download is cancelled")
        
def download():
    global folderPath
    directory = str(folderPath.get())
    url = YouTube(str(link.get()))
    choice = var.get()
    if choice == 1:
        video = url.streams.get_by_itag(18)
    else:
        video = url.streams.get_by_itag(22)
    
    if directory is None:
        directory = ""
    video.download(directory)
    messagebox.showinfo("Information", "Your video is successfully downloaded.")
 
def downloader():
    try:
        messagebox.showinfo("Information", "Please be patient while the file is downloaded. This may take some time depending upon your internet connectivity.")
        showdetails()  
    except Exception as e:
        print(e)
        messagebox.showerror("Error", "An error occured. Please check your internet connectivity and make sure you entered a valid link.")

btnFind = ttk.Button(root, text = "Browse Folder", command= get_folderPath)

btnFind.place(relx  = 0.2, rely = 0.3, anchor= CENTER)  

Button(root, text = 'Download Now', command = downloader).place( relx = 0.5, rely=0.8, anchor = "center")

root.mainloop()

