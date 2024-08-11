<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>DeTox: YouTube Keyword Filter Extension</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
      color: #333;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
    }
    .container {
      max-width: 800px;
      margin: 0 auto;
      padding: 20px;
      background: #fff;
      border-radius: 8px;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }
    h1, h2 {
      color: #333;
    }
    h1 {
      text-align: center;
    }
    .logo {
      display: block;
      margin: 0 auto 20px;
      width: 150px;
      height: auto;
    }
    code {
      background: #f4f4f4;
      border: 1px solid #ddd;
      padding: 5px;
      border-radius: 4px;
    }
    ul {
      list-style: none;
      padding: 0;
    }
    ul li {
      background: #e9e9e9;
      margin: 5px 0;
      padding: 10px;
      border-radius: 4px;
    }
    a {
      color: #1a73e8;
    }
    a:hover {
      text-decoration: underline;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>DeTox: A YouTube Keyword Filter Extension</h1>
    <img src="bee.png" alt="Bee Logo" class="logo">
    
    <h2>Overview</h2>
    <p>
      The YouTube Keyword Filter is a Chrome extension designed to enhance your YouTube experience by allowing you to filter out videos based on specific keywords or categories. This extension provides a customizable way to manage the content you see on YouTube by either removing unrelated videos or highlighting those that match your interests.
    </p>
    
    <h2>Features</h2>
    <ul>
      <li><strong>Keyword Filtering</strong>: Filter out videos that do not contain specified keywords.</li>
      <li><strong>Category-Based Filtering</strong>: Choose from predefined categories (e.g., Coding, Music, Dance, Sports) with a list of relevant keywords.</li>
      <li><strong>Dynamic Content Management</strong>: Remove unrelated videos from the YouTube page in real-time.</li>
      <li><strong>Modern and Professional UI</strong>: User-friendly interface with a modern design.</li>
    </ul>
    
    <h2>Installation</h2>
    <ol>
      <li><strong>Download or Clone the Repository</strong><br>
        You can either download the ZIP file of this repository or clone it using Git:
        <pre><code>git clone https://github.com/yourusername/your-repository-name.git</code></pre>
      </li>
      <li><strong>Load the Extension in Chrome</strong><br>
        <ol>
          <li>Open Chrome and go to <code>chrome://extensions/</code>.</li>
          <li>Enable "Developer mode" using the toggle switch at the top right.</li>
          <li>Click on "Load unpacked" and select the directory where you have the extension files.</li>
        </ol>
      </li>
    </ol>
    
    <h2>Usage</h2>
    <ol>
      <li><strong>Open the Extension Popup</strong><br>
        Click on the extension icon in the Chrome toolbar to open the popup.
      </li>
      <li><strong>Select a Category</strong><br>
        Choose a category from the dropdown menu (e.g., Coding, Music, Dance, Sports).
      </li>
      <li><strong>Enter a Keyword</strong><br>
        Type a specific keyword you want to filter or focus on.
      </li>
      <li><strong>Save Settings</strong><br>
        Click the "Save" button to apply your settings. The extension will immediately start filtering YouTube videos based on your input.
      </li>
    </ol>
    
    <h2>Technical Details</h2>
    <h3>Files and Directories</h3>
    <ul>
      <li><code>manifest.json</code>: Configuration file for the Chrome extension.</li>
      <li><code>popup.html</code>: HTML file for the extension popup UI.</li>
      <li><code>popup.js</code>: JavaScript file for handling user input and saving settings.</li>
      <li><code>content.js</code>: JavaScript file for filtering YouTube videos based on keywords.</li>
      <li><code>background.js</code>: Service worker for handling background tasks (if needed).</li>
    </ul>
    
    <h3>Code Structure</h3>
    <ul>
      <li><strong>Manifest Version</strong>: 3</li>
      <li><strong>Permissions</strong>: <code>activeTab</code>, <code>storage</code></li>
      <li><strong>Content Scripts</strong>: Applied to YouTube pages to manage video filtering.</li>
      <li><strong>Service Worker</strong>: Manages background tasks and state.</li>
    </ul>
    
    <h2>Contributing</h2>
    <p>We welcome contributions to improve this extension. If you have any suggestions or find issues, please follow these guidelines:</p>
    <ol>
      <li><strong>Fork the Repository</strong><br>
        Create a personal fork of the repository on GitHub.
      </li>
      <li><strong>Create a New Branch</strong><br>
        Create a new branch for your changes:
        <pre><code>git checkout -b feature/your-feature</code></pre>
      </li>
      <li><strong>Make Your Changes</strong><br>
        Implement your changes or add new features.
      </li>
      <li><strong>Submit a Pull Request</strong><br>
        Push your changes to your fork and submit a pull request to the main repository.
      </li>
    </ol>
    
    <h2>License</h2>
    <p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.</p>
    
    <h2>Contact</h2>
    <p>For any questions or further information, please contact us at <a href="mailto:your-email@example.com">your-email@example.com</a>.</p>
  </div>
</body>
</html>
