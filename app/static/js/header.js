document.addEventListener("DOMContentLoaded", function () {
  const activePage = window.location.pathname;

  document.querySelectorAll('.navbar-nav .nav-link').forEach(link => {
    if (link.pathname === activePage) {
      // Apply `.active` only to direct navigation links, excluding dropdown toggles
      if (!link.classList.contains('dropdown-toggle')) {
        link.classList.add('active');
      }

      // If this is a dropdown item, highlight the parent dropdown
      const parentDropdown = link.closest('.dropdown');
      if (parentDropdown) {
        parentDropdown.querySelector('.dropdown-toggle').classList.add('dropdown-active');
      }
    }
  });
});
