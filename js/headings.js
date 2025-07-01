// This script adds a link copy functionality to headings with the class "link-copy".
document.addEventListener("DOMContentLoaded", function () {
  const headers = document.querySelectorAll(".link-copy");

  headers.forEach(header => {
    if (!header.id) return;

    const link = document.createElement("a");
    link.href = `#${header.id}`;
    link.className = "heading-anchor";
    link.innerHTML = "🔗";

    link.onclick = function (e) {
      e.preventDefault();
      const url = `${window.location.origin}${window.location.pathname}#${header.id}`;
      navigator.clipboard.writeText(url).then(() => {
        link.innerHTML = "✅";
        setTimeout(() => link.innerHTML = "🔗", 1000);
      });
    };

    header.appendChild(link);
  });
});
