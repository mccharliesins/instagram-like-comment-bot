import random
import time
import pyautogui

time.sleep(5)
# Add sample comments here!
comments = [
    "Awesome post! 😄",
    "Love this! ❤️",
    "Great job, well done! 👍",
    "Keep up the good work! 👏",
    "I totally agree! 👌",
    "You're amazing! 😊",
    "Fantastic content! 🌟",
    "Woohoo! Congrats! 🎉",
    "This made my day! 😃",
    "Brilliant post, loved it! 💯",
    "You're a rockstar! 🤘",
    "So inspiring! 💪",
    "This is pure gold! 🏆",
    "Absolutely stunning! 😍",
    "Made me smile! 😄",
    "Impressive work! 👌👍",
    "You're on fire! 🔥",
    "I'm speechless! 😶",
    "Mind-blowing content! 🤯",
    "This is genius! 🧠",
    "Keep shining bright! ✨",
    "You're a superstar! ⭐",
    "Absolutely flawless! 💎",
    "This is everything! 🙌💯",
    "Hats off to you! 👒👏",
    "This deserves applause! 👏👏👏",
    "You're an inspiration! 💫"
]

waittime=range(1,7)
totallikesandcomments=50
i=0
while i<totallikesandcomments:
    random_comment = random.choice(comments)
    random_wait=random.choice(waittime)
    
    # Wait and then move to the post to like!
    time.sleep(random_wait)
    pyautogui.moveTo(606,493,1)
    pyautogui.doubleClick()
    
    # Wait and then move to comments to comment
    time.sleep(random_wait)
    pyautogui.moveTo(1406,956,0.5)
    time.sleep(random_wait)
    pyautogui.click()
    pyautogui.write(random_comment,0.2)
    time.sleep(1)
    pyautogui.press('enter')
    
    # Wait and move to next post!
    time.sleep(random_wait)
    pyautogui.moveTo(1865,548,1)
    time.sleep(random_wait)
    pyautogui.click()
    
    # Increament the value of I
    i+=1
    print(f"Total Likes & Comments: {i}")