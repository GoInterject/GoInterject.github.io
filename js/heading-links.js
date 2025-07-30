document.addEventListener("DOMContentLoaded", function () {
    // Add `.link-copy` to all h2–h6 headings
    document.querySelectorAll("h2, h3, h4, h5, h6").forEach(header => {
      if (!header.classList.contains("link-copy")) {
        header.classList.add("link-copy");
      }
    });
  
    // Enhance .link-copy headings with a clickable anchor
    document.querySelectorAll(".link-copy").forEach(header => {
      if (!header.id) return;
  
      const link = document.createElement("a");
      link.href = `#${header.id}`;
      link.className = "heading-anchor";
      link.innerHTML = '<i class="fa fa-link"></i>'; // initial icon
  
      link.onclick = function (e) {
        e.preventDefault();
        const url = `${window.location.origin}${window.location.pathname}#${header.id}`;
        navigator.clipboard.writeText(url).then(() => {
          link.innerHTML = '<i class="fa fa-check text-success"></i>';
          setTimeout(() => {
            link.innerHTML = '<i class="fa fa-link"></i>';
          }, 1000);
        });
      };
  
      header.appendChild(link);
    });
  });
  