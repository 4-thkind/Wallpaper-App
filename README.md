
```
 ██╗    ██╗ █████╗ ██╗     ██╗     ██████╗  █████╗ ██████╗ ███████╗██████╗      █████╗ ██████╗ ██████╗ 
 ██║    ██║██╔══██╗██║     ██║     ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗    ██╔══██╗██╔══██╗██╔══██╗
 ██║ █╗ ██║███████║██║     ██║     ██████╔╝███████║██████╔╝█████╗  ██████╔╝    ███████║██████╔╝██████╔╝
 ██║███╗██║██╔══██║██║     ██║     ██╔═══╝ ██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗    ██╔══██║██╔═══╝ ██╔═══╝ 
 ╚███╔███╔╝██║  ██║███████╗███████╗██║     ██║  ██║██║     ███████╗██║  ██║    ██║  ██║██║     ██║     
  ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝     ╚═╝     
```

**Your desktop. Your images. Your rules.**

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey?style=flat-square&logo=windows)
![GUI](https://img.shields.io/badge/GUI-Tkinter-orange?style=flat-square)
![Dependency](https://img.shields.io/badge/Dependency-Pillow-green?style=flat-square)

</div>

---

## What Is This?

Wallpaper App is a no-nonsense desktop utility that puts your own image collection front and center .No cloud sync, no background services, no unnecessary overhead just a clean preview window, two buttons, and your wallpaper changed in under a second. Built with Python and Tkinter, it hooks directly into the Windows API to swap your desktop background as fast as you can click.

---

## Getting It Running

The only thing standing between you and a fresh desktop is one dependency. Make sure you have Python 3.x installed, then run:

```bash
pip install Pillow
```

Next, create a folder called `wallpaperProto images` in the same directory as the script and fill it with any images you want to use-> `.jpg`, `.png`, and most common formats work out of the box. Then launch the app:

```bash
python wallpaper_app.py
```

That's it. No config files, no installation wizard, no nonsense.

---

## Using It

The interface is intentionally bare. On the left side of your mind, think of it as a slideshow you control; hit **Next Wallpaper** to flip through your images one by one, watch the preview update live, and when something catches your eye, hit **Set Wallpaper**. Your desktop changes immediately.

---

## Under the Hood

When the app starts, it reads every image from your `wallpaperProto images` folder and holds them in memory as resized previews (400x300) for fast, smooth cycling. The original resolution is never touched until you actually set a wallpaper. At that point, Pillow converts the chosen image to BMP the format Windows demands for its wallpaper API; writes it to a temporary file, and fires off a single call to `SystemParametersInfoW`. The whole operation takes a fraction of a second. The temp file is silently overwritten every time you make a new selection, so it never accumulates.

---

## Project Structure

```
wallpaper-app/
├── wallpaper_app.py
└── wallpaperProto images/
    ├── your_image.jpg
    ├── another_one.png
    └── ...
```

---

## One Thing to Know

This app is Windows-only. The wallpaper-setting mechanism relies on a Windows system call that simply does not exist on macOS or Linux. If you want to port it, the preview and cycling logic will carry over cleanly; only the `set_wall()` function needs to be rewritten for your platform.

---

<div align="center">
  <sub>Built with Python — small tool, big impact on your daily workspace.</sub>
</div>
