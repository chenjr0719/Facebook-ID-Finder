# Facebook-ID-Finder

A simple Python script to help you find id of Facebook

##  How does it work?

Just like you open your browser -> go to the Facebook Page -> right click and view source code -> ctrl + F to find **profile_id** in the source code.

## Requirement

Only requests, use pip to install it.

```
sudo pip install requests
```

## How to use?

```
python Facebook_ID_Finder.py target_address
```

It will print out the id from the address which you given.

Foe example:

```
python Facebook_ID_Finder.py https://www.facebook.com/prof.yeh/
```

There may occur the error because of the owner of your target address didn't allow his id reveal in public.
