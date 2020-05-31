# GIF Challenge Write-Up

#### Upon introduction
Starting this challenge, we were greeted with the message "A1l3N thought this was funny so we turned it into a challenge." and an attached gif: "chal.gif".

![Challenge GIF](chal.gif)

As soon as I opened the GIF, it was immediately fairly obvious what the point of this challenge was; frame by frame neon green numbers flashed up and slowly dissapeared as more numbers appeared.


#### The process
To extract all these numbers, there are a ton of frame-by-frame viewers out there, but I just used a program called [stegsolve](https://aur.archlinux.org/packages/stegsolve/). I opened the gif inside of stegsolve and used it's frame browser to identify the change in the image frame by frame, which easily allowed me to isolate each number that appeared. 

I then browsed through and noted down all the numbers in order:

`15 13 7 19 15 6 21 14 14 25 12 15 12`

Now at this point I was pretty confident the flag wasn't just going to be a sequence of obvious numbers. I noticed all the numbers were below 26, so I thought the logical next step would be to match each number to its corresponding place in the alphabet.

```
15	= o
13	= m
7	= g

19	= s
15	= o

6	= f
21	= u
14	= n
14	= n
25	= y

12	= l
15	= o
12	= l
```

#### Submission
So now with the message `omg so funny lol`, I replaced the spaces with underscores and tried to submit the flag with the CTF's formatting: `castorsCTF{omg_so_funny_lol}`.

**__Success! The flag was correct!__**
