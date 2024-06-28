#!/usr/bin/env python3

import os
import packaging.utils
import requests
import sys

def main():
  # Check if the correct number of command-line arguments is provided
  if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <repository>")
    sys.exit(1)

  # Extract the repository path from the command-line arguments
  repository = sys.argv[1]

  # Fetch releases from the GitHub API for the specified repository
  response = requests.get(f"https://api.github.com/repos/{repository}/releases")

  # Raise an error if the request was unsuccessful
  response.raise_for_status()

  # Parse the response JSON
  data = response.json()

  # Initialize variable to hold the assets of the first non-prerelease
  assets = None

  # Loop through the releases to find the first non-prerelease
  for release in data:
    if not release["prerelease"]:
      assets = release["assets"]
      break

  # Dictionary to hold package information
  packages = {}

  # Process each asset in the release
  for asset in assets:
    # Get the asset name and download URL
    name = asset["name"]
    url = asset["browser_download_url"]

    # Parse the wheel filename to extract package information
    parsed = packaging.utils.parse_wheel_filename(name)

    # Extract the package name from the parsed information
    package_name = parsed[0]

    # Initialize the package entry in the dictionary if not already present
    if package_name not in packages:
      packages[package_name] = []

    # Append the asset information to the package entry
    packages[package_name].append((name, url))

  # Generate HTML pages for each package
  for package_name, wheels in packages.items():
    # Create a directory for the package
    os.makedirs(f"_site/{package_name}", exist_ok=True)

    # Create an index.html file for the package
    with open(f"_site/{package_name}/index.html", "w") as file:
      file.write("<!DOCTYPE html>")
      file.write("<html>")
      file.write("<body>")
      file.write(f"<h1>Links for {package_name}</h1>")
      # Add links to each wheel file
      for (wheel_name, wheel_url) in wheels:
        file.write(f'<a href="{wheel_url}">{wheel_name}</a><br/>')
      file.write("</body>")
      file.write("</html>")

  # Create the main index.html file
  os.makedirs("_site", exist_ok=True)
  with open("_site/index.html", "w") as file:
    file.write("<!DOCTYPE html>")
    file.write("<html>")
    file.write("<body>")
    # Add links to each package
    for package_name in packages.keys():
      file.write(f'<a href="{package_name}/">{package_name}</a><br/>')
    file.write("</body>")
    file.write("</html>")

if __name__ == "__main__":
    main()
