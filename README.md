# IZANAGI - Introduction

This is a very primitive pixel art program that I wrote just for fun - and as a proof of concept as well. I wrote this program when I was still a Pascal learner - I'd never coded in other languages. Pascal was the first language I have ever learnt. Apart from school, the only thing that taught me Pascal was myself, along with a 11th grade Informatics school book. The book was in Vietnamese (\*\). It showed me everything about Pascal, about the history of programming languages and so on. It also had some tricks that deal with manipulating terminal graphics. I was really interested in it.

The program was initially just a take on The 8-Bit Guy's program that creates drawings on an LCD screen *(https://www.youtube.com/watch?v=pQk3XgpuaJ4 skip to 8:47)*. The program was named **PIXELDRAW**, and I could not come up with a better name for it. Its whole "cursor movement" and "sub-screen updating" routine was based on a **Snake** game - written in Pascal, by somebody else. Here are some of its features:

- The program has a canvas of 40x20 pseudo-pixels *(originally 32x16)*.
- You can choose all 16 Windows-terminal colours. However, I did not have enough keys for colours, so I grouped those 16 colours as dark and light palettes. You can switch  palettes by pressing **TAB**.
- You can move the mock cursor by using either the *archaic* **arrow keys** or the *contemporary but unusual* **gaming-WASD keys**.
- By pressing **SHIFT** and a number key, you can fill the canvas.
- The program supports save-and-load feature. However, the loading feature is yet to be fixed *(yes, there is a bug where if you try to load another canvas when you've already loaded a canvas, the program rage quits and exits before you could understand what has happened)*.

One thing about PIXELDRAW is its abysmal performance. I wrote it in Pascal and compiled it with Free Pascal IDE, so I expected that it would run fast enough. But whenever I tried the program, I realised - it was *(and still to this day)* AS SLOW AS MOLASSES. I knew this because programs written in languages like C++ has better performance, in terms of speed. Nevertheless, I am still very proud of my (un)holy creation. To others, it is not perfect, but to me, it is perfect enough - as long as it works like I expect.

Several months later, I created a Python version of PIXELDRAW. I had learnt Python from many sources, the first of which was from a Gopnik, named **Life of Boris** (https://www.youtube.com/watch?v=aI4CAJA6wgk). The Python version is just the same program, albeit with some changes.

- Pascal comes with **crt** library which is useful for handling terminal graphics. Python, on the other hand, does not provide you with any command for controlling the terminal. You have to use the 3rd-party **curses** library for that.
- The key mapping is different from that in Pascal version.
- The performance is greatly improved, as the cursor moves at an instant speed.
- The save-and-load feature works properly like you expect, especially the loading routine.

Eventually, starting from Version 2.0, I changed the name of the program, PIXELDRAW, to IZANAGI, after [Izanagi](https://en.wikipedia.org/wiki/Izanagi), the creator deity in Japanese mythology. I also compiled the Python version into executable binary using a program called **Auto-PY-to-EXE**.

The repository includes not only Pascal version, but also Python version, source codes and prototypes. I hope that whether or not you are a pixel art savvy, you will enjoy it as much as I do.

Stay safe - and good luck. Danke fürs Lesen.

*- Katsumi Kogen (光阮 勝己), 2021*

(\*\) In spite of my Japanese name, I am not a Japanese. I am a Vietnamese, and "Katsumi Kogen" is just my nickname. The name "Katsumi" drew inspiration from [Katsumi Minato](https://ultra.fandom.com/wiki/Katsumi_Minato) - the older brother of [Isami Minato](https://ultra.fandom.com/wiki/Isami_Minato) and [Asahi Minato](https://ultra.fandom.com/wiki/Asahi_Minato). The surname, "Kogen" (光阮) is my real Vietnamese name - 光 is my real name, and 阮 is my family name. And now you know who I am.
