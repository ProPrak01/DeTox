# <img src="bee.png" alt="Bee Logo" width="60" height="60" style="vertical-align: middle;"/> **   DeTox : A YouTube Keyword Filter Extension**


## Overview

The YouTube Keyword Filter is a Chrome extension designed to enhance your YouTube experience by allowing you to filter out videos based on specific keywords or categories. This extension provides a customizable way to manage the content you see on YouTube by either removing unrelated videos or highlighting those that match your interests.

## Features

* **Keyword Filtering**: Filter out videos that do not contain specified keywords.
* **Category-Based Filtering**: Choose from predefined categories (e.g., Coding, Music, Dance, Sports) with a list of relevant keywords.
* **Dynamic Content Management**: Remove unrelated videos from the YouTube page in real-time.
* **Modern and Professional UI**: User-friendly interface with a modern design.

## Installation

1. Download or Clone the Repository
You can either download the ZIP file of this repository or clone it using Git:

bash
git clone https://github.com/yourusername/your-repository-name.git

2. Load the Extension in Chrome
3. Open Chrome and go to chrome://extensions/.
4. Enable "Developer mode" using the toggle switch at the top right.
5. Click on "Load unpacked" and select the directory where you have the extension files.

## Usage

Open the Extension Popup:

Click on the extension icon in the Chrome toolbar to open the popup.


Select a Category:

Choose a category from the dropdown menu (e.g., Coding, Music, Dance, Sports).


Enter a Keyword:

Type a specific keyword you want to filter or focus on.


Save Settings:

Click the "Save" button to apply your settings. The extension will immediately start filtering YouTube videos based on your input.



Technical Details
Files and Directories

manifest.json: Configuration file for the Chrome extension.
popup.html: HTML file for the extension popup UI.
popup.js: JavaScript file for handling user input and saving settings.
content.js: JavaScript file for filtering YouTube videos based on keywords.
background.js: Service worker for handling background tasks (if needed).

Code Structure

Manifest Version: 3
Permissions: activeTab, storage
Content Scripts: Applied to YouTube pages to manage video filtering.
Service Worker: Manages background tasks and state.

Contributing
We welcome contributions to improve this extension. If you have any suggestions or find issues, please follow these guidelines:

Fork the Repository:

Create a personal fork of the repository on GitHub.


Create a New Branch:

Create a new branch for your changes:



bashCopygit checkout -b feature/your-feature

Make Your Changes:

Implement your changes or add new features.


Submit a Pull Request:

Push your changes to your fork and submit a pull request to the main repository.



## License
This project is licensed under the MIT License. See the LICENSE file for details.
Contact
For any questions or further information, please contact us at your-email@example.com.
