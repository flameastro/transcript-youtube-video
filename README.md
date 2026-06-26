<div align="center">

![Stars](https://img.shields.io/github/stars/flameastro/transcript-youtube-video)
![Forks](https://img.shields.io/github/forks/flameastro/transcript-youtube-video)
![Issues](https://img.shields.io/github/issues/flameastro/transcript-youtube-video)

</div>

# 📜 transcript-youtube-video

---

## 📑 Table of Contents

* [📜 What is it?]([#-what-is-it)
* [🧰 Requirements]([#-requirements)
* [🚀 How to Use]([#-how-to-use)
* [📄 Output Examples]([#-output-examples)
* [⚠️ Warning]([#%EF%B8%8F-warning)
* [❓ Issues]([#-issues)


## 📜 What is it?

**transcript-youtube-video** is a Python project designed to automatically collect the full transcript of a YouTube video.
A video **transcript** is essentially the same as the **subtitles**, so this program will **retrieve the subtitles for a specific video** for you.

## 🧰 Requirements

### 🔀 1. Install git

To verify if you have git, try this on your command line (Terminal):
```bash
git -v
```

Expected result: git version 2.[...] or something like this  
If this message don't appear to you, then, [install git here](https://git-scm.com/install/)

### 🔁 2. Clone the repository

Paste this into your command line (Terminal):

```bash
git clone https://github.com/flameastro/transcript-youtube-video.git
cd transcript-youtube-video
```

If the result be something like this:
```txt
Cloning into 'transcript-youtube-video'...  
remote: Enumerating objects: 62, done.
remote: Counting objects: 100% (62/62), done.
remote: Compressing objects: 100% (44/44), done.
remote: Total 62 (delta 27), reused 48 (delta 17), pack-reused 0 (from 0)
Receiving objects: 100% (62/62), 1.86 MiB | 10.25 MiB/s, done.
Resolving deltas: 100% (27/27), done.
```

Then, you clone the repository successfully!

### 🐍 3. Install Python

Go to [Python Downloads](https://www.python.org/downloads/)
Then select your operating system
If you need help, watch one of this videos:

- <img src="https://images.icon-icons.com/729/PNG/512/windows_icon-icons.com_62712.png" width=32> For [Windows](https://www.youtube.com/watch?v=e70ykVBazAg)
- <img src="https://icons.veryicon.com/png/o/commerce-shopping/merchant-product-icon-library/mac-21.png" width=32> For [Mac](https://www.youtube.com/watch?v=utVZYVJSTZA)
- <img src="https://cdn-icons-png.flaticon.com/512/6124/6124995.png" width=32>For [Linux](https://www.youtube.com/watch?v=kkXziXPY6Do)

### 📦 4. Install the dependencies (the libraries of the project)

Go to your Terminal and paste:
```bash
pip install -r requirements.txt
playwright install
```

## 🚀 How to Use

Go to your terminal and paste:
```bash
python main.py
```

If you get an error, try:

```bash
python3 main.py
```

Then, this message will be displayed:
```txt
Paste the URL of the video here:
>>>
```

So you need to get an youtube link and then paste the url, like this:


```txt
Paste the URL of the video here:
>>>https://youtu.be/rdwz7QiG0lk?si=IAwr1C-2Afk6KkiG
```

Then another message will be displayed:

```txt
Did you want time in the file? [y/n]:
>>>
```

You need to press y or n;  
* If you **press y**: You will get all the time of the video. Example: 00:00: Welcome back guys! In this video we will [...]
* If you **press n**: You don't get the time of the video. Example: Welcome back guys! In this video we will [...]

## 📄 Output Examples

> Example with time
> <img src="assets/transcript-v1.png" alt="Transcript example with timestamps">

> Example without time
> <img src="assets/transcript-v2.png" alt="Transcript example without timestamps">

## ⚠️ Warning

* If you put a video on it and it now create the transcript.txt file, maybe that's why:
- They have a little or no audio (eg. a meme, or a very short video)
- They have so many content (eg. the video has more than 10 hours of duration)
- The creator disabled the captions (some creators disabled the captions)

In these cases, the `transcript.txt` file may be empty

## ❓ Issues

Any doubt or found an issue? Feel free to [go the issues sections](https://github.com/flameastro/transcript-youtube-video/issues) and create a new issue!
