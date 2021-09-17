import tkinter as tk
from tkinter import ttk,END
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
import bs4

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

def Close():
    root.destroy()

class Instabot:
  def __init__(self):
      self.bot = webdriver.Chrome('chromedriver.exe')

  def login(self,username, password):
    username = str(username.get())
    password = str(password.get())
    bot = self.bot
    bot.get('https://instagram.com/accounts/login')
    time.sleep(3)
    bot.find_element_by_name('username').send_keys(username)
    bot.find_element_by_name('password').send_keys(password + Keys.RETURN)
    time.sleep(3)

  def hashtag_backend(self):
    pass

  def likePosts(self, hashtag, likes):
      hashtag = str(hashtag.get())
      likes = str(likes.get())
      bot = self.bot
      time.sleep(3)
      if(hashtag[0] == '#'):
        bot.get('https://www.instagram.com/explore/tags/' + hashtag[1:] + '/')

      else:
        bot.get('https://www.instagram.com/' + hashtag + '/?hl=en')
      bot.find_element_by_class_name('v1Nh3').click()
      i = 1
      while(i <= int(likes)):
          time.sleep(3)
          bot.find_element_by_class_name('fr66n').click()
          bot.find_element_by_class_name(
              'coreSpriteRightPaginationArrow').click()
          i += 1
          
  def unfollow(self, profileName,unfollowAmount):
      bot = self.bot
      profileName = str(profileName.get())
      unfollowAmount = str(unfollowAmount.get())
      bot.get('https://instagram.com/' + profileName + '/following/')
      time.sleep(4)
      following = bot.find_element_by_partial_link_text("following")
      following.click()
      time.sleep(4)
      for i in range (int(unfollowAmount)):
          bot.find_element_by_xpath('//button[text()="Following"]')\
              .click()
          bot.find_element_by_xpath('//button[text()="Unfollow"]')\
              .click()
          time.sleep(3)

