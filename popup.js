document.getElementById("saveKeyword").addEventListener("click", () => {
  const keyword = document.getElementById("keyword").value.trim();
  const category = document.getElementById("category").value;

  if (keyword && category) {
    chrome.storage.local.set({ keyword: keyword, category: category }, () => {
      alert("Settings saved!");
    });

    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      chrome.tabs.reload(tabs[0].id);
    });
  } else {
    alert("Please select a category and enter a keyword.");
  }
});
