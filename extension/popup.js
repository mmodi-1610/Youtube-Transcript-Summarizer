async function getVideoIdFromUrl(url) {
  try {
    const urlObj = new URL(url);
    return urlObj.searchParams.get("v");
  } catch {
    return null;
  }
}

document.addEventListener("DOMContentLoaded", async () => {
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  const videoId = await getVideoIdFromUrl(tab.url);

  if (!videoId) {
    document.getElementById("loading").style.display = "none";
    document.getElementById("error").textContent = "Not a valid YouTube video.";
    return;
  }

  try {
    const response = await fetch(`http://localhost:8000/summarize?video_id=${videoId}`);
    const data = await response.json();

    if (data.error) throw new Error(data.error);

    document.getElementById("loading").style.display = "none";
    document.getElementById("summary").style.display = "block";
    document.getElementById("short").textContent = data.summary.short;
    document.getElementById("medium").textContent = data.summary.medium;
    document.getElementById("detailed").textContent = data.summary.detailed;
  } catch (err) {
    document.getElementById("loading").style.display = "none";
    document.getElementById("error").textContent = "Error: " + err.message;
  }
});