class InstaBot(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("InstaBot")
        self.frames = dict()

        container = ttk.Frame(self)
        container.grid(padx=60, pady=30, sticky="EW")

        loginframe = LoginPage(container, self)
        loginframe.grid(row=0, column=0, sticky="NSEW")

        optionframe = OptionPage(container, self)
        optionframe.grid(row=0, column=0, sticky="NSEW")

        likeframe = LikesPage(container, self)
        likeframe.grid(row=0, column=0, sticky="NSEW")

        unfollowframe = UnfollowPage(container, self)
        unfollowframe.grid(row=0, column=0, sticky="NSEW")

        hashtagframe = HashtagPage(container, self)
        hashtagframe.grid(row=0, column=0, sticky="NSEW")

        self.frames[LoginPage] = loginframe
        self.frames[OptionPage] = optionframe
        self.frames[LikesPage] = likeframe
        self.frames[UnfollowPage] = unfollowframe
        self.frames[HashtagPage] = hashtagframe

        self.show_frame(LoginPage)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()

obj = Instabot()
class LoginPage(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)

        self.username = tk.StringVar()
        self.password = tk.StringVar()

        title = tk.Label(self, text="InstaBot", fg="black",
                         bg="salmon", font="Helvetica 15 bold")
        title.grid(sticky="EW", columnspan=10, padx=10, pady=10)

        username_label = ttk.Label(self, text="Username: ")
        username_input = ttk.Entry(self, width=15, textvariable=self.username)
        username_label.grid(column=0, row=1, sticky="EW", padx=5, pady=5)
        username_input.grid(column=1, row=1, sticky="EW", padx=5, pady=5)
        username_input.focus()

        password_label = ttk.Label(self, text="Password: ")
        password_input = ttk.Entry(self, width=15, textvariable=self.password)
        password_label.grid(column=0, row=2, sticky="EW", padx=5, pady=5)
        password_input.grid(column=1, row=2, sticky="EW", padx=5, pady=5)
        
        login_button = tk.Button(
            self, text="Login", width=5, bg="#FCDEC0", command=lambda: [controller.show_frame(OptionPage), obj.login(self.username, self.password)])
        login_button.grid(column=0, row=5, sticky="EW", padx=7, pady=7)

        cancel_button = tk.Button(
            self, text="❌ Cancel", width=5, bg="#FCDEC0", command=Close)
        cancel_button.grid(column=1, row=5, sticky="EW", padx=7, pady=7)


class OptionPage(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)

        title = tk.Label(self, text="InstaBot", fg="black",
                         bg="salmon", font="Helvetica 15 bold")
        title.grid(sticky="EW", columnspan=10, padx=4, pady=4)

        hashtag_button = tk.Button(self, text="Hashtag", width=10, bg="#FCDEC0",command=lambda: controller.show_frame(HashtagPage))
        hashtag_button.grid(column=0, row=1, sticky="EW", padx=7, pady=7)

        likes_button = tk.Button(self, text="Likes", width=10, bg="#FCDEC0",
                                 command=lambda: [controller.show_frame(LikesPage)])
        likes_button.grid(column=0, row=2, sticky="EW", padx=7, pady=7)

        unfollow_button = tk.Button(
            self, text="Unfollow", width=10, bg="#FCDEC0",command=lambda: controller.show_frame(UnfollowPage))
        unfollow_button.grid(column=1, row=1, sticky="EW", padx=7, pady=7)

        back_button = tk.Button(self, text="Back", width=10, bg="#FCDEC0",command=lambda: controller.show_frame(LoginPage))
        back_button.grid(column=1, row=2, sticky="EW", padx=7, pady=7)


class LikesPage(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)
        
        self.hashtag = tk.StringVar()
        self.likes = tk.StringVar()
       
        title = tk.Label(self, text="InstaBot", fg="black",
                         bg="salmon", font="Helvetica 15 bold")
        title.grid(sticky="EW", columnspan=10, padx=10, pady=10)

        hashtag_label = ttk.Label(self, text="Hashtag/Profile: ")
        hashtag_input = ttk.Entry(self, width=15, textvariable=self.hashtag)
        hashtag_label.grid(column=0, row=1, sticky="EW", padx=5, pady=5)
        hashtag_input.grid(column=1, row=1, sticky="EW", padx=5, pady=5)
        hashtag_input.focus()

        likes_label = ttk.Label(self, text="Number of posts:")
        likes_input = ttk.Entry(self, width=15, textvariable=self.likes)
        likes_label.grid(column=0, row=2, sticky="EW", padx=5, pady=5)
        likes_input.grid(column=1, row=2, sticky="EW", padx=5, pady=5)
        likes_input.focus()

        submit_button = tk.Button(self, text="Submit", width=5, bg="#FCDEC0", command=lambda: [
                                  obj.likePosts(self.hashtag, self.likes)])
        submit_button.grid(column=0, row=5, sticky="NSEW", padx=7, pady=7)

        back_button = tk.Button(self, text="Back", width=10, bg="#FCDEC0",
                                command=lambda: controller.show_frame(OptionPage))
        back_button.grid(column=1, row=5, sticky="W", padx=7, pady=7)


class UnfollowPage(ttk.Frame):
    def __init__(self, container,controller):
        super().__init__(container)

        self.profileName = tk.StringVar()
        self.unfollowAmount=tk.StringVar()

        title = tk.Label(self, text="InstaBot", fg="black", bg="salmon", font="Helvetica 15 bold")
        title.grid(sticky="EW", columnspan=10, padx=10, pady=10)

        profile_label = ttk.Label(self, text="Hashtag/Profile: ")
        profile_input = ttk.Entry(self, width=15, textvariable=self.profileName)
        profile_label.grid(column=0, row=1, sticky="EW", padx=5, pady=5)
        profile_input.grid(column=1, row=1, sticky="EW", padx=5, pady=5)
        profile_input.focus()

        unfollow_Amount_label = ttk.Label(self, text="Number:")
        unfollow_Amount_input = ttk.Entry(self, width=15, textvariable=self.unfollowAmount)
        unfollow_Amount_label.grid(column=0, row=2, sticky="EW", padx=5, pady=5)
        unfollow_Amount_input.grid(column=1, row=2, sticky="EW", padx=5, pady=5)
        unfollow_Amount_input.focus()

        submit_button = tk.Button(self, text="Submit", width=5, bg="#FCDEC0",command=lambda: [obj.unfollow(self.profileName, self.unfollowAmount)])
        submit_button.grid(column=0, row=5, sticky="NSEW", padx=7, pady=7)

        back_button = tk.Button(self, text="Back", width=10, bg="#FCDEC0",command=lambda: controller.show_frame(OptionPage))
        back_button.grid(column=1, row=5,sticky="W", padx=7, pady=7)
class HashtagPage(ttk.Frame):
    def __init__(self, container,controller):
        super().__init__(container)

        heading = tk.Label(self, text="Trending Hashtag", fg="black", bg="light grey", font="Helvetica 15 bold")
        heading.grid(sticky="EW", columnspan=10, padx=10, pady=10)
        res = requests.get('http://best-hashtags.com/hashtag/trending/')
        res.text
        soup = bs4.BeautifulSoup(res.text,'lxml')
        hashtag_out =""
        c= 0
        for i in soup.select('.tag-box'):
          if(c<5):
            hashtag_out += i.text
            c+=1

        hashtag_out = str(hashtag_out)
        disp_out = tk.Text(self, width=20,height=7)
        disp_out.grid(sticky="NSEW",columnspan=12,ipady=15)
        disp_out.insert(END, str(hashtag_out))
        back_button = tk.Button(self, text="Back", width=10, bg="#FCDEC0",command=lambda: controller.show_frame(OptionPage))
        back_button.grid(column=4, row=3,sticky="W", padx=7, pady=7)
       

root = InstaBot() 
root.columnconfigure(0, weight=1)
root.geometry("405x310")
root.resizable(False, False)
root.configure(bg='#8FC1D4')
s = ttk.Style()
s.configure('TFrame', background='#8FC1D4')
s.configure('TLabel', background='#8FC1D4')
root.mainloop()
