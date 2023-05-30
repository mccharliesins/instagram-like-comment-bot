import random
import time
import pyautogui

comments = [
    "Awesome post! 😄",
    "Thanks for sharing! 🙌",
    "Love this! ❤️",
    "Great job, well done! 👍",
    "Keep up the good work! 👏",
    "Haha, that's hilarious! 😂",
    "I totally agree! 👌",
    "You're amazing! 😊",
    "Fantastic content! 🌟",
    "Woohoo! Congrats! 🎉",
    "This made my day! 😃",
    "Thank you so much! 🙏",
    "Brilliant post, loved it! 💯",
    "You're a rockstar! 🤘",
    "So inspiring! 💪",
    "This is pure gold! 🏆",
    "Absolutely stunning! 😍",
    "Made me smile! 😄",
    "Well said! 👏👏👏",
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

waittime=range(1,8)
while True:
    random_comment = random.choice(comments)
    random_wait=random.choice(waittime)
    pyautogui.moveTo(606,493,)
    click double to like(606,493)
    go to comments (1406,956)
    go to the next post(1865,548)
while True:
    print(pyautogui.position())