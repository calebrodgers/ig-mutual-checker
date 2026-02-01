# Instagram Followers and Following Comparator

This script (`main.py`) is designed to help you analyze and compare your Instagram followers and following lists using your Instagram data export. It is intended for use with the JSON files found in the `connections/followers_and_following/` directory of your Instagram data download.

## Features
- Compare your followers and following lists
- Identify users you follow who don't follow you back
- Identify users who follow you but you don't follow back
- Easily customizable for other types of comparisons

## Usage
1. **Place your Instagram data files** in the `connections/followers_and_following/` directory. The relevant files are usually named:
   - `followers_1.json`
   - `following.json`

2. **Run the script:**
   ```bash
   python main.py
   ```

3. **View the output:**
   - The script will print lists of users you follow who don't follow you back, and users who follow you but you don't follow back.

## File Structure
```
connections/
  followers_and_following/
    main.py
    followers_1.json
    following.json
    ...
```

## Customization
- You can modify the script to compare other JSON files or extract additional insights from your Instagram data.

## Requirements
- Python 3.x
- No external dependencies (uses only the Python standard library)

## Disclaimer
This script is for personal use only. Do not share your Instagram data with others. Always keep your data secure.

---

**Author:** Caleb Rodgers
**Date:** February 2026
