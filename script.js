document.addEventListener("DOMContentLoaded", function () {
  const tabs = document.querySelectorAll(".tab");
  const tabContents = document.querySelectorAll(".tab-content");

  tabs.forEach((tab) => {
    tab.addEventListener("click", () => {
      // Remove the "active" class from all tab contents
      tabContents.forEach((content) => {
        content.classList.remove("active");
      });

      const tabId = tab.getAttribute("data-tab");
      const content = document.getElementById(tabId);

      // Add the "active" class to the selected tab content
      content.classList.add("active");
    });
  });

  // Default to the first tab being active
  tabContents[0].classList.add("active");
});
